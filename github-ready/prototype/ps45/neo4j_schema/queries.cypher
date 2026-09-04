// SIH26045 Neo4j Key Traversal Queries
// Run in Neo4j Browser for testing

// ============================
// 1. FULL IP + REGULATORY PATHWAY FOR A FORMULATION
// ============================
MATCH (f:Formulation {name: $name})-[:IS_CLASSIFIED_AS]->(c)
OPTIONAL MATCH (c)-[b:BARS|a:ALLOWS]->(ip:IPRight)
OPTIONAL MATCH (f)-[:REQUIRES]->(ap:Approval)
OPTIONAL MATCH (f)-[:TRIGGERS]->(abs:ABSLiability)
OPTIONAL MATCH (c)-[:ALLOWS]->(ip2:IPRight)
RETURN 
  f.name AS formulation,
  c.name AS classification,
  collect(DISTINCT {type: ip.type, jurisdiction: ip.jurisdiction, bars: b IS NOT NULL, allows: a IS NOT NULL, reason: COALESCE(b.reason, a.reason)}) AS ip_rights,
  collect(DISTINCT {type: ap.type, pathway: ap.pathway, timeline: ap.timeline_months}) AS approvals,
  collect(DISTINCT {trigger: abs.trigger, forms: abs.forms, benefit_sharing: abs.benefit_sharing_pct}) AS abs_liabilities
ORDER BY f.name;

// Example: Test with Chyavanprash
// :param name => "Chyavanprash"


// ============================
// 2. CITATION GRAPH: STATUTES GOVERNING PROCEDURES & FORMS
// ============================
MATCH (s:Statute)-[:GOVERNS]->(p:Procedure)-[:USES_FORM]->(form:Form)
RETURN 
  s.name AS statute,
  s.section AS section,
  s.version_date AS version,
  s.gazette_date AS gazette,
  p.name AS procedure,
  form.name AS form,
  form.purpose AS form_purpose
ORDER BY s.jurisdiction, s.name, p.name;


// ============================
// 3. CLASSIFICATION -> IP RIGHTS MATRIX
// ============================
MATCH (c:Classification)-[r:BARS|ALLOWS]->(ip:IPRight)
RETURN 
  c.name AS classification,
  ip.type AS ip_right,
  ip.jurisdiction AS jurisdiction,
  TYPE(r) AS relationship,
  r.reason AS reason
ORDER BY c.name, ip.type, ip.jurisdiction;


// ============================
// 4. ABS TRIGGER CHECK FOR FORMULATION + ENTITY TYPE
// ============================
MATCH (f:Formulation {name: $name})-[:TRIGGERS]->(abs:ABSLiability)
WHERE abs.trigger CONTAINS $entity_type  // "Foreign" or "Indian"
RETURN 
  f.name AS formulation,
  abs.trigger AS trigger,
  abs.forms AS forms,
  abs.benefit_sharing_pct AS benefit_sharing,
  abs.authority AS authority,
  abs.description AS description;

// Example: 
// :param name => "Giloy Phytopharma"
// :param entity_type => "Foreign"


// ============================
// 5. STATUTE VERSION CHECK (ANTI-STALE-LAW)
// ============================
MATCH (s:Statute)
WHERE s.name CONTAINS $keyword
RETURN 
  s.name AS statute,
  s.version_date AS version,
  s.gazette_date AS gazette,
  s.url AS source
ORDER BY s.version_date DESC;

// Example:
// :param keyword => "Biological Diversity"


// ============================
// 6. FORMULATION INGREDIENT -> MARKER COMPOUND LOOKUP
// ============================
MATCH (f:Formulation {name: $name})
RETURN 
  f.name AS formulation,
  f.ingredients AS ingredients,
  f.marker_compounds AS markers,
  f.api_monograph AS has_api_monograph,
  f.tkdl_record AS has_tkdl_record,
  f.classification AS classification;

// Example:
// :param name => "Giloy Phytopharma"


// ============================
// 7. PROCEDURE TIMELINE + FORMS SUMMARY
// ============================
MATCH (p:Procedure)
OPTIONAL MATCH (p)-[:USES_FORM]->(f:Form)
RETURN 
  p.name AS procedure,
  p.authority AS authority,
  p.timeline_months AS timeline_months,
  p.fees_inr AS fees_inr,
  p.fees_usd AS fees_usd,
  collect(f.name) AS forms
ORDER BY p.timeline_months;


// ============================
// 8. ALL STATUTES BY JURISDICTION
// ============================
MATCH (s:Statute)
RETURN 
  s.jurisdiction AS jurisdiction,
  collect({name: s.name, section: s.section, version: s.version_date, gazette: s.gazette_date}) AS statutes
ORDER BY s.jurisdiction;


// ============================
// 9. FORMULATION CLASSIFICATION DISTRIBUTION
// ============================
MATCH (f:Formulation)-[:IS_CLASSIFIED_AS]->(c:Classification)
RETURN 
  c.name AS classification,
  count(f) AS count,
  collect(f.name) AS formulations
ORDER BY count DESC;


// ============================
// 10. IP RIGHTS AVAILABLE PER JURISDICTION
// ============================
MATCH (ip:IPRight)
RETURN 
  ip.jurisdiction AS jurisdiction,
  collect({type: ip.type, term: ip.term_years, requirements: ip.requirements}) AS rights
ORDER BY ip.jurisdiction;