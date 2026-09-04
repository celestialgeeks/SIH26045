# SIH26045 — Platform Pivot: From Chatbot to Integrated Ayurveda Business Platform

**Date:** 2026-09-04 | **Team:** ps45 | **Status:** STRATEGIC PIVOT RECOMMENDED

---

## 🎯 YOUR INSIGHT — VALIDATED AGAINST PS & MINISTRY VISION

| Your Concern | PS Alignment | Ministry Vision | Verdict |
|--------------|--------------|-----------------|---------|
| "Chatbot might get eliminated at national level" | ✅ PS says "IP facilitator escalation" — not just Q&A | ✅ Ministry launched **Ayush Nivesh Saarthi** (29 May 2025) — unified platform for investors | **VALID** |
| "All problems of Ayurveda businesses" | ✅ PS mentions ABS, GRATK, jurisdiction, TKDL — MULTIPLE domains | ✅ Ministry wants **end-to-end support** for Ayurveda startups | **VALID** |
| "Latest compliance, updates, advancements" | ✅ PS demands "version-tracked corpus" + "Gazette date badge" | ✅ **Ayush Suraksha Portal** (10k+ complaints) + **BHASHINI Rajyam** (22 languages) | **VALID** |
| "Legal compliance because RAG might hallucinate" | ✅ PS explicitly says "citation correctness or ABSTAIN" | ✅ **IP India 2025 Guidelines** require strict citation | **VALID** |

**Conclusion:** Your instinct is CORRECT. A chatbot is a **feature**, not a **product**. The Ministry wants a **platform**.

---

## 📊 CURRENT STATE vs. DESIRED STATE

### **Current State (What We Built)**
```
┌─────────────────────────────────────┐
│     IP-SAKTI Chatbot (RAG)          │
│  ┌─────────────────────────────┐    │
│  │ 5-Q Wizard → Dual RAG →     │    │
│  │ Citation Validator → Answer │    │
│  └─────────────────────────────┘    │
│  + Sarvam AI voice                  │
│  + Neo4j graph                      │
└─────────────────────────────────────┘
```

**Problem:** This is a **single-use tool**. Startup asks one question, gets answer, leaves. No retention, no workflow, no integration with Ministry platforms.

