# Case Study Audit (Jun 2026)

**Source of truth:** `content/case-studies/cases.json` + `UPDATE-NOTES.md`  
**Compared against:** one-pager, emails, Astro site (`dist/` from `npm run build`)

---

## Critical fixes (done or in progress)

| Issue | Was wrong | Correct |
|-------|-----------|---------|
| **Karmanos** | $100K donors, Tommy Hearns signing | ~25 gloves, **staff-signed**, gifted to **cancer survivors** (2024). Fundraiser committee invite. |
| **Ven Johnson** | Generic "event swag" | **Nats at the Zoo** (Kalamazoo, July). ~800+ hoodies/tees/hats. **Holly Q.**, Marketing Director. Sold out. |
| **Orfin** | Vague blankets story | **~80 blankets in 10 days** when 4imprint couldn't. **Laura D.** Gifting catalog + holiday shortbread. Quote: "You're my guy..." |
| **Weldaloy** | Missing from sales assets | **300 solar chargers** to all clients; **500 cable kits to France**. **Norm F.** quotes. **Add to one-pager.** |
| **Awecomm** | On one-pager/site but **removed from cases.json** | Re-added to JSON. Holiday Gifting Made Easy program still valid. |
| **Live website** | Legacy `site/` HTML was stale | Astro builds from `cases.json` — run `npm run build` after JSON edits |

---

## Do NOT publish (owner confirmed)

- Ven Johnson: incumbent vendor / holiday win-back angle
- Thornton & Grooms: **10,000-client gifting program** as completed (pipeline only — in talks)
- Karmanos: Tommy Hearns / mega-donor framing

---

## Missing from cases.json (consider adding)

| Story | In original library? | Priority |
|-------|---------------------|----------|
| **Awecomm AI Conference** | Yes | **In JSON** — featured |
| USA-Made prospect (Scott) | Yes | Low — sales story, not client |
| Second Awecomm-network holiday company | Owner noted pending | High when name available |

---

## Strongest stories by audience (for emails / one-pager)

| Audience | Lead with | Second | Third |
|----------|-----------|--------|-------|
| **Gifting / marketing** | Weldaloy (Norm quotes) | Orfin (10-day save) | Awecomm (holiday program) |
| **Legal / financial** | Ven Johnson (Nats at the Zoo) | Orfin (Laura D.) | — |
| **Construction / trades** | Northstar (durability) | Thornton (webstore, Karen B. quote) | — |
| **Manufacturing / tech** | Weldaloy | Averna (DNA embroidery) | — |
| **Nonprofit** | Karmanos (survivor gloves) | Sparrow (5-day rescue) | — |

---

## Still needed from owner

- [ ] Holly Q. direct quote (Ven Johnson)
- [x] Logo Clothing Shop send email — **hello@logoclothingshop.com**
- [ ] Second Awecomm-network company name + story
- [ ] Photos (deferred)
- [ ] Permission to name 4imprint in Orfin story (currently OK in JSON)

---

## Asset sync checklist

- [x] Audit document
- [x] `cases.json` includes Awecomm
- [x] One-pager updated (Weldaloy, Orfin, Ven Johnson)
- [x] Emails updated with accurate stories
- [x] Website built from JSON via Astro (`npm run build`)
- [x] Homepage featured story updated
