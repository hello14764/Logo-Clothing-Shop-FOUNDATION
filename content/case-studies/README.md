# Case Studies — How to Add Content

## STOP — read this first

### **`site/case-studies/*.html` is GENERATED. Do not edit by hand.**

1. Edit **`cases.json`** in this folder  
2. Run: `python scripts/generate-case-studies.py`  
3. Any hand-edits to HTML **will be overwritten** on the next run  

**Source of truth:** `content/case-studies/cases.json`  
**Website output:** `site/case-studies/`  
**GTM thread notes:** `UPDATE-NOTES.md`, `AUDIT.md`, `docs/gtm/HANDOFF.md`

---

## Best way to add or update stories

### Option A — Paste in chat (GTM or website thread)
Copy/paste each case study as plain text. Owner notes go in `UPDATE-NOTES.md`.

### Option B — Edit `cases.json` (required for website)
All live case study pages are generated from:

`content/case-studies/cases.json`

After editing, run:

```powershell
python scripts/generate-case-studies.py
```

### Option C — Google Doc / Notion
Export **text only**. Keep PDFs in Drive, not Git.

---

## What goes in the repo (lightweight)

| Asset | Where | Size guidance |
|-------|--------|----------------|
| Story data | `cases.json` | Kilobytes |
| Web photos | `site/images/case-studies/` | Under 200 KB each, compressed |
| PDF archive | Google Drive / OneDrive | **Not** in Git |
| Sales one-pager | `content/sales/` | **Not deployed to website** |

### Photo tips
- Export JPG at ~1600px wide max
- Use [Squoosh](https://squoosh.app) before adding
- 3–6 images per case study is enough

---

## Files in this folder

| File | Purpose |
|------|---------|
| `cases.json` | **Source of truth** for all case study pages |
| `UPDATE-NOTES.md` | Raw owner interview notes |
| `AUDIT.md` | Accuracy audit vs sales assets |
| `index.md` | Slug index |
| `README.md` | This file |

---

## Template for new entries in `cases.json`

See existing entries for structure. Required fields: `slug`, `title`, `category`, `group`, `summary`, `client`, `goal`, `challenge`, `solution`, `result`, `takeaway`.

Optional: `quote`, `featured`, `card_teaser`, `note`, `pipeline_note`
