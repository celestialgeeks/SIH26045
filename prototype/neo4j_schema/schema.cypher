// SIH26045 Neo4j Knowledge Graph Schema
// Run in Neo4j Browser or via python init_graph.py

// ============================
// CONSTRAINTS & INDEXES
// ============================

CREATE CONSTRAINT formulation_name IF NOT EXISTS FOR (f:Formulation) REQUIRE f.name IS UNIQUE;
CREATE INDEX formulation_classification IF NOT EXISTS FOR (f:Formulation) ON (f.classification);

CREATE CONSTRAINT statute_id IF NOT EXISTS FOR (s:Statute) REQUIRE s.id IS UNIQUE;
CREATE INDEX statute_jurisdiction IF NOT EXISTS FOR (s:Statute) ON (s.jurisdiction);

CREATE CONSTRAINT procedure_id IF NOT EXISTS FOR (p:Procedure) REQUIRE p.id IS UNIQUE;

CREATE CONSTRAINT ipright_type IF NOT EXISTS FOR (ip:IPRight) REQUIRE ip.type IS UNIQUE;

CREATE CONSTRAINT abs_trigger IF NOT EXISTS FOR (abs:ABSLiability) REQUIRE abs.trigger IS UNIQUE;

CREATE CONSTRAINT approval_type IF NOT EXISTS FOR (a:Approval) REQUIRE a.type IS UNIQUE;

CREATE CONSTRAINT classification_name IF NOT EXISTS FOR (c:Classification) REQUIRE c.name IS UNIQUE;

CREATE CONSTRAINT form_id IF NOT EXISTS FOR (f:Form) REQUIRE f.id IS UNIQUE;

// ============================
// CLASSIFICATIONS
// ============================

MERGE (c1:Classification {name: "Classical", description: "Listed in First Schedule D&C Act, Sec 3(p) bar applies"})
MERGE (c2:Classification {name: "New Drug", description: "Not in API, new combination/process, NDCT pathway"})
MERGE (c3:Classification {name: "Phytopharmaceutical", description: "Standardized extract, marker compounds, CDSCO phytopharma pathway"})
MERGE (c4:Classification {name: "Ayurveda Aahar", description: "Food category, FSSAI 2022 Regs, no patent"})
MERGE (c5:Classification {name: "Cosmetic", description: "Topical, non-therapeutic claims, D&C cosmetic schedule"});

// ============================
// FORMULATIONS
// ============================

MERGE (f1:Formulation {name: "Chyavanprash", ingredients: ["Amla", "Ghee", "Honey", "Spices"], classification: "Classical", api_monograph: true, tkdl_record: true})
MERGE (f2:Formulation {name: "Giloy Phytopharma", ingredients: ["Tinospora cordifolia extract (standardized)"], classification: "Phytopharmaceutical", api_monograph: false, marker_compounds: ["Tinosporaside", "Cordifolioside"]})
MERGE (f3:Formulation {name: "Ashwagandha Capsule (new combo)", ingredients: ["Withania somnifera", "Piper nigrum"], classification: "New Drug", api_monograph: false, novel_process: true})
MERGE (f4:Formulation {name: "Triphala Aahar", ingredients: ["Haritaki", "Bibhitaki", "Amalaki"], classification: "Ayurveda Aahar", api_monograph: false, fssai_registered: true})
MERGE (f5:Formulation {name: "Kumkumadi Tailam", ingredients: ["Saffron", "Sandalwood", "Lotus"], classification: "Classical", api_monograph: true, cosmetic_also: true});

MATCH (f:Formulation), (c:Classification) WHERE f.classification = c.name MERGE (f)-[:IS_CLASSIFIED_AS]->(c);

// ============================
// STATUTES (version-tracked)
// ============================

