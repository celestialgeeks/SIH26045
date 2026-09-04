# SIH26 — SIH 2026 IDEA Presentation Playbook (6-Slide Format)

> For @sih26 — this is the ONLY PPT format that gets submitted to SIH portal. Follow exactly.

## Official Slide Budget (6 slides, 2–3 min pitch)

### Slide 1 — Problem Statement
- PS ID (e.g. SIH25099), Organisation (e.g. MathWorks), Category (Software/Hardware), Theme
- Title + Problem in 2-3 lines (your words, not copy-paste)
- Context: who faces this, why now

### Slide 2 — Proposed Solution & Innovation
- One-sentence solution thesis
- Key features (3-5 bullets, visual icons)
- What makes it novel vs existing (USP table: Existing → Gap → Your fix)
- Diagram: high-level concept visual

### Slide 3 — Technical Approach
- Architecture block diagram (frontend → backend → AI/DB → deployment)
- Stack table: language, framework, model, infra, hardware (if any)
- Workflow / sequence (step 1 → 2 → 3)
- APIs / datasets / models used (cite sources)

### Slide 4 — Feasibility & Challenges
- Feasibility: why you CAN build it (data available, hardware cheap, tech mature)
- Risks + mitigation (table: Risk | Impact | Mitigation)
- Execution plan (timeline: week 1 → 4)
- Dependencies & assumptions

### Slide 5 — Impact, Beneficiaries & Future Scope (+ Demo)
- Impact metrics (e.g. "reduces crop disease detection 60% → saves ₹X/acre")
- Beneficiaries (farmers, ministry, citizens...)
- Scalability, cost, sustainability
- Prototype/demo: screenshot + QR/link to video (2-min demo)
- Future scope (3 bullets: scale, monetise, integrate)

### Slide 6 — References & Research
- Papers (arxiv IDs), datasets, government reports, prior SIH winners
- 4-6 citations, APA-ish, with links
- Team details footer (6 members, contact)

---

## Design Discipline (judge-tested)

- **Density**: ≤6 bullets/slide, ≤8 words/bullet. No paragraphs.
- **Visual hierarchy**: Title (32pt) → subtitle → body (18-20pt). One diagram per slide minimum.
- **Palette**: SIH-friendly (navy + teal + white, or ministry brand). High contrast, no neon.
- **Assets**: Architecture diagram (excalidraw style), stack icons, flowchart, impact numbers as big KPIs.
- **File**: Editable .pptx, 16:9, <10MB. Include speaker notes (30-40s per slide).

## Build Command (for @sih26)

Via `slide-skill` competition route:

```bash
# 1. Write outline markdown: projects/sih26/ppt/outline_SIH<id>.md
# 2. Hand-author SVG pages (free-design) OR use competition workflow
# 3. Convert + QA
slide-skill quickstart outline.md --mode ai   # if OPENAI_API_KEY available
# or deterministic fast fallback:
slide-skill quickstart outline.md --mode fast
```

Always QA: `scripts/visual_review.py` + `pptx_delivery_check.py` before claiming done.

## Common Failures to Avoid

- Copy-pasting PS text verbatim → judges flag plagiarism
- No architecture diagram → "how does it work?" penalty
- No demo link → prototype credibility zero
- 10+ slides → auto-reject (strict 6-slide limit for IDEA submission)
- Generic "AI/ML will solve it" without stack specifics → feasibility fail
