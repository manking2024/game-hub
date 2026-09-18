#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_site.py — Generate the GameHub static site from data/games.json (zero third-party deps).

Usage:
    python tools/gen_site.py

Output (written to repo root, which is the GitHub Pages publish root):
    index.html         Home: hero + category sections + game cards
    games/<slug>.html  One page per game (Article + FAQPage schema / iframe / original content / related games)
    sitemap.xml        All URLs (for Google Search Console)
    robots.txt         Allow all + sitemap pointer

Workflow:
    1. Produce content with the geo-content-optimizer skill -> fill data/games.json
    2. Run this script -> regenerate every page
    3. git push -> GitHub Pages auto-publishes
"""
import datetime
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "games.json")


def esc(value):
    """HTML-escape titles/bodies so quotes and angle brackets never break the page."""
    return html.escape(str(value), quote=True)


def load():
    with open(DATA, "r", encoding="utf-8-sig") as f:
        return json.load(f)


def slugify(title_en):
    """Turn an English title into a URL slug."""
    s = re.sub(r"[^a-z0-9]+", "-", title_en.lower()).strip("-")
    return s or "game"


# ---------- Schema ----------

def schema_article(game, site):
    url = f"{site['domain']}/games/{game['slug']}.html"
    date = game.get("date", datetime.date.today().isoformat())
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": f"{game['title']} — Play Online Free",
        "description": game.get("description", game.get("summary", "")),
        "url": url,
        "datePublished": date,
        "dateModified": date,
        "inLanguage": "en-US",
    }


def schema_faq(game):
    faqs = game.get("faq", [])
    if not faqs:
        return None
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": f["q"],
             "acceptedAnswer": {"@type": "Answer", "text": f["a"]}}
            for f in faqs
        ],
    }


# ---------- Page rendering ----------

def related_games(game, all_games, n=3):
    """Prefer same category, then fill with others; never include self."""
    same = [g for g in all_games if g["category"] == game["category"] and g["slug"] != game["slug"]]
    others = [g for g in all_games if g["category"] != game["category"] and g["slug"] != game["slug"]]
    return (same + others)[:n]


def render_game_page(game, site, all_games):
    title = f"{game['title']} — Play Online Free"
    canon = f"{site['domain']}/games/{game['slug']}.html"
    blocks = [schema_article(game, site)]
    faq_schema = schema_faq(game)
    if faq_schema:
        blocks.append(faq_schema)
    jsonld = "\n".join(
        f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>'
        for b in blocks
    )

    sections = "\n".join(
        f"<section class=\"content-block\">\n<h2>{esc(s['h2'])}</h2>\n<p>{esc(s['body'])}</p>\n</section>"
        for s in game.get("sections", [])
    )

    faq_html = ""
    if game.get("faq"):
        items = "\n".join(
            f"<li class=\"faq-item\"><h3>{esc(f['q'])}</h3><p>{esc(f['a'])}</p></li>"
            for f in game["faq"]
        )
        faq_html = (
            "<section class=\"content-block\">\n"
            "<h2>Frequently Asked Questions</h2>\n"
            f"<ul class=\"faq-list\">{items}</ul>\n</section>"
        )

    rel = related_games(game, all_games)
    rel_html = ""
    if rel:
        cards = "\n".join(
            f'<a class="card" href="games/{g["slug"]}.html">'
            f'<span class="card-tag tag-{esc(g["category"])}">{esc(g["category"])}</span>'
            f'<strong>{esc(g["title"])}</strong>'
            f'<em>{esc(g.get("summary", ""))[:90]}</em>'
            f'<span class="card-arrow">Play now →</span></a>'
            for g in rel
        )
        rel_html = (
            "<section class=\"related\">\n"
            "<h2>More Games You'll Love</h2>\n"
            f"<div class=\"card-grid\">{cards}</div>\n</section>"
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(game.get('description', game.get('summary', '')))}">
<meta name="keywords" content="{esc(', '.join(game.get('keywords', [])))}">
<link rel="canonical" href="{esc(canon)}">
<link rel="stylesheet" href="../assets/style.css">
{jsonld}
</head>
<body>
<header class="site-header">
  <a class="brand" href="../index.html"><span class="logo">G</span>GameHub</a>
  <a class="header-link" href="../index.html">← All Games</a>
</header>
<main class="wrap">
  <article class="game-page">
    <nav class="crumbs"><a href="../index.html">Home</a><span class="sep">/</span><span>{esc(game['category'])}</span></nav>
    <h1>Play {esc(game['title'])} Online</h1>
    <p class="lead">{esc(game.get('summary', ''))}</p>

    <div class="game-card">
      <div class="game-frame">
        <iframe src="{esc(game['embed_url'])}"
                title="{esc(game['title'])} — play online"
                loading="lazy" allowfullscreen></iframe>
      </div>
    </div>
    <p class="tip">Game provided by a third-party platform. If it fails to load, refresh the page.</p>

    <div class="content">
{sections}
{faq_html}
    </div>
  </article>
{rel_html}
</main>
<footer class="site-footer">
  <p>© {datetime.date.today().year} {esc(site['name'])} · Free online games for fun · Game content © their respective platforms</p>
</footer>
</body>
</html>
"""


