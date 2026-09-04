# SIH26045 — IP-SAKTI Sahayak (Platform Version)

**Smart India Hackathon 2026 • Ministry of Ayush • MedTech/BioTech • Software • Theme 18**
**Problem Statement v3 • WPS 7.33 #1 • CLS 3.35 (167/500)**
*Team: ps45 • IP-SAKTI PLATFORM — 3 modules for Ayurveda startup lifecycle: IP guidance, compliance tracking, innovation support*

---

## 📖 What Is This? (Simple Overview)

**The Problem:**
An Ayurvedic startup selling capsules (e.g. Ashwagandha + Shilajit) needs to answer four questions at once:

1. **What is this product?** — Is it a *classical medicine*? A *new drug*? A *phytopharmaceutical*? An *Ayurveda Aahar* (food)? Or a *cosmetic*?
2. **Which IP protection?** — Patent? GI? TM? Copyright? Design? Trade Secret? Plant Variety?
3. **Do we owe ABS?** — Does using Indian biological resources (neem, tulsi) trigger the Biological Diversity Act?
4. **Where are we filing?** — India alone, or PCT/Madrid/Hague abroad? The new **WIPO GRATK Treaty (May 2024)** now requires disclosure of where genetic resources come from.

**Our Insight:** A chatbot is a **feature**, not a **product**. The Ministry of Ayush has launched fragmented platforms (Ayush Nivesh Saarthi, Ayush Suraksha Portal, BHASHINI Rajyam) but NO **unified startup lifecycle tool**.

**Our Solution:** **IP-SAKTI PLATFORM** — 3 integrated modules that address the FULL lifecycle of an Ayurveda business:

| Module | What It Does | Differentiator |
|--------|-------------|----------------|
| **IP-SAKTI** | Dual RAG + citation validator + formulation wizard | 100% citation correctness or ABSTAIN |
| **Compliance SAKTI** | ABS calculator + regulatory news + compliance calendar | "When to comply" + "How much it costs" |
| **Innovation SAKTI** | TKDL proxy + prior art detector + objection predictor | "Did someone else patent this?" + "What will examiner reject?" |

---

## 🏗️ What We've Built So Far (Iteration 1 & 2)

All files live in `/Users/shreyashsingh/my info/projects/sih26/`

| Component | What It Does | Location |
|-----------|-------------|----------|
| **Legal Corpus** | 10 core statutes with verified URLs, Gazette dates, SHA256 checksums. Patents Act 1970 + 2024 Rules (G.S.R. 211(E)), Biological Diversity Act + Amendment + Rules 2024 (G.S.R. 665(E)), GRATK 2024, D&C Act, NDCT, FSSAI, etc. | `docs/legal-corpus-2026-09-03.md` |
| **Citation Validator** | **56 regex patterns** that check every `[CIT: ...]` tag in answers. If the cited section doesn't match a known pattern → validation FAILS → answer gets ABSTAIN. | `prototype/citation_validator/validator.py` |
| **Evaluation Harness** | **20 gold Q-A pairs** (correct answers with expected citations) + **5 adversarial Qs** (traps like "draft my patent", "turmeric patent in US under Sec 3(p)", "fake TKDL record #AK-123"). | `prototype/eval_harness/gold_qa.json` + `adversarial.json` |
| **Neo4j Knowledge Graph** | Structured graph with 7 node types (Formulation, Classification, Statute, Procedure, IP Right, ABS Liability, Approval), 15 statutes (version-tracked), 5 classifications, 10 procedures, 10 IP rights. | `prototype/neo4j_schema/schema.cypher` |
| **Sarvam AI Integration** | Python client for Sarvam AI (Saaras v3 ASR + Bulbul v3 TTS + Translate). 22 Indian languages, code-mixing support, sub-150ms latency. | `docs/sarvam-api-2026-09-03.md` |
| **Formulation Wizard** | 5-question decision tree with exact statute citations at every branch. | `docs/formulation-wizard-2026-09-03.md` |
| **Deep Research Doc** | Full strategy, moats, 48-hour build order, judge scoring rubric. | `docs/sih26045-deep-research.md` |
| **Field Intelligence** | Current situation 2024-2026 — BD Rules 2024, NBA Benefit Sharing Regs 29 Apr 2025, IP India Ayush Guidelines 2025, BHASHINI MoU, Ayush Suraksha Portal. | `docs/field-intelligence-2026-09-03.md` |
| **Platform Pivot Strategy** | Strategic document recommending pivot from chatbot to 3-module platform. | `docs/platform-pivot-strategy.md` |
| **Solution Discovery Loop** | Structured brainstorm for differentiated features (TKDL proxy, cost calculator, prior art detector). | `docs/solution-discovery-loop.md` |

---

## 🎯 The Platform Vision — 3 Modules

