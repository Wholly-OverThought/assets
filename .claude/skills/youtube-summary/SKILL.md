---
name: youtube-summary
description: Fetches a YouTube video's transcript and turns it into a color-coded, scannable bullet-point summary rendered as an HTML Artifact — bullets are grouped into categories like Key Takeaways, Facts & Stats, Warnings & Caveats, Notable Quotes, and Action Items, each tagged with a distinct color and linked back to its exact timestamp in the video. Use this skill whenever the user pastes a youtube.com or youtu.be link and asks to summarize, recap, break down, TL;DR, or "give me the key points" of it, or asks what a video covers, or wants to skim a long video without watching the whole thing — even if they don't use the word "summary" explicitly (e.g. "what does this video say about X", "watch this and tell me the highlights", "turn this into notes").
---

# YouTube Summary

Turn a YouTube video into a color-coded bullet summary the user can scan in
under a minute instead of watching the whole thing. The point of the color
coding is skimmability: a reader should be able to tell at a glance which
bullets are the actual takeaway versus a supporting fact versus something to
be skeptical of, without reading every word.

## Step 1 — Resolve the video

Accept whatever the user gives you: a full `youtube.com/watch?v=...` URL, a
`youtu.be/...` short link, a Shorts/embed/live URL, or a bare 11-character
video ID. Don't ask the user to clean it up first — the bundled script
handles all of these.

## Step 2 — Fetch metadata + transcript

Run the bundled script rather than writing your own fetch logic — it already
handles the yt-dlp/youtube-transcript-api fallback chain, caption-track
selection, and error classification:

```bash
python3 "<skill_dir>/scripts/fetch_transcript.py" "<url_or_id>"
```

It prints one JSON object to stdout. On success:

```json
{
  "ok": true,
  "video_id": "...",
  "title": "...",
  "channel": "...",
  "duration_seconds": 754,
  "thumbnail": "https://...",
  "url": "https://www.youtube.com/watch?v=...",
  "transcript": [{"start": 12.5, "text": "..."}, ...]
}
```

The first run may take a few extra seconds if it needs to `pip install
yt-dlp`. That's expected, not a failure.

### If it fails

The script returns `{"ok": false, "reason": "...", "error": "..."}`. Match
`reason` to a plain-language response — don't just dump the raw error at the
user:

- `no_captions` — This video has no subtitles or auto-captions available
  (common for music videos, or channels that disable auto-captions). Tell
  the user directly; there's no transcript to summarize from. Don't attempt
  to guess content from the title/description alone and present it as a
  summary.
- `private` — The video is private or unlisted in a way that blocks access.
- `age_restricted` — YouTube is gating it behind a sign-in/age check that
  the script can't pass.
- `live` — It's a live stream currently in progress; there's no finished
  transcript yet. Suggest trying again after it ends.
- `unavailable` — Removed, deleted, or the ID/URL doesn't resolve to a real
  video. Double-check the link with the user.
- `network_blocked` — The environment's network policy is blocking outbound
  requests to YouTube (this happens in some sandboxed/cloud Claude Code
  sessions with restricted egress — check `curl -sS
  "$HTTPS_PROXY/__agentproxy/status"` if `HTTPS_PROXY` is set and you want
  to confirm). Explain this is an environment restriction, not a bug in the
  request, and that it should work in a session with normal internet
  access (e.g. local Claude Code).
- `dependency_missing` — Couldn't install `yt-dlp` or
  `youtube-transcript-api` (e.g. no access to PyPI). Same idea: an
  environment limitation, tell the user plainly.

In every failure case, stop here — don't fabricate a summary from the video
title alone.

## Step 3 — Read the transcript and pull out bullets

Read through the `transcript` array yourself (you're the summarizer here —
no external API call needed) and pull out bullets, keeping the `start`
timestamp of the moment each bullet comes from.

For a very long transcript (roughly 90+ minutes / a huge JSON array), don't
try to hold every word in working memory equally — skim for structure first
(topic shifts, repeated emphasis, numbers, "the big thing is...", Q&A
segments), then go back for exact quotes/figures in the sections that matter
most. Bullets should be information-dense paraphrases in your own words,
not verbatim transcript slices — except for the Quotes category, which
should be verbatim.

### Categories and colors

Use these five categories with these fixed colors as your default — they
cover most videos and keep the color meaning consistent if the user
summarizes several videos in a row:

| Category | Meaning | Color |
|---|---|---|
| Key Takeaways | The core points — what you'd tell a friend in 30 seconds | green |
| Facts & Stats | Concrete data, numbers, dates, named studies/sources mentioned | blue |
| Warnings & Caveats | Myths debunked, common mistakes, "don't do X", exceptions/limitations | amber |
| Notable Quotes | Verbatim, quotable lines — keep exact wording | purple |
| Action Items | Concrete next steps the viewer could actually do | teal |

Adapt to the content rather than forcing every video into all five:

- A tutorial/how-to video: lean on Key Takeaways + Action Items + Warnings
  (common mistakes). Facts & Stats can be thin or dropped if there's
  nothing quantitative.
- A news/explainer video: lean on Facts & Stats + Key Takeaways. Action
  Items can be dropped entirely if there's nothing actionable.
- A podcast/interview: Notable Quotes carries more weight; consider adding
  a per-guest or per-topic grouping under Key Takeaways if the conversation
  covers distinct segments.
- Skip any category that would end up empty or padded with filler — an
  omitted section beats a section with one weak, obvious bullet in it.

Every bullet should trace back to a real moment in the transcript. Keep the
`start` timestamp (in seconds) for each bullet so it can be linked.

## Step 4 — Build the HTML artifact

Before writing the HTML, load the `artifact-design` skill (via the Skill
tool) to calibrate visual weight for this piece — it's a short reference
document, not a dashboard, so keep the design restrained rather than
building out a heavy layout.

Structure to build:

1. **Header**: video thumbnail, title (linked to the source URL), channel
   name, and duration if available.
2. **Body**: one section per category actually used, each visually tagged
   with its color (e.g. a colored left border or a small colored pill next
   to the category heading — not colored body text, which hurts
   readability). Bullets within a section are a normal list.
3. **Timestamp links**: turn each bullet's timestamp into a link back to
   that exact moment: `{video_url_without_query}&t={round(start)}s` — e.g.
   `https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=125s`. Render it as a
   small `12:05` — style timestamp chip before or after the bullet text, not
   as a full inline URL.
4. Follow the Artifact tool's theme-awareness rules (light/dark tokens, no
   color defined only inside one media block) — a color-coded summary is
   useless if the colors wash out or clash in dark mode.

Publish with the `Artifact` tool:
- `title`: the video's title (trimmed if very long) — a name, not a
  description.
- `description`: one sentence, e.g. "Color-coded summary of {channel}'s
  video on {topic}."
- `favicon`: pick one emoji that fits the category mix (e.g. 🎥 as a safe
  default).

## Notes

- This skill does not download or store video/audio — only text (captions)
  and small metadata fields (title, channel, duration, a thumbnail URL).
- If the transcript is auto-generated captions, expect occasional
  transcription errors (misheard words, no punctuation) — use judgment when
  a word is obviously a mis-transcription of a name or term and quietly
  correct it in your bullets (but never in a verbatim Quote).
- The bundled script is the only supported way to fetch the transcript in
  this skill — don't shell out to `curl youtube.com/...` directly or hand-roll
  a different scraping approach; the script already encodes the fallback
  chain and error handling this skill depends on.
