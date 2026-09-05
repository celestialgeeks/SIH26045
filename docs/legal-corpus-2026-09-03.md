# SIH26045 — Legal Corpus Acquisition (Exact Sources)
**Date:** 2026-09-03 | **Researcher:** @researcher | **Iteration:** 1/4
**Status:** EXTENDED 2026-09-05 — 10→13 docs. Added UPI + InPASS + TM Registry (deployable completeness). See §Decision Log 2026-09-05. G.S.R.665(E) direct Gazette link TODO.

---

## Verified Legal Corpus Table

| # | Document | Official Source URL | Gazette Notification | Gazette Date | Access Method | Pages | SHA256 (to verify) |
|---|----------|---------------------|---------------------|--------------|---------------|-------|-------------------|
| 1 | **Patents Act 1970 (as amended)** | https://ipindia.gov.in/writereaddata/Portal/IPORule/1_83_1_Patent_Amendment_Rule_2024_Gazette_Copy.pdf | — | — | Direct PDF download from IP India | ~60 | TBD after download |
| 2 | **Patents (Amendment) Rules 2024** | https://ipindia.gov.in/writereaddata/Portal/IPORule/1_83_1_Patent_Amendment_Rule_2024_Gazette_Copy.pdf | **G.S.R. 211(E)** | **15 March 2024** | Direct PDF (same file as above) | ~30 | TBD |
| 3 | **Biological Diversity Act 2002** | http://nbaindia.org/uploaded/pdf/Regu2025.pdf | — | 2002 (amended 2023) | NBA website PDF | ~40 | TBD |
| 4 | **Biological Diversity (Amendment) Act 2023** | http://nbaindia.org/uploaded/pdf/Regu2025.pdf | — | **1 April 2024** (in force) | NBA website PDF (included in Rules 2025 doc) | ~15 | TBD |
| 5 | **Biological Diversity Rules 2024** | http://nbaindia.org/uploaded/pdf/Regu2025.pdf | **G.S.R. 665(E)** | **22 Oct 2024** (notified), **25 Dec 2024** (in force) | NBA website PDF (Regu2025.pdf) | ~50 | TBD |
| 6 | **WIPO GRATK Treaty 2024** | https://www.wipo.int/edocs/mdocs/tk/en/gratk_dc/gratk_dc_7.pdf | — | **24 May 2024** (adopted) | WIPO official PDF (GRATK/DC/7) | ~25 | TBD |
| 7 | **Ayurvedic Pharmacopoeia of India (API)** | https://ayush.gov.in / https://echarak.ayush.gov.in | — | Ongoing (Parts I-X) | Ministry of Ayush website, E-Charak portal | Vol I-X | TBD |
| 8 | **IMPPAT 2.0 Database** | https://cb.imsc.res.in/imppat | — | **17 June 2022** (v2.0) | Web interface + bulk downloader (GitHub) | N/A (DB) | N/A |
| 9 | **Drugs & Magic Remedies Act 1954 + 2024 Advisory** | https://cdsco.gov.in | — | 1954 + 2024 advisory | CDSCO website | ~10 | TBD |
| 10 | **FSSAI Ayurveda Aahar Regulations 2022** | https://fssai.gov.in | — | 2022 | FSSAI website | ~15 | TBD |

---

## Key Gazette Notifications (Verified)

### Patents (Amendment) Rules 2024
- **Notification:** G.S.R. 211(E)
- **Date:** 15 March 2024
- **Department:** Ministry of Commerce & Industry, DPIIT
- **Key Changes:**
  - Form 27 (working statement) → triennial filing (was annual)
  - First statement due within 6 years (was 3 months)
  - Certificate of registration of patent (CRN) filing
  - Disclosure of biological resource origin in patent applications
  - Grace period clarification for "learned society" disclosures

### Biological Diversity Rules 2024
- **Notification:** G.S.R. 665(E)
- **Date:** 22 October 2024 (notified), 25 December 2024 (in force)
- **Ministry:** MoEFCC
- **Key Changes:**
  - Supersedes BD Rules 2004
  - Online procedures, digital payments to National Biodiversity Fund
  - Form 1: Research/bio-survey/bio-utilization access
  - Form 2: Commercial utilization access
  - Form 11: Certificate of origin for cultivated medicinal plants (BMC issues in 15 days)
  - Fee: INR 10,000 (individual), INR 20,000 (entity)
  - Prior NBA approval before IPR grant for foreign entities
  - 45-day intimation to NBA after IPR grant
  - Decriminalized offenses → fines up to INR 50 lakh

### WIPO GRATK Treaty 2024
- **Adopted:** 24 May 2024 (Diplomatic Conference, Geneva)
- **Entry into force:** 3 months after 15 ratifications
- **Key Articles:**
  - **Art 1:** Objectives — enhance patent system efficacy/transparency/quality re: GR & TK
  - **Art 3:** Mandatory disclosure — country of origin of GR, or Indigenous People/local community for associated TK
  - **Art 3.2:** If unknown → disclose source of GR/TK
  - **"Based on" definition:** GR/TK necessary for invention, invention depends on specific properties
  - **Art 5:** Sanctions — only for fraudulent intent; no revocation solely for non-disclosure
  - **Art 6:** Rectification opportunity pre/post grant
  - **Non-retroactive** (Art 28 VCLT)

