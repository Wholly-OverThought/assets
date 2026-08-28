# Time Management System — Idea Log

Raw capture of thinking so far. Not a spec yet — just getting everything into one place so it's part of the project's working context. Append new entries below rather than rewriting old ones, so the history of how the thinking evolved stays visible.

---

## 2026-08-25

### Context / goal
Building a time management system product. The end deliverable is a template someone can print and use exactly as-is, with the expectation that over time people will customize it to their own details. Likely sold as printable PDFs.

### Core structure: instructions + worksheets
Two layers:
- **Instructions** — spells out almost exactly what to do, step by step (e.g., "you pray, meditate, then journal").
- **Worksheets** — the actual pages someone fills in / uses daily.

### The "block" system
- A separate page/section lists **blocks**: named categories like Hygiene, Body, Productivity, Relationships, etc.
- Each block is a group of tasks.
- The user arranges blocks into their schedule in whatever order they want, and can move them around.
- Open question (not yet decided): what exactly governs the transitions from block to block, and what happens in the gaps between blocks that aren't part of any block.

### Time structure around the blocks
- Regular check-ins, roughly every 15 minutes — also triggered if the person gets stuck or drifts into a distraction.
- A short prayer, 1–5 minutes, roughly hourly.
- These check-ins/prayers and the block system feel like they blend together — currently thinking they're actually part of one single unified system rather than separate things.

### Journal — likely a separate product
Originally considered part of the same system, but journaling turned out to be substantial enough ("kind of a thing all night") that it's probably its own product, not merged into the time-management worksheets — partly a scope/sequencing call, since other products need to get finished and released first.

Two journal components:
- **Morning journal** — future-facing. Journaling about the future *as if already successful*: future-identity familiarization with success. Deliberately displacing the stress/worry/bad-outcome predictions the brain defaults to, by making the positive future feel more real/likely instead. Includes prompts for: things to remember, things to let go of/forget, relationships — all framed around the day ahead.
- **Evening journal** — more traditional in format, but still prompt-driven. Not yet fully specified.
- There will likely be multiple check-ins throughout the day tied to the journal too, working hand-in-hand with the time-management/block system above.

### Open questions / not yet decided
- Exact task lists inside each block.
- Exact ordering logic / rules for how blocks transition into each other.
- What structure governs unscheduled/non-block time.
- Full prompt set for the evening journal.

## 2026-08-26

### Block examples (concrete)
- **Hygiene block**: shower, shave, brush teeth.
- **Body block**: stretch, shoulder PT, lift weights.
- Pattern: each block is a named category, made up of a handful of small, concrete tasks.

### Why blocks have to be movable, not static
Start each day with an ideal time and order for the blocks. But most days something abnormal happens — have to wait to do one, so another gets moved. If the blocks were static/fixed in place, that disruption would be discouraging very fast. Because they're movable, the day can get reshuffled and the person still accomplishes the blocks and doesn't feel like a failure just because the original order didn't hold. The movability is *the* mechanism that protects against the all-or-nothing/discouragement trap.

### Check-in cadence (refined)
Two distinct check-in layers, both running through the day:
- **Hourly prayer / meditation check-ins.**
- **15–30 min mindfulness alarms** (separate from the hourly prayer/meditation — a tighter-interval nudge).

### Core design philosophy
"The contents of the boxes is critical." The system works by **intentionally increasing successes by breaking things down into micro steps.** This is the design principle behind why tasks inside a block are small and concrete (shower, shave, brush teeth — not "do hygiene").

**Origin**: this idea came out of a period in prison — needed ways to pass time, so started building small, structured routines to get through the day. Called them "micro routines" at the time. That's the direct root of the block/micro-step approach.

### Journal structure (refined)
- **AM entry**: forward-looking identity prompting (journaling the day as already successful — future-identity work) plus check-ins.
- **PM entry**: prompts focused on processing (the day that happened).

### Open design question: how do "movable blocks" work as a physical/printed product?
Raised by the user, not yet decided: the ideal mental model is something like a whiteboard with magnets, or a drag-and-drop app — physically/visibly rearranging block pieces. Not yet resolved how to translate that into a printable PDF product, since PDFs are static by nature.

**Constraint**: whatever the mechanism, it can't require cutting out pieces or writing on laminate — not realistically sellable as a plain print product. Needs to work as ordinary paper.

Working direction: a once-printed "block menu" reference page (all blocks + their tasks) plus a daily/weekly schedule page with blank numbered slots — the person writes today's block order into the slots in pen. Reordering during the day = crossing out/rewriting, not physically relocating a piece. Not yet fully decided, but this is the current default approach.

### Print format variants
Some pages will be printed as a folded piece of paper (single-sided, folds down into a smaller booklet/card format). Also want a second version of that same page that's printed both sides and still foldable. Not yet decided which specific pages get which treatment — noting the requirement so page layouts get designed with folding in mind (content placement can't assume a flat single surface).