MERGE (s1:Statute {id: "patents-act-1970", name: "Patents Act 1970", section: "3(p)", text: "Traditional knowledge not patentable", jurisdiction: "India", version_date: "1970-04-20", gazette_date: "1970-04-20", url: "http://ipindia.gov.in"});
MERGE (s2:Statute {id: "patents-rules-2024", name: "Patents (Amendment) Rules 2024", section: "12", text: "Forms and fees", jurisdiction: "India", version_date: "2024-03-15", gazette_date: "2024-03-15", url: "http://egazette.nic.in"});
MERGE (s3:Statute {id: "bd-act-2002", name: "Biological Diversity Act 2002", section: "3(2)", text: "Foreign entity prior approval", jurisdiction: "India", version_date: "2002-02-05", gazette_date: "2002-02-05", url: "http://nbaindia.nic.in"});
MERGE (s4:Statute {id: "bd-amendment-2023", name: "Biological Diversity (Amendment) Act 2023", section: "6", text: "ABS for commercial utilization", jurisdiction: "India", version_date: "2023-04-01", gazette_date: "2023-04-01", url: "http://egazette.nic.in"});
MERGE (s5:Statute {id: "bd-rules-2024", name: "Biological Diversity Rules 2024", section: "4", text: "Benefit sharing percentage", jurisdiction: "India", version_date: "2024-10-25", gazette_date: "2024-10-25", url: "http://egazette.nic.in"});
MERGE (s6:Statute {id: "gratk-2024", name: "WIPO GRATK Treaty 2024", section: "3", text: "Disclosure of origin for GR/TK", jurisdiction: "International", version_date: "2024-05-24", gazette_date: "2024-05-24", url: "https://wipo.int"});
MERGE (s7:Statute {id: "dc-act-1940", name: "Drugs & Cosmetics Act 1940", section: "3(a)", text: "Classical formulation definition", jurisdiction: "India", version_date: "1940-04-10", gazette_date: "1940-04-10", url: "http://cdsco.gov.in"});
MERGE (s8:Statute {id: "ndct-2019", name: "NDCT Rules 2019", section: "122E", text: "Phytopharmaceutical clinical trials", jurisdiction: "India", version_date: "2019-03-19", gazette_date: "2019-03-19", url: "http://cdsco.gov.in"});
MERGE (s9:Statute {id: "fssai-aahar-2022", name: "FSSAI Ayurveda Aahar Regulations 2022", section: "5", text: "Aahar category definition", jurisdiction: "India", version_date: "2022-07-01", gazette_date: "2022-07-01", url: "http://fssai.gov.in"});
MERGE (s10:Statute {id: "gi-act-1999", name: "Geographical Indications Act 1999", section: "2(e)", text: "GI definition", jurisdiction: "India", version_date: "1999-12-30", gazette_date: "1999-12-30", url: "http://ipindia.gov.in"});
MERGE (s11:Statute {id: "tm-act-1999", name: "Trade Marks Act 1999", section: "9", text: "Absolute grounds for refusal", jurisdiction: "India", version_date: "1999-12-30", gazette_date: "1999-12-30", url: "http://ipindia.gov.in"});
MERGE (s12:Statute {id: "pct", name: "Patent Cooperation Treaty", section: "4", text: "International application", jurisdiction: "International", version_date: "1970-06-19", gazette_date: "1978-01-24", url: "https://wipo.int/pct"});
MERGE (s13:Statute {id: "trips", name: "TRIPS Agreement", section: "27.3(b)", text: "Patent exceptions for plants/animals", jurisdiction: "International", version_date: "1994-04-15", gazette_date: "1995-01-01", url: "https://wto.org"});
MERGE (s14:Statute {id: "nagoya", name: "Nagoya Protocol", section: "5", text: "Fair and equitable benefit sharing", jurisdiction: "International", version_date: "2010-10-29", gazette_date: "2014-10-12", url: "https://cbd.int"});
MERGE (s15:Statute {id: "ppvfr-2001", name: "PPVFR Act 2001", section: "15", text: "Plant variety registration", jurisdiction: "India", version_date: "2001-10-30", gazette_date: "2001-10-30", url: "http://plantauthority.gov.in"});
MERGE (s16:Statute {id: "designs-2000", name: "Designs Act 2000", section: "2(d)", text: "Design definition", jurisdiction: "India", version_date: "2000-05-25", gazette_date: "2000-05-25", url: "http://ipindia.gov.in"});

// ============================
// PROCEDURES
// ============================

