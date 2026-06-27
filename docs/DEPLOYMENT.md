# Deployment — what goes live vs what stays internal

## Rule

| Location | On stitchandstoneco.com? | In GitHub backup? |
|----------|--------------------------|-------------------|
| `site/` | **YES** — this is the entire public website | Yes |
| `content/sales/` | **NO** — emails, one-pager, strategy | Yes (recommended: private repo) |
| `content/case-studies/` (JSON, notes) | **NO** — source data only | Yes |
| `content/copy/` | **NO** — drafting outlines | Yes |
| `docs/` | **NO** | Yes |
| `.cursor/` | **NO** | Optional (working notes) |

**Sales PDFs you email to clients are never part of the website** as long as publish directory is `site/` only.

---

## Netlify / Cloudflare Pages setup

When you connect GitHub:

| Setting | Value |
|---------|-------|
| **Publish directory** | `site` |
| **Build command** | *(leave empty for static HTML)* |

Optional: run case study generator before deploy if you add a build step later:

```
python scripts/generate-case-studies.py
```

For now, commit generated HTML in `site/case-studies/` after JSON changes.

---

## GitHub repo visibility

| Repo type | Who sees sales emails & one-pager |
|-----------|-----------------------------------|
| **Private** | Only you / collaborators |
| **Public** | Anyone on GitHub (still NOT on your website) |

**Recommendation:** Private GitHub repo. Website is public via Netlify; repo stays backup + collaboration.

---

## What NOT to put in `site/`

- Sales email templates
- Printable one-pager HTML
- Internal case study notes (`UPDATE-NOTES.md`, `AUDIT.md`)
- GTM plans

Keep those in `content/sales/` and `docs/gtm/`.

---

## PDF files

Do not commit large PDF exports to Git if you can avoid it. Generate fresh from `content/sales/one-pager.html` when needed.

If you save PDFs locally, add to `.gitignore` (already configured for `*.pdf` in sales folder).

---

## Launch checklist

1. Connect repo to Netlify/Cloudflare — publish dir = `site`
2. Point stitchandstoneco.com DNS to host
3. Verify `content/sales/` URLs are not reachable on live domain
4. Later: 301 logoclothingshop.com → new site
