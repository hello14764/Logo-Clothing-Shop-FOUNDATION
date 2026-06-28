# Project Brief — Logo Clothing Shop

**Read this file first at the start of every session. Update it at the end of every session.**

**Last updated:** Jun 27, 2026 — design rollout complete; services nav locked; push pending  
**Owner:** Joe Toma · hello@logoclothingshop.com

---

## How to use this file

### At session start (5 minutes)

1. Open this file and read **Project snapshot** + **Current focus** + **Blockers**.
2. Check **90-day week** — know which week you are in (`docs/gtm/90-DAY-PLAN.md`).
3. Tell the AI (or yourself): *"Read PROJECT-BRIEF.md and continue from Next session."*
4. Do not start new work until you know whether this session is **website**, **GTM**, or **both**.

### At session end (5–10 minutes)

1. Update **Last updated** (date + one-line summary of session).
2. Fill in **Done this session** (concrete outcomes, not intentions).
3. Replace **Next session** with 1–3 specific tasks (who/what/when if known).
4. Update any status tables that changed (website, GTM, blockers).
5. List **Files touched** so the next session knows what drifted.
6. If something important changed for all docs (new email rule, launch date, brand decision), note it under **Decisions log** and update `docs/gtm/HANDOFF.md` when you have time.

### Writing rules for every section

| Rule | Why |
|------|-----|
| **Facts only in status tables** | If it did not happen, do not mark it done |
| **Dates in US form:** Jun 29, 2026 | Matches 90-day plan |
| **No em dashes** in customer-facing copy elsewhere; OK in internal brief |
| **Replace, do not append forever** | "Next session" is overwritten each time; move completed items to "Done this session" or delete |
| **Keep Done this session to last 1–3 sessions** | Archive older bullets to **Session log** (bottom) or delete if captured in git commits |
| **Link paths, not vibes** | Write `content/sales/one-pager.html`, not "the PDF thing" |
| **Pipeline numbers live in your spreadsheet** | Brief holds summaries only (e.g. "Top 30: 12 named, 0 contacted") |

---

## Project snapshot (change rarely)

Lock these only when Joe confirms a change. Update HANDOFF + sales templates if contact/brand rules change here.

| Item | Current truth |
|------|----------------|
| **Brand live** | Logo Clothing Shop · soon Stitch & Stone Co. (bridge only) |
| **Contact everywhere** | hello@logoclothingshop.com |
| **Launch domain** | logoclothingshop.com (custom domain not connected yet) |
| **Netlify** | Deploy OK · generic `*.netlify.app` URL |
| **stitchandstoneco.com** | Not live · no redirect from logoclothingshop.com yet |
| **Google Business Profile** | Logo Clothing Shop · 280 N Old Woodward Ave |
| **Primary CTA** | Plan a Gifting Program |
| **Case studies source** | `content/case-studies/cases.json` → `npm run build` |
| **Sales assets** | `content/sales/` — never on live website |
| **Operator** | Solo; production help as needed; strong capacity |
| **Gifting tiers** | Open ($25 / $75 / $150+ per person typical) |
| **Turnaround** | ~1–2 weeks; can push ~10 days |
| **Sales method** | Active Sandler training |
| **Services (4)** | Embroidery · Screen Printing · Web Store Programs · Promotional Products |

**Deep reference (do not duplicate here):** `docs/gtm/HANDOFF.md` · `docs/SITE-ARCHITECTURE.md` · `docs/DEPLOYMENT.md`

---

## Git / GitHub (this repo)

**Commit author (locked for this repo):**

| Field | Value |
|-------|--------|
| **Name** | Joe Toma |
| **Email** | hello@logoclothingshop.com |

Set locally (already configured in `.git/config`):

```powershell
git config user.email "hello@logoclothingshop.com"
git config user.name "Joe Toma"
```

**GitHub:** Add and verify **hello@logoclothingshop.com** in GitHub → Settings → Emails so commits link to your account.

**AI / Cursor:** Do not use global `git config`. Use repo-local settings above. Never commit as `cursoragent@cursor.com` or an unverified address.

---

## Current focus

**How to update:** One sentence on what matters *this week*. Overwrite each session.

> Website design rollout done (34 pages). Push to GitHub/Netlify next. **Monday Jun 29:** 90-day plan Week 1 + Top 30 list.

**Session type today:** Website design rollout · complete

---

## 90-day plan progress

**How to update:** Set **Current week** every Monday. Copy the week's theme from `docs/gtm/90-DAY-PLAN.md`. Track metrics in your spreadsheet; summarize counts here.

| Field | Value |
|-------|--------|
| **Plan start** | Monday, **June 29, 2026** (Week 1) |
| **Plan end** | ~September 27, 2026 |
| **Current week** | Not started *(Week 1 begins Jun 29)* |
| **Week theme** | Positioning lock · Top 30 list · intro script · signature/voicemail |
| **This week's targets** | Positioning doc · Top 30 spreadsheet tab · email signature live |

### Cumulative metrics (from spreadsheet)

| Metric | Target (Wk 12) | Actual | Last updated |
|--------|----------------|--------|--------------|
| Warm touches | 60+ | 0 | — |
| Discovery calls | 15+ | 0 | — |
| Proposals sent | 8+ | 0 | — |
| Holiday programs in discussion | 3+ | 0 | — |
| Referral names collected | 20+ | 0 | — |

