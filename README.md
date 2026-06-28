# Logo Clothing Shop → Stitch & Stone Co.

Foundation repo for **logoclothingshop.com** (website launch) and **go-to-market sales assets** (emails, one-pager). Brand: Logo Clothing Shop today · soon Stitch & Stone Co. **stitchandstoneco.com** is not live yet.

---

## Two workstreams — don't mix them up

| Workstream | Cursor thread | You edit | Never touch |
|------------|---------------|----------|-------------|
| **Website** | Website build thread | `src/`, `public/`, `content/copy/` | `content/sales/` |
| **Go-to-market** | GTM / sales thread | `content/sales/`, `cases.json`, `docs/gtm/90-DAY-PLAN.md` | `src/` pages by hand |

**Handoff for GTM thread:** [`docs/gtm/HANDOFF.md`](docs/gtm/HANDOFF.md)  
**Session brief (read/update every session):** [`docs/PROJECT-BRIEF.md`](docs/PROJECT-BRIEF.md)

---

## Repo map

```
/
├── src/                       ← ASTRO WEBSITE SOURCE
│   ├── pages/                 ← routes (index, corporate-gifting, case-studies, …)
│   ├── layouts/               ← BaseLayout
│   ├── components/            ← Header, Footer, Card, Button, …
│   ├── lib/                   ← site.ts, caseStudies.ts
│   └── styles/global.css
├── public/                    ← static assets (logo SVG, future images)
├── dist/                      ← BUILD OUTPUT (Netlify publishes this)
├── content/
│   ├── copy/                  ← website page outlines (00–05)
│   ├── case-studies/
│   │   ├── cases.json         ← SOURCE OF TRUTH for case studies
│   │   ├── UPDATE-NOTES.md
│   │   └── AUDIT.md
│   └── sales/                 ← INTERNAL GTM — not deployed
├── brand/                     ← colors.md, logo assets
├── docs/
├── scripts/
│   └── serve.ps1              ← npm run dev
├── site/                      ← DEPRECATED static prototype (do not edit)
├── astro.config.mjs
├── tailwind.config.mjs
└── package.json
```

---

## Source of truth — quick reference

| Changing… | Edit this | Then run… |
|-----------|-----------|-----------|
| Case study content | `content/case-studies/cases.json` | `npm run build` |
| Sales emails / PDF | `content/sales/` | Re-print PDF from `one-pager.html` |
| Website page copy | `src/pages/` or `content/copy/*.md` | `npm run dev` |
| Website design | `tailwind.config.mjs`, `src/styles/global.css` | `npm run dev` |
| Site structure / nav | `docs/SITE-ARCHITECTURE.md`, `src/lib/site.ts` | Add pages in `src/pages/` |
| Logo | `brand/logo-current/` → `public/images/` | Replace SVG when PNG ready |

---

## Preview the website

```powershell
.\scripts\serve.ps1
```

Open **http://localhost:4321** · Press `Ctrl+C` to stop.

First time: run `npm install` from the repo root.

---

## Website build status

| Done | Next (Phase 2) |
|------|----------------|
| Astro + Tailwind scaffold with brand palette | Services hub + 4 service pages |
| Home, Corporate Gifting, How It Works, Contact | Industries hub + 2–4 industry pages |
| All 20 case study pages (from JSON) | About page |
| Netlify deploy (generic URL) | Connect logoclothingshop.com · contact form |
| Shared layout, components, JSON-LD schema | Photography via Astro Image |

Full plan: [`docs/SITE-ARCHITECTURE.md`](docs/SITE-ARCHITECTURE.md)

---

## GitHub backup vs live website

**The whole repo can push to GitHub for backup.**  
**Only `dist/` (from `npm run build`) goes live** on Netlify (currently generic URL; **logoclothingshop.com** custom domain next).

Sales emails, one-pager, and internal notes in `content/sales/` stay in the repo but **never appear on logoclothingshop.com** if you follow [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md).

Recommendation: use a **private** GitHub repo if sales copy should not be public.

---

## Domains

| Domain | Role |
|--------|------|
| logoclothingshop.com | **Launch domain** — connect to Netlify next (~2-week target) |
| stitchandstoneco.com | Future primary — not live yet |
| stitchstoneco.com | Future 301 → primary |
| Redirect today | **None** — logoclothingshop.com does not redirect yet |

---

## Commands

| Task | Command |
|------|---------|
| Install dependencies | `npm install` |
| Preview site | `npm run dev` or `.\scripts\serve.ps1` |
| Production build | `npm run build` |
| Git backup | `git add .` then `git commit -m "message"` |
