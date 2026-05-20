# -*- coding: utf-8 -*-
"""Builds the multi-page Ahmed Bedeer portfolio from shared templates."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("about",        "about",        "about.html"),
    ("expertise",    "expertise",    "expertise.html"),
    ("frameworks",   "frameworks",   "frameworks.html"),
    ("experience",   "experience",   "experience.html"),
    ("case-studies", "case studies", "case-studies.html"),
    ("services",     "services",     "services.html"),
    ("skills",       "skills",       "skills.html"),
]

def nav_links(active):
    lis = ""
    for key, label, href in NAV:
        cls = ' class="active"' if key == active else ''
        lis += f'    <li><a href="{href}"{cls}>{label}</a></li>\n'
    cta_cls = ' active' if active == 'contact' else ''
    lis += f'    <li><a href="contact.html" class="nav-cta{cta_cls}">Contact</a></li>\n'
    return lis

def drawer_links(active):
    out = ""
    for key, label, href in NAV:
        cls = ' class="active"' if key == active else ''
        out += f'  <a href="{href}"{cls}>{label.title()}</a>\n'
    out += '  <a href="contact.html" class="drawer-cta">Contact →</a>\n'
    return out

def head(title, desc, active):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="assets/styles.css" />
</head>
<body>

<nav>
  <a href="index.html" class="nav-logo">
    <span class="nav-avatar">AB</span>
    <span class="nav-logo-text">Ahmed<span>.</span>Bedeer</span>
  </a>
  <ul class="nav-links">
{nav_links(active)}  </ul>
  <button class="nav-toggle" aria-label="Open menu" aria-expanded="false"><span></span></button>
</nav>

<div class="mobile-drawer">
{drawer_links(active)}</div>
'''

def footer():
    fn = ""
    for key, label, href in NAV:
        fn += f'    <a href="{href}">{label}</a>\n'
    return f'''
<footer>
  <div class="footer-logo">Ahmed Bedeer<span>.</span></div>
  <div class="footer-nav">
{fn}    <a href="contact.html">contact</a>
  </div>
  <p>© 2026 Ahmed M. Bedeer · Al Khobar, KSA · Enterprise Architect</p>
  <p>TOGAF · NORA · ArchiMate · v2.0</p>
</footer>

<script src="assets/main.js"></script>
</body>
</html>'''

def write(name, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(body)
    print("wrote", name)

# ---------------------------------------------------------------------------
# Reusable BDAT-style logical architecture SVG (ArchiMate-flavoured)
# ---------------------------------------------------------------------------
LAYER_COLORS = {
    "business":    "#FBBF24",
    "application": "#3B82F6",
    "data":        "#22D3EE",
    "technology":  "#A78BFA",
    "integration": "#10B981",
}

def arch_svg(title, layers):
    """layers: list of (label, key, [node strings])"""
    band_h = 86
    gap = 14
    pad_top = 46
    width = 760
    height = pad_top + len(layers) * (band_h + gap) + 8
    parts = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{title}">']
    parts.append(f'<text x="0" y="22" fill="#94A3B8" font-family="JetBrains Mono, monospace" font-size="13" letter-spacing="0.5">// {title}</text>')
    y = pad_top
    for label, key, nodes in layers:
        color = LAYER_COLORS.get(key, "#3B82F6")
        parts.append(f'<rect x="0" y="{y}" width="{width}" height="{band_h}" rx="12" fill="rgba(15,26,54,0.55)" stroke="{color}" stroke-opacity="0.35"/>')
        parts.append(f'<rect x="0" y="{y}" width="6" height="{band_h}" rx="3" fill="{color}"/>')
        parts.append(f'<text x="20" y="{y+26}" fill="{color}" font-family="JetBrains Mono, monospace" font-size="11" letter-spacing="1">{label.upper()}</text>')
        # node chips
        cx = 20
        cy = y + 44
        chip_h = 30
        for n in nodes:
            w = 16 + len(n) * 7.6
            parts.append(f'<rect x="{cx:.0f}" y="{cy}" width="{w:.0f}" height="{chip_h}" rx="8" fill="rgba(5,9,23,0.6)" stroke="{color}" stroke-opacity="0.45"/>')
            parts.append(f'<text x="{cx + w/2:.0f}" y="{cy+20}" fill="#F1F5F9" font-family="Inter, sans-serif" font-size="12.5" text-anchor="middle">{n}</text>')
            cx += w + 10
        y += band_h + gap
    # connecting arrows between layers (center)
    parts.append('</svg>')
    return '<div class="arch-frame">' + "".join(parts) + '</div>'

# ===========================================================================
# Build pages in a separate module section
# ===========================================================================
import pages
pages.build(head, footer, write, arch_svg)
print("DONE")
