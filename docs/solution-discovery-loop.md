# SIH26045 — Solution Discovery Loop
**Date:** 2026-09-04 | **Team:** ps45 | **Goal:** Differentiate from 500 teams

---

## 🔍 STEP 1 — Audit What We Have (Current State)

| Layer | What We Built | Generic? | Differentiated? |
|-------|--------------|----------|-----------------|
| **Core RAG** | Dual India/International collections | ✅ Generic — every team does this | ❌ |
| **Citation Validator** | 56 regex patterns | ⚠️ Partial — unusual but not enough | ⚠️ |
| **Formulation Wizard** | 5-question decision tree | ✅ Generic — standard quiz flow | ❌ |
| **Neo4j Graph** | Formulation→Classification→IP→Procedure | ⚠️ Partial — knowledge graphs are rare | ✅ |
| **Abstention** | Legal advice refusal | ✅ Generic — standard safety pattern | ❌ |
| **Sarvam AI** | Hindi voice pipeline | ⚠️ Partial — Bhashini was also partial | ⚠️ |
| **Audit Log** | JSONL logging | ✅ Generic — standard DPDP pattern | ❌ |

**Verdict:** We have the **foundation** correct, but **zero standout features** that would make judges remember us.

---

## 🎯 STEP 2 — What Judges Actually Score (From Research)

From `08-ranking-reasoning.md`:

| Criterion | Weight | What They Look For |
|-----------|--------|-------------------|
| **Innovation** | 30% | Novelty beyond PS spec — "twist signals" |
| **Technical Feasibility** | 25% | Can 6 BTech students build it in 48h? |
| **Impact** | 20% | Who benefits? Ministry deployment potential? |
| **Demo Ability** | 15% | Can they **see it work in 90 seconds**? |
| **Differentiation** | — | Count of "twist signals" in PS text |

