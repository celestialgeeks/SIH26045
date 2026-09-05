# SIH26045 — IP-SAKTI Sahayak 2.0
## Final 6-Slide PPT Content (Official SIH2026 Template)

**Team:** PrajnaPath (6) — IPS Academy, Indore
**Problem Statement:** SIH26045 | **Organization:** Ministry of Ayush
**Theme:** MedTech / BioTech / HealthTech | **Category:** Software

---

# SLIDE 1 — TITLE

## Text for PPT

```
SMART INDIA HACKATHON 2025
• Problem Statement ID – SIH26045
• Problem Statement Title – IP-SAKTI Sahayak
• Theme – MedTech / BioTech / HealthTech
• PS Category – Software
• Team ID – [fill on portal]
• Team Name (Registered on portal) – PrajnaPath
```

### Large Title on Slide

```
            IP-SAKTI SAKHAYAK 2.0
    Enhancing India's IP Sakta Tool for Ayurveda
         Multilingual · Source-Cited · Judge-Ready
```

### Tagline (under title)

```
Five modular features built ON TOP of the Ministry's
existing IP Sakta — not a new platform.
```

### Bottom-left — Team Block

```
PrajnaPath (6)
IPS Academy, Indore
```

### Bottom-right — QR Code Placeholder

```
┌─────────────┐
│   [ QR ]    │  ← github.com/prajnapath/
│             │     ip-sakti-sahayak
│  github.com │
│  prajna...  │
└─────────────┘
```

### Diagram Layout (Slide 1 visual)

