// ── Reveal on scroll ──────────────────────────────────────────
const reveals = document.querySelectorAll('.reveal');
if (reveals.length) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => entry.target.classList.add('visible'), (i % 5) * 80);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  reveals.forEach(el => observer.observe(el));
}

// ── Mobile menu toggle ────────────────────────────────────────
const navToggle = document.querySelector('.nav-toggle');
if (navToggle) {
  navToggle.addEventListener('click', () => {
    document.body.classList.toggle('menu-open');
    const open = document.body.classList.contains('menu-open');
    navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.style.overflow = open ? 'hidden' : '';
  });
  document.querySelectorAll('.mobile-drawer a').forEach(a => {
    a.addEventListener('click', () => {
      document.body.classList.remove('menu-open');
      document.body.style.overflow = '';
    });
  });
}

// ── Skill bar fill animation on reveal ────────────────────────
const bars = document.querySelectorAll('.skill-bar i[data-w]');
if (bars.length) {
  const barObs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        el.style.transition = 'width 1s cubic-bezier(.2,.7,.2,1)';
        requestAnimationFrame(() => { el.style.width = el.dataset.w; });
        barObs.unobserve(el);
      }
    });
  }, { threshold: 0.4 });
  bars.forEach(b => { b.style.width = '0%'; barObs.observe(b); });
}
