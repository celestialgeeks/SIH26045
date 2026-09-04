# SIH26045 — Formulation Classification Wizard (Exact Decision Tree)
**Date:** 2026-09-03 | **Researcher:** @researcher | **Iteration:** 1/4
**Status:** COMPLETE — 5-question flow with exact statute citations at every branch

---

## Formulation Classification Decision Tree

The PS requires a **stateful wizard (3-5 turns)** that asks minimum clarifying questions to classify the formulation, then provides jurisdiction-specific guidance with citations. This is NOT a one-shot chatbot.

---

### Mermaid Flowchart

```mermaid
flowchart TD
    START[User describes formulation] --> Q1
    
    Q1[Q1: Is the formulation listed in<br/>First Schedule of D&C Act?<br/><i>Sec 3(a), First Schedule books</i>] -->|YES| CLASSICAL
    Q1 -->|NO / UNSURE| Q2
    
    CLASSICAL[CLASSICAL FORMULATION<br/>Sec 3(p) Patents Act bars patent<br/>TKDL/API prior art exists<br/>Route: GI / TM only] --> END_ABSTAIN
    
    Q2[Q2: Is it a NEW DRUG?<br/>Not in API, new combination/process<br/><i>NDCT Rules 2019, Rule 122E<br/>CDSCO approval required</i>] -->|YES| NEW_DRUG
    Q2 -->|NO| Q3
    
    NEW_DRUG[NEW DRUG PATHWAY<br/>Patent POSSIBLE if novel/inventive<br/>Sec 3(p) analysis needed<br/>CDSCO + Patent dual track<br/>NDCT Rules 2019 compliance] --> END_CITED
    
    Q3[Q3: Is it a PHYTOPHARMACEUTICAL?<br/>Standardized extract, marker compounds<br/><i>CDSCO Phytopharma Guidelines 2024<br/>Schedule T GMP</i>] -->|YES| PHYTO
    Q3 -->|NO| Q4
    
    PHYTO[PHYTOPHARMACEUTICAL<br/>CDSCO phytopharma pathway<br/>Patent + regulatory dual track<br/>Standardized markers required] --> END_CITED
    
    Q4[Q4: Is it an AYURVEDA AAHAR?<br/>Food category, nutritional claims<br/><i>FSSAI Ayurveda Aahar Regs 2022<br/>No patent, TM/GI only</i>] -->|YES| AAHAR
    Q4 -->|NO| Q5
    
    AAHAR[AYURVEDA AAHAR (Food)<br/>FSSAI 2022 Regs apply<br/>NO patent eligibility<br/>TM + GI only route] --> END_ABSTAIN
    
    Q5[Q5: Is it a COSMETIC?<br/>Topical, non-therapeutic claims<br/><i>D&C Act Cosmetic Schedule<br/>Different IP regime</i>] -->|YES| COSMETIC
    Q5 -->|NO| UNCLASSIFIED
    
    COSMETIC[COSMETIC PRODUCT<br/>D&C Act cosmetic provisions<br/>TM + Design patent possible<br/>No drug license needed] --> END_CITED
    
    UNCLASSIFIED[UNCLASSIFIED / HYBRID<br/>Requires facilitator escalation<br/>ABSTAIN with disclaimer] --> END_ABSTAIN
    
    END_CITED[Answer with citations<br/>India tab + International tab<br/>Confidence: HIGH/MEDIUM] --> END
    END_ABSTAIN[ABSTAIN: Information only<br/>See IP facilitator<br/>Disclaimer banner logged] --> END
    END[Log to audit_log.jsonl<br/>DPDP compliance]
```

---

## Question Details with Exact Citations

### Q1: Classical Formulation Check
**Question:** "Is this formulation listed in the **First Schedule** of the Drugs & Cosmetics Act, 1940 (authoritative books of Ayurveda/Siddha/Unani)?"

