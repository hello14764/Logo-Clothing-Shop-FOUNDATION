#!/usr/bin/env python3
"""DEPRECATED — Do not use.

Live case study pages are built by Astro from content/case-studies/cases.json.
Run: npm run build

This script only generated legacy HTML into site/case-studies/ (deprecated prototype).
"""

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES_FILE = ROOT / "content" / "case-studies" / "cases.json"
OUT_DIR = ROOT / "site" / "case-studies"


def site_header(root, css, js):
    img = f"{root}images/general/logo-clothing-shop.svg"
    return f"""  <header class="site-header">
    <div class="container header-inner">
      <div class="logo-wrap">
        <a href="{root}" class="logo-lockup">
          <img src="{img}" alt="Logo Clothing Shop" class="logo-img" width="200" height="60">
        </a>
        <span class="logo-bridge">Becoming Stitch &amp; Stone Co.</span>
      </div>
      <button class="nav-toggle" aria-expanded="false" aria-controls="main-nav" aria-label="Toggle navigation">
        <span></span><span></span><span></span>
      </button>
      <nav id="main-nav" class="main-nav" aria-label="Main">
        <ul>
          <li><a href="{root}corporate-gifting/">Corporate Gifting</a></li>
          <li><a href="{root}how-it-works/">How It Works</a></li>
          <li><a href="{root}case-studies/">Case Studies</a></li>
        </ul>
        <div class="nav-cta">
          <a href="{root}contact/" class="btn btn-primary">Plan a Gifting Program</a>
        </div>
      </nav>
      <a href="{root}contact/" class="btn btn-primary header-cta-desktop">Plan a Gifting Program</a>
    </div>
  </header>"""


def site_footer(root):
    img = f"{root}images/general/logo-clothing-shop.svg"
    return f"""  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a href="{root}" class="logo-lockup">
            <img src="{img}" alt="Logo Clothing Shop" class="logo-img" width="200" height="60">
          </a>
          <p>Corporate gifting and in-house decoration. Birmingham, Michigan.</p>
          <p>
            <a href="mailto:hello@logoclothingshop.com">hello@logoclothingshop.com</a><br>
            <a href="tel:+12483828182">(248) 382-8182</a> office<br>
            <a href="tel:+12484709926">(248) 470-9926</a> cell
          </p>
          <p class="footer-bridge">Introducing Stitch &amp; Stone Co., our next chapter. Same team, same craft.</p>
        </div>
        <nav class="footer-nav" aria-label="Footer">
          <h4>Explore</h4>
          <ul>
            <li><a href="{root}corporate-gifting/">Corporate Gifting</a></li>
            <li><a href="{root}how-it-works/">How It Works</a></li>
            <li><a href="{root}case-studies/">Case Studies</a></li>
          </ul>
        </nav>
        <nav class="footer-nav">
          <h4>Get started</h4>
          <ul>
            <li><a href="{root}contact/">Plan a Gifting Program</a></li>
            <li><a href="https://meetings.hubspot.com/joe-toma/introductory-call">Book a call</a></li>
          </ul>
        </nav>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Logo Clothing Shop. All rights reserved.</p>
      </div>
    </div>
  </footer>"""


CASE_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Case Study | Logo Clothing Shop</title>
  <meta name="description" content="{meta}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css}">
</head>
<body>
{header}
  <main>
    <section class="page-hero">
      <div class="container">
        <p class="case-tag">{category}</p>
        <h1>{title}</h1>
        <p class="lead">{summary}</p>
      </div>
    </section>
    <section class="section">
      <div class="container prose-wide">
{body}
      </div>
    </section>
    <section class="section section-dark cta-band">
      <div class="container">
        <h2>Ready to plan your next program?</h2>
        <p>Let's talk about what you're building, gifting, apparel, or both.</p>
        <a href="{root}contact/" class="btn btn-inverse">Plan a Gifting Program</a>
      </div>
    </section>
  </main>
{footer}
  <script src="{js}"></script>
