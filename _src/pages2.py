# -*- coding: utf-8 -*-
"""Remaining page bodies."""

def build_rest(head, footer, write, arch_svg, _cta):

    # =====================================================================
    # EXPERTISE — core expertise + domains
    # =====================================================================
    p = head("Expertise &amp; Domains — Ahmed M. Bedeer",
        "Core expertise across enterprise architecture, digital transformation, healthcare informatics, integration, data, software, cloud, security, and delivery — applied across nine domains.",
        "expertise")
    p += '''
<div class="page-hero">
  <div class="breadcrumb"><a href="index.html">home</a><span class="sep">/</span><span class="here">expertise</span></div>
  <h1>Where I <em>specialize.</em></h1>
  <p class="lead">From strategic enterprise architecture down to integration engineering — the full vertical from boardroom to platform, applied across many industries.</p>
</div>

<section id="expertise" style="padding-top:50px;">
  <div style="max-width:1300px;margin:0 auto;">
    <span class="section-tag">Core Expertise</span>
    <h2>Nine capabilities, <em>one practice.</em></h2>
    <p class="section-desc">Each capability ties back to a measurable business outcome — that is the line between a solution architect and an enterprise architect.</p>
    <div class="expertise-grid">
      ''' + _expertise_cards() + '''
    </div>
  </div>
</section>

<section id="domains" style="padding-top:0;">
  <div class="domains-wrap">
    <span class="section-tag">Domains</span>
    <h2>Domains I <em>work across.</em></h2>
    <p class="section-desc">My architecture practice is intentionally cross-domain. The frameworks stay constant; the context adapts.</p>
    <div class="domains-grid">
      ''' + _domain_cards() + '''
    </div>
  </div>
</section>
'''
    p += _cta("Need a capability mapped to your roadmap?", "I assess current-state capabilities and design the target-state vision with a phased, governed transition plan.")
    p += footer()
    write("expertise.html", p)

    # =====================================================================
    # FRAMEWORKS — TOGAF/NORA/ArchiMate + governance & risk
    # =====================================================================
    p = head("Frameworks &amp; Governance — Ahmed M. Bedeer",
        "TOGAF, NORA, and ArchiMate as one integrated practice — plus architecture governance, the Architecture Review Board, risk registers, guardrails, Zero Trust, and compliance.",
        "frameworks")
    p += '''
<div class="page-hero">
  <div class="breadcrumb"><a href="index.html">home</a><span class="sep">/</span><span class="here">frameworks</span></div>
  <h1>Three lenses,<br>one <em>integrated practice.</em></h1>
  <p class="lead">Together they answer the three questions every transformation must: <strong>why</strong> we are changing, <strong>what</strong> we are building, and <strong>how</strong> it aligns with national and international standards.</p>
</div>

<section id="frameworks" style="padding-top:50px;">
  <div class="frameworks-wrap">
    <span class="section-tag">Architecture Frameworks</span>
    <h2>The methods I <em>anchor on.</em></h2>
    <div class="frameworks-grid">
      <div class="framework-card reveal">
        <div class="framework-mono">// Framework 01</div>
        <div class="framework-name">TOGAF</div>
        <div class="framework-tagline">The Open Group Architecture Framework</div>
        <p class="framework-desc">A disciplined, iterative method for designing the enterprise. I apply the Architecture Development Method (ADM) end-to-end — vision through governance — keeping every artifact traceable to business value.</p>
        <ul class="framework-list">
          <li>ADM phases A through H</li>
          <li>Architecture Repository &amp; Continuum</li>
          <li>Capability-based planning</li>
          <li>Architecture Governance Board</li>
          <li>Reference models &amp; building blocks</li>
        </ul>
      </div>
      <div class="framework-card purple reveal">
        <div class="framework-mono">// Framework 02</div>
        <div class="framework-name">NORA</div>
        <div class="framework-tagline">National Overall Reference Architecture · KSA</div>
        <p class="framework-desc">Saudi Arabia's reference architecture for digital government. I align engagements with NORA to ensure compliance with national digital governance, interoperability, and citizen-experience standards across Vision 2030 initiatives.</p>
        <ul class="framework-list">
          <li>Business · Data · Application · Tech layers</li>
          <li>Saudi digital governance alignment</li>
          <li>Vision 2030 traceability</li>
          <li>Interoperability standards</li>
          <li>Citizen-centric service design</li>
        </ul>
      </div>
      <div class="framework-card amber reveal">
        <div class="framework-mono">// Framework 03</div>
        <div class="framework-name">ArchiMate</div>
        <div class="framework-tagline">Open Group Modeling Standard</div>
        <p class="framework-desc">The visual language that makes architecture decisions reviewable. I model business processes, application landscapes, data flows, and technology stacks as a single, navigable map — bridging strategy and implementation.</p>
        <ul class="framework-list">
          <li>Strategy, Business, Application, Tech, Physical</li>
          <li>Motivation &amp; Implementation extensions</li>
          <li>Cross-layer relationships &amp; viewpoints</li>
          <li>Sparx EA &amp; Visual Paradigm modeling</li>
          <li>Living architecture documentation</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="page-section">
  <div class="inner">
    <span class="section-tag">Governance &amp; Risk</span>
    <h2>What separates an <em>enterprise architect.</em></h2>
    <p class="section-desc">Anyone can draw a target state. The discipline is governing the journey — managing risk, setting guardrails, and proving compliance the whole way.</p>
    <div class="cs-cols">
      <div class="cs-block reveal">
        <div class="blk-label">Architecture Governance</div>
        <p>I stand up and run <strong>Architecture Review Boards (ARB)</strong> — a cadence where every significant decision is reviewed against principles, standards, and the target architecture before it ships.</p>
        <ul>
          <li>Architecture principles &amp; decision records (ADRs)</li>
          <li>Compliance reviews at each ADM gate</li>
          <li>Vendor &amp; SOW technical review against standards</li>
          <li>Exception &amp; waiver process with sunset dates</li>
        </ul>
      </div>
      <div class="cs-block reveal">
        <div class="blk-label">Risk &amp; Controls</div>
        <p>Risk is tracked, owned, and burned down — not discovered at go-live. I maintain a living <strong>risk register</strong> and design <strong>guardrails</strong> into the platform so the safe path is the easy path.</p>
        <ul>
          <li>Risk register with owners, likelihood &amp; impact</li>
          <li>Privacy-by-design &amp; least-privilege guardrails</li>
          <li>Zero Trust segmentation &amp; identity controls</li>
          <li>HIPAA / GDPR alignment, audit logging, encryption</li>
        </ul>
      </div>
    </div>
    <div class="cs-block span2 reveal" style="margin-top:22px;">
      <div class="blk-label">Compliance &amp; standards in play</div>
      <div class="gov-chips">
        <span class="chip">TOGAF ADM Governance</span>
        <span class="chip">NORA · KSA Digital Governance</span>
        <span class="chip">HIMSS Stage 6</span>
        <span class="chip">HIPAA</span>
        <span class="chip">GDPR</span>
        <span class="chip">Zero Trust</span>
        <span class="chip">AAA Model</span>
        <span class="chip">Encryption-at-Rest</span>
        <span class="chip">Audit Logging</span>
      </div>
    </div>
  </div>
</section>
'''
    p += _cta("Building a governance function from scratch?", "I help establish ARBs, principles, and risk processes that make transformation auditable and repeatable.")
    p += footer()
    write("frameworks.html", p)

    # =====================================================================
    # EXPERIENCE — timeline
    # =====================================================================
    p = head("Experience — Ahmed M. Bedeer",
        "A seven-year trajectory from data analysis and infrastructure to enterprise architecture and digital transformation leadership across Saudi Arabia.",
        "experience")
    p += '''
<div class="page-hero">
  <div class="breadcrumb"><a href="index.html">home</a><span class="sep">/</span><span class="here">experience</span></div>
  <h1>A <em>seven-year</em> trajectory.</h1>
  <p class="lead">From data analysis and infrastructure to enterprise architecture and digital transformation leadership across the Gulf.</p>
</div>

<section id="experience" style="padding-top:50px;">
  <div class="experience-wrap">
    <div class="timeline">
      <div class="timeline-item reveal">
        <div class="timeline-dot current"></div>
        <div class="timeline-meta"><span>2026 — Present</span><span class="timeline-pill">Independent</span></div>
        <div class="timeline-role">Enterprise Architecture &amp; Digital Transformation Consultant</div>
        <div class="timeline-org">Independent Practice · Cross-Industry · <strong>KSA / Remote</strong></div>
        <ul class="timeline-points">
          <li>Lead <strong>enterprise architecture initiatives</strong> aligned with TOGAF and NORA frameworks across healthcare and SME environments.</li>
          <li>Design <em>end-to-end digital transformation strategies</em> integrating governance, operating models, and data architecture.</li>
          <li>Establish enterprise <strong>data governance frameworks</strong>, master data models, and analytics roadmaps.</li>
          <li>Advise executive leadership on technology investment, modernization strategy, and transformation execution.</li>
        </ul>
      </div>
      <div class="timeline-item reveal">
        <div class="timeline-dot"></div>
        <div class="timeline-meta"><span>Aug 2023 — Present</span><span class="timeline-pill">Healthcare · KSA</span></div>
        <div class="timeline-role">Healthcare IT Project Engineer</div>
        <div class="timeline-org">GAD International · <strong>Heart &amp; Lung Institute, Al Khobar</strong> — first specialized cardiac &amp; pulmonary hospital in the Middle East</div>
        <ul class="timeline-points">
          <li>Architected enterprise digital health ecosystem integrating <strong>EHR, LIS, RIS/PACS, ICU, and patient portals</strong>, achieving <em>85% HIMSS Stage 6 readiness</em>.</li>
          <li>Designed interoperability architecture using <strong>FHIR APIs, HL7 messaging, IoT integration, and Mirth Connect</strong> across 7 hospital departments and 3 outpatient clinics.</li>
          <li>Built <strong>ODS → EDW data platform</strong> with ETL pipelines feeding BI dashboards for OR utilization, readmission risk, and supply-chain efficiency.</li>
          <li>Modeled UML-driven revenue-cycle workflows reducing <em>month-end close by 25%</em>.</li>
          <li>Implemented VLAN-segmented networks, HA WAN links, and DR architecture with <em>sub-1% RTO failover</em>.</li>
          <li>Authored privacy-by-design controls (AAA, audit logging, encryption-at-rest) satisfying HIPAA &amp; GDPR.</li>
          <li>Active PMO member — technical documentation, LC/ITC reviews, vendor SOW alignment with hospital vision.</li>
        </ul>
      </div>
      <div class="timeline-item reveal">
        <div class="timeline-dot"></div>
        <div class="timeline-meta"><span>Mar 2024 — Present</span><span class="timeline-pill">Freelance · HIMS</span></div>
        <div class="timeline-role">Healthcare Digitalization &amp; Telehealth Consultant</div>
        <div class="timeline-org">Freelance HIMS Project · <strong>Gulf Region</strong></div>
        <ul class="timeline-points">
          <li>Strategic advisor for aligning digital health initiatives with global <strong>HIMSS, HL7, HIPAA, FHIR</strong> frameworks.</li>
          <li>Led initiatives to improve digital health maturity and organizational <em>interoperability</em>.</li>
          <li>Directed health data integration efforts using HL7 protocols for seamless information exchange.</li>
          <li>Championed <em>FHIR adoption</em> for efficient, secure, modern EHR interoperability.</li>
        </ul>
      </div>
      <div class="timeline-item reveal">
        <div class="timeline-dot"></div>
        <div class="timeline-meta"><span>Mar 2022 — Aug 2023</span><span class="timeline-pill">ICT Build</span></div>
        <div class="timeline-role">IT Project Engineer</div>
        <div class="timeline-org">GAD International · <strong>Baha Medical Center, KSA</strong></div>
        <ul class="timeline-points">
          <li>Delivered <em>90% readiness</em> of ICT hospital infrastructure including firewalls, VLANs, Active Directory, and DNS.</li>
          <li>Implemented network protocols — <strong>VLANs, OSPF, IP Access Lists</strong> — across hospital backbone.</li>
          <li>Configured DNS, email servers, Wi-Fi infrastructure, and Active Directory for clinical operations.</li>
          <li>Tested and commissioned hospital systems achieving <em>75% infrastructure completion</em> on schedule.</li>
          <li>Provided on-site and remote technical support for HIS/ERP system rollout.</li>
        </ul>
      </div>
      <div class="timeline-item reveal">
        <div class="timeline-dot"></div>
        <div class="timeline-meta"><span>Jan 2022 — Mar 2022</span><span class="timeline-pill">Analytics</span></div>
        <div class="timeline-role">Data Analyst &amp; IT Engineer</div>
        <div class="timeline-org">Medical Mall · <strong>Riyadh, KSA</strong></div>
        <ul class="timeline-points">
          <li>Built Power BI analytics and SQL reporting platforms for supply-chain and operational intelligence.</li>
          <li>Developed automation and workforce-management applications improving organizational efficiency.</li>
          <li>Designed organizational plans and future-state visions in support of business strategy.</li>
          <li>Modeled business data and built desktop applications for <em>CV analysis and supply-chain</em> use cases.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
'''
    p += _cta("Want references or a deeper walkthrough?", "I'm happy to walk through any engagement in detail and connect you with references on request.")
    p += footer()
    write("experience.html", p)

    # delegate
    import pages3
    pages3.build_more(head, footer, write, arch_svg, _cta)