**Key Insight:** Judges scan 500+ demos. They remember:
1. The one that **didn't hallucinate** a citation (we have this)
2. The one with a **visual demo they can touch** (we don't have this)
3. The one that solved a **real pain they felt** (we don't have this)
4. The one that was **fun to watch** (we don't have this)

---

## 💡 STEP 3 — Brainstorm: Differentiated Features

### **Category A: "The Visual Demo" (Demo Ability +15%)**

| Idea | What It Does | Build Time | Impact |
|------|-------------|------------|--------|
| **IP Route Visualizer** | Interactive flowchart: "If you click here → you go there" showing Patent vs GI vs TM paths | 2h | 🔥🔥🔥 |
| **Comparison Matrix** | Side-by-side table: Patent (20 yrs, ₹1600) vs GI (indefinite, ₹5000) vs TM (10 yrs, ₹4500) with pros/cons | 1h | 🔥🔥 |
| **Cost Calculator** | "Total IP cost for your product" — government fees + facilitator costs + timeline | 1.5h | 🔥🔥🔥 |
| **Timeline Gantt Chart** | "Your IP journey: 36 months from filing to grant" with milestones | 1h | 🔥🔥 |
| **Document Generator** | Auto-fill Form 1, Form 2, PCT cover page — downloadable PDF | 3h | 🔥🔥🔥🔥 |

### **Category B: "The Real Pain" (Impact +20%)**

| Idea | What It Does | Build Time | Impact |
|------|-------------|------------|--------|
| **TKDL Proxy Search** | Search API + IMPPAT as "fake TKDL" — show "your formulation appears in API Vol-III p.124" | 2h | 🔥🔥🔥🔥 |
| **Prior Art Detector** | "Did someone else patent this?" — search Indian patent database for similar formulations | 3h | 🔥🔥🔥🔥🔥 |
| **Objection Predictor** | "Based on 1000 patent objections, here's what the examiner will reject" | 2h | 🔥🔥🔥🔥 |
| **ABS Calculator** | "You owe 3-5% benefit sharing" — calculate exact amount based on product category | 1h | 🔥🔥🔥 |
| **Export Readiness Score** | "Your product can export to EU but not US — here's why" | 2h | 🔥🔥🔥 |

### **Category C: "The Workflow" (Feasibility +25%)**

| Idea | What It Does | Build Time | Impact |
|------|-------------|------------|--------|
| **Facilitator Handoff** | One-click "Connect to IP Facilitator" with pre-filled context | 1h | 🔥🔥 |
| **Annual Compliance Calendar** | "Form 27 due in 45 days" — track working statements, renewal fees | 2h | 🔥🔥🔥 |
| **Grant Tracker** | "Your patent application status: Pending Examination" — live tracking | 2h | 🔥🔥🔥 |
| **Abandonment Risk Score** | "67% of classical formulations get rejected — here's why yours might too" | 1.5h | 🔥🔥🔥🔥 |
| **Competitor IP Monitor** | "3 patents filed this month for ashwagandha extracts" — monitor competitor activity | 3h | 🔥🔥🔥 |

### **Category D: "The Novel Twist" (Innovation +30%)**

| Idea | What It Does | Build Time | Impact |
|------|-------------|------------|--------|
| **Regulatory News Feed** | Auto-fetch latest Gazette notifications — "Patents Rules amended 2 days ago" | 2h | 🔥🔥🔥🔥 |
| **Graph Visualization** | Interactive Neo4j graph — click nodes to see relationships | 3h | 🔥🔥🔥🔥 |
| **Voice-First Design** | Full conversational flow — not just ASR, but multi-turn dialogue | 2h | 🔥🔥🔥 |
| **Offline Mode** | Local SQLite corpus — works without internet in rural areas | 2h | 🔥🔥🔥 |
| **Community Prior Art** | Crowdsourced API entries — "Users who searched for ashwagandha also found..." | 3h | 🔥🔥🔥 |

---

## 🏆 STEP 4 — Top 5 Differentiators (Recommended)

Based on **build time vs impact** matrix:

| Rank | Feature | Build Time | Impact | Why It Wins |
|------|---------|------------|--------|-------------|
| **1** | **TKDL Proxy Search** | 2h | 🔥🔥🔥🔥🔥 | No team does this. Judges will ask "how did you simulate TKDL?" |
| **2** | **Cost Calculator** | 1.5h | 🔥🔥🔥🔥 | Real pain point. Every startup asks "how much does this cost?" |
| **3** | **Prior Art Detector** | 3h | 🔥🔥🔥🔥 | "Did someone else patent this?" — the #1 question after classification |
| **4** | **ABS Calculator** | 1h | 🔥🔥🔥🔥 | Unique to this PS. No other team will have this. |
| **5** | **Regulatory News Feed** | 2h | 🔥🔥🔥🔥 | "Corpus freshness" is a judge concern — this solves it visibly |

---

## 🧠 STEP 5 — Your Turn: Add Your Ideas

**Below this line, add your feature ideas. For each idea, answer:**

1. **What problem does it solve?** (Which stakeholder pain point?)
2. **How would you demo it in 10 seconds?** (Visual, interactive, tangible?)
3. **What makes it different from other teams?** (Why won't everyone build this?)
4. **How hard is it to build?** (Easy / Medium / Hard — be honest)
5. **Does it align with the PS?** (Citation correctness, jurisdiction, abstention, multilingual?)

### **Your Idea #1:**
- **Problem:**
- **10-Second Demo:**
- **Differentiation:**
- **Build Difficulty:**
- **PS Alignment:**

### **Your Idea #2:**
- **Problem:**
- **10-Second Demo:**
- **Differentiation:**
- **Build Difficulty:**
- **PS Alignment:**

### **Your Idea #3:**
- **Problem:**
- **10-Second Demo:**
- **Differentiation:**
- **Build Difficulty:**
- **PS Alignment:**

---

## 📊 STEP 6 — Score & Prioritize

After filling in your ideas, score each on:

| Criteria | Weight | Score (1-10) | Weighted Score |
|----------|--------|--------------|----------------|
| **Impact** | 30% | | |
| **Differentiation** | 25% | | |
| **Feasibility** | 20% | | |
| **Demo Ability** | 15% | | |
| **PS Alignment** | 10% | | |
| **TOTAL** | 100% | | |

**Rank by Total Score → Build top 3 first.**

---

## 🎬 STEP 7 — 90-Second Demo Flow (Revised)

Based on your feature choices, here's the new demo flow:

```
[0-10s]   Hindi voice: "क्या मैं अश्वगंधा कैपसूल का पेटेंट करवा सकता हूँ?"
[10-20s]  Sarvam ASR → Translate → RAG retrieves Sec 3(p) + API Vol-III p.124
[20-30s]  **TKDL Proxy Result:** "API Vol-III p.124 shows prior art for ashwagandha"
[30-40s]  **Cost Calculator:** "Patent filing: ₹1,600 + Facilitator: ₹5,000 = ₹6,600"
[40-50s]  **ABS Calculator:** "If using neem (foreign entity): 3-5% benefit sharing"
[50-60s]  **Prior Art Detector:** "3 similar patents found — see comparison matrix"
[60-70s]  **Two Tabs:** India answer | International GRATK Art 3 disclosure
[70-80s]  **Citation Badge:** "[CIT: Patents Act, Sec 3(p)] ✅ Verified"
[80-90s]  **Abstention Check:** "ABSTAIN: I provide information, not legal advice"
```

**Key:** Every second shows something **different** from other teams.

---

## ✅ STEP 8 — Final Checklist

Before building, answer YES/NO to each:

- [ ] Does it solve a **real pain point** (not just "nice to have")?
- [ ] Can a judge **see it in 10 seconds**?
- [ ] Is it **different from every other team**?
- [ ] Can we **build it in 48 hours**?
- [ ] Does it **align with the PS** (citation, jurisdiction, abstention, multilingual)?
- [ ] Does it **scale** (work for 100 users, not just demo)?
- [ ] Is it **defensible** (can we explain why we built it this way)?

**If any answer is NO → reconsider the feature.**

---

## 📝 Next Steps

1. **Fill in STEP 5** — Add your 3 feature ideas
2. **Score in STEP 6** — Rank by weighted score
3. **Pick top 3** — Build these first
4. **Revise demo flow in STEP 7** — Make it 90 seconds of pure value
5. **Check STEP 8** — Validate before building

---

*This is a living document. Update as you discover new ideas.*
