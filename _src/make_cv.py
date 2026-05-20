# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable, ListFlowable, ListItem)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT

NAVY = colors.HexColor("#0F1A36")
INK = colors.HexColor("#1E293B")
INK2 = colors.HexColor("#475569")
BLUE = colors.HexColor("#2563EB")
CYAN = colors.HexColor("#0891B2")
LINE = colors.HexColor("#CBD5E1")

doc = SimpleDocTemplate("assets/Ahmed-M-Bedeer-CV.pdf", pagesize=A4,
                        leftMargin=16*mm, rightMargin=16*mm, topMargin=14*mm, bottomMargin=12*mm,
                        title="Ahmed M. Bedeer — CV", author="Ahmed M. Bedeer")
S = getSampleStyleSheet()
story = []

name = ParagraphStyle("name", parent=S["Title"], fontName="Helvetica-Bold", fontSize=22,
                      textColor=NAVY, spaceAfter=2, leading=24)
role = ParagraphStyle("role", parent=S["Normal"], fontName="Helvetica", fontSize=10.5,
                      textColor=CYAN, spaceAfter=4)
contact = ParagraphStyle("contact", parent=S["Normal"], fontName="Helvetica", fontSize=8.6,
                         textColor=INK2, spaceAfter=2, leading=12)
h = ParagraphStyle("h", parent=S["Heading2"], fontName="Helvetica-Bold", fontSize=11,
                   textColor=BLUE, spaceBefore=10, spaceAfter=3)
body = ParagraphStyle("body", parent=S["Normal"], fontName="Helvetica", fontSize=9,
                      textColor=INK, leading=12.5, spaceAfter=3, alignment=TA_LEFT)
small = ParagraphStyle("small", parent=body, fontSize=8.6, textColor=INK2)
roleh = ParagraphStyle("roleh", parent=body, fontName="Helvetica-Bold", fontSize=9.6, textColor=NAVY, spaceAfter=0)
org = ParagraphStyle("org", parent=small, fontName="Helvetica-Oblique", spaceAfter=2)
bullet = ParagraphStyle("bullet", parent=body, fontSize=8.7, leading=11.6, leftIndent=8, spaceAfter=1.5)

def rule():
    story.append(Spacer(1, 1))
    story.append(HRFlowable(width="100%", thickness=0.7, color=LINE, spaceBefore=2, spaceAfter=4))

# Header
story.append(Paragraph("Ahmed M. Bedeer", name))
story.append(Paragraph("Enterprise Architect &middot; Digital Transformation Specialist &middot; Solution Architect", role))
story.append(Paragraph(
    "Al Khobar, Saudi Arabia &nbsp;|&nbsp; abedeer332@gmail.com &nbsp;|&nbsp; +966 53 947 8399 &nbsp;|&nbsp; "
    "linkedin.com/in/ahmed-bedeer &nbsp;|&nbsp; github.com/ahmedbdeer", contact))
rule()

# Profile
story.append(Paragraph("Professional Profile", h))
story.append(Paragraph(
    "Enterprise Architecture &amp; Digital Transformation specialist with 7+ years delivering enterprise-scale "
    "healthcare and technology programs across Saudi Arabia. I translate C-level vision into governed, executable "
    "transformation roadmaps &mdash; anchored in <b>TOGAF</b>, <b>NORA</b>, and <b>ArchiMate</b>, and proven by "
    "measurable clinical, operational, and financial outcomes. Technology-agnostic; CPHIMS-aligned; fluent in "
    "HL7/FHIR/DICOM/SNOMED. I bridge business and technology, lead change, and govern delivery end-to-end.", body))

# Core expertise (two-col table)
story.append(Paragraph("Core Expertise", h))
exp = [
    "Enterprise Architecture (TOGAF ADM, BDAT)", "Digital Transformation &amp; Operating Models",
    "Healthcare Informatics (HIMSS Stage 6)", "Integration &amp; Interoperability (HL7/FHIR)",
    "Data Architecture &amp; Analytics (EDW/BI/ML)", "Solution Architecture (Java/Spring, microservices)",
    "Cloud &amp; Infrastructure (Docker/K8s, DR/HA)", "Security &amp; Compliance (HIPAA/GDPR, Zero Trust)",
    "Architecture Governance (ARB, risk register)", "Leadership, Change &amp; Stakeholder Management",
]
rows = [[Paragraph("&bull; "+exp[i], small), Paragraph("&bull; "+exp[i+1], small)] for i in range(0, len(exp), 2)]
t = Table(rows, colWidths=[88*mm, 88*mm])
t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),1.5)]))
story.append(t)

# Experience
story.append(Paragraph("Experience", h))
def job(rolep, orgp, dates, points):
    head = Table([[Paragraph(rolep, roleh), Paragraph(dates, ParagraphStyle("d", parent=small, alignment=TA_RIGHT))]],
                 colWidths=[120*mm, 56*mm])
    head.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)]))
    story.append(head)
    story.append(Paragraph(orgp, org))
    items = [ListItem(Paragraph(p, bullet), value="square", leftIndent=10) for p in points]
    story.append(ListFlowable(items, bulletType="bullet", start="square", bulletColor=CYAN, bulletFontSize=5, leftIndent=6))
    story.append(Spacer(1, 3))

