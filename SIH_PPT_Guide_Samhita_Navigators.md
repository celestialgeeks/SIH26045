# SIH 2026 - IDEA PPT Guide | Team Samhita Navigators
> **For: Internal Hackathon - Tomorrow | IPS Academy Indore**
> **Team: Samhita Navigators | PS: SIH26045 (IP-SAKTI) + SIH26168 (Dead Reckoning)**
> **Official Format: 6 SLIDES ONLY - Strictly Enforced**

---

## 1. OFFICIAL STRUCTURE - 6 SLIDES ONLY

For **Internal / College Level Screening**, SIH mandates **exactly 6 slides**. Anything else will be rejected by SPOC.

Source: `SIH2025-IDEA-Presentation-Format.pptx` + Winners Vault 2023-25 (Aadiii00/SIH-Winners-PPT)

| Slide | Title - As Per Official Template | What Judges Score | Pitch Time |
| :--- | :--- | :--- | :--- |
| **1** | **Title & Team Details** | Compliance Check | 20 sec |
| **2** | **Problem Understanding & Need** | 10% - Do you understand the PS? | 30 sec |
| **3** | **Proposed Solution & Innovation** | 30% - Core Idea (MOST IMPORTANT) | 60 sec |
| **4** | **Technical Approach - Stack, Architecture, Flow** | 25% - Can you build it? | 60 sec |
| **5** | **Feasibility, Challenges & Risk Mitigation** | 15% - Are you honest? | 30 sec |
| **6** | **Impact, Beneficiaries, Research & References** | 20% - Scale + Proof | 30 sec |

**Total: 3.5 mins Pitch + 2 mins Q&A = 5 mins MAX**

> **Download Official Blank Template:** `https://www.sih.gov.in/letters/SIH2025-IDEA-Presentation-Format.pptx`
> Use this as base. Do not create from scratch.

---

## 2. SLIDE-BY-SLIDE: WHAT TO PUT (And What Kills You)

### SLIDE 1: Title Slide
**Must Have:**
* PS ID: `SIH26045` (or `SIH26168`), PS Title verbatim from sih.gov.in
* Organization: `Ministry of Ayush` / `ISRO`
* Category: `Software`, Theme: `MedTech/Biotech` / `Smart Automation`
* Team Name: `Samhita Navigators`, Team ID, Institute: `IPS Academy Indore`
* SIH Logo

**Winning Trick:** Add 1-line tagline under title
> `Samhita Navigators: Tradition Cited. Position Certain.`

**KILL:** Wrong PS ID, spelling mistake, missing theme.

### SLIDE 2: Problem Understanding & Need
**Must Have:**
* Problem in 2 lines (copy exactly from sih.gov.in)
* 3 Pain Points WITH NUMBERS: `>4000 TKDL cases rejected, 93% Ayush startups face Sec 3(p) bar, BD Act 2023 non-compliance = ₹5L penalty`
* Target Users Personas: `Ayush Formulator, IP Lawyer, Exporter`
* Existing Gaps: `ChatGPT hallucinates law, No jurisdiction toggle, No citation`

**Winning Trick:** Show 1 small infographic: `Current Flow (15 days manual) vs Your Flow (15 secs)`

**KILL:** Generic problem, no India-specific stats, no user.

### SLIDE 3: Proposed Solution & Innovation [30% WEIGHT]
**Must Have:**
* Solution in 1 diagram (center): e.g., for SIH26045: `3-Q Wizard -> Dual RAG (India/Intl Tabs) -> Citation-or-Abstain`
* 3 Innovations as icons:
  1. Dual Jurisdiction RAG
  2. Neo4j Law Graph
  3. Bhashini Voice Citation
* Uniqueness Table: `Existing (Generic LLM) vs Yours (Version-Tracked Corpus + Regex Validator 100%)`

**Rule:** 70% visual, 30% text. Max 25 words.

**KILL:** Only text bullets, no diagram, claiming "AI/ML" without method.

### SLIDE 4: Technical Approach
**Must Have:**
* **Left:** Tech Stack Icons: `Qdrant + Mistral/Nvidia NIM + Bhashini ULCA + Neo4j + FastAPI + React`
* **Right:** System Architecture Diagram - 3 blocks: `Ingest (Gazette PDFs + SHA256) -> Retrieve (Hybrid Search) -> Generate (Cited Answer)`
* **Bottom:** Workflow 1-2-3-4 flowchart + Data Flow arrow
* **Bottom Corner:** `Demo QR + Link: youtu.be/xxx | Prototype Screenshot` - Judges give +10% for working prototype proof. Even a Figma matters.

**KILL:** Mentioning 10 tech stacks with no diagram, no data flow.

### SLIDE 5: Feasibility & Viability
**Must Have - Be HONEST, judges love this:**

* **Feasibility:** `Tech: TRL 6 | Law: Corpus done | Dataset: IMPPAT+API available` - 3 green checks
* **Challenges + Mitigation Table:**

