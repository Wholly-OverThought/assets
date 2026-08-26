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

### Build order / product roadmap
Two separate products to start, built one at a time:
1. **Time Management System** — build this first.
2. **Journal** — build second.

While building, expect discussion of both to overlap/interleave in conversation — but they stay two distinct products for now, not merged.

Down the line, likely (not decided) that they get joined together into something bigger — either the two combined, or combined plus something else added in.