</body>
</html>"""


def section(title, text):
    if isinstance(text, list):
        items = "\n".join(f"        <li>{t}</li>" for t in text)
        inner = f"        <ul>\n{items}\n        </ul>"
    else:
        inner = f"        <p>{text}</p>"
    return f'        <div class="case-section">\n          <h2>{title}</h2>\n{inner}\n        </div>'


def build_body(case):
    parts = [
        section("Client", case["client"]),
        section("Goal", case["goal"]),
        section("Challenge", case["challenge"]),
        section("Solution", case["solution"]),
        section("Result", case["result"]),
    ]
    q = case.get("quote")
    if q and q.get("text"):
        quote_html = f'        <blockquote><p>&ldquo;{q["text"]}&rdquo;</p><p class="text-muted">{q["name"]}, {q["title"]}</p></blockquote>'
        parts.append(f'        <div class="case-section">\n          <h2>In their words</h2>\n{quote_html}\n        </div>')
    parts.append(section("Key takeaway", case["takeaway"]))
    if case.get("note"):
        parts.append(f'        <p class="text-muted" style="font-size:0.875rem;margin-top:1.5rem;">Note: {case["note"]}</p>')
    return "\n".join(parts)


def main():
    cases = json.loads(CASES_FILE.read_text(encoding="utf-8"))
    for case in cases:
        slug = case["slug"]
        depth = slug.count("/")  # always flat
        css = "../../css/styles.css"
        js = "../../js/nav.js"
        root = "../../"
        body = build_body(case)
        html = CASE_PAGE.format(
            title=case["title"],
            meta=case["summary"][:155],
            css=css,
            js=js,
            root=root,
            header=site_header(root, css, js),
            footer=site_footer(root),
            category=case["category"],
            summary=case["summary"],
            body=body,
        )
        out = OUT_DIR / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"Wrote {out}")

    # Index page
    index_cases = cases
    featured = [c for c in cases if c.get("featured")]
    categories = {}
    for c in cases:
        categories.setdefault(c["group"], []).append(c)

    cards_featured = "\n".join(
        f'''          <article class="card">
            <p class="case-tag">{c["category"]}</p>
            <h3><a href="{c["slug"]}/" style="text-decoration:none;color:inherit;">{c["title"]}</a></h3>
            <p class="text-muted">{c["summary"]}</p>
            <a href="{c["slug"]}/" class="card-link">Read case study</a>
          </article>'''
        for c in featured
    )

    category_blocks = []
    for group, items in categories.items():
        cards = "\n".join(
            f'''          <article class="card">
            <p class="case-tag">{c["category"]}</p>
            <h3><a href="{c["slug"]}/" style="text-decoration:none;color:inherit;">{c["title"]}</a></h3>
            <p class="text-muted">{c["card_teaser"]}</p>
            <a href="{c["slug"]}/" class="card-link">Read case study</a>
          </article>'''
            for c in items
        )
        category_blocks.append(
            f'        <h2 class="category-label">{group}</h2>\n        <div class="card-grid card-grid-3">\n{cards}\n        </div>'
        )

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Case Studies | Logo Clothing Shop</title>
  <meta name="description" content="Case studies in corporate gifting, embroidery, and branded apparel. Michigan companies trust Logo Clothing Shop.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/styles.css">
</head>
<body>
{site_header("../", "../css/styles.css", "../js/nav.js")}
  <main>
    <section class="page-hero">
      <div class="container">
        <h1>Case studies</h1>
        <p class="lead">Curated gifting, precision embroidery, and branded programs. Real work for Michigan organizations.</p>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="section-header">
          <h2>Featured</h2>
          <p class="text-muted">Gifting, law, nonprofit, and trades. A sample of how we partner with clients.</p>
        </div>
        <div class="case-grid-featured">
{cards_featured}
        </div>
      </div>
    </section>
    <section class="section section-alt">
      <div class="container">
{chr(10).join(category_blocks)}
      </div>
    </section>
    <section class="section section-dark cta-band">
      <div class="container">
        <h2>Your story could be next</h2>
        <p>Tell us about your team, event, or gifting program.</p>
        <a href="../contact/" class="btn btn-inverse">Plan a Gifting Program</a>
      </div>
    </section>
  </main>
{site_footer("../")}
  <script src="../js/nav.js"></script>
</body>
</html>"""

    (OUT_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print(f"Wrote {OUT_DIR / 'index.html'}")


if __name__ == "__main__":
    main()