def _expertise_cards():
    data = [
        ("EA", "Enterprise Architecture", "TOGAF-aligned architecture roadmaps, capability modeling, operating models, and IT governance. Translate strategy into structured BDAT layers with clear transition states.", "Sparx EA · Visual Paradigm · ArchiMate"),
        ("DX", "Digital Transformation", "Business–IT alignment, process re-engineering, automation, and KPI-driven execution. From transformation roadmaps to change enablement and value realization.", "NORA · TOGAF · KPI frameworks"),
        ("⚕", "Healthcare Informatics", "HIS, EHR/EMR, ERP, LIS, RIS/PACS, ICU and patient-facing portals. End-to-end clinical workflow design and HIMSS Stage 6 readiness execution.", "HIMSS · CPHIMS · HL7 · FHIR"),
        ("⇄", "Integration &amp; Interoperability", "Mirth Connect integration bus, FHIR APIs, HL7 v2.x, and DICOM. Terminology mapping against LOINC and SNOMED CT for regulatory reporting and CDS hooks.", "Mirth · API-First · REST · iPaaS"),
        ("Σ", "Data &amp; Analytics", "ODS → EDW pipelines, ETL orchestration, BI dashboards, and predictive analytics. Data governance, master data, and population health registries.", "Power BI · Tableau · Python · SQL"),
        ("{ }", "Software Engineering", "Java 17 / Spring Boot microservices, Node.js services, OODA design, RESTful APIs, and PostgreSQL/MySQL platforms — built API-first and production-ready.", "Java · Spring · Node · PostgreSQL"),
        ("☁", "Cloud &amp; Infrastructure", "Docker, Kubernetes, VLAN-segmented networks, HA WAN links, active-passive clustering, and DR architectures with sub-1% RTO failover.", "Docker · K8s · Aruba · Palo Alto"),
        ("🛡", "Security &amp; Compliance", "Privacy-by-design controls satisfying HIPAA &amp; GDPR — AAA model, audit logging, encryption-at-rest. Security architecture aligned with healthcare regulation.", "HIPAA · GDPR · AAA · IAM"),
        ("⚙", "Project &amp; Program Delivery", "Active PMO collaboration, technical documentation, vendor &amp; SOW review, and SME advisory. Lean Six Sigma, Agile, and operational excellence.", "Agile · Lean Six Sigma · PMO"),
    ]
    out = ""
    for icon, h, p, tools in data:
        out += f'''<div class="expertise-card reveal">
        <div class="expertise-icon">{icon}</div>
        <h3>{h}</h3>
        <p>{p}</p>
        <div class="tools"><span>tools:</span> {tools}</div>
      </div>
      '''
    return out