**Shape:** Minimal — a single "IP Sakta → IP Sakta+5" arrow graphic.
- Left: a box labelled **"IP Sakta (Existing Ministry Tool)"** in Ministry blue (#0F2A52)
- Right: a box labelled **"IP Sakta Sahayak 2.0"** in deep green with 5 small icons attached: 📋 Citation Validator · 🔍 TKDL Proxy · ⚖️ ABS Calculator · 🗣️ Sarvam Voice · 🧙 Formulation Wizard
- A bold arrow between them with text **"5 Modular Enhancements"**
- Below the arrow: **"Not a new platform — an enhancement of one the Ministry already owns."**

### Speaker Notes (Slide 1)
- "We are not building a new AI assistant from scratch. The Ministry already has IP Sakta. Our job is to give it 5 modular superpowers."
- "Every feature is self-contained — can be deployed independently, tested independently, and the Ministry can pick any one without taking the whole stack."

---

# SLIDE 2 — SOLUTION IDEA (INNOVATION & UNIQUENESS)

## Title on Slide
```
SOLUTION IDEA
```

## 3-Second Hook (top centre, large font)
```
Your Ayurveda formulation — Patent? GI? New Drug? Classical?
Answered in 90 seconds with source citations, in your language.
```

## Visual — 5 Feature Cards (two rows: 3 top, 2 bottom)

```
╔══════════════════╗  ╔══════════════════╗  ╔══════════════════╗
║  📋  CITATION    ║  ╔══════════════════╗ ║  🗣️  SARVAM     ║
║     VALIDATOR    ║  ║  🔍  TKDL        ║  ║     AI VOICE     ║
║  56 regex, 100%  ║  ║     PROXY SEARCH ║  ║  Hindi↔English   ║
║  or ABSTAIN      ║  ║  API + IMPPAT    ║  ║  22 languages    ║
╚══════════════════╝  ║  TKDL is NDA-only ║  ╚══════════════════╝
                       ╚══════════════════╝
╔══════════════════╗  ╔══════════════════╗
║  ⚖️  ABS         ║  ║  🧙  FORMULATION ║
║     CALCULATOR   ║  ║     WIZARD       ║
║  BD Rules 2024   ║  ║  5-Q decision    ║
║  3–5% benefit    ║  ║     tree         ║
║     sharing %    ║  ║  Classical/Propri- ║
╚══════════════════╝  ║  etary/Phyto/     ║
                       ║  Aahar/Cosmetic  ║
                       ╚══════════════════╝
```

### Each card — small subtitle

| Card | Subtitle |
|---|---|
| Citation Validator | 56 compiled patterns — no LLM guessing its own citations |
| TKDL Proxy Search | Full TKDL is NDA-only; we proxy via API + IMPPAT transparently |
| Sarvam AI Voice | Saaras v3 ASR + Bulbul v3 TTS — sub-150ms, Hinglish code-mix |
| ABS Calculator | BD Rules 2024, DSI=BR update, 3–5% benefit-sharing range |
| Formulation Wizard | 5-question tree — Classify → Route → Cite |

## Unique Value (one-line, bottom centre)
```
Jurisdiction toggle (India 🇮🇳 | International 🌐) — answers never conflated.
```

### Diagram Layout (Slide 2 visual)
- 5 feature cards in a 3+2 grid
- Each card: rounded rectangle, Ministry blue (#0F2A52) background, white icon + text
- A connecting line from a central "IP Sakta 2.0" node to each card (hub-and-spoke)
- Bottom: jurisdiction toggle visual — two toggle buttons (India / International)

### Speaker Notes (Slide 2)
- "Each of these 5 features is a standalone module the Ministry can adopt incrementally."
- "The jurisdiction toggle is the single most important UX decision — we never mix India and international law in one answer."

---

# SLIDE 3 — TECHNICAL APPROACH

## Title on Slide
```
TECHNICAL APPROACH
```

## Architecture Diagram (7 layers, top-to-bottom)

```
LAYER 1  ┌──────────────────────────────────────────────────────┐
         │  FRONTEND — React / Next.js + Tailwind               │
         │  India 🇮🇳 / International 🌐 toggle · voice input    │
         └──────────────────────────────────────────────────────┘
                          │
         ┌────────────────▼─────────────────────────────────────┐
LAYER 2  │  VOICE PIPELINE — Sarvam AI                          │
         │  Saaras v3 ASR (22 langs, sub-150ms)                 │
         │  Bulbul v3 TTS (explanation → voice, citations kept  │
         │  in English)                                         │
         └────────────────▼─────────────────────────────────────┘
                          │
         ┌────────────────▼─────────────────────────────────────┐
LAYER 3  │  AGENTIC ROUTER — FastAPI                            │
         │  Formulation Wizard (5-Q tree) → route to IP/ABS/    │
         │  Export/Compliance sub-agent                         │
         └────────────────▼─────────────────────────────────────┘
                          │
         ┌────────────────▼─────────────────────────────────────┐
LAYER 4  │  DUAL RAG — Qdrant × 2 collections                   │
         │  India collection: Patents Act, BD Act/Rules,        │
         │  D&C Act, FSSAI, GRATK Treaty                        │
         │  International collection: WIPO GRATK, Nagoya,       │
         │  TRIPS, PCT, Madrid, Budapest                        │
         └────────────────▼─────────────────────────────────────┘
                          │
         ┌────────────────▼─────────────────────────────────────┐
LAYER 5  │  KNOWLEDGE GRAPH — Neo4j                             │
         │  7 node types · 15 statutes · 2-hop traversal        │
         │  (Formulation → IP Right → Procedure → ABS)          │
         └────────────────▼─────────────────────────────────────┘
                          │
         ┌────────────────▼─────────────────────────────────────┐
LAYER 6  │  CITATION VALIDATOR — Python `re`                    │
         │  56 compiled regex patterns                          │
         │  ANSWER / PARTIAL / ABSTAIN gate                     │
         └────────────────▼─────────────────────────────────────┘
                          │
         ┌────────────────▼─────────────────────────────────────┐
LAYER 7  │  AUDIT & COMPLIANCE                                  │
         │  audit_log.jsonl · DPDP consent · Gazette-date badge │
         └──────────────────────────────────────────────────────┘
```

*(Design note: single accent gradient top-to-bottom — saffron at Layer 1 fading to deep green at Layer 7.)*

## Tech Stack Table

| Layer | Technology | Why This Choice |
|---|---|---|
| Frontend | **React / Next.js** | Tab-based India/International UI, fast iteration for demo |
| Backend API | **FastAPI (Python)** | Async, auto-docs, easy to wire RAG + validator + graph |
| Vector DB | **Qdrant** (2 collections) | Native payload filtering → hard jurisdiction isolation |
| Embeddings | **BAAI/bge-m3** | Multilingual — embeds Hindi queries against English chunks |
| Knowledge Graph | **Neo4j** | 2-hop traversal for structured legal logic beats pure vector |
| LLM | **Llama-3-70B via Groq** | Fast inference for live demo; swappable per cost/latency |
| Voice (ASR+TTS) | **Sarvam AI** | 22 langs, sub-150ms, native Hinglish code-mixing |
| Citation Validator | **Python `re` (56 patterns)** | Deterministic, auditable — no LLM judging its own citations |
| Audit Log | **JSONL + DPDP consent gate** | Lightweight, human-readable, DPDP-aligned |
| Deployment | **Vercel (FE) + Render (API)** | Zero-ops, demo-ready in hours |

## 6-Step Query Flow (horizontal pipeline, left→right)

```
①         ②           ③          ④           ⑤           ⑥
USER →  ASR      →  RAG     →  VALIDATOR →  CITATION  →  TTS
(voice/   (Saaras    (Dual      (56 regex,  (badge on   (Bulbul v3,
 text,    v3, 22     Qdrant +    ANSWER/    answer     text→voice,
22 langs) languages) Neo4j 2-hop)  ABSTAIN)   [CIT:       target lang)
                                               Sec 3(p)]
                                               ✅ Verified)
```

## Key Metrics Strip (4 large numbers in a row)

| **56** | **100%** | **<150ms** | **100%** |
|---|---|---|---|
| Regex citation patterns | Adversarial abstention rate | Voice latency (Sarvam Fast mode) | India/International isolation |

---

# SLIDE 4 — FEASIBILITY AND VIABILITY

## Title on Slide
```
FEASIBILITY AND VIABILITY
```

### Subtitle (top right)
```
Built to Ship in 48 Hours · Designed to Run in Production
```

## Feasibility — 3 Columns (mirrors winning PPT layout)

| **Technical** | **Resource** | **Legal & Compliance** |
|---|---|---|
| Fully open-source/freemium stack (Qdrant, Neo4j Community, FastAPI) — no exotic hardware | Runs on a single free-tier VM (Render) + Vercel frontend for pilot scale | Every citation traces to a Gazette-dated public document — no paid/proprietary source without explicit logged consent |
| Formulation Wizard is a hardcoded 5-Q state machine (no LLM calls) — deterministic and cheap | 6-person BTech team maps 1:1 onto 7 architecture layers — no single point of overload | DPDP-aligned from day one: consent checkbox + `audit_log.jsonl` |
| Citation validator is pure regex — zero model drift, 100% reproducible output | Sarvam AI and Groq both offer free credits covering hackathon + early pilot volume | Hardcoded "not legal advice" abstention limits liability for a Ministry-facing deployment |

## Challenges & Mitigation — Numbered Pairs (01–05)

| # | Challenge | Mitigation |
|---|---|---|
| 01 | Law changes — corpus goes stale (BD Rules, GRATK ratifications, Patents Rules amendments) | Every chunk carries a Gazette-date badge; version-tracked corpus with quarterly refresh checklist |
| 02 | Citation validator misses a rare statute → false negative | Regex library grows via review loop (30 → 56 patterns and counting); unmatched claims fail safe into ABSTAIN, never a guess |
| 03 | TKDL Proxy mistaken for real TKDL access | UI explicitly labels results "API/IMPPAT — TKDL proxy"; one-click escalation to verified TKDL search via facilitator |
| 04 | Legal nuance lost in Hindi↔English translation | Retrieval and citation always in English; Sarvam translates only the explanation layer, never the statute text |
| 05 | Judges question the "enhances IP Sakta" claim | Framed transparently with dated PIB/Gazette evidence (Ayush Nivesh Saarthi, BHASHINI Rajyam MoU) — not an existing integration we don't have |

### Diagram Layout (Slide 4 visual)
- Left side: 3-col feasibility table (Technical / Resource / Legal)
- Right side: 01–05 challenge↔mitigation pairs as horizontal bars with arrows connecting challenge → mitigation (same visual grammar as Telhan Sathi / Invariants reference decks)
- Use saffron (#FF6B00) for challenge boxes, green for mitigation boxes

---

# SLIDE 5 — IMPACT AND BENEFITS

## Title on Slide
```
IMPACT AND BENEFITS
```

### Opening Tagline (quote style, top)
```
"From a confused founder to a cited, jurisdiction-correct answer — in 90 seconds."
```

## 4-Stakeholder Matrix

| Stakeholder | Pain Today | Impact With IP-SAKTI Sahayak 2.0 |
|---|---|---|
| **Entrepreneur** | Doesn't know Classical vs New Drug vs Aahar vs Phytopharma; risks 6–36 months and ₹1,600–₹50,000 on misrouted filing | Instant classification + cited pathway + ABS estimate, in their own language, before spending a rupee |
| **Examiner / IP Facilitator** | Manually re-explains Sec 3(p), TKDL limits, BD Rules 2024 to every walk-in; backlog rising (64k pending, per BananaIP 2024) | Pre-vetted, cited, jurisdiction-correct queries cut repetitive first-line explanation — time shifts to genuinely complex cases |
| **Ministry of Ayush** | Ayush Suraksha Portal logged 10,000+ misleading-claim complaints; no proactive guidance layer upstream | Citation validator doubles as proactive enforcement/education layer, aligned with Ministry's BHASHINI Rajyam push |
| **Public / Consumer** | No easy way to tell genuine Ayurvedic IP claim from unverified one | Transparent `[CIT: ...]` answers build public trust in Ayush-labelled products |

## Metrics Strip (3 large stat callouts)

| **10K+** | **500+** | **₹50L** |
|---|---|---|
| Registered users — Year-1 pilot target via State Ayush Cell / facilitator network | Queries/day at steady state (~1.25L queries/year at 250 active platform-days) | Estimated annual savings — illustrative model, conservative floor |

## 3 Use Case Scenarios (narrative vignettes)

**Scenario 1 — The First-Time Founder**
A Jaipur founder asks in Hindi, by voice: *"Can I patent my Ashwagandha-Shilajit capsule?"* In seconds: New Drug classification (novel combination), Sec 2(1)(j) + Sec 3(p) analysis, and confirmation no wild-collected bio-resource triggers ABS. She skips a ~₹1,000–15,000 facilitator consultation for a question the tool answers free.

**Scenario 2 — The Exporter**
A Kerala phytopharma company asks about exporting a standardized Giloy extract to the EU. The **International tab** returns GRATK Art 3 disclosure + EMA Herbal Directive requirements — kept separate from the India CDSCO pathway — preventing a costly jurisdiction-mixing filing error.

**Scenario 3 — The Facilitator's Desk**
A State Ayush Cell facilitator pulls up a founder's TKDL-adjacent query. Instead of guessing, the tool returns *"API Vol-III, p.124 — proxy prior art"* and routes to a verified TKDL search only where genuinely needed — freeing the facilitator's time for complex cases.

## ROI Calculation (waterfall diagram)

| Step | Assumption | Calculation |
|---|---|---|
| 1. Query volume | 500 queries/day × 250 active platform-days/year | **125,000 queries/year** |
| 2. Avoided consultations | ~4% of queries would otherwise need a paid facilitator check | 125,000 × 4% = **5,000 avoided consultations/year** |
| 3. Avg. avoided fee | ₹1,000 per first-cut classification + citation check | 5,000 × ₹1,000 = **₹50,00,000 (₹50L) saved/year** |
| 4. Additional (conservative, not counted) | 1-in-200 queries (625/year) prevented from a misfiled application (avg ₹8,000 wasted fee) | **₹50L more** — headline figure is a floor |
| 5. Platform cost | Open-source stack + free-tier hosting at pilot scale | **~₹0–5,000/month** |

**Payback period:** Near-immediate — infrastructure cost is negligible against even the conservative ₹50L/year savings estimate.

### Diagram Layout (Slide 5 visual)
- Top: stakeholder matrix as 2-column table (Pain / Impact)
- Middle: 3 stat callouts in large bold typography with icons
- Bottom: 3 use case vignettes as small narrative cards (smaller text, not competing with stats)
- ROI waterfall as a simple staircase diagram (each step adds to the next, ending in a highlighted "₹50L+" box)

---

# SLIDE 6 — RESEARCH AND REFERENCES

## Title on Slide
```
RESEARCH AND REFERENCES
```

### Subtitle
```
Built on Gazette-Verified Law — Not Guesswork
```

## 10 Statutory Citations (Gazette-Verified)

| \# | Statute / Instrument | Section / Rule | Gazette Ref | Date |
|---|---|---|---|---|
| 1 | Patents Act, 1970 | Sec 3(p) — traditional knowledge bar | — | 1970 (as amended) |
| 2 | Patents (Amendment) Rules, 2024 | Rule 12, Form 27 | **G.S.R. 211(E)** | 15 Mar 2024 |
| 3 | Biological Diversity Act, 2002 | Sec 3(2) — foreign entity approval | — | 2002 |
| 4 | Biological Diversity (Amendment) Act, 2023 | Sec 6 — ABS for commercial use | — | In force 1 Apr 2024 |
| 5 | Biological Diversity Rules, 2024 | Rule 4, Form 1 / Form 2 | **G.S.R. 665(E)** | Notified 22 Oct 2024 |
| 6 | NBA Benefit Sharing Regulations, 2025 | DSI = biological resource | — | 29 Apr 2025 |
| 7 | WIPO GRATK Treaty, 2024 | Art 3 — disclosure of origin | — | Adopted 24 May 2024 |
| 8 | Drugs & Cosmetics Act, 1940 | Sec 3(a), First Schedule | — | 1940 (as amended) |
| 9 | New Drugs & Clinical Trials Rules, 2019 | Rule 122E — phytopharma definition | — | 19 Mar 2019 |
| 10 | FSSAI Ayurveda Aahar Regulations, 2022 | Reg 5 — food category | — | 2022 |

## Competitor / Alternative Comparison Matrix

| Capability | **IP-SAKTI Sahayak 2.0** (Ours) | IP Sakta (Existing) | Bhashini | TKDL | Manual CA / Patent Attorney |
|---|---|---|---|---|---|
| Citation-verified answers (or abstain) | ✔ | ✘ | N/A | ✔ (internal only) | ✔ |
| India vs International kept separate | ✔ | ✘ | N/A | N/A | ✔ (if experienced) |
| Formulation classification wizard | ✔ | ✘ | N/A | N/A | ✔ (manual) |
| ABS / benefit-sharing calculator | ✔ | ✘ | N/A | N/A | ⚠ (case-by-case) |
| TKDL prior-art transparency | ✔ (proxy) | ✘ | N/A | ✔ (patent offices only) | ⚠ (via NDA access) |
| Multilingual voice (22 languages) | ✔ | ✘ | ⚠ (infra only) | ✘ | ✘ |
| Public accessibility | ✔ | ✔ | ✔ | ✘ (NDA to 17 offices) | ✘ (paid, by appointment) |
| Cost to founder | Free | Free | Free | N/A | ₹1,000–₹50,000+ |
| Availability | 24/7 | Business hours | 24/7 | N/A | Business hours |
| DPDP-compliant audit trail | ✔ | ✘ (unknown) | N/A | N/A | ⚠ (informal) |

*✔ = Yes · ✘ = No · ⚠ = Partial/Inconsistent · N/A = Not applicable*

## Primary Research — Survey (Placeholder — Run Before Finalizing)

| Finding | Placeholder % | What To Actually Ask |
|---|---|---|
| Entrepreneurs who don't know their product's IP classification | **[XX]%** | "Do you know whether your product qualifies as Classical, New Drug, Phytopharma, Aahar, or Cosmetic?" |
| Entrepreneurs aware of ABS / benefit-sharing obligations | **[XX]%** | "Are you aware that using a bio-resource may require NBA approval and benefit-sharing?" |
| Entrepreneurs who consulted a paid CA/attorney before filing | **[XX]%** | "Did you pay for legal consultation before your first IP filing attempt?" |
| Entrepreneurs who would use a free, cited AI assistant | **[XX]%** | "Would you use a free tool that answers IP questions with exact legal citations?" |

> **Action:** Run a 15–20 person survey with Ayurveda founders / IP facilitators before the final pitch. Replace placeholders with real numbers.

## Government Sources (additional)

| Source | Link |
|---|---|
| IP India — Guidelines for Examination of Ayush Related Inventions (2025, 14p) | `ipindia.gov.in/frontend/pdf/patents/guidelines/...` |
| NBA India — Biological Diversity Rules 2024 | `nbaindia.org` |
| Conventus — BD Act Amendment Analysis (Oct 2024) | `conventus.in` |
| PIB — Ayush Nivesh Saarthi Portal Launch (29 May 2025) | `pib.gov.in` |
| DD News — BHASHINI × Ayush MoU (10 Apr 2026) | `ddnews.gov.in` |
| Trilegal — BD Rules 2024 Analysis (Oct 2024) | `trilegal.com` |

## QR Code + Contact Block (bottom of slide)

```
┌─────────────────────────────┐
│                             │
│        [ QR CODE ]          │   ← github.com/prajnapath/
│                             │      ip-sakti-sahayak
│  github.com/                │
│  prajnapath/                │
│  ip-sakti-sahayak           │
│                             │
└─────────────────────────────┘

Team: PrajnaPath (6)  ·  IPS Academy, Indore
Contact: [team-email]@gmail.com  |  +91-[phone]
GitHub:  github.com/prajnapath/ip-sakti-sahayak
Demo:    [drive/youtube link]
```

### Diagram Layout (Slide 6 visual)
- Top: 10 citations as a compact 2-column table (left: statute name bolded, right: Gazette ref + date)
- Middle: Competitor comparison matrix — 5 columns, ✔/✘ grid
- Below matrix: 4 survey findings as large percentage callouts (once real numbers are in)
- Bottom: QR code bottom-right, contact block bottom-left

---

# COLOUR PALETTE & DESIGN GUIDELINES

| Element | Colour |
|---|---|
| Primary (Ministry Blue) | `#0F2A52` |
| Accent (Saffron) | `#FF6B00` |
| Secondary (Deep Green — Ayush) | `#1B5E20` |
| Background (light) | `#F5F5F5` |
| Text (dark) | `#1A1A1A` |
| Success / Verified badge | `#2E7D32` |
| Abstain / Warning | `#C62828` |

### Typography
- **Headings:** Bold, 28–36pt, Ministry Blue
- **Body:** Regular, 14–18pt, dark grey
- **Stats (large numbers):** 48–64pt, Saffron or Deep Green
- **Citations (small):** 10–12pt, muted grey

### General Rules (from winning PPT analysis)
1. **<30 words per slide** in body text — let visuals carry the weight
2. **One visual per slide** — never two competing diagrams
3. **Numbers everywhere** — judges remember stats, not prose
4. **Gazette dates visible** — proves you read the actual law, not a blog
5. **Prototype proof** — QR code to GitHub + demo video
6. **Clean palette** — no more than 3 colours on any slide

---

# CLARIFYING QUESTIONS (Before Final PPT Creation)

1. **Team ID on SIH portal** — What is your registered Team ID? (Slide 1 requires this)
2. **GitHub repo URL** — Is it `github.com/prajnapath/ip-sakti-sahayak` or a different org/name?
3. **Demo video link** — Do you have a YouTube/Drive link for the QR code on Slide 1 & 6?
4. **Contact email & phone** — For the contact block on Slide 6
5. **Real survey numbers** — Have you run a 15–20 person survey yet? If yes, what are the percentages?
6. **Team members** — Should we list names on the title slide, or keep it as "PrajnaPath (6), IPS Academy, Indore"?
7. **PPT tool** — Are you creating this in PowerPoint, Google Slides, or a tool like Tome/Canva? (Affects output format)

---

# NEXT STEPS

1. Answer the 7 clarifying questions above
2. I will generate the final `.pptx` file (or Google Slides-compatible markdown) with all 6 slides populated
3. If you need a live demo script (90-second walkthrough for judges), I can write that next