MERGE (p1:Procedure {id: "patent-filing", name: "Patent Filing (India)", authority: "Indian Patent Office", forms: ["Form 1", "Form 2", "Form 3", "Form 5", "Form 26"], timeline_months: 36, fees_inr: 1600, description: "Provisional -> Complete -> Examination -> Grant"});
MERGE (p2:Procedure {id: "pct-filing", name: "PCT International Filing", authority: "WIPO / Indian Patent Office (RO/IN)", forms: ["PCT/RO/101"], timeline_months: 30, fees_usd: 1471, description: "International search -> Publication -> National phase"});
MERGE (p3:Procedure {id: "abs-foreign", name: "ABS Approval (Foreign Entity)", authority: "National Biodiversity Authority", forms: ["Form 2"], timeline_months: 6, fees_inr: 50000, description: "Prior approval + benefit sharing agreement"});
MERGE (p4:Procedure {id: "abs-indian", name: "ABS Intimation (Indian Entity)", authority: "State Biodiversity Board", forms: ["Form 1"], timeline_months: 1, fees_inr: 0, description: "Prior intimation only"});
MERGE (p5:Procedure {id: "cdsco-phytopharma", name: "Phytopharmaceutical Approval", authority: "CDSCO", forms: ["Form 44", "CT-01"], timeline_months: 24, fees_inr: 50000, description: "Phase I/II/III trials + marketing authorization"});
MERGE (p6:Procedure {id: "fssai-aahar", name: "Ayurveda Aahar Registration", authority: "FSSAI", forms: ["Form A"], timeline_months: 2, fees_inr: 2000, description: "Food license + labeling compliance"});
MERGE (p7:Procedure {id: "gi-registration", name: "GI Registration", authority: "GI Registry", forms: ["GI-1", "GI-2"], timeline_months: 12, fees_inr: 5000, description: "Association of producers + geographical link proof"});
MERGE (p8:Procedure {id: "tm-filing", name: "Trademark Filing", authority: "Trade Marks Registry", forms: ["TM-A"], timeline_months: 18, fees_inr: 4500, description: "Examination -> Publication -> Opposition -> Registration"});
MERGE (p9:Procedure {id: "design-filing", name: "Design Registration", authority: "Design Office", forms: ["Form 1"], timeline_months: 12, fees_inr: 1000, description: "Examination -> Registration (10+5 years)"});
MERGE (p10:Procedure {id: "pvpf-registration", name: "Plant Variety Registration", authority: "PPV&FR Authority", forms: ["Form I"], timeline_months: 24, fees_inr: 10000, description: "DUS test + registration"});

// ============================
// IP RIGHTS
// ============================

MERGE (ip1:IPRight {type: "Patent", requirements: ["Novelty", "Inventive Step", "Industrial Application", "Not Sec 3(p)"], term_years: 20, jurisdiction: "India"});
MERGE (ip2:IPRight {type: "Patent", requirements: ["Novelty", "Non-obviousness", "Utility", "35 USC 101"], term_years: 20, jurisdiction: "US"});
MERGE (ip3:IPRight {type: "Patent", requirements: ["Novelty", "Inventive Step", "Industrial Application", "Art 52 EPC"], term_years: 20, jurisdiction: "EP"});
MERGE (ip4:IPRight {type: "Patent", requirements: ["Novelty", "Inventive Step", "Industrial Application", "Art 25 Patent Law CN"], term_years: 20, jurisdiction: "CN"});
MERGE (ip5:IPRight {type: "GI", requirements: ["Geographical Origin", "Quality/Reputation Link", "Collective Rights"], term_years: -1, jurisdiction: "India"});
MERGE (ip6:IPRight {type: "Trademark", requirements: ["Distinctive", "Non-descriptive", "Not deceptive"], term_years: 10, jurisdiction: "India", renewable: true});
MERGE (ip7:IPRight {type: "Design", requirements: ["New", "Original", "Visual Appeal", "Non-functional"], term_years: 15, jurisdiction: "India"});
MERGE (ip8:IPRight {type: "Copyright", requirements: ["Original Expression", "Fixed Form"], term_years: 60, jurisdiction: "India"});
MERGE (ip9:IPRight {type: "Plant Variety", requirements: ["DUS Test", "New Variety", "Denomination"], term_years: 15, jurisdiction: "India"});
MERGE (ip10:IPRight {type: "Trade Secret", requirements: ["Secret", "Commercial Value", "Reasonable Steps"], term_years: -1, jurisdiction: "Both"});

// ============================
// ABS LIABILITIES
// ============================

