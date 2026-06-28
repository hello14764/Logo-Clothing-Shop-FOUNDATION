# Cursor rules — Logo Clothing Shop / Stitch & Stone website

**Read first every session:** `[docs/PROJECT-BRIEF.md](docs/PROJECT-BRIEF.md)` — update at session close

```md
.
```



**Active focus:** Astro site Phase 2 + GTM in parallel (website not paused)

Detailed rules for the AI live in `.cursor/rules/`:


| Rule file               | Applies when                                                   |
| ----------------------- | -------------------------------------------------------------- |
| `website-phase-1.mdc`   | Editing `src/**`, `public/**`, Tailwind, website content       |
| `case-studies.mdc`      | Editing `content/case-studies/cases.json`                      |
| `sales-not-website.mdc` | Editing `content/sales/**` (GTM thread — do not mix into site) |


**Read first for website work:**

- `docs/SITE-ARCHITECTURE.md` — nav, sitemap, positioning
- `docs/DEPLOYMENT.md` — Astro build, `dist/` deploys live
- `README.md` — repo map

**GTM / sales work:** `docs/gtm/HANDOFF.md` (different thread)

---



## Stack


| Layer              | Location                                                                  |
| ------------------ | ------------------------------------------------------------------------- |
| Astro + Tailwind   | `src/`, `astro.config.mjs`, `tailwind.config.mjs`                         |
| Static assets      | `public/`                                                                 |
| Case study data    | `content/case-studies/cases.json` → `src/pages/case-studies/[slug].astro` |
| Build output       | `dist/` (Netlify publish)                                                 |
| Legacy static site | `site/` (deprecated, do not edit)                                         |


---



## Phase 1 (complete)


| Page              | Route                       | Status           |
| ----------------- | --------------------------- | ---------------- |
| Home              | `/`                         | Ported           |
| Corporate Gifting | `/corporate-gifting/`       | Ported           |
| How It Works      | `/how-it-works/`            | Ported           |
| Contact           | `/contact/`                 | Ported           |
| Case Studies      | `/case-studies/` + 20 slugs | Ported from JSON |


**Phase 2 (next):** Services, Industries, About, Insights

---



## Commands

```powershell
npm install
npm run dev          # http://localhost:4321
npm run build        # output → dist/
.\scripts\serve.ps1  # runs npm run dev
```

Publish directory for live site: `dist` (`netlify.toml`)