# Stitch & Stone Co. — Site Architecture Plan

**Domain:** stitchandstoneco.com (primary) · stitchstoneco.com (redirect)  
**Launch phase:** Build in repo → preview deploy → go live → redirect logoclothingshop.com  
**Positioning:** Corporate gifting first · In-house production as proof

---

## Brand hierarchy (how offerings relate)

```
CORPORATE GIFTING          ← Lead with this (homepage, nav, CTAs, SEO priority)
    │
    ├── Curation & consulting (packages, occasions, ship-to-home)
    └── Powered by in-house production ↓

PRODUCTION & PROMO         ← Credibility + existing promo clients
    ├── Embroidery
    ├── Screen printing
    ├── Full-color decoration
    └── Promotional products · "Your partner in promo"
```

**Rule:** Gifting is the *why*. Services are the *how*. Never bury gifting under a generic "Services" dropdown as item #4.

---

## Primary navigation (header)

| Item | Type | URL | Notes |
|------|------|-----|-------|
| **Corporate Gifting** | Link | `/corporate-gifting/` | Standalone top-level — not nested |
| **Services** | Dropdown | `/services/` | Production & promo hub |
| ↳ Embroidery | Link | `/services/embroidery/` | |
| ↳ Screen Printing | Link | `/services/screen-printing/` | |
| ↳ Full-Color Decoration | Link | `/services/full-color-decoration/` | |
| ↳ Promotional Products | Link | `/services/promotional-products/` | "Partner in promo" lives here |
| **Industries** | Dropdown | `/industries/` | SEO hub + proof you get their world |
| ↳ Construction | Link | `/industries/construction/` | Launch priority |
| ↳ Legal & Financial | Link | `/industries/legal-financial/` | Launch priority |
| ↳ Technology & Science | Link | `/industries/technology-science/` | Detroit growth angle |
| ↳ Professional Services | Link | `/industries/professional-services/` | Insurance, etc. |
| **Case Studies** | Link | `/case-studies/` | |
| **About** | Link | `/about/` | Story, Michigan, Logo Clothing Shop bridge |
| **Insights** | Link | `/insights/` | Blog (premium label; URL can stay `/insights/`) |
| **[Plan a Gifting Program]** | CTA button | `/contact/` | Always visible — primary conversion |

**Mobile:** Same items in hamburger. CTA button sticky or at top of menu.

**Footer nav:** Repeat primary links + Privacy + (later) Careers. Tagline: *Known to many clients as Logo Clothing Shop.*

---

## Full sitemap

### Launch (v1 — go live)

| Page | URL | Priority |
|------|-----|----------|
| Home | `/` | P0 |
| Corporate Gifting | `/corporate-gifting/` | P0 |
| How It Works | `/how-it-works/` | P0 |
| Contact / Start a Project | `/contact/` | P0 |
| Services overview | `/services/` | P1 |
| Embroidery | `/services/embroidery/` | P1 |
| Screen Printing | `/services/screen-printing/` | P1 |
| Full-Color Decoration | `/services/full-color-decoration/` | P1 |
| Promotional Products | `/services/promotional-products/` | P1 |
| Industries hub | `/industries/` | P1 |
| Construction | `/industries/construction/` | P1 |
| Legal & Financial | `/industries/legal-financial/` | P1 |
| Case Studies index | `/case-studies/` | P1 |
| 2–3 case study pages | `/case-studies/[slug]/` | P1 |
| About | `/about/` | P1 |

### Phase 2 (within 60 days of launch)

| Page | URL |
|------|-----|
| Technology & Science | `/industries/technology-science/` |
| Professional Services | `/industries/professional-services/` |
| More case studies | `/case-studies/[slug]/` |
| Insights index | `/insights/` |
| 3–5 pillar blog posts | `/insights/[slug]/` |

### Phase 3 (ongoing)

| Page | URL |
|------|-----|
| Gifting sub-pages (optional) | `/corporate-gifting/holiday-programs/` etc. |
| FAQ | `/faq/` |
| 404 + thank-you pages | `/thank-you/` |

---

## Homepage wireframe (section order)

Gifting-first. Production supports trust — does not lead.

1. **Hero**
   - Headline: corporate gifting outcome
   - Subhead: curated programs · in-house embroidery & screen print · Michigan
   - Primary CTA: *Plan a Gifting Program*
   - Secondary CTA: *See how it works*
   - Visual: real package / unboxing (or thread motif placeholder until photos ready)

2. **Trust strip**
   - Client logos OR "Trusted by teams across construction, legal, and finance"
   - Optional: years in business, in-house production badge

3. **The problem → your answer** (short)
   - "Marketing teams don't need another catalog — they need a partner who curates, produces, and delivers."

4. **Gifting programs** (3 cards)
   - Employee appreciation & milestones
   - Client & referral gifting
   - Holiday & ship-to-home programs
   - Each links to `/corporate-gifting/` anchors or sections

5. **How it works** (4 steps)
   - Discover → Curate → Produce → Deliver
   - Link to `/how-it-works/`

6. **Featured case study**
   - One strong story (construction or legal)
   - Link to `/case-studies/`

7. **Industries teaser**
   - 3–4 tiles linking to industry pages

