#!/usr/bin/env python3
"""Fetch a YouTube video's metadata + timestamped transcript as JSON.

Usage:
    python3 fetch_transcript.py <youtube_url_or_video_id> [--out FILE]

Prints a single JSON object to stdout (or writes it to --out):

  Success:
    {
      "ok": true,
      "video_id": "...",
      "title": "...",
      "channel": "...",
      "duration_seconds": 754,
      "thumbnail": "https://...",
      "url": "https://www.youtube.com/watch?v=...",
      "transcript": [{"start": 0.5, "text": "..."}, ...]
    }

  Failure:
    {
      "ok": false,
      "reason": "no_captions" | "private" | "age_restricted" | "live"
                | "unavailable" | "network_blocked" | "dependency_missing"
                | "unknown",
      "error": "human-readable detail"
    }

Strategy: try yt-dlp first (actively maintained, handles metadata +
subtitles in one extraction). If yt-dlp can't produce a transcript,
fall back to the youtube-transcript-api package for the transcript and
YouTube's oEmbed endpoint for lightweight metadata.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import urllib.request


def parse_video_id(raw: str) -> str:
    raw = raw.strip()
    if re.fullmatch(r"[\w-]{11}", raw):
        return raw
    patterns = [
        r"(?:v=|/videos/|embed/|shorts/|youtu\.be/|/live/)([\w-]{11})",
    ]
    for pat in patterns:
        m = re.search(pat, raw)
        if m:
            return m.group(1)
    raise ValueError(f"Could not extract a video ID from: {raw!r}")


def ensure_package(module_name: str, pip_name: str) -> bool:
    try:
        __import__(module_name)
        return True
    except ImportError:
        pass
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--quiet",
             "--disable-pip-version-check", pip_name],
            check=True, timeout=120,
        )
        __import__(module_name)
        return True
    except Exception:
        return False


def classify_ytdlp_error(msg: str) -> str:
    lo = msg.lower()
    if "private video" in lo:
        return "private"
    if "sign in to confirm your age" in lo or "age" in lo and "restrict" in lo:
        return "age_restricted"
    if "premiere" in lo or "is live" in lo or "live event" in lo:
        return "live"
    if "video unavailable" in lo or "removed" in lo or "does not exist" in lo:
        return "unavailable"
    if "unable to download" in lo or "urlopen" in lo or "timed out" in lo or "connection" in lo:
        return "network_blocked"
    return "unknown"


def pick_caption_track(info: dict):
    """Return (lang, url) for the best available json3 caption track."""
    for bucket_name in ("subtitles", "automatic_captions"):
        bucket = info.get(bucket_name) or {}
        if not bucket:
            continue
        langs = list(bucket.keys())
        preferred = [l for l in langs if l == "en"] + \
                    [l for l in langs if l.startswith("en") and l != "en"] + \
                    langs
        seen = set()
        for lang in preferred:
            if lang in seen:
                continue
            seen.add(lang)
            tracks = bucket.get(lang, [])
            for t in tracks:
                if t.get("ext") == "json3":
                    return lang, t["url"]
            if tracks:
                return lang, tracks[0]["url"]
    return None, None


def parse_json3_captions(raw: bytes):
    data = json.loads(raw)
    out = []
    for event in data.get("events", []):
        segs = event.get("segs")
        if not segs:
            continue
        text = "".join(s.get("utf8", "") for s in segs).strip()
        if not text or text == "\n":
            continue
        start = event.get("tStartMs", 0) / 1000.0
        out.append({"start": round(start, 2), "text": text.replace("\n", " ")})
    return out


def try_ytdlp(video_id: str):
    if not ensure_package("yt_dlp", "yt-dlp"):
        return None, {"ok": False, "reason": "dependency_missing",
                       "error": "Could not install yt-dlp (no network access to PyPI, or install failed)."}

    import yt_dlp

    url = f"https://www.youtube.com/watch?v={video_id}"
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        return None, {"ok": False, "reason": classify_ytdlp_error(str(e)), "error": str(e)}

    if info.get("is_live"):
        return None, {"ok": False, "reason": "live", "error": "Video is a live stream in progress."}

    lang, cap_url = pick_caption_track(info)
    transcript = None
    if cap_url:
        try:
            req = urllib.request.Request(cap_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read()
            transcript = parse_json3_captions(raw)
        except Exception:
            transcript = None

    metadata = {
        "video_id": video_id,
        "title": info.get("title"),
        "channel": info.get("uploader") or info.get("channel"),
        "duration_seconds": info.get("duration"),
        "thumbnail": info.get("thumbnail"),
        "url": info.get("webpage_url", url),
    }

    if not transcript:
        return metadata, {"ok": False, "reason": "no_captions",
                           "error": "No subtitles or auto-captions are available for this video."}

    return metadata, {"ok": True, "transcript": transcript}


def try_transcript_api_fallback(video_id: str, metadata_hint: dict | None):
    if not ensure_package("youtube_transcript_api", "youtube-transcript-api"):
        return {"ok": False, "reason": "dependency_missing",
                "error": "Could not install youtube-transcript-api either."}

    from youtube_transcript_api import YouTubeTranscriptApi

    try:
        raw = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        msg = str(e)
        lo = msg.lower()
        if "disabled" in lo or "no transcript" in lo:
            reason = "no_captions"
        elif "private" in lo:
            reason = "private"
        elif "unavailable" in lo:
            reason = "unavailable"
        else:
            reason = "unknown"
        return {"ok": False, "reason": reason, "error": msg}

    transcript = [{"start": round(seg["start"], 2), "text": seg["text"].replace("\n", " ")}
                  for seg in raw]

    metadata = metadata_hint or {}
    if not metadata.get("title"):
        try:
            oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
            with urllib.request.urlopen(oembed_url, timeout=15) as resp:
                oembed = json.loads(resp.read())
            metadata.update({
                "title": oembed.get("title"),
                "channel": oembed.get("author_name"),
                "thumbnail": oembed.get("thumbnail_url"),
            })
        except Exception:
            pass

    metadata.setdefault("video_id", video_id)
    metadata.setdefault("url", f"https://www.youtube.com/watch?v={video_id}")
    metadata.setdefault("duration_seconds", None)
    metadata.setdefault("thumbnail", metadata.get("thumbnail"))
    metadata.setdefault("channel", metadata.get("channel"))
    metadata.setdefault("title", metadata.get("title"))

    return {"ok": True, "transcript": transcript, **{k: v for k, v in metadata.items() if k != "ok"}}


def main():
    args = sys.argv[1:]
    if not args:
        print(json.dumps({"ok": False, "reason": "unknown", "error": "Usage: fetch_transcript.py <url_or_id> [--out FILE]"}))
        sys.exit(1)

    out_file = None
    if "--out" in args:
        idx = args.index("--out")
        out_file = args[idx + 1]
        del args[idx:idx + 2]

    try:
        video_id = parse_video_id(args[0])
    except ValueError as e:
        result = {"ok": False, "reason": "unknown", "error": str(e)}
        _emit(result, out_file)
        sys.exit(1)

    metadata, outcome = try_ytdlp(video_id)

    if not outcome.get("ok"):
        fallback = try_transcript_api_fallback(video_id, metadata)
        if fallback.get("ok"):
            result = fallback
        else:
            # Prefer the yt-dlp failure reason if it was more specific than "unknown".
            result = outcome if outcome.get("reason") not in (None, "unknown") else fallback
    else:
        result = {"ok": True, **metadata, "transcript": outcome["transcript"]}

    _emit(result, out_file)
    sys.exit(0 if result.get("ok") else 1)


def _emit(result: dict, out_file: str | None):
    text = json.dumps(result, indent=2, ensure_ascii=False)
    if out_file:
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        print(text)


if __name__ == "__main__":
    main()
