# Idea: Guided Bible Study AI Chatbot

Status: concept / not yet built
Captured: 2026-08-22

## One-line pitch

An AI chatbot with deep, comprehensive knowledge of the Bible and related
fields (theology, history, archaeology, textual criticism, comparative
religion, philosophy) that can hold the deepest conversation imaginable
about existence in general and Christianity/religion in particular —
paired with preloaded guided study plans that teach a user everything
about the Bible, including a personalized whole-Bible reading plan and
in-depth study of hundreds of individual passages/topics.

## Core experience

1. **Conversational depth** — not a Q&A bot that gives shallow verse
   lookups. It should be able to go as deep as the user wants: original
   language (Hebrew/Greek/Aramaic) word studies, historical-critical
   context, different denominational/theological interpretations,
   philosophical and apologetic angles, comparisons with other religions
   and worldviews, honest engagement with hard/skeptical questions.
2. **Guided plans, not just open chat** — preloaded, structured
   curricula the user can start at any time:
   - **Whole-Bible reading plan**, personalized to pace (e.g. 90 days,
     1 year, 3 years), reading style (chronological, canonical,
     Old/New Testament interleaved), and available daily time.
   - **Deep-dive study tracks** covering hundreds of topics/passages in
     depth (e.g. "the Sermon on the Mount," "the Exodus narrative,"
     "Pauline theology of grace," "the Psalms of lament," "Genesis 1-3
     and creation," "Revelation's symbolism," "the historical Jesus,"
     "textual transmission of the NT," etc.), each combining scripture,
     commentary, historical background, and discussion questions.
3. **Personalization** — onboarding captures the user's background
   (new believer, lifelong Christian, skeptic/seeker, academic
   interest, etc.), goals, and time budget, and the chatbot assembles a
   plan from there. Progress is tracked so the plan adapts over time.
4. **Supporting materials per session/topic**:
   - Printable/exportable worksheets (fill-in study guides, reflection
     questions, cross-reference charts, memory-verse cards).
   - Curated additional reading (commentaries, articles, books,
     original-language resources) with citations.
   - Discussion/reflection prompts suitable for journaling or small
     groups.

## Content/knowledge scope

- Full biblical text (multiple translations) with cross-references.
- Historical and cultural background (ANE history, Second Temple
  Judaism, Greco-Roman world, archaeology).
- Original languages: Hebrew, Aramaic, Koine Greek — word studies,
  grammar notes, lexicons.
- Theology across major traditions (Catholic, Orthodox, Protestant
  denominations) presented fairly, with the bot's own default stance
  (if any) made transparent rather than hidden.
- Comparative religion and philosophy of religion, so conversations
  about existence, meaning, and other faiths are handled with the same
  depth as in-tradition Christian questions.
- Church history and how the canon/text came together (helps with
  skeptic-style questions about reliability, authorship, textual
  variants, etc.).

## Format / delivery

Not yet decided — options to weigh later:
- **Desktop app** (this was the explicit requirement: whatever gets
  built should be available to the desktop app too, not just a web
  chat).
- Companion mobile/web app for on-the-go reading-plan check-ins.
- Underlying engine: a Claude-based chatbot with a curated system
  prompt/knowledge base + retrieval over primary sources (Bible text,
  commentaries, lexicons) rather than relying purely on model memory,
  so citations stay accurate and verifiable.
- Worksheets/reading generated as exportable PDFs or markdown.

## Open questions for later

- Which Bible translation(s) to ship by default, and licensing for
  translation text + commentary/reference content.
- How much of the content is generated on-the-fly by the model vs.
  pulled from a fixed, curated study-plan library (accuracy/trust
  tradeoff).
- Whether this becomes its own product/app, or a mode inside an
  existing app.
- Monetization: free vs. paid plans, one-time purchase vs.
  subscription (this repo already contains cover/thumbnail assets for
  a "faith-leaders" prompt pack — possible relation/cross-sell).

## Next steps (not started)

- [ ] Decide delivery format (desktop app architecture, tech stack).
- [ ] Draft the onboarding flow / personalization questionnaire.
- [ ] Draft the structure of one full deep-dive study module as a
      template (e.g. "Sermon on the Mount") to validate the format
      before scaling to hundreds of topics.
- [ ] Decide translation/content licensing.
