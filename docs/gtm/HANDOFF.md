# Handoff for Go-To-Market thread

**Last updated:** Jun 2026  
**Purpose:** Sync the GTM/sales Cursor thread with work done in the website thread. Read this before editing sales or case study content.

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
| `site/*.html` | Built/maintained in website thread |
| `site/css/` | Design tokens, layout |
| `content/copy/` | Website page outlines |

**Exception:** After you edit `cases.json`, run `python scripts/generate-case-studies.py` (or ask website thread) to refresh `site/case-studies/`.

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
- **Send FROM:** Logo Clothing Shop email (not stitchandstoneco.com yet)
- **Stitch and Stone:** one subtle intro line only until launch

### One-pager PDF (print from HTML)

- File: `content/sales/one-pager.html`
- Featured stories: **Weldaloy, Orfin, Ven Johnson**
- Logo Clothing Shop prominent; Stitch and Stone as small bridge line
- Contact: Joe Toma, Business Development Director, Birmingham address, office + cell, HubSpot booking link
- Replace `[your Logo Clothing Shop email]` before sending

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
python scripts/generate-case-studies.py
         ↓
site/case-studies/*.html          ← DO NOT EDIT BY HAND
```

Also see: `content/case-studies/AUDIT.md`, `UPDATE-NOTES.md`

---

## Still needed from owner

- [ ] Logo Clothing Shop send email address (for PDF + signatures)
- [ ] Holly Q. direct quote (Ven Johnson)
- [ ] Second Awecomm-network holiday company (name + story)
- [ ] Photos (deferred)

---

## GitHub + website — won't jumble

- **GitHub backup** = whole repo (use **private** repo for sales privacy)
- **Live website** = **`site/` folder only** — sales never deploys

See `docs/DEPLOYMENT.md`. Your emails and one-pager stay in `content/sales/` and do not appear on stitchandstoneco.com.

---

## If you're unsure where to put something

| Content type | Put it here |
|--------------|-------------|
| New case study story | `UPDATE-NOTES.md` then `cases.json` |
| Email script | `content/sales/` |
| Website homepage copy | Tell website thread → `content/copy/` |
| Photo for email/PDF | Your local machine or Drive — not required in repo |
| Photo for live site | `site/images/` (website thread) |