### Blocks must be defined beforehand — needs its own instructions
The system should include explicit instructions for *how to define your blocks* before you start using the daily pages — this is a setup step, not just "here's a blank template." Likely lives on/near the Blocks page or as part of the Instructions page.

Body block task examples, expanded list: exercise, stretch, PT, jog, situps (these are options/examples to pull from, not all required).

### Edition strategy: Christian version of every variation
Want a Christian edition of each variation of the product (default/standard, adaptive/chronic-pain, etc.) — biblical themes and verses woven in (e.g. the quotes sections become verses). Important constraint: this must be a genuine *option*, not the default framing — don't want non-Christian users to feel like the product is only for Christians. So: a neutral/secular default edition, plus a parallel Christian edition, for each variation of the system. Not yet built for any page; apply once each page's default content is settled, since building the themed version before the base content is finalized would mean redoing it.

### Accessibility variant needed: chronic pain / limited function
Important, not yet designed: a version of the system (at minimum the Body block, possibly broader) for people with chronic pain, debilitating pain, or who can't exercise normally / can't function fully. The standard "stretch, PT, lift weights, jog, situps" task set doesn't work for this audience — needs its own adapted task set and framing, not just "do less of the same things."

### Accessibility variant — not just one swapped block, a full edition
User's read after seeing the adaptive Body block draft: good direction, but dropping just that one block into the otherwise-standard pack and selling it as "the chronic pain version" isn't enough — it needs to be more thoroughly reworked. Two concrete pieces identified:
- **Hygiene needs the same tiered treatment as Body.** For someone chronically ill/disabled, tasks like shower/brush teeth aren't warm-up tasks — they can be the entire day's accomplishment. Needs its own capacity-tiered version (Hygiene-Adaptive), same tier structure as Body-Adaptive.
- **"Doctors & Diagnoses" block replaces Work/School.** For this audience, the structural equivalent of a work/school block is managing appointments, symptom tracking, medication/treatment plans, insurance and paperwork.
This confirms the Chronic Pain / Limited-Function edition is a genuinely separate, reworked pack (multiple adapted blocks), not a single insert page added to the standard pack.

### Accessibility variant — first draft built
Built as `products/time-management-system/pages/block-body-adaptive.html` (drop-in replacement for the standard Body block). Design approach: **tiered by capacity, not fixed by calendar.** Three tiers (Flare/low-capacity, Moderate, Higher-capacity) — the person picks whichever tier matches their body that day, and completing any tier counts as the block being done. This extends the same anti-discouragement principle already used for movable blocks (reordering protects against schedule disruption) to apply to *intensity* instead of *time* — protects against the boom/bust cycle common in chronic pain (pushing hard on a good day, crashing after). Includes a "Pacing, Not Pushing" callout: stop at comfortable effort not pain onset, and explicit permission that choosing the lowest tier is not falling behind. Not yet reviewed by the user.

### Relationships block(s) — reworked
Instead of one generic "Relationships" block, break it into: a separate block for each close family member (and/or gf/bf/spouse — i.e. one block per specific person who matters most), plus one catch-all block for everybody else (general reach-out tasks — post on social media, check in with extended contacts, etc.). Replaces the single generic Relationships block from the earlier example.

### New block idea: "Power Hour"
A block built around a running to-do list of all non-recurring tasks you want to complete (not the repeating daily stuff — the one-off list). During the hour, pick 3 from the list to work on. If there's extra time or energy left, do more — 1 more, 2 more, keep going if it's there. Explicitly: "no rules, only guidelines" — the 3-item pick is a starting guideline, not a hard cap or requirement.

### New block idea: "Set Up Tomorrow"
Idea, not finalized: a block for getting things ready for the next day — laying out tomorrow's blocks, getting things physically ready (clothes, bag, whatever), etc. Would slot in as an evening/end-of-day block alongside Hygiene, Body, Productivity, Relationships.

### Page list (Time Management System document set)
Multiple distinct pages, not one worksheet:
1. **Instructions page** — how to use the whole system.
2. **Layout/overview page** — shows how all the other pages relate to each other (the big picture / map of the system).
3. **Blocks page** — the block menu/reference (block names + their tasks).
4. **Check-in pages** — AM, PM, and hourly; some of these are simple checkmark-style (not full write-in).
5. **Organize-the-blocks page** — where the day's block order gets set/rearranged; possibly the same physical page as the check-in page rather than a separate one (not decided).
6. **Quotes** — important, recurring content throughout the product. On-brand, inspirational, but specifically: clever, truth, paradox, "thinker" tone — not generic motivational-poster style.

More pages likely to get added as this develops.

### Build order / product roadmap
Two separate products to start, built one at a time:
1. **Time Management System** — build this first.
2. **Journal** — build second.

While building, expect discussion of both to overlap/interleave in conversation — but they stay two distinct products for now, not merged.

Down the line, likely (not decided) that they get joined together into something bigger — either the two combined, or combined plus something else added in.
