# -*- coding: utf-8 -*-
"""Case studies, services, skills, contact."""

def build_more(head, footer, write, arch_svg, _cta):

    # =====================================================================
    # CASE STUDIES — impact KPIs + 4 detailed case studies
    # =====================================================================
    p = head("Case Studies — Ahmed M. Bedeer",
        "Detailed architecture case studies: context, role, frameworks, architecture views, key trade-offs and decision logic, governance & risk, and measurable business outcomes including ROI and TCO.",
        "case-studies")
    p += '''
<div class="page-hero">
  <div class="breadcrumb"><a href="index.html">home</a><span class="sep">/</span><span class="here">case studies</span></div>
  <h1>Architecture that <em>moved KPIs.</em></h1>
  <p class="lead">Each case follows the same architectural narrative: the challenge, my role, the frameworks applied, the architecture, the <strong>trade-offs I made and why</strong>, how it was governed, and the business outcomes — clinical, operational, and financial.</p>
</div>

<section class="page-section" style="padding-top:40px;">
  <div class="inner">
    <span class="section-tag">Selected Impact</span>
    <h2 style="margin-bottom:40px;">The numbers, <em>up front.</em></h2>
    <div class="impact-grid">
      <div class="impact-card reveal"><div class="impact-num">12<span>%</span></div><div class="impact-label">ICU LOS Reduction</div><div class="impact-desc">Predictive analytics &amp; care-gap alerting integrated into the EDW supported proactive outreach.</div></div>
      <div class="impact-card reveal"><div class="impact-num">85<span>%</span></div><div class="impact-label">HIMSS Stage 6 Readiness</div><div class="impact-desc">End-to-end EHR/EMR, RIS/PACS, LIS, perioperative, ICU, and portal flows aligned with HIMSS standards.</div></div>
      <div class="impact-card reveal"><div class="impact-num">25<span>%</span></div><div class="impact-label">Faster Month-End Close</div><div class="impact-desc">UML-modeled revenue-cycle workflows streamlined order lifecycle and charge capture.</div></div>
      <div class="impact-card reveal"><div class="impact-num">40<span>%</span></div><div class="impact-label">Less Admin Overhead</div><div class="impact-desc">Patient-centric Java/Spring Boot application automated appointment &amp; insurance workflows.</div></div>
      <div class="impact-card reveal"><div class="impact-num">50<span>%</span></div><div class="impact-label">Throughput Boost</div><div class="impact-desc">Kubernetes-based microservices scaling lifted e-commerce transaction throughput at peak load.</div></div>
      <div class="impact-card reveal"><div class="impact-num">30<span>%</span></div><div class="impact-label">Faster HR Cycles</div><div class="impact-desc">Cloud-native automation reduced HR leave-approval time via Docker + Java workflows.</div></div>
      <div class="impact-card reveal"><div class="impact-num">90<span>%</span></div><div class="impact-label">ICT Infra Delivered</div><div class="impact-desc">Baha Medical Center critical infrastructure including network protocols and secure data systems.</div></div>
      <div class="impact-card reveal"><div class="impact-num">$500K<span>+</span></div><div class="impact-label">Cost-Savings Identified</div><div class="impact-desc">Automated market analysis dashboard delivered real-time insights for stakeholder decisions.</div></div>
    </div>
  </div>
</section>

<section class="page-section" style="padding-top:10px;">
  <div class="inner">
    <span class="section-tag">Featured Case Studies</span>
    <h2 style="margin-bottom:8px;">A closer <em>look.</em></h2>
    <p class="section-desc">Four engagements where strategy, architecture, and engineering came together. <em style="color:var(--ink-3);font-style:normal;font-size:13px;">Financial figures marked &ldquo;modeled&rdquo; are illustrative estimates — replace with verified client numbers before publishing.</em></p>
'''
    # ---- CASE 01 ----
    p += _case(
        kicker="Case 01 · Healthcare · Greenfield Enterprise Architecture",
        title="GAD Heart &amp; Lung Institute — Greenfield Digital Health EA",
        metrics=[("85%","HIMSS Stage 6 readiness"),("7+3","departments + clinics"),("&lt;1%","RTO failover"),("100%","BDAT layers modeled")],
        arch=arch_svg("Logical view · BDAT (ArchiMate-aligned)", [
            ("Business","business",["Patient Journey","Revenue Cycle","Clinical Ops"]),
            ("Application","application",["EHR/EMR","RIS/PACS","LIS","ICU","Portal"]),
            ("Data","data",["FHIR","HL7 v2","SNOMED/LOINC","ODS → EDW"]),
            ("Technology","technology",["Mirth Bus","Kubernetes","VLAN/DR","IAM"]),
        ]),
        context="The first specialized cardiac &amp; pulmonary hospital in the Middle East was being built from the ground up. There was no legacy estate to migrate — but also no reference to anchor on. Every clinical, application, data, and technology decision had to be made deliberately and aligned to a single target architecture.",
        role="I led the enterprise architecture end-to-end as Healthcare IT Project Engineer and active PMO member — owning the BDAT model, the interoperability design, and the technical review of vendor proposals against the hospital's vision.",
        approach=["<strong>TOGAF ADM</strong> Phases A→D to set vision, business, data, application and technology architectures.","<strong>ArchiMate</strong> to model the patient journey across all layers as one navigable map.","<strong>HIMSS Stage 6</strong> as the maturity yardstick for every clinical flow.","<strong>NORA</strong> &amp; HIPAA/GDPR as the governance and compliance backbone."],
        tradeoffs=[
            ("Integration","Point-to-point interfaces","Central integration bus (Mirth Connect)", True,
             "An N×N web of point-to-point HL7 feeds is cheap to start but its cost and fragility grow quadratically. A central bus added upfront effort but cut per-interface cost, isolated failures, and made every new system a single connection — the right TCO over a multi-year estate."),
            ("Interoperability","HL7 v2 only","FHIR-first, HL7 v2 where required", True,
             "FHIR future-proofs APIs and portal/IoT integration; HL7 v2 was retained only where vendor systems mandated it. This balanced modern interoperability against vendor reality."),
            ("EHR","Build custom EHR","Buy &amp; integrate certified EHR", True,
             "A greenfield tempts a custom build, but a certified EHR de-risks compliance and time-to-go-live. Architecture effort went into integration and data, not reinventing the record."),
        ],
        gov=["TOGAF ADM gates","Architecture Review Board","Risk register","HIPAA","GDPR","Zero Trust segmentation","AAA · audit logging","Encryption-at-rest"],
        outcomes="<strong>85% HIMSS Stage 6 readiness</strong> with main flows mapped per system and department. The bus-based design is projected to reduce integration <strong>OPEX</strong> versus point-to-point as systems are added — a <em>modeled</em> 30–40% lower cost-per-interface over the estate lifecycle. DR architecture delivered <strong>sub-1% RTO failover</strong>, protecting clinical continuity.",
        user="Patients gained a single portal for access and results; clinicians worked from one coherent record instead of swivel-chairing between systems — shortening the path from arrival to care.",
    )
    # ---- CASE 02 ----
    p += _case(
        kicker="Case 02 · Infrastructure · ICT Healthcare Environment",
        title="Baha Medical Center — Secure ICT Deployment",
        metrics=[("90%","critical infra delivered"),("75%","on-schedule completion"),("0","unsegmented zones"),("100%","protocol coverage")],
        arch=arch_svg("Network &amp; resilience view", [
            ("Clinical Services","business",["HIS / ERP","Imaging","Labs"]),
            ("Application","application",["Active Directory","DNS","Email","Wi-Fi"]),
            ("Network","technology",["Aruba Switching","Palo Alto FW","VLANs · OSPF"]),
            ("Resilience","integration",["HA Links","DR Site","Backups"]),
        ]),
        context="A hospital cannot open without a clinical-grade network. Baha Medical Center needed its entire ICT backbone — switching, firewalls, identity, DNS, and resilience — designed, built, and commissioned to support HIS/ERP rollout on a fixed schedule.",
        role="As IT Project Engineer I designed and supervised the implementation of the ICT environment and rolled out the network-protocol layer across the clinical backbone, providing on-site and remote support through commissioning.",
        approach=["Segmented, defense-in-depth network design (<strong>VLANs, OSPF, IP access lists</strong>).","<strong>Aruba</strong> switching and <strong>Palo Alto</strong> firewalls as the standardized stack.","<strong>Active Directory + DNS</strong> for identity and name resolution.","Test-and-commission discipline tied to the project schedule."],
        tradeoffs=[
            ("Resilience","Active-active clustering","Active-passive clustering", True,
             "Active-active maximizes utilization but doubles operational complexity and split-brain risk. For a new clinical site, active-passive gave predictable failover and far simpler operations — resilience the team could actually run."),
            ("DR","Cloud-based DR","On-prem DR site", True,
             "Regulatory and latency constraints for clinical data favored an on-prem DR posture at this stage, with a documented path to hybrid later."),
            ("Vendors","Best-of-breed mix","Standardized Aruba + Palo Alto stack", True,
             "A single, well-supported stack lowered maintenance OPEX and training burden versus a best-of-breed patchwork — the right call for a lean hospital IT team."),
        ],
        gov=["Change control","Network segmentation","Zero Trust principles","Access lists","Commissioning sign-off","Vendor SOW review"],
        outcomes="<strong>90% of critical infrastructure delivered</strong> with full network-protocol coverage and secure patient-data systems, hitting <strong>75% completion on schedule</strong>. The standardized vendor stack is projected to lower ongoing maintenance <strong>OPEX</strong> and shorten mean-time-to-repair — a <em>modeled</em> reduction in support effort for the in-house team.",
        user="Clinical staff received a reliable, segmented network from day one — uptime and security that users never had to think about, which is exactly the point.",
    )
    # ---- CASE 03 ----
    p += _case(
        kicker="Case 03 · Application · Patient-Centric Platform",
        title="Patient-Centric Healthcare Application",
        metrics=[("40%","less admin overhead"),("95%","production-ready"),("API","-first design"),("24/7","self-service")],
        arch=arch_svg("Solution view · microservices", [
            ("Business","business",["Appointments","Insurance","Front Desk"]),
            ("Application","application",["Scheduling","Insurance Svc","Notifications","Node UI"]),
            ("Data","data",["PostgreSQL","Event Log"]),
            ("Technology","technology",["Spring Boot","Docker","API Gateway"]),
        ]),
        context="Front-desk staff were drowning in manual appointment and insurance workflows — slow, error-prone, and a poor patient experience. The hospital needed an automated, patient-facing platform that operations could trust.",
        role="I designed the solution architecture — domain decomposition, API contracts, data model, and the OODA-driven analysis from requirements to use cases to notation — and guided the build to production-readiness.",
        approach=["<strong>Domain-driven microservices</strong> in Java 17 / Spring Boot.","<strong>API-first</strong> contracts with a Node.js front-of-house layer.","<strong>OODA</strong> method: requirements → use cases → notation → build.","PostgreSQL data modeling with auditability built in."],
        tradeoffs=[
            ("Decomposition","Monolith","Microservices", True,
             "A monolith ships faster on day one, but the roadmap demanded independent scaling of scheduling vs. insurance and parallel team delivery. Bounded microservices traded a little upfront overhead for scalability and change-isolation — justified by the growth plan, not by fashion."),
            ("Stack","Node.js end-to-end","Java/Spring core + Node UI", True,
             "Java/Spring brought transactional rigor and a mature ecosystem for the core domain; Node served the responsive front-of-house. Right tool per layer — a technology-agnostic call."),
            ("Scheduling","SaaS scheduling product","Build on owned services", True,
             "An off-the-shelf scheduler was faster, but deep insurance-workflow coupling and data-ownership needs favored building on owned services with full control of PHI."),
        ],
        gov=["API security","PHI handling","Audit logging","Least privilege","Code review gates"],
        outcomes="<strong>40% reduction in administrative overhead</strong> via automated appointment and insurance workflows; the platform reached <strong>95% production-readiness</strong>. Staff hours redirected from manual entry to patient care translate to a <em>modeled</em> recurring <strong>OPEX</strong> saving and a fast payback on build cost.",
        user="Patients self-serve appointments and insurance 24/7 instead of waiting on a phone line; the front desk handles exceptions, not data entry — a measurably better journey on both sides of the counter.",
    )
    # ---- CASE 04 ----
    p += _case(
        kicker="Case 04 · Data &amp; Analytics · Prediction + Decision Support",
        title="Predictive No-Show Model &amp; Market Intelligence Dashboard",
        metrics=[("85%","no-show forecast accuracy"),("$500K+","savings identified"),("Real-time","stakeholder insight"),("EDW","-backed")],
        arch=arch_svg("Analytics &amp; data view", [
            ("Business","business",["Clinic Access","Market Strategy"]),
            ("Analytics","application",["No-Show Model","Power BI","Tableau"]),
            ("Data","data",["EDW","Feature Store","SQL Marts"]),
            ("Technology","technology",["Python","Pandas","scikit-learn","ETL"]),
        ]),
        context="Two decision problems, one data foundation: clinics were losing revenue to patient no-shows, and stakeholders lacked timely market intelligence. Both needed trustworthy data and the right modeling choice — not the most fashionable one.",
        role="I built the data architecture and the analytics — the ETL into the EDW, the predictive no-show model, and the automated market-analysis dashboard surfacing insights in real time.",
        approach=["<strong>ODS → EDW</strong> with governed ETL as the single source of truth.","<strong>scikit-learn</strong> predictive model on engineered features.","<strong>Power BI + Tableau</strong> for executive-facing dashboards.","Data governance &amp; PII handling baked into the pipeline."],
        tradeoffs=[
            ("Model","Deep learning","Classical ML (gradient-boosted / logistic)", True,
             "A neural net was tempting, but on tabular clinic data it adds cost, opacity, and ops burden for marginal lift. Classical ML hit 85% accuracy with explainability clinicians could trust — the same discipline as choosing RAG over fine-tuning: pick the option that wins on cost, data fit, and maintainability, not novelty."),
            ("Latency","Real-time scoring","Batch (daily) scoring", True,
             "No-show risk doesn't change minute-to-minute; daily batch scoring delivered the value at a fraction of the streaming infrastructure cost."),
            ("BI","Build custom app","Power BI / Tableau on the EDW", True,
             "Reusing governed BI tools on the EDW beat a bespoke app on time-to-value and TCO, and kept one version of the truth."),
        ],
        gov=["Data governance","PII / PHI controls","Model monitoring","Source-of-truth EDW","Access control"],
        outcomes="<strong>85% no-show forecast accuracy</strong> enabled proactive outreach and reduced clinic revenue loss; the market dashboard surfaced <strong>$500K+ in identified cost-savings</strong> for stakeholders in real time. Choosing classical ML and batch scoring kept model-ops <strong>TCO</strong> low while delivering the business result.",
        user="Fewer missed appointments means better access for the patients who need the slot, and leaders make calls on live data instead of last month's report.",
    )
    p += '''  </div>
</section>
'''
    p += _cta("Want a case study written up for your project?", "I package engagements as executive one-pagers, architecture views, and short walkthroughs — exactly the multi-modal format decision-makers respond to.")
    p += footer()
    write("case-studies.html", p)

    # =====================================================================
    # SERVICES
    # =====================================================================
    p = head("Services — Ahmed M. Bedeer",
        "Architecture and transformation engagements: enterprise architecture & strategy, healthcare digital transformation, data architecture, solution architecture, cloud modernization, and executive advisory.",
        "services")
    p += '''
<div class="page-hero">
  <div class="breadcrumb"><a href="index.html">home</a><span class="sep">/</span><span class="here">services</span></div>
  <h1>How I can <em>help you.</em></h1>
  <p class="lead">Engagements tailored to executive teams, healthcare providers, and technology organizations operating across the Gulf and beyond.</p>
</div>

<section id="services" style="padding-top:50px;">
  <div style="max-width:1300px;margin:0 auto;">
    <div class="services-grid">
      <div class="service-card featured reveal">
        <div class="service-pill">Most Requested</div>
        <h3>Enterprise Architecture &amp; Strategy</h3>
        <p>End-to-end TOGAF-aligned engagements — from current-state assessment to target-state vision and a phased transition roadmap with clear governance.</p>
        <ul class="service-list"><li>Architecture Vision &amp; Capability Mapping</li><li>Business · Data · Application · Tech layers</li><li>NORA alignment for KSA programs</li><li>ArchiMate modeling &amp; documentation</li><li>Architecture Governance Board enablement</li></ul>
      </div>
      <div class="service-card reveal">
        <div class="service-pill">Healthcare</div>
        <h3>Healthcare Digital Transformation</h3>
        <p>Hospital and clinic transformations executed against HIMSS Stage 6+ readiness — from EHR selection to interoperability rollout and clinical informatics maturity.</p>
        <ul class="service-list"><li>HIS / EHR / EMR architecture</li><li>HL7 · FHIR · DICOM integration</li><li>Mirth Connect &amp; integration bus design</li><li>HIMSS readiness &amp; CPHIMS-aligned advisory</li><li>Privacy-by-design (HIPAA / GDPR)</li></ul>
      </div>
      <div class="service-card reveal">
        <div class="service-pill">Data</div>
        <h3>Data Architecture &amp; Analytics</h3>
        <p>From data governance frameworks to ODS → EDW pipelines and BI platforms — the data foundation that feeds dashboards, ML models, and executive decisions.</p>
        <ul class="service-list"><li>Data governance &amp; master data models</li><li>EDW design &amp; ETL orchestration</li><li>Power BI / Tableau dashboarding</li><li>Predictive analytics with Python</li><li>KPI frameworks &amp; data storytelling</li></ul>
      </div>
      <div class="service-card reveal">
        <div class="service-pill">Solution</div>
        <h3>Solution Architecture</h3>
        <p>API-first solution architectures in Java/Spring Boot and Node.js — microservices, REST APIs, database design, and OODA-driven analysis bridging product and platform.</p>
        <ul class="service-list"><li>Microservices &amp; domain-driven design</li><li>API design &amp; integration patterns</li><li>PostgreSQL / MySQL data modeling</li><li>OODA: requirements → use cases → notation</li><li>System design &amp; technical reviews</li></ul>
      </div>
      <div class="service-card reveal">
        <div class="service-pill">Cloud</div>
        <h3>Cloud &amp; Platform Modernization</h3>
        <p>Containerize, orchestrate, scale. Modernization roadmaps that move workloads onto Docker/Kubernetes with the resilience and DR posture an enterprise needs.</p>
        <ul class="service-list"><li>Docker &amp; Kubernetes platform design</li><li>HA &amp; Disaster Recovery architecture</li><li>Network segmentation (VLANs, firewalls)</li><li>Hybrid &amp; private cloud patterns</li><li>Reliability, observability, cost guardrails</li></ul>
      </div>
      <div class="service-card reveal">
        <div class="service-pill">Advisory</div>
        <h3>Executive &amp; PMO Advisory</h3>
        <p>Trusted advisor for chairmen, CIOs, and PMOs. From technical reviews of vendor proposals to weekly governance support and SME consultation across the program lifecycle.</p>
        <ul class="service-list"><li>Vendor &amp; SOW technical review</li><li>PMO &amp; weekly governance support</li><li>SME / chairman advisory sessions</li><li>Business plans &amp; org charts</li><li>Lean Six Sigma &amp; Agile enablement</li></ul>
      </div>
    </div>
  </div>
</section>

<section class="page-section">
  <div class="inner">
    <span class="section-tag">How I deliver</span>
    <h2>An <em>engagement model</em> built for decisions.</h2>
    <p class="section-desc">Every engagement produces artifacts that executives can act on — not shelfware.</p>
    <div class="lead-grid">
      <div class="lead-card reveal"><div class="lc-icon">🗂️</div><h3>Architecture views</h3><p>ArchiMate / UML models and BDAT diagrams in Sparx EA or Visual Paradigm — the living, reviewable source of truth.</p></div>
      <div class="lead-card reveal"><div class="lc-icon">📊</div><h3>Executive one-pagers</h3><p>Slide decks and concise summaries that translate architecture into investment, risk, and outcome language for the board.</p></div>
      <div class="lead-card reveal"><div class="lc-icon">🎥</div><h3>Walkthroughs</h3><p>Short, focused walkthroughs of design philosophy and trade-offs — multi-modal content so every stakeholder gets it.</p></div>
    </div>
  </div>
</section>
'''
    p += _cta("Not sure which engagement fits?", "Tell me the business problem and I'll propose the lightest engagement that gets you a confident decision.")
    p += footer()
    write("services.html", p)

    # =====================================================================
    # SKILLS — matrix + stack + certifications + education
    # =====================================================================
    p = head("Skills &amp; Certifications — Ahmed M. Bedeer",
        "Technical skills matrix across architecture frameworks, cloud platforms, engineering, data, healthcare standards, security, methods, and tools — plus certifications and education.",
        "skills")
    p += '''
<div class="page-hero">
  <div class="breadcrumb"><a href="index.html">home</a><span class="sep">/</span><span class="here">skills</span></div>
  <h1>The <em>skills matrix.</em></h1>
  <p class="lead">A practitioner's stack, organized for fast reading — selected based on outcomes, not hype. I am technology-agnostic: the matrix shows depth, not allegiance.</p>
</div>

<section class="page-section" style="padding-top:50px;">
  <div class="inner">
    <span class="section-tag">Technical Skills Matrix</span>
    <h2 style="margin-bottom:40px;">By <em>category.</em></h2>
    <div class="matrix">
''' + _matrix() + '''    </div>
  </div>
</section>

<section id="stack" style="padding-top:10px;">
  <div class="stack-wrap">
    <span class="section-tag">Full Stack</span>
    <h2>Everything in <em>the toolbox.</em></h2>
    <p class="section-desc">The complete practitioner stack — covering modeling, engineering, data, infrastructure, compliance, and methods.</p>
    <div class="stack-grid">
''' + _stack_rows() + '''    </div>
  </div>
</section>

<section id="certifications" style="padding-top:10px;">
  <div class="cert-wrap">
    <span class="section-tag">Certifications &amp; Education</span>
    <h2>Continuously <em>credentialed.</em></h2>
    <p class="section-desc">Formal certifications and continuous learning across enterprise architecture, healthcare informatics, networking, programming, and management.</p>
    <div class="cert-grid">
''' + _cert_cards() + '''    </div>
    <div class="edu-strip">
      <div class="edu-card reveal">
        <div class="edu-meta">2015 — 2019 · Egypt</div>
        <h4>Bachelor's Degree in Computer Science</h4>
        <p><strong style="color:var(--ink);">Thebes Academy</strong>, Cairo, Egypt — graduation project: <em style="color:var(--cyan);font-style:normal;">Unity 3D Physics Game Development</em>. Foundation in OOP, systems design, networking, and applied computer science.</p>
      </div>
      <div class="lang-card reveal">
        <h4 style="margin-bottom:16px;">Languages</h4>
        <div class="lang-row"><span style="color:var(--ink);">English</span><span style="color:var(--ink-3);font-family:var(--mono);font-size:11px;">Professional</span><div class="lang-bar"><i style="width:92%;"></i></div></div>
        <div class="lang-row"><span style="color:var(--ink);">Arabic</span><span style="color:var(--ink-3);font-family:var(--mono);font-size:11px;">Native</span><div class="lang-bar"><i style="width:100%;"></i></div></div>
      </div>
    </div>
  </div>
</section>
'''
    p += _cta("Need a specific skill verified?", "Download the CV for the full credential list, or ask for evidence on any item — I keep the receipts.")
    p += footer()
    write("skills.html", p)

    # =====================================================================
    # CONTACT
    # =====================================================================
    p = head("Contact — Ahmed M. Bedeer",
        "Get in touch with Ahmed Bedeer for enterprise architecture, digital transformation, healthcare IT, or data engagements in KSA or remotely.",
        "contact")
    p += '''
<div class="page-hero">
  <div class="breadcrumb"><a href="index.html">home</a><span class="sep">/</span><span class="here">contact</span></div>
  <h1>Let's <em>build something durable.</em></h1>
  <p class="lead">Engaging on architecture, transformation, healthcare IT, or data programs in KSA or remotely? Let's talk.</p>
</div>

<section id="contact" style="padding-top:50px;text-align:left;">
  <div class="contact-wrap" style="margin:0 auto;">
    <div class="contact-cards reveal">
      <a href="mailto:abedeer332@gmail.com" class="contact-card"><div class="contact-icon">✉</div><div class="label">Email</div><div class="value">abedeer332@gmail.com</div></a>
      <a href="tel:+966539478399" class="contact-card"><div class="contact-icon">☎</div><div class="label">Phone</div><div class="value">+966 53 947 8399</div></a>
      <a href="https://www.linkedin.com/in/ahmed-bedeer" target="_blank" rel="noopener" class="contact-card"><div class="contact-icon">in</div><div class="label">LinkedIn</div><div class="value">/ahmed-bedeer</div></a>
      <a href="https://www.github.com/ahmedbdeer" target="_blank" rel="noopener" class="contact-card"><div class="contact-icon">{ }</div><div class="label">GitHub</div><div class="value">@ahmedbdeer</div></a>
      <a href="assets/Ahmed-M-Bedeer-CV.pdf" download class="contact-card"><div class="contact-icon">↓</div><div class="label">Curriculum Vitae</div><div class="value">Download PDF</div></a>
      <a href="services.html" class="contact-card"><div class="contact-icon">⚡</div><div class="label">Engagement</div><div class="value">Consulting · Advisory</div></a>
    </div>

    <div class="agnostic-banner reveal" style="margin-top:40px;">
      <div class="ab-mark">stay<br>in the loop</div>
      <p><strong>I share lessons-learned regularly on LinkedIn</strong> — architecture notes, trade-offs from live engagements, and digital-transformation patterns from the Gulf. Connect there for the running commentary between case studies.</p>
    </div>
  </div>
</section>
'''
    p += footer()
    write("contact.html", p)


