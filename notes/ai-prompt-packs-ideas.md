# AI Prompt Packs — Idea Log

## 2026-09-23

### The discovery
User asked urgently for faster-to-produce, faster-to-sell digital products (income pressure, Time Management System takes too many personalized iteration rounds to ship quickly). Checked the repo root and found ~29 cover/thumbnail image pairs already made (`cover_1280x720_*.png` / `thumb_600x600_*.png`), committed months ago with no accompanying product content. Opened one (`cover_1280x720_life-coach.png`) and it spells out the actual product: **"The [Niche]'s AI Prompt Pack" — 40 done-for-you AI prompts**, organized into 4 categories (Sessions, Content, Client Comms, Offers for the coach example), works with ChatGPT/Claude/Gemini/any AI tool.

This means the catalog structure, branding, and niche list were already planned — only the actual prompt content was never written. That's a much better fit for "fast + sellable" than the Blocks system: it's systematized (same 4-category, 40-prompt shape per niche) rather than personal, so it doesn't need round after round of individual taste-driven iteration.

### Existing catalog (from cover filenames — all still need content written)
**Niche packs (~20):** airbnb-host, amazon-fba-seller, chiropractor-wellness, etsy-seller, faith-leaders, fitness-coach, freelance-writer, home-contractor, life-coach, nonprofit-director, real-estate-agent, restaurant-owner, social-media-manager, teacher, therapist-private-practice, virtual-assistant, wedding-photographer, wedding-planner, yoga-instructor, youtube-creator.

**Bundles (7):** bundle-new-5pack, bundle-original-5pack, bundle-set2-5pack (a/b), bundle-set2-10pack, bundle-mega-10pack, bundle-ultimate-20pack — presumably curated groupings of the niche packs above at different price points.

**Meta/skill guides (2):** skill-guide-ai-prompt-packs, skill-guide-website-templates — likely "how to use AI prompt packs" and a separate (currently unspecified) website-templates product line, not yet explored.

### First one built
`products/ai-prompt-packs/life-business-coach/` — full 40-prompt pack for Life & Business Coach, matching the existing cover's branding (dark brown/orange). Structure: cover page, "How to Use This Pack" page (5 steps + a client-privacy note), then 4 category pages of 10 prompts each. Built as proof of concept — pushed for user review.

### Plan going forward (not yet confirmed by user)
Once the Life & Business Coach pack is approved as the right format/tone/quality bar, batch out the remaining ~19 niche packs using the same structure (4 categories × 10 prompts, tailored per niche) without needing per-pack review cycles — the format is now proven, so speed is the point. Bundles can likely be assembled mechanically once enough individual packs exist (just merge PDFs + a combined cover). Website-templates skill guide is a different product shape, not yet scoped.

### Open questions
- Confirm the 4 categories generalize across all niches, or do some niches need different category names (e.g., "Client Comms" may not fit a restaurant-owner or Etsy seller as cleanly)?
- Where will these actually sell (Etsy, Gumroad, own site)? Affects whether a licensing/usage-rights blurb is needed in the pack.
- Bundle contents/pricing — which packs go in which bundle tier?