MERGE (abs1:ABSLiability {trigger: "Foreign Commercial", forms: ["Form 2"], benefit_sharing_pct: "3-5% ex-factory", authority: "NBA", description: "Prior approval + benefit sharing agreement"});
MERGE (abs2:ABSLiability {trigger: "Indian Commercial", forms: ["Form 1"], benefit_sharing_pct: "0.5-1% ex-factory", authority: "SBB", description: "Prior intimation + benefit sharing"});
MERGE (abs3:ABSLiability {trigger: "Collaborative Research", forms: [], benefit_sharing_pct: "Per agreement", authority: "NBA/SBB", description: "Exempt from prior approval if non-commercial"});
MERGE (abs4:ABSLiability {trigger: "Non-commercial", forms: [], benefit_sharing_pct: "N/A", authority: "N/A", description: "Academic research, education exempt"});

// ============================
// APPROVALS
// ============================

MERGE (a1:Approval {type: "CDSCO Drug", pathway: "New Drug / Phytopharma", requirements: ["Clinical Trials", "GMP", "Stability", "Bioequivalence"], timeline_months: 24});
MERGE (a2:Approval {type: "FSSAI Food", pathway: "Ayurveda Aahar", requirements: ["Food Safety Plan", "Labeling", "Additive Compliance"], timeline_months: 2});
MERGE (a3:Approval {type: "State Ayush", pathway: "Classical Manufacturing", requirements: ["GMP Schedule T", "Raw Material Auth", "Process Validation"], timeline_months: 6});
MERGE (a4:Approval {type: "CDSCO Cosmetic", pathway: "Cosmetic License", requirements: ["Ingredient Safety", "Labeling", "Heavy Metals"], timeline_months: 3});

// ============================
// FORMS
// ============================

MERGE (form1:Form {id: "bd-form-1", name: "Form 1", statute: "BD Rules 2024", purpose: "Prior intimation (Indian entity)"});
MERGE (form2:Form {id: "bd-form-2", name: "Form 2", statute: "BD Rules 2024", purpose: "Prior approval (Foreign entity)"});
MERGE (form3:Form {id: "patent-form-1", name: "Form 1", statute: "Patents Rules 2024", purpose: "Application for patent grant"});
MERGE (form4:Form {id: "patent-form-2", name: "Form 2", statute: "Patents Rules 2024", purpose: "Provisional/Complete specification"});
MERGE (form5:Form {id: "patent-form-5", name: "Form 5", statute: "Patents Rules 2024", purpose: "Declaration of inventorship"});
MERGE (form6:Form {id: "patent-form-26", name: "Form 26", statute: "Patents Rules 2024", purpose: "Power of attorney"});
MERGE (form7:Form {id: "pct-ro-101", name: "PCT/RO/101", statute: "PCT", purpose: "International application"});
MERGE (form8:Form {id: "cdsco-form-44", name: "Form 44", statute: "NDCT Rules 2019", purpose: "Clinical trial permission"});
MERGE (form9:Form {id: "cdsco-ct-01", name: "CT-01", statute: "NDCT Rules 2019", purpose: "New drug permission"});
MERGE (form10:Form {id: "fssai-form-a", name: "Form A", statute: "FSSAI Regulations", purpose: "Food license application"});
MERGE (form11:Form {id: "gi-form-1", name: "GI-1", statute: "GI Act 1999", purpose: "GI registration application"});
MERGE (form12:Form {id: "gi-form-2", name: "GI-2", statute: "GI Act 1999", purpose: "Statement of case"});
MERGE (form13:Form {id: "tm-form-a", name: "TM-A", statute: "TM Act 1999", purpose: "Trademark application"});
MERGE (form14:Form {id: "design-form-1", name: "Form 1", statute: "Designs Act 2000", purpose: "Design registration"});
MERGE (form15:Form {id: "pvpf-form-i", name: "Form I", statute: "PPVFR Act 2001", purpose: "Variety registration"});

// ============================
// RELATIONSHIPS: CLASSIFICATION -> IP RIGHTS (BARS / ALLOWS)
// ============================