# ---------------------------------------------------------------------------
# Case study renderer
# ---------------------------------------------------------------------------
def _case(kicker, title, metrics, arch, context, role, approach, tradeoffs, gov, outcomes, user):
    m = "".join(f'<div class="cs-metric"><b>{v}</b><span>{l}</span></div>' for v, l in metrics)
    ap = "".join(f"<li>{a}</li>" for a in approach)
    rows = ""
    for dim, a, b, chosen_b, why in tradeoffs:
        rows += f'''<tr class="chosen">
          <td class="opt">{dim}</td>
          <td>{a}</td>
          <td>{b}<span class="badge-chosen">chosen</span></td>
          <td>{why}</td>
        </tr>'''
    chips = "".join(f'<span class="chip">{g}</span>' for g in gov)
    return f'''
    <article class="cs reveal">
      <div class="cs-head">
        <div class="cs-kicker">{kicker}</div>
        <h3>{title}</h3>
        <div class="cs-metrics">{m}</div>
      </div>

      {arch}

      <div class="cs-cols" style="margin-top:24px;">
        <div class="cs-block"><div class="blk-label">The challenge</div><p>{context}</p></div>
        <div class="cs-block"><div class="blk-label">My role</div><p>{role}</p></div>
      </div>

      <div class="cs-block span2" style="margin-top:22px;">
        <div class="blk-label">Approach &amp; frameworks</div>
        <ul>{ap}</ul>
      </div>

      <div class="cs-block span2" style="margin-top:22px;">
        <div class="blk-label">Key trade-offs &amp; decision logic — <em style="color:var(--ink-2);font-style:normal;text-transform:none;letter-spacing:0;">why this, not that</em></div>
        <div style="overflow-x:auto;">
        <table class="tradeoff">
          <thead><tr><th>Decision</th><th>Considered</th><th>Selected</th><th>Why</th></tr></thead>
          <tbody>{rows}</tbody>
        </table>
        </div>
      </div>

      <div class="cs-cols" style="margin-top:22px;">
        <div class="cs-block">
          <div class="blk-label">Governance &amp; risk</div>
          <div class="gov-chips" style="margin-top:0;">{chips}</div>
        </div>
        <div class="cs-block">
          <div class="blk-label">Business outcomes &amp; ROI / TCO</div>
          <p>{outcomes}</p>
        </div>
      </div>

      <div class="cs-block span2" style="margin-top:22px;">
        <div class="blk-label">User &amp; citizen centricity</div>
        <p>{user}</p>
      </div>
    </article>
'''


