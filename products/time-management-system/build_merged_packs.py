#!/usr/bin/env python3
"""
build_merged_packs.py — Assembles the Standard and Adaptive Time Management
System packs from individually-rendered page PDFs, then overlays page
numbers and a 4-step mini-map ("Set Up / Blocks / Daily Use / Check-In")
on every page.

Page numbers and the mini-map are added here, at merge time, rather than
hardcoded into each source HTML page. Instructions spans 2 physical pages,
and several pages (Daily Organizer, Check-In, Relationships, Blank Blocks)
are shared between the Standard and Adaptive packs at different absolute
positions — hardcoding numbers per-file broke every time either pack's
length changed. Doing it here means it's always correct for whichever
pack is being assembled.

Usage: python3 build_merged_packs.py
Run from products/time-management-system/ (expects pdf/*.pdf to already
be rendered from pages/*.html).
"""

import fitz  # pymupdf
from pathlib import Path

BASE = Path(__file__).parent
PDF_DIR = BASE / "pdf"

STEPS = [("SETUP", "Set Up"), ("BLOCKS", "Blocks"), ("DAILY", "Daily Use"), ("CHECKIN", "Check-In")]

# (source filename stem, display label, step key)
STANDARD_MANIFEST = [
    ("instructions", "Instructions", "SETUP"),
    ("overview", "Overview", "SETUP"),
    ("blocks", "Blocks", "BLOCKS"),
    ("blocks-relationships", "Blocks — Relationships", "BLOCKS"),
    ("blocks-blank", "Blocks — Blank", "BLOCKS"),
    ("blocks-blank-2", "Blocks — Blank (More)", "BLOCKS"),
    ("daily-organizer", "Daily Organizer", "DAILY"),
    ("daily-organizer-foldable", "Daily Organizer — Foldable", "DAILY"),
    ("blocks-foldable-blank", "Blocks — Blank (Foldable)", "DAILY"),
    ("checkin", "Check-In", "CHECKIN"),
]

ADAPTIVE_MANIFEST = [
    ("instructions-adaptive", "Instructions", "SETUP"),
    ("overview-adaptive", "Overview", "SETUP"),
    ("blocks-adaptive", "Blocks", "BLOCKS"),
    ("blocks-relationships", "Blocks — Relationships", "BLOCKS"),
    ("blocks-blank", "Blocks — Blank", "BLOCKS"),
    ("blocks-blank-2", "Blocks — Blank (More)", "BLOCKS"),
    ("block-hygiene-adaptive", "Hygiene — Adaptive", "BLOCKS"),
    ("block-body-adaptive", "Body — Adaptive", "BLOCKS"),
    ("block-doctors-diagnoses", "Doctors & Diagnoses", "BLOCKS"),
    ("daily-organizer", "Daily Organizer", "DAILY"),
    ("daily-organizer-foldable", "Daily Organizer — Foldable", "DAILY"),
    ("blocks-foldable-blank", "Blocks — Blank (Foldable)", "DAILY"),
    ("checkin", "Check-In", "CHECKIN"),
]

INACTIVE = (0.65, 0.65, 0.65)
ACTIVE = (0.09, 0.09, 0.1)


def draw_overlay(page, step_key, page_num, total_pages):
    rect = page.rect
    w, h = rect.width, rect.height
    landscape = w > h

    # Page number — bottom-right corner, small and quiet.
    pn_text = f"{page_num} / {total_pages}"
    pn_fontsize = 6.5
    pn_x = w - 0.42 * 72 if not landscape else w - 0.35 * 72
    pn_y = h - (0.22 * 72 if not landscape else 0.14 * 72)
    page.insert_text((pn_x - fitz.get_text_length(pn_text, fontsize=pn_fontsize, fontname="helv"), pn_y),
                      pn_text, fontsize=pn_fontsize, fontname="helv", color=INACTIVE)

    # Mini-map — small 4-step breadcrumb, bottom-left, current step bolded.
    mm_fontsize = 6.2
    x = 0.65 * 72 if not landscape else 0.5 * 72
    y = h - (0.22 * 72 if not landscape else 0.14 * 72)
    sep = "   ·   "
    for i, (key, label) in enumerate(STEPS):
        active = key == step_key
        color = ACTIVE if active else INACTIVE
        fname = "hebo" if active else "helv"
        text = label.upper()
        page.insert_text((x, y), text, fontsize=mm_fontsize, fontname=fname, color=color)
        x += fitz.get_text_length(text, fontsize=mm_fontsize, fontname=fname)
        if i < len(STEPS) - 1:
            page.insert_text((x, y), sep, fontsize=mm_fontsize, fontname="helv", color=INACTIVE)
            x += fitz.get_text_length(sep, fontsize=mm_fontsize, fontname="helv")


def build_pack(manifest, out_name, title):
    out = fitz.open()
    page_steps = []  # step_key per physical output page

    for stem, _label, step_key in manifest:
        src = fitz.open(str(PDF_DIR / f"{stem}.pdf"))
        out.insert_pdf(src)
        page_steps.extend([step_key] * src.page_count)
        src.close()

    total = out.page_count
    for i in range(total):
        draw_overlay(out[i], page_steps[i], i + 1, total)

    out.set_metadata({"title": title, "author": "Wholly OverThought"})
    out_path = PDF_DIR / out_name
    out.save(str(out_path))
    out.close()
    print(f"{out_name}: {total} pages")


if __name__ == "__main__":
    build_pack(STANDARD_MANIFEST, "time-management-system-v1.pdf", "Time Management System")
    build_pack(ADAPTIVE_MANIFEST, "time-management-system-adaptive-v1.pdf", "Time Management System - Adaptive Edition")