job("Enterprise Architecture &amp; Digital Transformation Consultant",
    "Independent Practice &middot; Cross-Industry &middot; KSA / Remote", "2026 &ndash; Present",
    ["Lead enterprise architecture initiatives aligned with TOGAF and NORA across healthcare and SME environments.",
     "Design end-to-end transformation strategies integrating governance, operating models, and data architecture.",
     "Establish data governance frameworks, master data models, and analytics roadmaps; advise executives on investment and modernization."])
job("Healthcare IT Project Engineer",
    "GAD International &middot; Heart &amp; Lung Institute, Al Khobar (first specialized cardiac &amp; pulmonary hospital in the Middle East)", "Aug 2023 &ndash; Present",
    ["Architected enterprise digital-health ecosystem (EHR, LIS, RIS/PACS, ICU, portals) &mdash; 85% HIMSS Stage 6 readiness.",
     "Designed interoperability via FHIR APIs, HL7, IoT, and Mirth Connect across 7 departments and 3 clinics.",
     "Built ODS &rarr; EDW platform with ETL feeding BI dashboards; UML revenue-cycle workflows cut month-end close 25%.",
     "Implemented VLAN segmentation, HA WAN, and DR (sub-1% RTO); privacy-by-design controls (AAA, audit, encryption) for HIPAA/GDPR.",
     "Active PMO member: technical documentation, vendor SOW review, architecture governance."])
job("Healthcare Digitalization &amp; Telehealth Consultant",
    "Freelance HIMS Project &middot; Gulf Region", "Mar 2024 &ndash; Present",
    ["Strategic advisor aligning digital-health initiatives with HIMSS, HL7, HIPAA, and FHIR.",
     "Improved interoperability and digital-health maturity; championed FHIR adoption for modern EHR exchange."])
job("IT Project Engineer",
    "GAD International &middot; Baha Medical Center, KSA", "Mar 2022 &ndash; Aug 2023",
    ["Delivered 90% of ICT hospital infrastructure (firewalls, VLANs, OSPF, Active Directory, DNS).",
     "Tested and commissioned hospital systems on schedule; supported HIS/ERP rollout."])
job("Data Analyst &amp; IT Engineer",
    "Medical Mall &middot; Riyadh, KSA", "Jan 2022 &ndash; Mar 2022",
    ["Built Power BI analytics and SQL reporting for supply-chain and operational intelligence; automation apps improving efficiency."])

# Selected impact
story.append(Paragraph("Selected Impact", h))
impact = ["12% ICU length-of-stay reduction", "85% HIMSS Stage 6 readiness", "25% faster month-end close",
          "40% less administrative overhead", "90% ICT infrastructure delivered", "$500K+ cost-savings identified",
          "85% no-show forecast accuracy", "Sub-1% RTO failover"]
rows = [[Paragraph("&bull; "+impact[i], small), Paragraph("&bull; "+impact[i+1] if i+1 < len(impact) else "", small)] for i in range(0, len(impact), 2)]
t = Table(rows, colWidths=[88*mm, 88*mm])
t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),1.5)]))
story.append(t)

# Skills matrix
story.append(Paragraph("Technical Skills", h))
skills = [
    ("Architecture Frameworks", "TOGAF, NORA, ArchiMate, UML, Sparx EA, Visual Paradigm"),
    ("Engineering", "Java 17, Spring Boot, Node.js, Microservices, REST/API-first, OODA"),
    ("Data &amp; Analytics", "SQL, PostgreSQL, MySQL, EDW/ODS, ETL, Python, Pandas, scikit-learn, Power BI, Tableau"),
    ("Healthcare Standards", "HL7, FHIR, DICOM, SNOMED CT, LOINC, ICD-10, Mirth Connect, HIMSS, CPHIMS"),
    ("Cloud &amp; Infrastructure", "Docker, Kubernetes, DR/HA, VLANs, OSPF, Aruba, Palo Alto, Active Directory, DNS"),
    ("Security &amp; Compliance", "HIPAA, GDPR, Zero Trust, AAA, IAM, audit logging, encryption, privacy-by-design"),
    ("Methods &amp; Governance", "Architecture Governance (ARB), Agile, Lean Six Sigma, Business Analysis, PMO"),
]
for cat, items in skills:
    story.append(Paragraph(f"<b>{cat}:</b> {items}", small))

# Certs + education two-col
story.append(Paragraph("Certifications &amp; Education", h))
left = ("<b>Certifications:</b> CPHIMS (HIMSS); Enterprise Architecture Foundations; CCNP ENCOR / CCNA; "
        "CompTIA Network+; Microsoft PowerShell; SAP Production Planning; Java 17 / Spring / System Design; "
        "Data Analysis Professional (Udacity); Lean Six Sigma; Agile &amp; Project Management; Operational Excellence.")
right = ("<b>Education:</b> B.Sc. Computer Science, Thebes Academy, Cairo (2015&ndash;2019). "
         "<br/><b>Languages:</b> English (Professional), Arabic (Native). "
         "<br/><b>Nationality:</b> Egyptian.")
t = Table([[Paragraph(left, small), Paragraph(right, small)]], colWidths=[104*mm, 72*mm])
t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0)]))
story.append(t)

doc.build(story)
print("CV built")