**Citations if YES:**
- **D&C Act 1940, Sec 3(a)** — Definition of Ayurvedic/Siddha/Unani drug
- **D&C Act 1940, Sec 3(h)(i)** — "patent or proprietary medicine" definition (excludes classical)
- **D&C Act 1940, Sec 7A** — Sections 5 & 7 NOT applicable to classical drugs
- **Patents Act 1970, Sec 3(p)** — "invention which in effect, is traditional knowledge" — NOT patentable
- **TKDL** — 4.5 lakh formulations transcribed (CSIR + Ayush)
- **Ayurvedic Pharmacopoeia of India (API)** — Open proxy for TKDL prior art

**Action:** 
- India tab: Cite Sec 3(p) + API volume/page → **ABSTAIN on patent**, suggest GI/TM
- International tab: WIPO GRATK Art 3 disclosure required if filing abroad

---

### Q2: New Drug Check
**Question:** "Is this a **new drug** — not in API, new combination of ingredients, new process, or new therapeutic indication?"

**Citations if YES:**
- **NDCT Rules 2019, Rule 122E** — Definition of "new drug"
- **NDCT Rules 2019, Chapter III** — Clinical trial requirements (Phase I-IV)
- **CDSCO New Drug Approval** — Form 44/45, Subject Expert Committee
- **Patents Act 1970, Sec 2(1)(j)** — "invention" = new product/process involving inventive step
- **Patents Act 1970, Sec 3(p)** — Still applies: must prove NOT traditional knowledge
- **Patents (Amendment) Rules 2024, G.S.R. 211(E)** — Form 27 triennial, bio-resource disclosure

**Action:**
- India tab: Patent path possible IF novel/inventive over prior art (API/IMPPAT/TKDL)
- Cite NDCT Rules for regulatory, Patents Act for IP
- International tab: PCT filing, GRATK Art 3 disclosure if bio-resource used

---

### Q3: Phytopharmaceutical Check
**Question:** "Is this a **standardized extract** with defined marker compounds, manufactured under GMP for therapeutic use?"

**Citations if YES:**
- **CDSCO Phytopharmaceutical Guidelines** (2024 updates)
- **Drugs & Cosmetics Act, Schedule T** — GMP for Ayurveda/Siddha/Unani
- **NDCT Rules 2019** — Clinical data requirements (may need Phase III/IV)
- **Patents Act 1970** — Patentable if novel extract process + therapeutic efficacy
- **FSSAI** — Not applicable (not food category)

**Action:**
- India tab: Dual track — CDSCO phytopharma approval + Patent application
- Cite Schedule T GMP, CDSCO guidelines
- International tab: EMA Herbal Directive (EU), FDA Botanical Guidance (US)

---

### Q4: Ayurveda Aahar Check
**Question:** "Is this positioned as a **food/nutritional product** (Ayurveda Aahar) rather than a medicine?"

**Citations if YES:**
- **FSSAI Ayurveda Aahar Regulations 2022** — Food category, not drug
- **FSS Act 2006** — Licensing/registration as food business
- **NO patent eligibility** — Food products not patentable per se
- **TM + GI only** — Brand protection via trademark, geographical indication

**Action:**
- India tab: FSSAI route, **ABSTAIN on patent**, cite FSSAI Regs 2022
- International tab: Novel Food Regulation (EU), GRAS (US) — different pathways

---

### Q5: Cosmetic Check
**Question:** "Is this a **topical product with only cosmetic claims** (cleansing, beautifying) — no therapeutic claims?"

**Citations if YES:**
- **D&C Act 1940, Sec 3(aaa)** — Definition of cosmetic
- **D&C Act, Cosmetic Schedule** — Standards, labeling
- **Patents Act** — Design patent possible for packaging/appearance
- **TM Act 1999** — Brand protection
- **NO drug license** — Different regulatory track

**Action:**
- India tab: Cosmetic regulatory route, Design patent + TM
- International tab: EU Cosmetic Regulation 1223/2009, FDA FD&C Act

---

## Unclassified / Hybrid → Escalation