def _matrix():
    groups = [
        ("EA", "Architecture Frameworks", "frameworks · notations", [
            ("TOGAF (ADM, governance)", "Expert", 92),
            ("ArchiMate modeling", "Expert", 90),
            ("NORA (KSA)", "Advanced", 85),
            ("Sparx EA / Visual Paradigm", "Advanced", 82),
            ("UML · Enterprise Integration", "Advanced", 84),
        ]),
        ("☁", "Cloud &amp; Infrastructure", "platforms · networks", [
            ("Docker", "Advanced", 85),
            ("Kubernetes", "Advanced", 80),
            ("DR &amp; High Availability", "Advanced", 84),
            ("VLANs · OSPF · Segmentation", "Advanced", 86),
            ("Aruba · Palo Alto · AD · DNS", "Advanced", 83),
        ]),
        ("{ }", "Engineering", "backend · platforms", [
            ("Java 17", "Expert", 88),
            ("Spring Boot · Microservices", "Advanced", 86),
            ("REST / API-First design", "Expert", 90),
            ("Node.js", "Proficient", 72),
            ("OODA · Design patterns", "Advanced", 82),
        ]),
        ("Σ", "Data &amp; Analytics", "storage · modeling · BI", [
            ("SQL · PostgreSQL · MySQL", "Advanced", 86),
            ("EDW / ODS · ETL", "Advanced", 84),
            ("Python · Pandas", "Advanced", 80),
            ("scikit-learn (predictive)", "Proficient", 75),
            ("Power BI · Tableau", "Advanced", 83),
        ]),
        ("⚕", "Healthcare Standards", "interoperability", [
            ("HL7 v2.x", "Advanced", 85),
            ("FHIR", "Advanced", 86),
            ("DICOM", "Advanced", 80),
            ("SNOMED CT · LOINC · ICD-10", "Advanced", 82),
            ("Mirth Connect", "Advanced", 84),
        ]),
        ("🛡", "Security &amp; Compliance", "regulatory · controls", [
            ("HIPAA", "Advanced", 86),
            ("GDPR", "Advanced", 84),
            ("Zero Trust · AAA · IAM", "Advanced", 82),
            ("Audit logging · Encryption", "Advanced", 85),
            ("Privacy-by-design", "Advanced", 84),
        ]),
        ("⚙", "Methods &amp; Governance", "delivery · practice", [
            ("Architecture Governance (ARB)", "Advanced", 85),
            ("Agile", "Advanced", 84),
            ("Lean Six Sigma", "Advanced", 80),
            ("Business Analysis", "Advanced", 83),
            ("PMO &amp; Operational Excellence", "Advanced", 82),
        ]),
        ("🔧", "Tools &amp; Software", "productivity · platforms", [
            ("Sparx EA · Visual Paradigm", "Advanced", 82),
            ("Power BI · Tableau", "Advanced", 83),
            ("Azure DevOps", "Proficient", 74),
            ("PowerShell · Windows Server", "Advanced", 80),
            ("React · JS (front-of-house)", "Proficient", 70),
        ]),
    ]
    out = ""
    for icon, name, sub, skills in groups:
        rows = ""
        for sname, level, pct in skills:
            rows += f'''<div class="skill-row">
          <div class="sr-top"><span class="sr-name">{sname}</span><span class="sr-level">{level}</span></div>
          <div class="skill-bar"><i data-w="{pct}%"></i></div>
        </div>'''
        out += f'''      <div class="matrix-group reveal">
        <h3><span class="mg-icon">{icon}</span>{name}</h3>
        <div class="mg-sub">{sub}</div>
        {rows}
      </div>
'''
    return out