def render_index(site, all_games):
    categories = {}
    for g in all_games:
        categories.setdefault(g["category"], []).append(g)

    hero_pills = "".join(
        f'<a class="pill" href="#cat-{esc(cat)}">{esc(cat)}<span class="pill-count">{len(games)}</span></a>'
        for cat, games in categories.items()
    )

    blocks = []
    for cat, games in categories.items():
        cards = "\n".join(
            f'<a class="card" href="games/{esc(g["slug"])}.html">'
            f'<span class="card-tag tag-{esc(g["category"])}">{esc(g["category"])}</span>'
            f'<strong>{esc(g["title"])}</strong>'
            f'<em>{esc(g.get("summary", ""))[:100]}</em>'
            f'<span class="card-arrow">Play now →</span></a>'
            for g in games
        )
        blocks.append(
            f'<section class="cat-section" id="cat-{esc(cat)}">\n'
            f'<div class="section-head"><h2>{esc(cat.capitalize())} Games</h2><span class="count">{len(games)}</span></div>\n'
            f'<div class="card-grid">{cards}</div>\n</section>'
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(site['name'])} — Free Online Games, Play Instantly</title>
<meta name="description" content="{esc(site['description'])}">
<meta name="keywords" content="{esc(site['keywords'])}">
<link rel="canonical" href="{esc(site['domain'])}/">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site-header">
  <span class="brand"><span class="logo">G</span>{esc(site['name'])}</span>
</header>
<section class="hero">
  <h1>Play Free Online Games Instantly</h1>
  <p class="hero-sub">{esc(site['description'])}</p>
  <div class="hero-pills">{hero_pills}</div>
</section>
<main class="wrap">
  <p class="lead">{len(all_games)} games and counting — new titles added regularly.</p>
{''.join(blocks)}
</main>
<footer class="site-footer">
  <p>© {datetime.date.today().year} {esc(site['name'])} · Free online games for fun · Game content © their respective platforms</p>
</footer>
</body>
</html>
"""


def render_sitemap(site, all_games, today):
    urls = [f"{site['domain']}/"]
    urls += [f"{site['domain']}/games/{g['slug']}.html" for g in all_games]
    items = "\n".join(
        f"  <url><loc>{u}</loc><lastmod>{today}</lastmod><changefreq>daily</changefreq><priority>0.8</priority></url>"
        for u in urls
    )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{items}
</urlset>
"""


def main():
    data = load()
    site = data["site"]
    games = data["games"]

    today = datetime.date.today().isoformat()
    for g in games:
        g.setdefault("slug", slugify(g.get("title_en", g["title"])))
        g.setdefault("date", today)

    games_dir = os.path.join(ROOT, "games")
    os.makedirs(games_dir, exist_ok=True)

    for g in games:
        path = os.path.join(games_dir, f"{g['slug']}.html")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(render_game_page(g, site, games))
        print(f"[gen] {path}")

    index_path = os.path.join(ROOT, "index.html")
    with open(index_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(render_index(site, games))
    print(f"[gen] {index_path}")

    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write(render_sitemap(site, games, today))
    print(f"[gen] {os.path.join(ROOT, 'sitemap.xml')}")

    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: " + site["domain"] + "/sitemap.xml\n")
    print(f"[gen] {os.path.join(ROOT, 'robots.txt')}")

    print(f"[gen] Done: {len(games)} games, {len(games) + 3} files generated")


if __name__ == "__main__":
    sys.exit(main())