**If no clear match after 5 questions:**
- **Response:** "I provide information only, not legal advice. This formulation doesn't clearly fit one category. Please consult a registered IP facilitator or patent attorney."
- **Log:** `audit_log.jsonl` with query, classification=UNCLASSIFIED, action=ESCALATED
- **DPDP:** Consent checkbox before storing query

---

## India vs International Tab Enforcement (Architecture)

### Retrieval Layer Separation
```python
# Two separate vector collections
INDIA_COLLECTION = "india_legal_corpus"      # Patents Act, D&C Act, BD Act, NDCT, FSSAI, etc.
INTERNATIONAL_COLLECTION = "intl_legal_corpus"  # TRIPS, CBD, Nagoya, GRATK, PCT, Madrid, EMA, FDA
```

### Generation Layer Separation
```python
SYSTEM_PROMPT_INDIA = """
You are an Ayush IP assistant for INDIAN jurisdiction ONLY.
Answer ONLY from <context>. Cite [CIT: Statute Section Rule].
If context lacks answer: "Not found in Indian corpus — abstaining."
Never mix international law in this tab.
"""

SYSTEM_PROMPT_INTL = """
You are an Ayush IP assistant for INTERNATIONAL jurisdiction ONLY.
Answer ONLY from <context>. Cite [CIT: Treaty Article Rule].
If context lacks answer: "Not found in international corpus — abstaining."
Never mix Indian law in this tab.
"""
```

---

## Abstention Classifier (3-Class)

```python
# Prompt for classifier
CLASSIFIER_PROMPT = """
Classify the user query into ONE of three classes:
1. ANSWER — Can be answered from corpus with citations
2. PARTIAL — Some info in corpus, but incomplete → answer what we have + abstain on rest
3. ABSTAIN — Out of scope (drafting, legal advice, unclassified formulation) → refuse + escalate

Examples:
- "Can I patent Chyavanprash?" → ABSTAIN (classical, Sec 3(p))
- "Draft my patent claim for ashwagandha extract" → ABSTAIN (drafting = legal advice)
- "What is Sec 3(p) of Patents Act?" → ANSWER
- "Export giloy to EU requirements?" → PARTIAL (int'l tab only)
- "Is turmeric patentable in US under Sec 3(p)?" → ABSTAIN (jurisdiction error - Sec 3(p) is India)
"""
```

---

## Implementation Checklist for 48-Hour Build

- [ ] Hardcode 5-question wizard state machine (dict-based, no LLM)
- [ ] Each question has: text, citations (India + Intl), next_state mapping
- [ ] Dual RAG: India collection + International collection (separate Qdrant)
- [ ] Citation validator: regex `\[CIT: .+\]` must match retrieved chunk verbatim
- [ ] Abstention classifier (3-class prompt) runs before final answer
- [ ] Bhashini: Translate query HI→EN, retrieve EN, answer EN→HI, keep EN citations
- [ ] Audit log: JSONL with timestamp, query, classification, citations, abstention_flag
- [ ] Corpus freshness badge: "Last synced: Rules 2024 (Gazette 25 Oct 2024)"
- [ ] Demo flow: Hindi voice → ASR → Translate → RAG (dual) → Translate → TTS

---

## Sources Cited

1. D&C Act 1940 (First Schedule): https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2022/acts_and_rules/Drugs%20and%20Cosmetics%20Act%2C%201940.pdf
2. Patents Act 1970 Sec 3(p): https://ipindia.gov.in/writereaddata/Portal/IPORule/1_83_1_Patent_Amendment_Rule_2024_Gazette_Copy.pdf
3. NDCT Rules 2019: https://cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/NewDrugs_CTRules_2019.pdf
4. FSSAI Ayurveda Aahar 2022: https://fssai.gov.in
5. CDSCO Phytopharma Guidelines: https://cdsco.gov.in
6. WIPO GRATK Treaty: https://www.wipo.int/edocs/mdocs/tk/en/gratk_dc/gratk_dc_7.pdf
7. Biological Diversity Rules 2024: http://nbaindia.org/uploaded/pdf/Regu2025.pdf