def _stack_rows():
    rows = [
        ("EA", "Architecture &amp; Modeling", "frameworks · notations", [("blue","TOGAF"),("blue","NORA"),("cyan","ArchiMate"),("cyan","Sparx EA"),("","Visual Paradigm"),("","UML"),("","Enterprise Integration")]),
        ("⚕", "Healthcare Standards", "interoperability", [("blue","HL7"),("blue","FHIR"),("cyan","DICOM"),("cyan","SNOMED CT"),("","LOINC"),("","CPT"),("","ICD-10"),("","Mirth Connect")]),
        ("{ }", "Engineering", "backend · platforms", [("purple","Java 17"),("purple","Spring Boot"),("","Node.js"),("","Microservices"),("","REST APIs"),("","API-First"),("","OODA"),("","Design Patterns")]),
        ("DB", "Data Platforms", "storage · analytics", [("blue","PostgreSQL"),("blue","MySQL"),("cyan","SQL"),("cyan","ETL"),("","Python"),("","Pandas"),("","scikit-learn"),("","EDW / ODS"),("","Power BI"),("","Tableau")]),
        ("☁", "Cloud &amp; Infrastructure", "platforms · networks", [("blue","Docker"),("blue","Kubernetes"),("cyan","Aruba"),("cyan","Palo Alto"),("","VLANs"),("","OSPF"),("","Active Directory"),("","DNS"),("","DR Architecture"),("","High Availability")]),
        ("🛡", "Compliance &amp; Security", "regulatory · controls", [("blue","HIPAA"),("blue","GDPR"),("cyan","HIMSS"),("cyan","CPHIMS"),("","AAA Model"),("","Audit Logging"),("","Encryption-at-Rest"),("","Privacy-by-Design")]),
        ("⚙", "Methods &amp; Practice", "delivery · governance", [("green","Agile"),("green","Lean Six Sigma"),("","Business Analysis"),("","Operational Excellence"),("","Product Management"),("","PMO"),("","SAP Production Planning")]),
        ("🔧", "Productivity &amp; AI", "tools · workflows", [("blue","PowerShell"),("cyan","API Documentation"),("","Windows Server"),("purple","AI &amp; Vibe Coding"),("","Azure DevOps"),("","React"),("","JS")]),
    ]
    out = ""
    for icon, name, sub, items in rows:
        chips = "".join(f'<span class="tag {c}">{t}</span>' for c, t in items)
        out += f'''      <div class="stack-row reveal">
        <div class="stack-label"><div class="stack-icon">{icon}</div><div class="stack-name">{name}<small>{sub}</small></div></div>
        <div class="stack-items">{chips}</div>
      </div>
'''
    return out