---

## Drugs & Cosmetics Act — First Schedule (Classical Formulations)

**Authoritative Books for Ayurveda (First Schedule, Section 3(a)):**
- **Original 54 books** including: Charaka Samhita, Sushruta Samhita, Ashtanga Hridaya, Ashtanga Samgraha, Sharangadhara Samhita, Bhaishajya Ratnavali, Bhava Prakasha, Yoga Ratnakara, Rasaratna Samuchaya, etc.
- **Amendment 1987 (GSR 735(E)):** Added **54-A Ayurvedic Formulary of India (Part-I)**, **54-B Ayurveda Sara Sangraha**, **54-C Ayurvedic Pharmacopoeia of India**, **54-D Ayurvedic Pharmacopoeia of India and its Parts**
- **Draft Amendment 2024:** Expands to **227 books** (adds vernacular texts with author names)

**Classical Formulation Definition (Sec 3(a)):** Medicines manufactured *exclusively* in accordance with formulae in First Schedule books.

**Patent/Proprietary Medicine (Sec 3(h)(i)):** Formulations containing only ingredients from First Schedule formulae, but NOT administered parenterally AND NOT in authoritative books.

**Sections 5 & 7 NOT applicable** to Ayurvedic/Siddha/Unani drugs (Sec 7A).

---

## Download Checklist for Team

```bash
# 1. Patents Act + Amendment Rules 2024
wget "https://ipindia.gov.in/writereaddata/Portal/IPORule/1_83_1_Patent_Amendment_Rule_2024_Gazette_Copy.pdf" -O patents_act_2024_gazette.pdf

# 2. Biological Diversity Act + Amendment 2023 + Rules 2024 + Regulations 2025
wget "http://nbaindia.org/uploaded/pdf/Regu2025.pdf" -O bd_act_rules_2024_2025.pdf

# 3. WIPO GRATK Treaty 2024
wget "https://www.wipo.int/edocs/mdocs/tk/en/gratk_dc/gratk_dc_7.pdf" -O wipo_gratk_treaty_2024.pdf

# 4. Drugs & Cosmetics Act 1940 (with First Schedule)
wget "https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2022/acts_and_rules/Drugs%20and%20Cosmetics%20Act%2C%201940.pdf" -O dca_1940_first_schedule.pdf

# 5. NDCT Rules 2019
wget "https://cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/NewDrugs_CTRules_2019.pdf" -O ndct_rules_2019.pdf

# 6. FSSAI Ayurveda Aahar Regs 2022
# Search FSSAI website for PDF

# 7. Drugs & Magic Remedies Act + 2024 Advisory
# Search CDSCO website
```

---

## Corpus Versioning Schema (for chunk metadata)

```json
{
  "doc_id": "patents_rules_2024",
  "title": "Patents (Amendment) Rules 2024",
  "gazette_notification": "G.S.R. 211(E)",
  "gazette_date": "2024-03-15",
  "source_url": "https://ipindia.gov.in/writereaddata/Portal/IPORule/1_83_1_Patent_Amendment_Rule_2024_Gazette_Copy.pdf",
  "sha256": "<compute after download>",
  "page_count": 30,
  "jurisdiction": "india",
  "doc_type": "rules",
  "version": "2024-03-15",
  "language": "en"
}
```

---

## Sources Cited

1. Gazette Tracker: https://gazettetracker.com/g/CG-DL-E-15032024-253078 (Patents Amendment Rules 2024)
2. Sandalaw Offices PDF: https://sandalawoffices.com/wp-content/uploads/2024/03/Patent_Amendment_Rule_2024_Gazette_.pdf
3. NBA Regu2025.pdf: http://nbaindia.org/uploaded/pdf/Regu2025.pdf (BD Act + Rules 2024 + Regs 2025)
4. Trilegal Roundup: https://trilegal.com/magazine/life-sciences-milestones-issue-14.html
5. WIPO GRATK/DC/7: https://www.wipo.int/edocs/mdocs/tk/en/gratk_dc/gratk_dc_7.pdf
6. WIPO Summary: https://www.wipo.int/en/web/treaties/ip/gratk/summary_gratk
7. IndiaCode First Schedule: https://upload.indiacode.nic.in/schedulefile?aid=AC_CEN_12_13_00023_194023_1523353460112&rid=628
8. CDSCO D&C Act PDF: https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2022/acts_and_rules/Drugs%20and%20Cosmetics%20Act%2C%201940.pdf
9. IMPPAT 2.0: https://cb.imsc.res.in/imppat, GitHub: https://github.com/asamallab/imppat2
10. NDCT Rules: https://cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/NewDrugs_CTRules_2019.pdf