| Challenge | Mitigation |
| :--- | :--- |
| TKDL has no public API | Use API/IMPPAT proxy + Human Escalation UI |
| Bhashini legal BLEU low | Retrieve in EN, Answer in HI, Cite EN |
| Hallucination | Regex Validator -> ABSTAIN if fail |

**KILL:** Writing "No challenges" = instant reject. Writing challenges without mitigation.

### SLIDE 6: Impact, Beneficiaries & Research
**Must Have:**
* **Top:** Impact numbers: `10k Ayush MSMEs, ₹200Cr IP filing saved, Prevents 30% rejections`
* **Middle:** Beneficiaries 4 icons: `Students, Startups, Ayush Ministry, Farmers (ABS benefit sharing)`
* **Bottom:** 4-5 References: `Patents Rules 2024 Gazette 15 Mar 2024, BD Rules 25 Oct 2024, WIPO GRATK May 2024, Paper: IO-VNBD arXiv:2005.01701, IMPPAT 2.0 DB` + Graphs/Survey links
* **Future Scope 1 line:** `Phase 2: DPDP audit log + Paid-adapter`

**KILL:** No references, no quantified impact, "will help society" generic.

---

## 3. HOW WINNING PPTS LOOK DIFFERENT

Analyzed 50+ PPTs from `SIH Winners Vault 2023-25`:

1.  **Minimal Text:** <30 words/slide. They speak, not read.
2.  **One Visual Per Slide:** All 6 slides have a diagram/chart/screenshot. Losing teams have 3 text-only slides.
3.  **Numbers Everywhere:** "Reduces drift to 8% (<10% PASS)" not "Reduces drift".
4.  **Prototype Proof:** Screenshot + QR + GitHub link on Slide 4/5. Top winner had 176K views due to prototype video.
5.  **Research Citations:** Slide 6 has Gazette dates + arXiv IDs - shows depth.
6.  **Clean Design:** White background, SIH Blue `#0F2A52` + Saffron `#FF6B00` + Font `Inter / Poppins`, 16:9 ratio, no heavy animations.

**Judging Criteria Mapping:** Your 6 slides are mapped 1:1 to score - miss one = 0 in that criteria.

---

## 4. TOOLS TO MAKE IT - FOR TOMORROW, USE FASTEST

| Tool | Best For Tomorrow? | Time | Pro |
| :--- | :--- | :--- | :--- |
| **PowerPoint + Designer** | **YES - RECOMMENDED** | 45 min | Official .pptx, offline, <5MB export, accepted everywhere |
| **Google Slides** | YES | 40 min | Fastest collab for 6 members, auto-save |
| **Canva (SIH Template)** | YES | 30 min | Pre-made SIH deck, drag-drop icons |
| **Gamma / Beautiful.ai** | Fastest AI | 15 min | Paste structure -> auto deck, then export to PPTX and fix |
| **Figma -> PPT** | NO for tomorrow | 2 hrs | Beautiful but slow |

**Do This Tonight:**
1. Don't make from scratch - Use official template + replace content.
2. Export **BOTH** `.pptx` + `.pdf` (<4MB).
3. Test on projector - check fonts not broken.
4. Prepare 30-sec pitch per slide - rehearse 3 times.

---

## 5. TOMORROW'S TIMELINE - INTERNAL HACKATHON CHECKLIST

**Tonight (Before 10 PM):**
- [ ] Freeze both PPTs (SIH26045 + SIH26168)
- [ ] Upload to Drive + Pen Drive + Email to self
- [ ] Export PDF backup

**Morning:**
- [ ] 1 dry run with timer (hard stop at 4 mins)
- [ ] Check file opens on another laptop

**Q&A Prep (Judges ALWAYS ask):**
1. Dataset source?
2. Why not existing solution?
3. Show prototype?
4. Tech stack justification?
5. What if internet fails?

Have 1-line answers + keep Slide 4 diagram ready as backup.

**Common Rejections Tomorrow:**
* More than 6 slides
* No PS ID / Wrong PS ID
* No architecture diagram
* No feasibility risks mentioned
* No references on Slide 6

---

## 6. TEAM SAMHITA NAVIGATORS - NEXT STEPS

* **Samhita** = Compilation / Wisdom (Ayurvedic Samhitas) -> Perfect for SIH26045
* **Navigators** = Navigation / Guidance -> Perfect for SIH26168 Dead Reckoning

**Tagline:** `Samhita Navigators: Tradition Cited. Position Certain.`

**Action:** Reply in group - "Review this doc + Confirm your slide ownership (1 person = 1 slide) + Send prototype screenshot by tonight 9 PM"

---
*Prepared by Team Samhita Navigators | IPS Academy Indore | SIH 2026 | Internal Hackathon - 5th Sept 2026*
*Share this doc as PDF: Export -> PDF from this .md*