def _cert_cards():
    data = [
        ("Healthcare","CPHIMS — Healthcare Information &amp; Management Systems","HIMSS"),
        ("Architecture","Enterprise Architecture Foundations","LinkedIn Learning"),
        ("Standards","HIMSS · HL7 · FHIR · DICOM · SNOMED · ICD-10 · CPT","Healthcare Interoperability"),
        ("Networking","CCNP ENCOR · CCNA Cert Prep","Cisco-Aligned"),
        ("Networking","CompTIA Network+ (N10-007)","CompTIA"),
        ("Networking","GNS3 · Networking Foundations · DNS · Troubleshooting","LinkedIn Learning"),
        ("System Admin","Microsoft PowerShell · Windows 10 IT Support","Microsoft"),
        ("System Admin","SAP Production Planning · API Documentation","Industry Training"),
        ("Programming","Java 17 · Spring · API Design First · System Design","Java Mentorship 2025"),
        ("Programming","OODA · RESTful · PostgreSQL · SQL Database","Enterprise Solution Architect Path"),
        ("Data","Data Analysis Professional — Python · ETL · Visualization","Udacity · 2021"),
        ("Data","Power BI · Tableau · R · Predictive Analytics","Data Analysis Path · 2024"),
        ("Management","Lean Six Sigma · Business Analysis · Product Management","PMI / NASBA"),
        ("Management","Project Management: Technical Projects · Agile Foundations","LinkedIn Learning"),
        ("Leadership","Operational Excellence · Setting a Vision · Practical Influencing","LinkedIn Learning"),
        ("Career","Building a Second Brain · Foster a Growth Mindset","Continuous Learning"),
    ]
    out = ""
    for cat, name, issuer in data:
        out += f'''      <div class="cert-card reveal"><div class="cert-cat">{cat}</div><div class="cert-name">{name}</div><div class="cert-issuer">{issuer}</div></div>
'''
    return out