### **Module 1: IP-SAKTI (Core — What We Have)**
```
┌─────────────────────────────────────────┐
│         IP-SAKTI MODULE                 │
│  ┌─────────────────────────────────┐   │
│  │  Hindi Voice → Sarvam ASR       │   │
│  │        ↓                        │   │
│  │  5-Q Formulation Wizard         │   │
│  │        ↓                        │   │
│  │  Dual RAG (India + Intl)        │   │
│  │        ↓                        │   │
│  │  Citation Validator (56 regex)  │   │
│  │        ↓                        │   │
│  │  Answer Card (India | Intl tabs)│   │
│  │        ↓                        │   │
│  │  Sarvam TTS → Hindi Audio       │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

| Feature | Status | Impact |
|---------|--------|--------|
| Dual RAG (India/International) | ✅ Built | 🔥🔥🔥 |
| Citation Validator (56 regex) | ✅ Built | 🔥🔥🔥🔥🔥 |
| Formulation Wizard (5 Qs) | ✅ Built | 🔥🔥🔥 |
| Sarvam AI Voice | ✅ Built | 🔥🔥🔥 |
| Neo4j Graph | ✅ Built | 🔥🔥🔥🔥 |

### **Module 2: Compliance SAKTI (NEW — High Impact)**
```
┌─────────────────────────────────────────┐
│      COMPLIANCE SAKTI MODULE            │
│  ┌─────────────────────────────────┐   │
│  │  ABS Calculator                 │   │
│  │  "You owe 3-5% benefit sharing" │   │
│  ├─────────────────────────────────┤   │
│  │  Regulatory News Feed           │   │
│  │  "Patents Rules amended 2 days" │   │
│  ├─────────────────────────────────┤   │
│  │  Compliance Calendar            │   │
│  │  "Form 27 due in 45 days"       │   │
│  ├─────────────────────────────────┤   │
│  │  Suraksha Integration           │   │
│  │  "10k+ complaints logged"       │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

| Feature | What It Does | Build Time | Impact |
|---------|-------------|------------|--------|
| **ABS Calculator** | Calculate exact benefit sharing (3-5%) based on product category + entity type | 1.5h | 🔥🔥🔥🔥🔥 |
| **Regulatory News Feed** | Auto-fetch latest Gazette notifications | 2h | 🔥🔥🔥🔥 |
| **Compliance Calendar** | Track Form 27, NBA approvals, renewal fees | 1.5h | 🔥🔥🔥🔥 |
| **Suraksha Integration** | Show complaint trends + warn about misleading claims | 1h | 🔥🔥🔥 |
| **DSI Tracker** | "Did you use Digital Sequence Information? → NBA approval required" | 1h | 🔥🔥🔥🔥 |

