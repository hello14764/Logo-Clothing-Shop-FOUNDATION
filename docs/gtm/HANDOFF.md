# Handoff for Go-To-Market thread

**Last updated:** Jun 27, 2026  
**Purpose:** Sync the GTM/sales Cursor thread with work done in the website thread. Read this before editing sales or case study content.

**Session brief:** [`docs/PROJECT-BRIEF.md`](../PROJECT-BRIEF.md) — **read first and update last every session**

---

## Current status (Jun 2026)

| Area | Status |
|------|--------|
| **Brand live** | Logo Clothing Shop · soon Stitch & Stone Co. (bridge only) |
| **Contact everywhere** | hello@logoclothingshop.com (monitored daily) |
| **Website** | Astro Phase 1 built; Netlify deploy live (generic URL); custom domain **logoclothingshop.com** next (~2-week launch target) |
| **stitchandstoneco.com** | Not live yet |
| **90-day plan** | Starts **Monday, June 29, 2026** (Week 1) |
| **Top 30 list** | Starts **Monday, June 29, 2026** (Week 1, Day 1) |
| **Workstreams** | Website + GTM **in parallel** (not paused) |

---

## Where YOU work (GTM thread)

| Folder / file | Your job |
|---------------|----------|
| `content/sales/` | Emails, one-pager PDF, EMAIL-STRATEGY.md |
| `content/case-studies/cases.json` | Add/update case study **stories** |
| `content/case-studies/UPDATE-NOTES.md` | Raw notes from calls / owner input |
| `docs/gtm/90-DAY-PLAN.md` | Outbound, referrals, holiday campaign |

## Where you do NOT work (website thread)

| Folder | Why |
|--------|-----|
| `src/**` | Astro website source — website thread |
| `public/**` | Static assets for live site |
| `content/copy/` | Website page outlines |
| `site/**` | **Deprecated** static prototype — do not edit |

**After you edit `cases.json`:** run `npm run build` locally or push to GitHub for Netlify to rebuild. Astro generates case study pages from JSON at build time.

---

## What changed recently (sales assets audit)

### Case studies corrected (was wrong in emails/PDF)

| Story | Old (wrong) | Now (correct) |
|-------|-------------|---------------|
| **Karmanos** | $100K donors, Tommy Hearns | ~25 gloves, staff-signed, gifted to **cancer survivors** (2024) |
| **Ven Johnson** | Generic event swag | **Nats at the Zoo**, Kalamazoo, July. **800+** pieces. **Holly Q.**, Marketing Director |
| **Orfin** | Vague blankets | **~80 blankets in 10 days**, 4imprint couldn't. **Laura D.** Gifting catalog + shortbread. "You're my guy." |
| **Weldaloy** | Was missing from sales | **300 solar chargers** → Norm F. quotes → **500 cable kits to France** |
| **Awecomm** | Dropped briefly | Re-added to `cases.json`. Holiday Gifting Made Easy program |

### Do NOT publish

- Ven Johnson: incumbent vendor / holiday win-back angle
- Thornton & Grooms: 10,000-client gifting as **completed** (pipeline only — in talks)
- Karmanos: Tommy Hearns / mega-donor framing

### Sales voice rules (locked)

- **Sandler:** pain first, permission to say no, mutual qualification, soft CTA
- **Human tone:** like talking into the mic — not brochure copy
- **No em dashes** in customer-facing copy
- **Send FROM:** hello@logoclothingshop.com (not stitchandstoneco.com yet)
- **Stitch and Stone:** one subtle intro line only until launch

### One-pager PDF (print from HTML)

- File: `content/sales/one-pager.html`
- Featured stories: **Weldaloy, Orfin, Ven Johnson**
- Logo Clothing Shop prominent; Stitch and Stone as small bridge line
- Contact: Joe Toma, Business Development Director, Birmingham address, office + cell, HubSpot booking link
- Email: **hello@logoclothingshop.com**

### Email templates

| File | Audience |
|------|----------|
| `email-gifting-general.md` | Marketing / HR — leads with Weldaloy + Orfin |
| `email-legal-financial.md` | Law / finance — Ven Johnson + Orfin |
| `email-construction-trades.md` | Trades — Northstar + Thornton (Karen B. quote) |

Strategy doc: `content/sales/EMAIL-STRATEGY.md`

---

## Source of truth for case studies

```
content/case-studies/cases.json   ← EDIT HERE
         ↓
npm run build   (or Netlify rebuild on push)
         ↓
dist/case-studies/*.html          ← live site output (do not edit by hand)
```

**Deprecated:** `scripts/generate-case-studies.py` and legacy `site/case-studies/*.html` — do not use.

Also see: `content/case-studies/AUDIT.md`, `UPDATE-NOTES.md`

---

## Still needed from owner

- [x] Logo Clothing Shop send email — **hello@logoclothingshop.com**
- [ ] Holly Q. direct quote (Ven Johnson)
- [ ] Second Awecomm-network holiday company (name + story)
- [ ] Photos (deferred)
- [ ] Legacy case library archive (`.cursor/Case Studies`) — preserve before cleanup

---

## GitHub + website — won't jumble

- **GitHub backup** = whole repo (use **private** repo for sales privacy)
- **Live website** = **`dist/`** from Astro (`npm run build`) — Netlify publishes this
- **Sales never deploys** — `content/sales/` stays internal even though it's in the repo

See `docs/DEPLOYMENT.md`. Your emails and one-pager do not appear on logoclothingshop.com.

---

## If you're unsure where to put something

| Content type | Put it here |
|--------------|-------------|
| New case study story | `UPDATE-NOTES.md` then `cases.json` |
| Email script | `content/sales/` |
| Website homepage copy | Tell website thread → `content/copy/` or `src/pages/` |
| Photo for email/PDF | Your local machine or Drive — not required in repo |
| Photo for live site | `public/images/` (website thread) |