def _domain_cards():
    data = [
        ("⚕", "Healthcare", "HIS, EHR, EMR, LIS, RIS/PACS, ICU systems, patient portals, clinical informatics."),
        ("🏛", "Government &amp; Public Sector", "NORA-aligned digital services, citizen experience, e-government interoperability."),
        ("📊", "Data &amp; Analytics", "EDW design, master data, BI platforms, predictive analytics, data governance."),
        ("☁", "Cloud &amp; Platform", "Microservices, container platforms, hybrid cloud, DR architecture, platform strategy."),
        ("🛒", "E-Commerce &amp; SME", "Scalable transaction platforms, OODA-driven design, automation, growth-stage architecture."),
        ("🏢", "Enterprise IT", "ERP, HR, finance integrations, IT operating models, automation, change enablement."),
        ("🔌", "Integration &amp; iPaaS", "HL7, FHIR, DICOM, REST APIs, Mirth Connect, message brokering, API-first design."),
        ("🛡", "Security &amp; Compliance", "HIPAA, GDPR, AAA model, audit logging, encryption, identity, privacy-by-design."),
    ]
    out = ""
    for icon, h, p in data:
        out += f'''<div class="domain-card reveal">
        <div class="domain-icon">{icon}</div>
        <h4>{h}</h4>
        <p>{p}</p>
      </div>
      '''
    return out