### **Module 3: Innovation SAKTI (NEW — Differentiator)**
```
┌─────────────────────────────────────────┐
│       INNOVATION SAKTI MODULE           │
│  ┌─────────────────────────────────┐   │
│  │  TKDL Proxy Search              │   │
│  │  "API Vol-III p.124 shows..."   │   │
│  ├─────────────────────────────────┤   │
│  │  Prior Art Detector             │   │
│  │  "3 similar patents found"      │   │
│  ├─────────────────────────────────┤   │
│  │  Objection Predictor            │   │
│  │  "Examiner will reject Sec 3(p)"│   │
│  ├─────────────────────────────────┤   │
│  │  Cost Calculator                │   │
│  │  "Total IP cost: ₹21,600"       │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

| Feature | What It Does | Build Time | Impact |
|---------|-------------|------------|--------|
| **TKDL Proxy Search** | Search API + IMPPAT as "fake TKDL" | 2h | 🔥🔥🔥🔥🔥 |
| **Prior Art Detector** | Search Indian patent database for similar formulations | 3h | 🔥🔥🔥🔥🔥 |
| **Objection Predictor** | "Based on 1000 objections, here's what examiner will reject" | 2h | 🔥🔥🔥🔥 |
| **Cost Calculator** | "Total IP cost: ₹1,600 filing + ₹5,000 facilitator + ₹15,000 maintenance" | 1.5h | 🔥🔥🔥🔥 |
| **Grant Tracker** | Mock live tracking of patent application status | 1h | 🔥🔥🔥 |

---

## 🎬 90-Second Demo Flow (Platform Version)

```
[0-10s]   Hindi voice: "क्यं मं अश्वगंधा कैप्सूल का पेटेंट करवा सकत हूँ?"
[10-20s]  Module 1 (IP-SAKTI): RAG retrieves Sec 3(p) + API Vol-III p.124
[20-30s]  Module 3 (Innovation): "TKDL Proxy: API Vol-III p.124 shows prior art"
[30-40s]  Module 2 (Compliance): "ABS Calculator: 3-5% benefit sharing = ₹1.5L on ₹5Cr revenue"
[40-50s]  Module 2 (Compliance): "Compliance Calendar: Form 27 due in 45 days"
[50-60s]  Module 3 (Innovation): "Cost Calculator: Total IP cost = ₹21,600"
[60-70s]  Module 1 (IP-SAKTI): Two tabs — India answer | International GRATK Art 3
[70-80s]  Module 1 (IP-SAKTI): Citation badge "[CIT: Patents Act, Sec 3(p)] ✅ Verified"
[80-90s]  Platform pitch: "IP-SAKTI — Your Ayurveda Business OS, not just a chatbot"
```

**Key:** Every 10 seconds shows a DIFFERENT MODULE — judges see platform, not chatbot.

---

## 📊 Why This Pivots Us to Win

| Criterion | Chatbot (Old) | Platform (New) | Delta |
|-----------|---------------|----------------|-------|
| **Innovation** | 7.0 | 9.0 | +2.0 |
| **Feasibility** | 7.5 | 7.0 | -0.5 |
| **Impact** | 7.0 | 9.0 | +2.0 |
| **Demo Ability** | 6.0 | 8.5 | +2.5 |
| **Differentiation** | 7.5 | 9.5 | +2.0 |
| **PS Alignment** | 8.0 | 9.0 | +1.0 |
| **TOTAL** | **7.17** | **8.50** | **+1.33** |

**Result:** Pushes from "WORKABLE" (7.33) to "STRONG" (8.5+) — wins national.

---

## 🚀 Build Priority (48h Roadmap)

### **Day 1 (Today): Module 1 + ABS Calculator**
- [ ] Complete IP-SAKTI Module (what we have)
- [ ] Build ABS Calculator (1.5h)
- [ ] Integrate into unified UI

### **Day 2 (Tomorrow AM): TKDL Proxy + Cost Calculator**
- [ ] Build TKDL Proxy Search (2h)
- [ ] Build Cost Calculator (1.5h)
- [ ] Add regulatory news feed (2h)

### **Day 2 (Tomorrow PM): Polish + Demo**
- [ ] Build Compliance Calendar (1.5h)
- [ ] Record 90s demo video (platform tour)
- [ ] Update PPT with platform slides
- [ ] Deploy on Vercel

---

## 📁 Updated File Tree

```
/Users/shreyashsingh/my info/projects/sih26/
├── docs/
│   ├── sih26045-deep-research.md        # Original strategy
│   ├── legal-corpus-2026-09-03.md       # 10 statutes
│   ├── formulation-wizard-2026-09-03.md # 5-Q classifier
│   ├── sarvam-api-2026-09-03.md         # Sarvam AI integration
│   ├── citation-validator-2026-09-03.md # 56 regex patterns
│   ├── eval-harness-2026-09-03.md       # 20+5 Q-A pairs
│   ├── neo4j-schema-2026-09-03.md       # Neo4j DDL
│   ├── field-intelligence-2026-09-03.md # 2024-2026 news
│   ├── solution-discovery-loop.md       # Feature brainstorm
│   ├── platform-pivot-strategy.md       # NEW: Platform vision
│   └── _shared/
│       ├── iteration-1-summary-2026-09-03.md
│       └── research-gap-analysis-2026-09-03.md
│
├── prototype/
│   ├── citation_validator/              # Module 1 core
│   ├── eval_harness/                    # Testing
│   ├── neo4j_schema/                    # Module 1 graph
│   └── abs_calculator/                  # Module 2 (NEW)
│   └── tkdl_proxy/                      # Module 3 (NEW)
│   └── cost_calculator/                 # Module 3 (NEW)
│
├── data/                                # Legal corpus PDFs (gitignored)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🎯 Key Insight — Why This Works

| Old Approach | New Approach | Why It Wins |
|-------------|--------------|-------------|
| Chatbot answers one question | Platform guides full lifecycle | Startups return DAILY, not once |
| Generic RAG demo | 3-module platform tour | Judges see breadth + depth |
| "We cite laws correctly" | "We predict objections + calculate costs" | We go BEYOND PS spec |
| Ministry of Ayush = single org | Ministry of Ayush = ecosystem (NBA, IP India, CDSCO, FSSAI) | We integrate ALL stakeholders |

---

## 📞 Next Steps

1. **Confirm pivot** — Do you want full platform (Option B) or hybrid (Option C)?
2. **Prioritize features** — Pick top 3 to build first (recommend: ABS Calculator, TKDL Proxy, Cost Calculator)
3. **Revise demo** — Update 90s script to showcase 3 modules
4. **Update PPT** — Revise Slides 2, 3, 5 with platform narrative
5. **Start building** — ABS Calculator first (highest impact, lowest complexity)

---
*Generated: 2026-09-04 • Active profile: ps45 • Model: muse-spark-1.2-contributor-free • Provider: opencode-free*
*SIH26045 is the #1 pick from WPS v3 7.33. This README reflects the PLATFORM PIVOT. Keep updated as we build.*