---

## Website status

**How to update:** Check Netlify deploy + local build. Note blockers that stop launch or paid ads.

| Item | Status |
|------|--------|
| **Pages live in repo** | 34 routes — Home, Corporate Gifting, How It Works, Contact, Services (+4), Industries (+2), Case Studies (+20), Insights |
| **Nav** | Corporate Gifting · Services ▾ · Industries ▾ · Resources ▾ · CTA |
| **Resources menu** | Case Studies · Insights |
| **Netlify** | Generic URL · rebuild on push |
| **Custom domain** | logoclothingshop.com — not connected |
| **Contact form** | Netlify Forms markup on `/contact/` — confirm in Netlify dashboard after deploy |
| **Photos** | Placeholders sitewide — swap when iPhone batch ready |
| **Reviews band** | Home placeholder — paste Google quotes later |
| **Copy voice** | Functional placeholder — human rewrite pass later |
| **Launch target** | ~2 weeks from Jun 27, 2026 |
| **Last build** | Jun 27, 2026 — pass (34 pages) |

---

## GTM / sales status

| Item | Status |
|------|--------|
| **One-pager PDF** | HTML ready · hello@ confirmed |
| **Email templates** | Ready · hello@ confirmed |
| **Top 30 list** | Starts **Monday Jun 29** |
| **HubSpot booking** | Active · in use |

---

## Blockers / waiting on

| Blocker | Owner | Notes |
|---------|-------|-------|
| Holly Q. direct quote | Joe | Ven Johnson case study |
| Logo PNG for one-pager | Joe | `content/sales/logo-clothing-shop-tall.png` |
| Custom domain DNS | Joe | Cloudflare → Netlify |
| Netlify Forms enable | Joe | After deploy — Site settings → Forms |
| iPhone photos | Joe | Templated backdrops · hero first |
| Google review text | Joe | Paste into home ReviewsBand |
| Legacy case library cleanup | Future | Archive `.cursor/Case Studies` |

---

## Decisions log

| Date | Decision |
|------|----------|
| Jun 27, 2026 | **Services (4):** Embroidery · Screen Printing · **Web Store Programs** · Promotional Products (dropped standalone Full-Color page; capability stays in production copy) |
| Jun 27, 2026 | Nav **Resources** dropdown: Case Studies + Insights |
| Jun 27, 2026 | How It Works in footer only; Contact = header CTA |
| Jun 27, 2026 | Live as Logo Clothing Shop; Stitch & Stone bridge only |
| Jun 27, 2026 | hello@logoclothingshop.com everywhere |
| Jun 27, 2026 | 90-day plan Week 1 starts **Monday, June 29, 2026** |

---

## Done this session

- Full **design rollout**: premium system on all pages, 34 routes built
- **Nav**: Services · Industries · Resources (Case Studies + Insights) dropdowns
- **New pages**: Services hub + 4 services, Industries hub + Construction + Legal/Financial, Insights placeholder
- **Home**: ReviewsBand placeholder, upgraded hero/sections
- **Contact**: premium layout + Netlify Forms markup
- **Services locked**: Embroidery · Screen Printing · Web Store Programs · Promotional Products
- Docs synced: PROJECT-BRIEF, SITE-ARCHITECTURE, 02-services-outline, Tier 1–4 from earlier today

---

## Next session

1. **Push to GitHub** — verify Netlify rebuild · click through all nav on live URL
2. **Monday Jun 29:** Week 1 — Top 30 list + positioning one-pager + email signature
3. **Connect logoclothingshop.com** when ready (Cloudflare → Netlify)
4. **Photos** when batch ready — hero slot first (same aspect ratios as placeholders)

---

## Files touched (recent)

```
src/lib/site.ts
src/components/* (Header, Footer, HomeHero, ReviewsBand, ImagePlaceholder, …)
src/pages/** (all routes)
docs/PROJECT-BRIEF.md
docs/SITE-ARCHITECTURE.md
content/copy/02-services-outline.md
(+ earlier: docs/gtm/*, content/sales/*, DEPLOYMENT.md)
```

---

## Session log (archive)

### Jun 27, 2026 (session 2)
- Design rollout · 34 pages · Resources nav · Web Store Programs service

### Jun 27, 2026 (session 1)
- Doc sync · PROJECT-BRIEF · Netlify deploy · local dev fix

---

## Quick links

| Doc | Use |
|-----|-----|
| [`docs/gtm/90-DAY-PLAN.md`](gtm/90-DAY-PLAN.md) | Weekly actions |
| [`docs/gtm/HANDOFF.md`](gtm/HANDOFF.md) | GTM + case study rules |
| [`docs/SITE-ARCHITECTURE.md`](SITE-ARCHITECTURE.md) | Sitemap + SEO |
| [`docs/DEPLOYMENT.md`](DEPLOYMENT.md) | What goes live |
| [`content/case-studies/cases.json`](../content/case-studies/cases.json) | Case study edits |
| [`content/sales/one-pager.html`](../content/sales/one-pager.html) | Print PDF |
