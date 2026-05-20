# -*- coding: utf-8 -*-
"""All page bodies for the Ahmed Bedeer portfolio."""

def build(head, footer, write, arch_svg):

    # =====================================================================
    # HOME (index.html) — Hero + quick links + featured outcomes + CTA
    # =====================================================================
    home = head(
        "Ahmed M. Bedeer — Enterprise Architect &amp; Digital Transformation Leader",
        "Enterprise Architecture & Digital Transformation Specialist · TOGAF · NORA · ArchiMate · HIMSS · 7+ years across healthcare and technology programs in KSA.",
        "home")
    home += '''
<section id="hero">
  <div class="hero-bg-blob blob-1"></div>
  <div class="hero-bg-blob blob-2"></div>

  <div class="hero-grid">
    <div class="hero-text">
      <div class="hero-badge">Available for Architecture &amp; Transformation Engagements · KSA · 2026</div>
      <h1>Architecting<br>digital <em>transformation.</em></h1>
      <p class="hero-sub">
        <strong>Enterprise Architect</strong> · <strong>Digital Transformation Specialist</strong> · <strong>Solution Architect</strong>. Aligning business vision with secure, scalable, interoperable platforms across <strong>TOGAF</strong>, <strong>NORA</strong>, and <strong>ArchiMate</strong> — with measurable clinical, operational, and financial impact.
      </p>
      <div class="hero-actions">
        <a href="case-studies.html" class="btn-primary">View Case Studies →</a>
        <a href="services.html" class="btn-ghost">Explore Services</a>
        <a href="assets/Ahmed-M-Bedeer-CV.pdf" class="cv-download" download>↓ Download CV <small>PDF</small></a>
      </div>
      <div class="hero-stats">
        <div>
          <div class="hero-stat-num">7<span>+</span></div>
          <div class="hero-stat-label">Years Experience</div>
        </div>
        <div>
          <div class="hero-stat-num">3</div>
          <div class="hero-stat-label">Architecture Frameworks</div>
        </div>
        <div>
          <div class="hero-stat-num">85<span>%</span></div>
          <div class="hero-stat-label">HIMSS Stage 6 Readiness</div>
        </div>
        <div>
          <div class="hero-stat-num">12<span>+</span></div>
          <div class="hero-stat-label">Tech &amp; Compliance Stds</div>
        </div>
      </div>
    </div>

    <div class="hero-visual">
      <div class="code-window">
        <div class="code-header">
          <div class="code-dots"><span></span><span></span><span></span></div>
          <div class="code-filename">enterprise_architecture<span class="ext">.archimate</span></div>
        </div>
        <div class="code-body">
<span class="code-comment"># TOGAF ADM · Phase B &rarr; C · Hospital EA</span><br>
<span class="code-keyword">domain</span> <span class="code-fn">Healthcare</span> {<br>
&nbsp;&nbsp;<span class="code-var">business</span>: <span class="code-string">"Patient Journey"</span>,<br>
&nbsp;&nbsp;<span class="code-var">data</span>:&nbsp;&nbsp;&nbsp;&nbsp; <span class="code-string">"FHIR · HL7 · SNOMED"</span>,<br>
&nbsp;&nbsp;<span class="code-var">app</span>:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [<span class="code-string">"EHR"</span>, <span class="code-string">"LIS"</span>, <span class="code-string">"RIS/PACS"</span>],<br>
&nbsp;&nbsp;<span class="code-var">tech</span>:&nbsp;&nbsp;&nbsp;&nbsp; <span class="code-string">"Mirth · K8s · DR"</span><br>
}<br>
<br>
<span class="code-fn">align</span>(<span class="code-var">vision</span>, <span class="code-var">capability_map</span>)<br>
&nbsp;&nbsp;.<span class="code-fn">withFramework</span>(<span class="code-string">"TOGAF"</span>, <span class="code-string">"NORA"</span>)<br>
&nbsp;&nbsp;.<span class="code-fn">compliance</span>(<span class="code-string">"HIPAA"</span>, <span class="code-string">"GDPR"</span>)<br>
&nbsp;&nbsp;.<span class="code-fn">deliver</span>()<br>
<br>
<span class="code-prompt">&gt;</span> <span class="code-comment">HIMSS Stage 6 · 85% readiness<span class="blink">&#9612;</span></span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="page-section">
  <div class="inner">
    <span class="section-tag">Navigate</span>
    <h2 style="margin-bottom:40px;">Explore the <em>practice.</em></h2>
    <div class="home-links">
      <a href="about.html" class="home-link reveal">
        <div class="hl-num">01</div><h3>About &amp; Leadership</h3>
        <p>Who I am, how I bridge business and technology, and how I lead change.</p>
        <span class="hl-go">Read more →</span>
      </a>
      <a href="expertise.html" class="home-link reveal">
        <div class="hl-num">02</div><h3>Expertise &amp; Domains</h3>
        <p>From boardroom strategy to integration engineering, across nine domains.</p>
        <span class="hl-go">Read more →</span>
      </a>
      <a href="frameworks.html" class="home-link reveal">
        <div class="hl-num">03</div><h3>Frameworks &amp; Governance</h3>
        <p>TOGAF · NORA · ArchiMate, plus architecture governance and risk.</p>
        <span class="hl-go">Read more →</span>
      </a>
      <a href="case-studies.html" class="home-link reveal">
        <div class="hl-num">04</div><h3>Case Studies</h3>
        <p>Engagements with trade-offs, architecture views, ROI, and outcomes.</p>
        <span class="hl-go">Read more →</span>
      </a>
    </div>
  </div>
</section>

<section class="page-section">
  <div class="inner">
    <span class="section-tag">Selected Impact</span>
    <h2 style="margin-bottom:40px;">Outcomes, not just <em>diagrams.</em></h2>
    <div class="impact-grid">
      <div class="impact-card reveal"><div class="impact-num">12<span>%</span></div><div class="impact-label">ICU LOS Reduction</div><div class="impact-desc">Predictive analytics &amp; care-gap alerting integrated into the EDW supported proactive outreach.</div></div>
      <div class="impact-card reveal"><div class="impact-num">25<span>%</span></div><div class="impact-label">Faster Month-End Close</div><div class="impact-desc">UML-modeled revenue-cycle workflows streamlined order lifecycle and charge capture.</div></div>
      <div class="impact-card reveal"><div class="impact-num">40<span>%</span></div><div class="impact-label">Less Admin Overhead</div><div class="impact-desc">Patient-centric Java/Spring Boot application automated appointment &amp; insurance workflows.</div></div>
      <div class="impact-card reveal"><div class="impact-num">$500K<span>+</span></div><div class="impact-label">Cost-Savings Identified</div><div class="impact-desc">Automated market analysis dashboard delivered real-time insights for stakeholder decisions.</div></div>
    </div>
    <div style="text-align:center;margin-top:36px;"><a href="case-studies.html" class="btn-ghost">See all case studies &amp; the numbers behind them →</a></div>
  </div>
</section>

<div class="cta-strip reveal">
  <h2>Have a transformation to <em>architect?</em></h2>
  <p>Whether it is a greenfield hospital build, a data-governance program, or a cloud modernization — let's align the business with technology that is secure, scalable, and demonstrably valuable.</p>
  <div class="row">
    <a href="contact.html" class="btn-primary">Start a Conversation →</a>
    <a href="assets/Ahmed-M-Bedeer-CV.pdf" class="btn-ghost" download>↓ Download CV</a>
  </div>
</div>
'''
    home += footer()
    write("index.html", home)

    # =====================================================================
    # ABOUT — bio + leadership/change + technology-agnostic + CV
    # =====================================================================
    about = head("About — Ahmed M. Bedeer | Enterprise Architect",
        "About Ahmed Bedeer — Enterprise Architecture & Digital Transformation specialist bridging business and technology, leadership, change management, and stakeholder alignment.",
        "about")
    about += '''
<div class="page-hero">
  <div class="breadcrumb"><a href="index.html">home</a><span class="sep">/</span><span class="here">about</span></div>
  <h1>Business vision.<br><em>Architected outcomes.</em></h1>
  <p class="lead">I translate C-level vision into governed, executable transformation — connecting strategy, architecture, and engineering into one coherent fabric.</p>
</div>

<section id="about" style="padding-top:60px;">
  <div class="about-grid">
    <div class="about-card reveal">
      <div class="about-avatar">AB</div>
      <div class="about-card-name">Ahmed M. Bedeer</div>
      <div class="about-card-role">$ enterprise_architect · digital_transformation</div>
      <div class="about-card-tags">
        <span class="tag blue">TOGAF</span>
        <span class="tag blue">NORA</span>
        <span class="tag cyan">ArchiMate</span>
        <span class="tag cyan">HIMSS</span>
        <span class="tag">HL7</span>
        <span class="tag">FHIR</span>
        <span class="tag">DICOM</span>
        <span class="tag purple">Java</span>
        <span class="tag purple">Spring Boot</span>
        <span class="tag green">CPHIMS</span>
      </div>
      <div class="about-meta">
        <div class="meta-item"><div class="meta-label">Based In</div><div class="meta-value">Al Khobar, KSA</div></div>
        <div class="meta-item"><div class="meta-label">Nationality</div><div class="meta-value">Egyptian 🇪🇬</div></div>
        <div class="meta-item"><div class="meta-label">Experience</div><div class="meta-value">7+ Years</div></div>
        <div class="meta-item"><div class="meta-label">Languages</div><div class="meta-value">EN · AR</div></div>
      </div>
      <a href="assets/Ahmed-M-Bedeer-CV.pdf" class="cv-download" download style="margin-top:24px;width:100%;justify-content:center;">↓ Download CV <small>PDF</small></a>
    </div>

    <div class="about-text reveal">
      <span class="section-tag">About Me</span>
      <h2>From strategy to <em>shipped value.</em></h2>
      <p>I am an <strong>Enterprise Architecture &amp; Digital Transformation Specialist</strong> based in <strong>Al Khobar, Saudi Arabia</strong>, delivering enterprise-scale healthcare and technology solutions for over <strong>seven years</strong>. My practice connects strategy, architecture, and engineering — translating C-level vision into governed, executable transformation roadmaps.</p>
      <p>My focus sits at the intersection of three frameworks: <em>TOGAF</em> for enterprise architecture discipline, <em>NORA</em> for alignment with Saudi digital governance, and <em>ArchiMate</em> for modeling business, application, data, and technology layers as one coherent fabric. I currently apply this lens to the <strong>GAD Heart &amp; Lung Institute</strong> — a newly established specialized hospital and the first of its kind in the Middle East.</p>
      <p>Beyond healthcare, I work flexibly across domains — building <em>data architectures</em>, <em>integration platforms</em>, and <em>cloud-native services</em> in Java, Spring Boot, and microservices. I'm CPHIMS-aligned, fluent in HL7/FHIR/DICOM/SNOMED/LOINC, and have shipped EDW pipelines, BI dashboards, and predictive analytics that moved real KPIs — including a <strong>12% reduction in ICU length of stay</strong> and a <strong>25% faster month-end close</strong>.</p>
      <p>Whether the engagement is a <strong>greenfield hospital build</strong>, a <strong>data governance program</strong>, or a <strong>cloud modernization</strong>, my goal is the same: align the business with technology that is secure, scalable, interoperable — and demonstrably valuable.</p>
    </div>
  </div>
</section>

<section class="page-section">
  <div class="inner">
    <span class="section-tag">Leadership &amp; Change</span>
    <h2>Bridging <em>business and technology.</em></h2>
    <p class="section-desc">Transformation is people and process before it is platform. I lead the human side of change as deliberately as the technical side.</p>
    <div class="lead-grid">
      <div class="lead-card reveal">
        <div class="lc-icon">🧭</div>
        <h3>Mentoring &amp; Leadership</h3>
        <p>Coaching engineers and analysts toward an architecture mindset, running Java/solution-architecture mentorship, and building "digital champions" who carry the change into daily operations.</p>
      </div>
      <div class="lead-card reveal">
        <div class="lc-icon">🔄</div>
        <h3>Change Management</h3>
        <p>Skills-gap surveys, phased adoption plans, and communication that makes the "why" land. I treat clinician and end-user readiness as a first-class deliverable, not an afterthought.</p>
      </div>
      <div class="lead-card reveal">
        <div class="lc-icon">🤝</div>
        <h3>Stakeholder Management</h3>
        <p>Trusted advisor to chairmen, CIOs, and PMOs. I translate between executive intent and engineering reality, keeping every architecture decision traceable to a business outcome.</p>
      </div>
    </div>
  </div>
</section>

<section class="page-section" style="padding-top:0;">
  <div class="agnostic-banner reveal">
    <div class="ab-mark">technology<br>= agnostic</div>
    <p><strong>I am deliberately technology-agnostic.</strong> The frameworks stay constant; the tools adapt to the problem. I choose the best fit for the business case — cost, data accuracy, time-to-value, and total cost of ownership — rather than the tool I happen to prefer. That neutrality is what lets executive teams trust the recommendation.</p>
  </div>
</section>

<section class="page-section">
  <div class="inner">
    <span class="section-tag">Beyond the architecture</span>
    <h2>The person behind <em>the practice.</em></h2>
    <p class="section-desc">A bit of the human side. Architecture is a craft I genuinely enjoy — and a few things keep the curiosity sharp.</p>
    <div class="lead-grid">
      <div class="lead-card reveal"><div class="lc-icon">🎮</div><h3>Builder at heart</h3><p>My CS graduation project was a Unity 3D physics game — I still love systems that simulate the real world and the discipline of making them perform.</p></div>
      <div class="lead-card reveal"><div class="lc-icon">📚</div><h3>Continuous learner</h3><p>"Building a Second Brain" and a growth-mindset habit keep me reading, modeling, and sharing lessons-learned with the community.</p></div>
      <div class="lead-card reveal"><div class="lc-icon">🌍</div><h3>Cross-culture</h3><p>Egyptian, working across the Gulf — comfortable bridging cultures, languages (EN/AR), and the gap between global standards and local governance.</p></div>
    </div>
  </div>
</section>
'''
    about += _cta("Want the full story in one page?", "Download the CV, or connect on LinkedIn for regular lessons-learned and architecture notes.")
    about += footer()
    write("about.html", about)

    # delegate the rest
    import pages2
    pages2.build_rest(head, footer, write, arch_svg, _cta)


def _cta(title, text):
    return f'''
<div class="cta-strip reveal">
  <h2>{title}</h2>
  <p>{text}</p>
  <div class="row">
    <a href="contact.html" class="btn-primary">Get in Touch →</a>
    <a href="https://www.linkedin.com/in/ahmed-bedeer" target="_blank" rel="noopener" class="btn-ghost">in · LinkedIn</a>
  </div>
</div>
'''