### **Desired State (Platform Vision)**
```
┌─────────────────────────────────────────────────────────────┐
│           IP-SAKTI PLATFORM — Ayurveda Business OS           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │ IP-SAKTI    │  │ Compliance  │  │ Innovation  │         │
│  │ Module      │  │ SAKTI       │  │ SAKTI       │         │
│  │             │  │             │  │             │         │
│  │ • Dual RAG  │  │ • ABS Calc  │  │ • TKDL Proxy│         │
│  │ • Wizard    │  │ • News Feed │  │ • Prior Art │         │
│  │ • Cit. Val  │  │ • Calendar  │  │ • Objection │         │
│  │ • Tabs      │  │ • Suraksha  │  │ • Cost Est. │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Shared Layer: Sarvam AI + Neo4j + Audit Log + DPDP  │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

**Benefit:** This is a **platform** that startups use DAILY, not a one-time chatbot.

---

## 🏛️ MINISTRY OF AYUSH VISION — WHAT THEY ACTUALLY WANT

From field intelligence (2024-2026):

| Platform/Initiative | What It Does | What's Missing |
|---------------------|--------------|----------------|
| **Ayush Nivesh Saarthi** (29 May 2025) | Unified policy/incentive/project interface for investors | ❌ No IP guidance, no compliance tracking |
| **Ayush Suraksha Portal** (30 May 2025) | Tracks 10k+ complaints on misleading ads/ADRs | ❌ No proactive guidance, no citation enforcement |
| **BHASHINI Rajyam** (10 Apr 2026) | 22-language integration across Ayush Grid | ❌ No IP-specific translation, no legal domain tuning |
| **IP India Ayush Guidelines 2025** | 14-page framework for AYUSH patent examination | ❌ No public access, no search tool |
| **TKDL** (CSIR + Ayush) | 4.5 lakh formulations, NDA-only access | ❌ Public can't search, no proxy available |
| **NBA Benefit Sharing Regs** (29 Apr 2025) | DSI = biological resource, 8 monetary + 14 non-monetary options | ❌ Complex, no calculator |

**Gap:** The Ministry has **fragmented platforms** but NO **unified startup lifecycle tool**.

**Our Opportunity:** Build the **missing piece** — a platform that connects all these dots for Ayurveda startups.

---

## 🧩 PLATFORM MODULES — WHAT TO BUILD

### **Module 1: IP-SAKTI (Core — What We Have)**
| Feature | Status | Enhancements Needed |
|---------|--------|---------------------|
| Dual RAG (India/International) | ✅ Built | Add DSI=BR update (Apr 2025) |
| Citation Validator (56 regex) | ✅ Built | Add Sec 3(e)/3(i)/3(j)/3(k) coverage |
| Formulation Wizard (5 Qs) | ✅ Built | Add device patentability branch (2025 Guidelines) |
| Sarvam AI Voice | ✅ Built | Add multi-turn dialogue |
| Neo4j Graph | ✅ Built | Add 2025 NBA regulations |

**Pitch:** "We don't just answer questions — we enforce citation correctness or ABSTAIN."

---

### **Module 2: Compliance SAKTI (NEW — High Impact)**
| Feature | What It Does | Build Time | Impact |
|---------|-------------|------------|--------|
| **ABS Calculator** | "You owe 3-5% benefit sharing" — calculate exact amount based on product category + entity type | 1.5h | 🔥🔥🔥🔥🔥 |
| **Regulatory News Feed** | Auto-fetch latest Gazette notifications — "Patents Rules amended 2 days ago" | 2h | 🔥🔥🔥🔥 |
| **Annual Compliance Calendar** | "Form 27 due in 45 days" — track working statements, renewal fees, NBA approvals | 1.5h | 🔥🔥🔥🔥 |
| **Suraksha Integration** | Show "10k+ complaints logged" + warn about misleading ad claims | 1h | 🔥🔥🔥 |
| **DSI Tracker** | "Did you use Digital Sequence Information? → NBA approval required" | 1h | 🔥🔥🔥🔥 |

**Pitch:** "We don't just tell you the law — we tell you WHEN to comply and HOW MUCH it costs."

---

### **Module 3: Innovation SAKTI (NEW — Differentiator)**
| Feature | What It Does | Build Time | Impact |
|---------|-------------|------------|--------|
| **TKDL Proxy Search** | Search API + IMPPAT as "fake TKDL" — show "your formulation appears in API Vol-III p.124" | 2h | 🔥🔥🔥🔥🔥 |
| **Prior Art Detector** | "Did someone else patent this?" — search Indian patent database for similar formulations | 3h | 🔥🔥🔥🔥🔥 |
| **Objection Predictor** | "Based on 1000 patent objections, here's what the examiner will reject" | 2h | 🔥🔥🔥🔥 |
| **Cost Calculator** | "Total IP cost for your product" — government fees + facilitator costs + timeline | 1.5h | 🔥🔥🔥🔥 |
| **Grant Tracker** | "Your patent application status: Pending Examination" — mock live tracking | 1h | 🔥🔥🔥 |

**Pitch:** "We don't just answer — we predict objections and calculate costs before you file."

---

## 🎬 REVISED 90-SECOND DEMO FLOW (Platform Version)

```
[0-10s]   Hindi voice: "क्यं मं अश्वगंधा कैप्सूल का पेटेंट करवा सकत हूँ?"
[10-20s]  IP-SAKTI Module: RAG retrieves Sec 3(p) + API Vol-III p.124
[20-30s]  **TKDL Proxy Result:** "API Vol-III p.124 shows prior art for ashwagandha"
[30-40s]  **ABS Calculator:** "If using neem (foreign entity): 3-5% benefit sharing = ₹1.5L on ₹5Cr revenue"
[40-50s]  **Compliance Calendar:** "Form 27 due in 45 days — here's your timeline"
[50-60s]  **Cost Estimate:** "Total IP cost: ₹1,600 (filing) + ₹5,000 (facilitator) + ₹15,000 (annual maintenance) = ₹21,600"
[60-70s]  **Two Tabs:** India answer | International GRATK Art 3 disclosure
[70-80s]  **Citation Badge:** "[CIT: Patents Act, Sec 3(p)] ✅ Verified"
[80-90s]  **Platform Pitch:** "IP-SAKTI — Your Ayurveda Business OS, not just a chatbot"
```

**Key Difference:** Every second shows a **DIFFERENT MODULE** — not just chatbot Q&A.

---

## 📈 WHY THIS PIVOT WINS AT NATIONAL LEVEL

| Criterion | Chatbot (Current) | Platform (Revised) | Why It Wins |
|-----------|-------------------|-------------------|-------------|
| **Innovation** | 7.0 (RAG + citation) | 9.0 (3 modules + Ministry alignment) | Judges see "platform" not "chatbot" |
| **Feasibility** | 7.5 (buildable in 48h) | 7.0 (slightly more complex) | Still buildable — modular design |
| **Impact** | 7.0 (helps startups) | 9.0 (aligns with Ministry vision) | Ministry already has fragmented platforms — we unify them |
| **Demo Ability** | 6.0 (90s chat) | 8.5 (90s platform tour) | Judges see MULTIPLE features, not one |
| **Differentiation** | 7.5 (citation validator) | 9.5 (TKDL proxy + ABS calc + cost est.) | No team will build 3 modules |
| **PS Alignment** | 8.0 (cites exact sections) | 9.0 (cites + complies + innovates) | Goes BEYOND PS spec |

**Net Score:** 7.47 → **8.5** (pushes from "WORKABLE" to "STRONG")

---

## 🛠️ IMPLEMENTATION ROADMAP

### **Week 1: Core Platform (Internal Hackathon)**
- [ ] Complete IP-SAKTI Module (what we have)
- [ ] Build ABS Calculator (1.5h)
- [ ] Build Cost Calculator (1.5h)
- [ ] Build Compliance Calendar (1.5h)
- [ ] Integrate all 3 modules into unified UI

### **Week 2: Innovation Modules (National Prep)**
- [ ] Build TKDL Proxy Search (2h)
- [ ] Build Prior Art Detector (3h)
- [ ] Build Objection Predictor (2h)
- [ ] Add regulatory news feed (2h)
- [ ] Full demo video (90s platform tour)

### **Week 3: Polish & Deploy (Final Prep)**
- [ ] Deploy on Vercel/Render
- [ ] Record 3 demo videos (Hindi, English, mixed)
- [ ] Update PPT with platform slides
- [ ] Test on Neo4j 5 live
- [ ] Final audit log + DPDP compliance check

---

## 🎯 PPT SLIDE REVISIONS

### **Slide 2: Proposed Solution (REVISION)**
**Before:** "RAG chatbot with dual tabs"
**After:** "IP-SAKTI Platform — 3 modules for Ayurveda startup lifecycle"

```
┌─────────────────────────────────────────────────────┐
│           IP-SAKTI PLATFORM — 3 MODULES             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │
│  │ IP-SAKTI    │  │ Compliance  │  │ Innovation  │  │
│  │ • Dual RAG  │  │ • ABS Calc  │  │ • TKDL Proxy│  │
│  │ • Wizard    │  │ • News Feed │  │ • Prior Art │  │
│  │ • Cit. Val  │  │ • Calendar  │  │ • Objection │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  │
│  Shared: Sarvam AI + Neo4j + Audit Log + DPDP        │
└─────────────────────────────────────────────────────┘
```

### **Slide 3: Technical Approach (REVISION)**
**Before:** "Dual RAG + citation validator"
**After:** "Platform architecture with 3 isolated modules + shared layer"

```
┌─────────────────────────────────────────────────────┐
│  Module 1: IP-SAKTI          Module 2: Compliance   │
│  • Dual RAG (India/Intl)     • ABS Calculator       │
│  • Citation Validator        • Regulatory News Feed │
│  • Formulation Wizard        • Compliance Calendar  │
├─────────────────────────────────────────────────────┤
│  Module 3: Innovation        Shared Layer           │
│  • TKDL Proxy Search         • Sarvam AI (ASR/TTS)  │
│  • Prior Art Detector        • Neo4j Knowledge Graph│
│  • Objection Predictor       • Audit Log + DPDP     │
└─────────────────────────────────────────────────────┘
```

### **Slide 5: Evaluation (REVISION)**
**Before:** "Answer accuracy >0.85, citation correctness 100%"
**After:** "Platform metrics — 3 modules, 50+ test cases, 90s demo"

| Metric | Target | How We Measure |
|--------|--------|----------------|
| **IP-SAKTI accuracy** | >0.85 | 20 gold Q-A pairs |
| **Citation correctness** | 100% or ABSTAIN | 56 regex patterns |
| **ABS calculator accuracy** | 100% | 5 test cases (Form 1 vs Form 2) |
| **Cost estimator accuracy** | ±10% | Compare with IP India fee schedule |
| **TKDL proxy recall** | >0.90 | Compare with API Vol-III index |
| **Platform demo time** | <90s | 3 modules showcased |

---

## ⚠️ RISKS & MITIGATIONS

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Scope creep** — 3 modules too much for 48h | High | Build Module 1 fully, Modules 2+3 as "coming soon" UI |
| **TKDL proxy fake** — judges call out simulation | Medium | Be transparent: "TKDL proxy via API + IMPPAT" — show API Vol-III p.124 |
| **ABS calculator wrong** — legal liability | Medium | Add disclaimer: "For informational purposes only — consult facilitator" |
| **Platform UI complex** — judges confused | Low | Start with Module 1 UI, add tabs for Modules 2+3 |
| **National level competition** — other teams also pivot | Medium | Move FAST — internal hackathon (05 Sep) is our deadline |

---

## ✅ DECISION POINT — YOUR CALL

| Option | Pros | Cons | Recommendation |
|--------|------|------|----------------|
| **A: Keep Chatbot** | Simpler, faster, less risk | Generic, might not win national | ❌ Not recommended |
| **B: Platform Pivot** | Differentiated, aligns with Ministry, wins national | More complex, needs prioritization | ✅ **RECOMMENDED** |
| **C: Hybrid** | Chatbot + 1-2 extra features | Best of both worlds | ✅ **CONSIDER** |

**My recommendation:** Go with **Option C (Hybrid)** — keep the chatbot as Module 1, add ABS Calculator + TKDL Proxy as Modules 2 & 3. This gives you:
- 100% of current work (Module 1)
- 2 high-impact differentiators (Modules 2+3)
- Platform narrative for judges
- Manageable scope for 48h build

---

## 📝 NEXT STEPS

1. **Confirm pivot direction** — Do you want to go full platform (Option B) or hybrid (Option C)?
2. **Prioritize features** — Pick top 3 differentiators to build first
3. **Revise demo flow** — Update 90-second script to showcase platform
4. **Update PPT** — Revise Slides 2, 3, 5 with platform narrative
5. **Start building** — ABS Calculator + TKDL Proxy first (highest impact, lowest complexity)

---

*This is a living strategic document. Update as we discover more.*
