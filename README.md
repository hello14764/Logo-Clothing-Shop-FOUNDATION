# Logo Clothing Shop → Stitch & Stone Co.

Foundation repo for **stitchandstoneco.com** (website) and **go-to-market sales assets** (emails, one-pager). Logo Clothing Shop stays live at logoclothingshop.com until launch.

---

## Two workstreams — don't mix them up

| Workstream | Cursor thread | You edit | Never touch |
|------------|---------------|----------|-------------|
| **Website** | Website build thread | `site/`, `content/copy/`, `site/css/` | `content/sales/` |
| **Go-to-market** | GTM / sales thread | `content/sales/`, `cases.json`, `docs/90-DAY-PLAN.md` | `site/` HTML by hand |

**Handoff for GTM thread:** [`docs/gtm/HANDOFF.md`](docs/gtm/HANDOFF.md)

---

## Repo map

```
/
├── site/                      ← LIVE WEBSITE ONLY (deploy this folder)
│   ├── index.html
│   ├── css/  js/
│   ├── images/                ← photos for web (hero, case-studies, general)
│   ├── contact/
│   ├── corporate-gifting/
│   ├── how-it-works/
│   └── case-studies/          ← GENERATED — do not edit by hand
│
├── content/
│   ├── copy/                  ← website page outlines (00–05)
│   ├── case-studies/
│   │   ├── cases.json         ← SOURCE OF TRUTH for case studies
│   │   ├── UPDATE-NOTES.md    ← raw owner notes
│   │   └── AUDIT.md           ← accuracy audit
│   └── sales/                 ← INTERNAL GTM — not deployed to website
│       ├── one-pager.html     ← print to PDF for email
│       ├── email-*.md
│       └── EMAIL-STRATEGY.md
│
├── brand/
│   └── logo-current/          ← master logo files
│
├── docs/
│   ├── SITE-ARCHITECTURE.md   ← website sitemap, nav, SEO
│   ├── DEPLOYMENT.md          ← what goes live vs stays private
│   └── gtm/
│       ├── HANDOFF.md         ← sync doc for GTM thread
│       └── 90-DAY-PLAN.md     ← go-to-market plan
│
├── scripts/
│   ├── serve.ps1              ← preview website locally
│   └── generate-case-studies.py
│
└── .cursor/                   ← informal working notes (not deployed)
```

---

## Source of truth — quick reference

| Changing… | Edit this | Then run… |
|-----------|-----------|-----------|
| Case study content | `content/case-studies/cases.json` | `python scripts/generate-case-studies.py` |
| Sales emails / PDF | `content/sales/` | Re-print PDF from `one-pager.html` |
| Website page copy | `content/copy/*.md` | Update matching `site/*.html` |
| Website design | `site/css/styles.css` | `.\scripts\serve.ps1` |
| Site structure / nav | `docs/SITE-ARCHITECTURE.md` | Build pages in `site/` |
| Logo | `brand/logo-current/` | Copy to `content/sales/` if one-pager needs it |

---

## Preview the website

```powershell
.\scripts\serve.ps1
```

Open **http://localhost:8080** · Press `Ctrl+C` to stop.

---

## Website build status

| Done | Next (Phase 2) |
|------|----------------|
| Home, Corporate Gifting, How It Works, Contact | Services hub + 4 service pages |
| All 20 case study pages (generated) | Industries hub + 2–4 industry pages |
| Shared CSS + mobile nav | About page |
| | Photos in `site/images/` |

Full plan: [`docs/SITE-ARCHITECTURE.md`](docs/SITE-ARCHITECTURE.md)

---

## GitHub backup vs live website

**The whole repo can push to GitHub for backup.**  
**Only `site/` goes live** when you connect Netlify or Cloudflare Pages.

Sales emails, one-pager, and internal notes in `content/sales/` stay in the repo but **never appear on stitchandstoneco.com** if you follow [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md).

Recommendation: use a **private** GitHub repo if sales copy should not be public.

---

## Domains

| Domain | Role |
|--------|------|
| stitchandstoneco.com | Primary (launch target) |
| stitchstoneco.com | 301 → primary |
| logoclothingshop.com | Redirect after launch |

---

## Commands

| Task | Command |
|------|---------|
| Preview site | `.\scripts\serve.ps1` |
| Regenerate case study pages | `python scripts/generate-case-studies.py` |
| Git backup | `git add .` then `git commit -m "message"` |
