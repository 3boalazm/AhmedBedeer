# Ahmed M. Bedeer — Personal Website

Single-page portfolio built in the same style as the reference sample, fully customized for Ahmed Bedeer (Enterprise Architect & Digital Transformation Specialist).

## Sections

1. **Hero** — name, title, intro, headline stats (years, frameworks, HIMSS readiness), animated code window with TOGAF/ArchiMate snippet
2. **About** — profile card with avatar (AB), quick metadata (location, nationality, experience, languages) + 4-paragraph bio
3. **Core Expertise** — 9 expertise cards covering EA, Digital Transformation, Healthcare Informatics, Integration, Data, Software, Cloud, Security, and Delivery
4. **Architecture Frameworks** — TOGAF · NORA · ArchiMate showcase with details for each
5. **Domains** — 8 industry/domain cards (Healthcare, Government, Data, Cloud, E-Commerce, Enterprise IT, Integration, Security)
6. **Experience Timeline** — 5 roles with dot timeline (current Independent practice, GAD Heart & Lung, Freelance HIMS, Baha Medical Center, Medical Mall Riyadh)
7. **Selected Impact** — 8 KPI/impact cards + 4 detailed case studies
8. **Services** — 6 service offerings (EA Strategy, Healthcare Transformation, Data Architecture, Solution Architecture, Cloud Modernization, Executive Advisory)
9. **Technical Stack** — 8 categorized stack rows covering Architecture, Healthcare Standards, Engineering, Data, Cloud, Compliance, Methods, Productivity
10. **Certifications & Education** — 16 certification cards + Education + Languages strip
11. **Contact** — 6 contact cards (email, phone, LinkedIn, GitHub, location, engagement)

## How to use

- Open `index.html` directly in any modern browser — no build step, no dependencies (fonts loaded from Google Fonts CDN).
- To deploy: drag-and-drop the file to Netlify, GitHub Pages, Vercel, or any static host.
- To customize the avatar: replace the `AB` initials in the `.about-avatar` div with an `<img>` tag pointing to a square portrait photo.

## Design notes

- Same dark theme aesthetic as the reference sample (dark navy → blue/cyan accents)
- Typography: **Syne** (display) + **Inter** (body) + **JetBrains Mono** (technical)
- All colors live in CSS custom properties at the top of the `<style>` block (`:root { ... }`) — change once, propagates everywhere
- Fully responsive (1024 / 900 / 600 / 540 breakpoints)
- Reveal-on-scroll animation via IntersectionObserver

## Edits you may want to make

- Replace the `AB` initials avatar with a real headshot
- Add real LinkedIn / GitHub / Scholar URLs if any change
- Update / extend the timeline as new engagements complete
- Add Sparx EA / Visual Paradigm exported diagram thumbnails as a "Selected Diagrams" section if you want to showcase modeling work