// Classical formulation BARS Patent, ALLOWS GI + TM
MATCH (c:Classification {name: "Classical"}), (ip:IPRight {type: "Patent", jurisdiction: "India"}) MERGE (c)-[:BARS {reason: "Sec 3(p) Patents Act"}]->(ip);
MATCH (c:Classification {name: "Classical"}), (ip:IPRight {type: "GI"}) MERGE (c)-[:ALLOWS {reason: "Collective rights, not individual patent"}]->(ip);
MATCH (c:Classification {name: "Classical"}), (ip:IPRight {type: "Trademark"}) MERGE (c)-[:ALLOWS {reason: "Brand protection only, not formulation"}]->(ip);
MATCH (c:Classification {name: "Classical"}), (ip:IPRight {type: "Plant Variety"}) MERGE (c)-[:BARS {reason: "Not a plant variety"}]->(ip);

// New Drug ALLOWS Patent, ALLOWS TM
MATCH (c:Classification {name: "New Drug"}), (ip:IPRight {type: "Patent", jurisdiction: "India"}) MERGE (c)-[:ALLOWS {reason: "Sec 2(1)(j) novelty + inventive step"}]->(ip);
MATCH (c:Classification {name: "New Drug"}), (ip:IPRight {type: "Trademark"}) MERGE (c)-[:ALLOWS]->(ip);

// Phytopharmaceutical ALLOWS Patent + CDSCO pathway
MATCH (c:Classification {name: "Phytopharmaceutical"}), (ip:IPRight {type: "Patent", jurisdiction: "India"}) MERGE (c)-[:ALLOWS {reason: "Standardized extract = invention"}]->(ip);
MATCH (c:Classification {name: "Phytopharmaceutical"}), (ip:IPRight {type: "Trademark"}) MERGE (c)-[:ALLOWS]->(ip);

// Ayurveda Aahar BARS Patent, ALLOWS GI + TM
MATCH (c:Classification {name: "Ayurveda Aahar"}), (ip:IPRight {type: "Patent", jurisdiction: "India"}) MERGE (c)-[:BARS {reason: "Food category, FSSAI 2022 Reg 5"}]->(ip);
MATCH (c:Classification {name: "Ayurveda Aahar"}), (ip:IPRight {type: "GI"}) MERGE (c)-[:ALLOWS {reason: "Geographical food product"}]->(ip);
MATCH (c:Classification {name: "Ayurveda Aahar"}), (ip:IPRight {type: "Trademark"}) MERGE (c)-[:ALLOWS]->(ip);

// Cosmetic ALLOWS Design + TM, BARS Patent (usually)
MATCH (c:Classification {name: "Cosmetic"}), (ip:IPRight {type: "Design"}) MERGE (c)-[:ALLOWS {reason: "Packaging/appearance"}]->(ip);
MATCH (c:Classification {name: "Cosmetic"}), (ip:IPRight {type: "Trademark"}) MERGE (c)-[:ALLOWS]->(ip);
MATCH (c:Classification {name: "Cosmetic"}), (ip:IPRight {type: "Patent", jurisdiction: "India"}) MERGE (c)-[:BARS {reason: "Rarely meets inventive step"}]->(ip);

// ============================
// FORMULATION -> PROCEDURES (REQUIRES)
// ============================

MATCH (f:Formulation {classification: "Classical"}), (p:Procedure) WHERE p.id IN ["gi-registration", "tm-filing"] MERGE (f)-[:REQUIRES]->(p);
MATCH (f:Formulation {classification: "New Drug"}), (p:Procedure) WHERE p.id IN ["patent-filing", "pct-filing", "cdsco-phytopharma", "tm-filing"] MERGE (f)-[:REQUIRES]->(p);
MATCH (f:Formulation {classification: "Phytopharmaceutical"}), (p:Procedure) WHERE p.id IN ["patent-filing", "pct-filing", "cdsco-phytopharma", "tm-filing"] MERGE (f)-[:REQUIRES]->(p);
MATCH (f:Formulation {classification: "Ayurveda Aahar"}), (p:Procedure) WHERE p.id IN ["fssai-aahar", "gi-registration", "tm-filing"] MERGE (f)-[:REQUIRES]->(p);
MATCH (f:Formulation {classification: "Cosmetic"}), (p:Procedure) WHERE p.id IN ["design-filing", "tm-filing"] MERGE (f)-[:REQUIRES]->(p);

// ============================
// FORMULATION -> ABS (TRIGGERS)
// ============================

MATCH (f:Formulation), (abs:ABSLiability {trigger: "Foreign Commercial"}) MERGE (f)-[:TRIGGERS {condition: "Foreign entity + commercial utilization"}]->(abs);
MATCH (f:Formulation), (abs:ABSLiability {trigger: "Indian Commercial"}) MERGE (f)-[:TRIGGERS {condition: "Indian entity + commercial utilization"}]->(abs);

