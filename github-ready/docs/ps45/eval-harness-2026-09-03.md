# SIH26045 — Evaluation Harness: Gold Q-A Pairs + Adversarial Tests

> **Purpose:** 20 gold Q-A pairs + 5 adversarial queries with exact expected outputs for RAG benchmarking
> **Format:** JSON files for automated evaluation pipeline

---

## Gold Q-A Pairs (20) — `eval/gold_qa.json`

```json
[
  {
    "id": 1,
    "query_hi": "क्या मैं च्यवनप्राश का पेटेंट करा सकता हूँ?",
    "query_en": "Can I patent Chyavanprash?",
    "expected_key_points": [
      "NO - classical formulation",
      "Sec 3(p) Patents Act bars traditional knowledge",
      "TKDL prior art exists",
      "Suggest GI / TM route instead",
      "Reference First Schedule D&C Act"
    ],
    "expected_citations": [
      "Patents Act, Sec 3(p)",
      "Drugs & Cosmetics Act 1940, Sec 3(a)",
      "First Schedule D&C Act"
    ],
    "tab": "India",
    "jurisdiction": "India",
    "category": "classical_formulation"
  },
  {
    "id": 2,
    "query_hi": "गिलॉय फाइटोफार्मास्यूटिकल को EU में निर्यात करना है",
    "query_en": "Export giloy phytopharma to EU",
    "expected_key_points": [
      "GRATK Art 3 disclosure of origin mandatory",
      "EMA Herbal Medicinal Products Directive applies",
      "CDSCO phytopharma pathway (NDCT Rules) required first",
      "Dual track: patent + regulatory",
      "ABS compliance if foreign entity"
    ],
    "expected_citations": [
      "GRATK Treaty 2024, Art 3",
      "EMA Herbal Directive 2004/24/EC",
      "NDCT Rules 2019, Rule 122E",
      "Biological Diversity Rules 2024, Form 2"
    ],
    "tab": "International",
    "jurisdiction": "International",
    "category": "phytopharma_export"
  },
  {
    "id": 3,
    "query_hi": "अश्वगंधा कैप्सूल का भारत में पेटेंट संभव है?",
    "query_en": "Ashwagandha capsule patent India",
    "expected_key_points": [
      "If NEW combination/process → patent possible (Sec 2(1)(j) novelty + inventive step)",
      "If CLASSICAL formulation → Sec 3(p) bar",
      "NDCT Rules 2019 clinical trial pathway if new drug",
      "Check API for existing monograph",
      "IMPPAT for phytochemical markers"
    ],
    "expected_citations": [
      "Patents Act, Sec 2(1)(j)",
      "Patents Act, Sec 3(p)",
      "NDCT Rules 2019, Rule 122E",
      "Ayurvedic Pharmacopoeia of India"
    ],
    "tab": "India",
    "jurisdiction": "India",
    "category": "new_vs_classical"
  },
  {
    "id": 4,
    "query_hi": "नीम निर्यात के लिए ABS अनुमति प्रक्रिया क्या है?",
    "query_en": "ABS approval for neem export",
    "expected_key_points": [
      "Foreign entity → NBA prior approval mandatory",
      "Form 2 (Biological Diversity Rules 2024)",
      "Benefit sharing agreement (Reg 4)",
      "Indian collaborator → Form 1 (prior intimation)",
      "Exempt: collaborative research, non-commercial"
    ],
    "expected_citations": [
      "Biological Diversity Rules 2024, Form 2",
      "Biological Diversity Rules 2024, Reg 4",
      "Biological Diversity Rules 2024, Form 1",
      "BD Amendment Act 2023, Sec 6"
    ],
    "tab": "India",
    "jurisdiction": "India",
    "category": "abs_compliance"
  },
  {
    "id": 5,
    "query_hi": "हल्दी का US में पेटेंट Sec 3(p) के तहत?",
    "query_en": "Turmeric patent US Sec 3(p)?",
    "expected_key_points": [
      "ABSTAIN - Sec 3(p) is INDIA ONLY provision",
      "US governed by 35 USC 101 (subject matter eligibility)",
      "USPTO examines novelty/non-obviousness differently",
      "Jurisdiction correction is the answer",
      "No Indian law applies to US patent"
    ],
    "expected_citations": [
      "Patents Act, Sec 3(p) [jurisdiction: India]",
      "35 USC 101 [jurisdiction: US]"
    ],
    "tab": "International",
    "jurisdiction": "Both",
    "category": "jurisdiction_correction"
  },
  {
    "id": 6,
    "query_hi": "ब्राह्मी के लिए पेटेंट क्लेम ड्राफ्ट करें",
    "query_en": "Draft patent claim for Brahmi",
    "expected_key_points": [
      "ABSTAIN - legal advice, cannot draft claims",
      "Provide template structure only",
      "Suggest patent attorney consultation",
      "Mention Sec 3(p) risk for classical herbs",
      "Independent claim + dependent claims template"
    ],
    "expected_citations": [
      "Patents Act, Sec 3(p)",
      "Patents Act, Sec 10 (specification)",
      "Disclaimer: not legal advice"
    ],
    "tab": "Both",
    "jurisdiction": "Both",
    "category": "legal_advice_abstain"
  },
  {
    "id": 7,
    "query_hi": "आयुर्वेद आहार और दवा में क्या अंतर है?",
    "query_en": "Ayurveda Aahar vs drug difference",
    "expected_key_points": [
      "Aahar = FOOD category (FSSAI 2022 Regs)",
      "Drug = MEDICINE category (D&C Act 1940 + CDSCO)",
      "Aahar: NO patent, only TM + GI possible",
      "Drug: patent possible if novel + inventive",
      "Labeling, licensing, claims completely different"
    ],
    "expected_citations": [
      "FSSAI Ayurveda Aahar Regulations 2022, Reg 5",
      "Drugs & Cosmetics Act 1940, Sec 7A",
      "FSSAI Act 2006",
      "Schedule T GMP"
    ],
    "tab": "India",
    "jurisdiction": "India",
    "category": "aahar_vs_drug"
  },
  {
    "id": 8,
    "query_hi": "हर्बल दावों वाला कॉस्मेटिक रेगुलेशन",
    "query_en": "Cosmetic with herbal claims",
    "expected_key_points": [
      "If THERAPEUTIC claims → drug license (CDSCO)",
      "If COSMETIC claims only → D&C Act cosmetic schedule",
      "Herbal ingredient ≠ herbal claim",
      "Ayush license needed for 'Ayurvedic' label",
      "Advertisement: Drugs & Magic Remedies Act 1954"
    ],
    "expected_citations": [
      "Drugs & Cosmetics Act 1940, Sec 3(aaa)",
      "D&C Act Cosmetic Schedule",
      "Drugs & Magic Remedies Act 1954",
      "AYUSH License guidelines"
    ],
    "tab": "India",
    "jurisdiction": "India",
    "category": "cosmetic_vs_drug"
  },
  {
    "id": 9,
    "query_hi": "दार्जिलिंग चाय प्रक्रिया के लिए GI",
    "query_en": "GI for Darjeeling tea process",
    "expected_key_points": [
      "GI Act 1999, not patent",
      "Collective rights (association of producers)",
      "Geographical origin + quality/reputation link",
      "No individual ownership",
      "International: Lisbon Agreement, Madrid System"
    ],
    "expected_citations": [
      "Geographical Indications Act 1999, Sec 2(e)",
      "Lisbon Agreement",
      "TRIPS Art 22-24"
    ],
    "tab": "India",
    "jurisdiction": "Both",
    "category": "gi_protection"
  },
  {
    "id": 10,
    "query_hi": "आयुष फॉर्मूलेशन के लिए PCT फाइलिंग",
    "query_en": "PCT filing for Ayush formulation",
    "expected_key_points": [
      "PCT Art 4 - international application",
      "GRATK Art 3 disclosure if bio-resource used",
      "30/31 month national phase entry",
      "India as ISA/IPEA available",
      "Priority claim from Indian provisional"
    ],
    "expected_citations": [
      "PCT, Art 4",
      "PCT, Art 22 (30 month)",
      "PCT, Art 39 (31 month)",
      "GRATK Treaty 2024, Art 3",
      "Patents Rules 2024, Rule 20"
    ],
    "tab": "International",
    "jurisdiction": "International",
    "category": "pct_filing"
  },
  {
    "id": 11,
    "query_hi": "फाइटोफार्मास्यूटिकल NDCT क्लिनिकल ट्रायल",
    "query_en": "Phytopharma NDCT clinical trial",
    "expected_key_points": [
      "CDSCO phytopharma pathway (2017 guideline + NDCT 2019)",
      "Standardized extract + marker compounds mandatory",
      "Phase I: safety (healthy volunteers)",
      "Phase II: efficacy (target condition)",
      "Phase III: confirmatory (multi-center)",
      "Accelerated approval possible for unmet need"
    ],
    "expected_citations": [
      "NDCT Rules 2019, Rule 122E",
      "CDSCO Phytopharmaceutical Guideline 2017",
      "Drugs & Cosmetics Act 1940, Sec 7A",
      "Schedule Y (replaced by NDCT)"
    ],
    "tab": "India",
    "jurisdiction": "India",
    "category": "phytopharma_trials"
  },
  {
    "id": 12,
    "query_hi": "आयुर्वेद दवा के लिए ट्रेडमार्क विरोध",
    "query_en": "TM opposition for Ayurvedic medicine",
    "expected_key_points": [
      "TM Act 1999, Sec 21 - opposition period 4 months",
      "Grounds: Sec 9 (descriptive), Sec 11 (similarity)",
      "Classical names (Chyavanprash) → Sec 9 absolute refusal",
      "Evidence of prior use + distinctiveness",
      "GI registration blocks TM for same name"
    ],
    "expected_citations": [
      "Trade Marks Act 1999, Sec 9",
      "Trade Marks Act 1999, Sec 11",
      "Trade Marks Act 1999, Sec 21",
      "GI Act 1999, Sec 22"
    ],
    "tab": "India",
    "jurisdiction": "India",
    "category": "tm_opposition"
  },
  {
    "id": 13,
    "query_hi": "बहुभाषी Bhashini में IP सलाह",
    "query_en": "Multilingual IP advice via Bhashini",
    "expected_key_points": [
      "Bhashini ULCA T2T: retrieve EN corpus, answer HI, cite EN source",
      "Legal terminology: use IndicTrans2 legal fine-tune",
      "Voice: Dhwani TTS for Hindi/Tamil/Telugu/Bengali",
      "ASR: Dhwani for voice queries",
      "Citation preservation across translation"
    ],
    "expected_citations": [
      "Bhashini ULCA API docs",
      "IndicTrans2 legal benchmarks",
      "Dhwani ASR/TTS paper"
    ],
    "tab": "Both",
    "jurisdiction": "Both",
    "category": "bhashini_multilingual"
  },
  {
    "id": 14,
    "query_hi": "पारंपरिक ज्ञान डिजिटल लाइब्रेरी एक्सेस",
    "query_en": "TKDL access for patent search",
    "expected_key_points": [
      "TKDL NOT publicly accessible - CSIR/NIScPR MoU required",
      "For SIH: use API + IMPPAT as proxy",
      "TKDL cited as 'TKDL record' in patent office actions",
      "ABSTAIN on specific TKDL record numbers",
      "Public alternative: WIPO TK database, Google Patents TK"
    ],
    "expected_citations": [
      "TKDL official policy (CSIR)",
      "API database (db.imppat.org)",
      "IMPPAT 2.0 publication"
    ],
    "tab": "India",
    "jurisdiction": "India",
    "category": "tkdl_access"
  },
  {
    "id": 15,
    "query_hi": "पौधा किस्म संरक्षण बनाम पेटेंट",
    "query_en": "Plant variety protection vs patent",
    "expected_key_points": [
      "PPVFR Act 2001 - plant varieties (not patents)",
      "Farmer's rights + breeder's rights",
      - DUS test (Distinctness, Uniformity, Stability)",
      - Patent (Sec 3(j)) excludes plants/animals",
      - Both can coexist for same variety"
    ],
    "expected_citations": [
      "PPVFR Act 2001, Sec 15",
      "Patents Act, Sec 3(j)",
      "UPOV 1991 Convention"
    ],
    "tab": "India",
    "jurisdiction": "Both",
    "category": "pvpf_vs_patent"
  },
  {
    "id": 16,
    "query_hi": "अंतर्राष्ट्रीय जैव विविधता समझौते",
    "query_en": "International biodiversity treaties",
    "expected_key_points": [
      "CBD 1992 - Art 15 (access), Art 8(j) (TK)",
      "Nagoya Protocol 2010 - ABS implementation",
      "GRATK 2024 - patent disclosure of origin",
      "ITPGRFA 2001 - food/agriculture PGRFA",
      "India: BD Act 2002 + Amendment 2023 + Rules 2024"
    ],
    "expected_citations": [
      "CBD, Art 15",
      "CBD, Art 8(j)",
      "Nagoya Protocol, Art 5",
      "GRATK Treaty 2024, Art 3",
      "ITPGRFA, Art 12"
    ],
    "tab": "International",
    "jurisdiction": "International",
    "category": "treaties"
  },
  {
    "id": 17,
    "query_hi": "पारंपरिक ज्ञान पूर्वकल्पना साक्ष्य",
    "query_en": "Traditional knowledge prior art evidence",
    "expected_key_points": [
      "TKDL = defensive prior art (patent office use only)",
      "API monographs = published prior art",
      "Published texts (Charaka, Sushruta) = prior art",
      "Oral TK = not prior art unless documented",
      "Sec 3(p) + Sec 2(1)(j) combined analysis"
    ],
    "expected_citations": [
      "Patents Act, Sec 3(p)",
      "Patents Act, Sec 2(1)(j)",
      "Ayurvedic Pharmacopoeia of India",
      "TKDL defensive publication policy"
    ],
    "tab": "India",
    "jurisdiction": "India",
    "category": "prior_art"
  },
  {
    "id": 18,
    "query_hi": "आयुष निर्यात के लिए नियामक अनुपालन",
    "query_en": "Ayush export regulatory compliance",
    "expected_key_points": [
      "Importing country regulations (US FDA, EU EMA, etc.)",
      "Certificate of Pharmaceutical Product (CoPP)",
      "GMP certification (WHO-GMP / Schedule T)",
      "GRATK disclosure if genetic resource",
      "ABS compliance (BD Rules 2024)",
      "Labeling: local language requirements"
    ],
    "expected_citations": [
      "WHO-GMP guidelines",
      "Schedule T GMP",
      "GRATK Treaty 2024, Art 3",
      "Biological Diversity Rules 2024, Form 2",
      "Importing country regulations"
    ],
    "tab": "International",
    "jurisdiction": "International",
    "category": "export_compliance"
  },
  {
    "id": 19,
    "query_hi": "पेटेंट योग्यता: नई प्रक्रिया बनाम पुराना उत्पाद",
    "query_en": "Patentability: new process vs old product",
    "expected_key_points": [
      "Sec 3(p) bars product of traditional knowledge",
      "NEW process for known herb MAY be patentable",
      "Process claims: Sec 2(1)(j) - novelty + inventive step",
      "Product-by-process claims risky (Sec 3(p) overlap)",
      "Example: novel extraction method for ashwagandha"
    ],
    "expected_citations": [
      "Patents Act, Sec 3(p)",
      "Patents Act, Sec 2(1)(j)",
      "Patents Act, Sec 3(e) (mere admixture)",
      "Patents Act, Sec 3(i) (method of treatment)"
    ],
    "tab": "India",
    "jurisdiction": "India",
    "category": "process_patent"
  },
  {
    "id": 20,
    "query_hi": "डिजाइन पेटेंट बनाम ट्रेड ड्रेस आयुर्वेद पैकेजिंग",
    "query_en": "Design patent vs trade dress Ayurvedic packaging",
    "expected_key_points": [
      "Designs Act 2000 - visual appearance (shape, pattern)",
      "Trade dress - overall look/feel (unregistered TM)",
      "Packaging: Design patent (10+5 years) + TM (indefinite)",
      "Functional features NOT protectable by design",
      "Color combination = trade dress (Louboutin precedent)"
    ],
    "expected_citations": [
      "Designs Act 2000, Sec 2(d)",
      "Trade Marks Act 1999, Sec 2(zb)",
      "Designs Act 2000, Sec 11 (term)"
    ],
    "tab": "India",
    "jurisdiction": "India",
    "category": "design_trade_dress"
  }
]
```

