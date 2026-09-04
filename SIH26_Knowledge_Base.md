# SIH26 Knowledge Base — Winning Strategy, History & PPT Playbook

> Loaded 2026-09-02 | Sources cited inline | For @sih26 consumption

---

## 1. What SIH Is

- **Smart India Hackathon** — world's largest open innovation hackathon (Ministry of Education + AICTE + MIC). Started 2017 with 28k teams, now 600k+ teams/edition, 1.3M+ students, 2,877+ PS historically, 133 startups born.
- **Tracks**: Software (apps, AI, web) + Hardware (IoT, robotics, physical prototypes). 36-hour grand finale at nodal centres.
- **Motto**: "No problem is too big. No idea is too small."

---

## 2. SIH26 Timeline & Rules (2026-09-02 snapshot)

| Milestone | Date |
|---|---|
| PS Release | **25 Aug 2026** (sih.gov.in) |
| Team Registration Deadline | **6 Sep 2026** |
| Internal Hackathons (college level) | **9-15 Sep 2026** (varies by institute) |
| SPOC Nomination → SIH Portal | **till 30 Sep 2026** (extended) |
| National Shortlisting | Sep-Oct 2026 |
| Grand Finale (36h) | **Dec 2026** |

- **Team**: 6 members, ≥1 female, inter-disciplinary encouraged. UG/PG/PhD eligible.
- **Scale 2026**: 226 PS (172 software, 54 hardware), 18 themes, 30+ orgs (ISRO, DRDO, ministries, Godrej, Autodesk, etc.). Full list: `sih.gov.in/sih2024PS` style page + mirrors at `sih-buddy.vercel.app`, `sih-2026-browser.vercel.app`, `codehuntersacademy.com/sih-2026-ps`.
- **SPOC** uploads max 50 teams/institute + event report + photos.

*Sources: thenewviews.com/win-smart-india-hackathon, thenewviews.com/sih-internal-hackathon, dev.to/avinash201199, sih-buddy.vercel.app*

---

## 3. Judging Criteria

| Criterion | What judges look for |
|---|---|
| **Innovation** | Novel, not copied — differentiation from existing solutions |
| **Feasibility** | Can it work IRL with available data/hardware/budget? |
| **Technical Execution** | Clean, working prototype > flashy slides |
| **Impact** | Helps people / govt / industry; measurable outcome |
| **Presentation** | Clear, structured, engaging — 6-slide discipline |

---

## 4. Winning Strategy (from past winners + analysis)

1. **PS Selection = 50% of win** — avoid most popular PS (cut-throat); hunt low-competition, high-impact. Check `sih2024PS` "Submitted Idea(s) Count" — e.g. Student Innovation PS had 500 submissions vs 107 for niche software PS. Use sih-buddy's 5 scores (feasibility, innovation, clarity, effort, demo-ability) + flags.
2. **Feasibility first** — confirm dataset actually exists (not "assumed"), hardware cost < ₹5-10k if hardware track, 90-second demo possible.
3. **Ministry intent** — research the posting org's real pain (e.g. AICTE MIC wants student innovation pipeline, not just code).
4. **Team** — mix juniors+seniors, cross-discipline (coder + designer + domain expert + presenter). Reliability > friendship.
5. **Mentor feedback** before locking PS.
6. **Prototype > PPT** — judges score working code/demo heavily. Even basic prototype beats pure theory.
7. **Scalability & sustainability narrative** — future scope + cost + deployment plan.

*Sources: thenewviews.com/win-smart-india-hackathon, thenewviews.com/how-to-win-smart-india-hackathon*

---

## 5. PPT Knowledge — Official 6-Slide IDEA Presentation Format

**This is THE submission format — not optional.**

Slides (exact from SIH2025/2026 IDEA Presentation Format, still current for 2026):

1. **Problem Statement** — PS ID, organisation, category (software/hardware), theme, title, problem description in your words.
2. **Proposed Solution** — Your idea, innovation, uniqueness, value proposition. Diagrams/flowcharts preferred.
3. **Technical Approach** — Stack, architecture, workflow, algorithms, APIs, hardware components. Block diagram + tech stack table.
4. **Feasibility & Challenges** — Can you build it? Risks + mitigation, dependencies, execution plan. Viability analysis.
5. **Impact, Beneficiaries & Future Scope** — Who benefits, impact metrics, scalability, cost, deployment, future enhancements + prototype/demo link or video.
6. **References & Research** — Papers, datasets, prior work, citations. Ground your claims.

**Design rules (judge-optimized)**:
- Minimal text (≤6 bullets/slide, ≤8 words/bullet), visuals over paragraphs.
- One idea per slide; consistent 16:9 layout; SIH branding optional but clean.
- Architecture diagram + workflow > text wall. Demo link/video QR on slide 5.
- Speaker notes + timing (2-3 min total pitch for internal round).
- Export as editable .pptx (not PDF) for portal upload; keep file < 10MB.

**Template sources**: `si h.gov.in` official template + Scribd mirrors: `SIH2025 IDEA Presentation Format` / `SIH2026 IDEA Presentation Format` (scribd.com/document/1074577964 etc.). Store copies in `reference/sih26/ppt-templates/`.

**Build rule for @sih26**: ALWAYS use `slide-skill` competition route (or free-design) — never raw python-pptx. Follow its QA gates: plan → outline → design_spec → SVG authoring → .pptx conversion → visual review.

---

## 6. End-to-End Flow for Shreyash

```
PHASE 1 DISCOVER (1-2 days)
  scrape all 226 PS → score → shortlist 5 → mentor review → lock 1
  tools: kimi-webbridge (sih.gov.in), web-research, parallel-cli, sih-buddy scoring

PHASE 2 RESEARCH (2-3 days)
  ministry deep-dive + arxiv papers + existing solutions audit + dataset/hardware check + tech stack options
  output: reference/sih26/research-notes/<PS_ID>.md with citations

PHASE 3 BUILD (2-4 weeks)
  plan.md → scaffold repo → prototype (software/hardware) → demo video
  tools: plan skill, github, spike, systematic-debugging, agents-room-orchestrator

PHASE 4 PRESENT (1-2 days)
  6-slide IDEA deck via slide-skill competition route + speaker notes
  output: projects/sih26/ppt/SIH26_<PS_ID>_IDEA.pptx

PHASE 5 SUBMIT
  kimi-webbridge fills sih.gov.in portal → upload PPT → verify nomination via SPOC
```

---

## 7. Useful Links (verify live before use)

- Official PS browser: https://sih.gov.in/sih2024PS (pattern for 2026: /sih2026PS)
- Official home: https://sih.gov.in
- Scored browser: https://sih-buddy.vercel.app (+ /cards, /list)
- Alt browser: https://sih-2026-browser.vercel.app
- Explorer: https://www.codehuntersacademy.com/sih-2026-ps
- GitHub mirror: https://github.com/NoBugNinja/Smart-India-Hackathon-SIH-2026-Problem-Statements
- Winning strategy: https://thenewviews.com/win-smart-india-hackathon, https://thenewviews.com/how-to-win-smart-india-hackathon
- Internal hackathon guide: https://thenewviews.com/sih-internal-hackathon
- PPT template (Scribd): https://www.scribd.com/document/1075380264/SIH2026-IDEA-Presentation-Format