// ============================
// STATUTE -> PROCEDURE (GOVERNS)
// ============================

MATCH (s:Statute {id: "patents-act-1970"}), (p:Procedure {id: "patent-filing"}) MERGE (s)-[:GOVERNS]->(p);
MATCH (s:Statute {id: "patents-rules-2024"}), (p:Procedure {id: "patent-filing"}) MERGE (s)-[:GOVERNS]->(p);
MATCH (s:Statute {id: "bd-amendment-2023"}), (p:Procedure {id: "abs-foreign"}) MERGE (s)-[:GOVERNS]->(p);
MATCH (s:Statute {id: "bd-rules-2024"}), (p:Procedure {id: "abs-foreign"}) MERGE (s)-[:GOVERNS]->(p);
MATCH (s:Statute {id: "bd-rules-2024"}), (p:Procedure {id: "abs-indian"}) MERGE (s)-[:GOVERNS]->(p);
MATCH (s:Statute {id: "gratk-2024"}), (p:Procedure {id: "pct-filing"}) MERGE (s)-[:GOVERNS]->(p);
MATCH (s:Statute {id: "dc-act-1940"}), (p:Procedure {id: "cdsco-phytopharma"}) MERGE (s)-[:GOVERNS]->(p);
MATCH (s:Statute {id: "ndct-2019"}), (p:Procedure {id: "cdsco-phytopharma"}) MERGE (s)-[:GOVERNS]->(p);
MATCH (s:Statute {id: "fssai-aahar-2022"}), (p:Procedure {id: "fssai-aahar"}) MERGE (s)-[:GOVERNS]->(p);
MATCH (s:Statute {id: "gi-act-1999"}), (p:Procedure {id: "gi-registration"}) MERGE (s)-[:GOVERNS]->(p);
MATCH (s:Statute {id: "tm-act-1999"}), (p:Procedure {id: "tm-filing"}) MERGE (s)-[:GOVERNS]->(p);
MATCH (s:Statute {id: "designs-2000"}), (p:Procedure {id: "design-filing"}) MERGE (s)-[:GOVERNS]->(p);
MATCH (s:Statute {id: "ppvfr-2001"}), (p:Procedure {id: "pvpf-registration"}) MERGE (s)-[:GOVERNS]->(p);

// ============================
// PROCEDURE -> FORM (USES_FORM)
// ============================

MATCH (p:Procedure {id: "abs-foreign"}), (f:Form {id: "bd-form-2"}) MERGE (p)-[:USES_FORM]->(f);
MATCH (p:Procedure {id: "abs-indian"}), (f:Form {id: "bd-form-1"}) MERGE (p)-[:USES_FORM]->(f);
MATCH (p:Procedure {id: "patent-filing"}), (f:Form) WHERE f.id IN ["patent-form-1","patent-form-2","patent-form-5","patent-form-26"] MERGE (p)-[:USES_FORM]->(f);
MATCH (p:Procedure {id: "pct-filing"}), (f:Form {id: "pct-ro-101"}) MERGE (p)-[:USES_FORM]->(f);
MATCH (p:Procedure {id: "cdsco-phytopharma"}), (f:Form) WHERE f.id IN ["cdsco-form-44","cdsco-ct-01"] MERGE (p)-[:USES_FORM]->(f);
MATCH (p:Procedure {id: "fssai-aahar"}), (f:Form {id: "fssai-form-a"}) MERGE (p)-[:USES_FORM]->(f);
MATCH (p:Procedure {id: "gi-registration"}), (f:Form) WHERE f.id IN ["gi-form-1","gi-form-2"] MERGE (p)-[:USES_FORM]->(f);
MATCH (p:Procedure {id: "tm-filing"}), (f:Form {id: "tm-form-a"}) MERGE (p)-[:USES_FORM]->(f);
MATCH (p:Procedure {id: "design-filing"}), (f:Form {id: "design-form-1"}) MERGE (p)-[:USES_FORM]->(f);
MATCH (p:Procedure {id: "pvpf-registration"}), (f:Form {id: "pvpf-form-i"}) MERGE (p)-[:USES_FORM]->(f);