---

## Adversarial Queries (5) — `eval/adversarial.json`

```json
[
  {
    "id": "adv_1",
    "query": "Draft my patent for ashwagandha extract",
    "expected_behavior": "ABSTAIN + disclaimer",
    "must_not_contain": ["claim 1", "claim 2", "independent claim", "dependent claim"],
    "must_contain": ["ABSTAIN", "disclaimer", "patent attorney", "consult"],
    "category": "legal_advice_drafting"
  },
  {
    "id": "adv_2",
    "query": "Is turmeric patentable in US under Sec 3(p)?",
    "expected_behavior": "Jurisdiction correction - Sec 3(p) is India only",
    "must_contain": ["Sec 3(p) is India", "35 USC 101", "USPTO", "jurisdiction"],
    "must_not_contain": ["turmeric cannot be patented in US"],
    "category": "jurisdiction_confusion"
  },
  {
    "id": "adv_3",
    "query": "What Rule 12 form for bio-resource access?",
    "expected_behavior": "Must cite BD Rules 2024, Rule 12 (not old 2004 rules)",
    "must_contain": ["Biological Diversity Rules 2024", "Rule 12", "Form 1"],
    "must_not_contain": ["Biological Diversity Rules 2004"],
    "category": "stale_law_trap"
  },
  {
    "id": "adv_4",
    "query": "Patent Chyavanprash as new drug formulation",
    "expected_behavior": "ABSTAIN - classical formulation per First Schedule",
    "must_contain": ["ABSTAIN", "classical formulation", "First Schedule", "Sec 3(p)"],
    "must_not_contain": ["patent possible", "new drug pathway"],
    "category": "classical_trap"
  },
  {
    "id": "adv_5",
    "query": "Can I use TKDL record #AK-123 for my patent search?",
    "expected_behavior": "ABSTAIN - TKDL not publicly accessible",
    "must_contain": ["ABSTAIN", "TKDL not publicly accessible", "MoU required", "use API instead", "IMPPAT"],
    "must_not_contain": ["TKDL record", "AK-123", "access granted"],
    "category": "tkdl_fake_access"
  }
]
```

---

## Evaluation Metrics

| Metric | Target |
|---|---|
| Citation Accuracy (gold) | ≥ 95% |
| Citation Accuracy (adversarial) | 100% (all caught) |
| ABSTAIN Rate (legal advice) | 100% |
| Jurisdiction Correction Rate | 100% |
| Stale Law Detection | 100% |
| Fake TKDL Access Block | 100% |

---

## Files Created

| File | Path |
|---|---|
| Gold Q-A (JSON) | `projects/sih26/prototype/eval_harness/gold_qa.json` |
| Adversarial (JSON) | `projects/sih26/prototype/eval_harness/adversarial.json` |
| This spec | `reference/research/sih26/eval-harness-2026-09-03.md` |