8. **Production credibility** (secondary band — stone palette, quieter)
   - "Every gift is backed by in-house decoration."
   - Icons: Embroidery · Screen print · Full color · Promo
   - CTA: *Explore our capabilities* → `/services/`
   - **Not** "Your partner in promo" here — that phrase lives on Services

9. **Consultative difference**
   - Deep discovery, curated packages, one point of contact

10. **Final CTA**
    - *Start a project* / *Book a curation call*

11. **Footer**

---

## Page purposes (one sentence each)

| Page | Job |
|------|-----|
| **Corporate Gifting** | Convert gifting buyers — occasions, packages, timelines, what's included |
| **How It Works** | Reduce friction — process, lead times, what you need from them |
| **Services** | Prove you're not a reseller; capture promo/production searches |
| **Service child pages** | Rank for "embroidery Detroit" etc.; link back to gifting |
| **Industries** | SEO + relevance — "they understand our world" |
| **Industry child pages** | Long-tail: "corporate gifting construction Michigan" |
| **Case Studies** | Proof — real outcomes, photos, quotes |
| **About** | Human trust, Michigan roots, rebrand bridge |
| **Insights** | SEO content engine + authority |
| **Contact** | Convert — form, phone; CTA label: Plan a Gifting Program |

---

## Gifting vs Services — copy rules

| Topic | Corporate Gifting page | Services pages |
|-------|------------------------|----------------|
| Tone | Strategic, warm, program-focused | Capable, precise, craft-focused |
| Buyer | Marketing / HR coordinator | Marketing + ops + existing promo buyers |
| CTA | Plan a Gifting Program | Talk about a project |
| "Partner in promo" | Mention once as breadth | Headline theme on `/services/promotional-products/` |
| Linking | Services → "See how we produce your gifts" | Every service page → banner: "Building a gifting program? Start here →" |

---

## SEO strategy (simple, actionable)

### Priority keywords (one primary page each)

| Target | Primary page |
|--------|--------------|
| corporate gifting Michigan / Detroit | `/corporate-gifting/` + Home |
| curated employee appreciation gifts | `/corporate-gifting/` |
| embroidery [city/region] | `/services/embroidery/` |
| screen printing [region] | `/services/screen-printing/` |
| promotional products partner | `/services/promotional-products/` |
| construction corporate gifts | `/industries/construction/` |
| law firm client gifts | `/industries/legal-financial/` |

### Industries — **yes, include them**

- One hub + one page per vertical = Google entry points
- Each industry page: pain points, gifting occasions, 1 case study link, CTA
- Do **not** launch 10 empty industry pages — start with 2–3 strong ones

### Blog (Insights) — **yes, but not empty on launch**

- Rename nav to **Insights** (fits premium brand; folder `/insights/`)
- Launch blog index only when you have **3 posts minimum**
- Pillar topics first:
  1. Corporate gifting guide for marketing teams
  2. Construction crew appreciation / milestone gifting
  3. Client thank-you gifts for law & finance (understated, premium)

### Case studies — **yes, high priority**

- Template: Client type · Challenge · Approach · Items · Result · quote
- Tag by industry for cross-linking
- Even anonymized ("Regional construction firm") beats no proof

### Technical SEO (when building)

- One `<h1>` per page
- Title pattern: `{Page} | Stitch & Stone Co. · Michigan`
- Meta descriptions unique per page
- Internal links: industry ↔ case study ↔ gifting
- Local: address/service area in footer; Google Business aligned at launch
- Fast static HTML; real alt text on photos

---

## URL & file structure (repo)

```
site/
├── index.html
├── corporate-gifting/
├── how-it-works/
├── contact/
├── services/
│   ├── index.html
│   ├── embroidery/
│   ├── screen-printing/
│   ├── full-color-decoration/
│   └── promotional-products/
├── industries/
│   ├── index.html
│   ├── construction/
│   ├── legal-financial/
│   └── ...
├── case-studies/
│   ├── index.html
│   └── [slug]/
├── insights/
│   ├── index.html
│   └── [slug]/
├── about/
├── css/
│   └── styles.css
├── js/                    # minimal only if needed
└── images/

content/
├── copy/                  # Markdown source for every page
├── case-studies/
└── insights/

brand/
├── colors.md
├── fonts.md
└── logo-stitch-stone/
```

---

## Build phases

| Phase | Pages | Goal |
|-------|-------|------|
| **1 — Foundation** | Home, Corporate Gifting, How It Works, Contact + shared CSS | Preview deploy |
| **2 — Trust** | Services (all), Industries (2), Case Studies (2–3), About | Go live ready |
| **3 — Growth** | Insights (3 posts), more industries, more case studies | SEO momentum |

---

## Design notes (for build)

- Thread motif: section dividers only — not full-page parallax
- Gifting sections: warmer, more whitespace, lifestyle/package photography
- Services sections: stone palette, process/detail shots
- One accent color (thread): copper or deep teal — pick one before CSS tokens

---

## Decisions locked

- [x] Primary CTA label: **Plan a Gifting Program**
- [x] Insights vs Blog in nav: **Insights**

## Open decisions

- [x] Phone number + service area copy for footer
- [ ] 2–3 case studies to write first (industry + rough story)
