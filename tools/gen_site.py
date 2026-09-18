#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_site.py — 从 data/games.json 生成游戏站静态页面（零第三方依赖）。

用法:
    python tools/gen_site.py

输出（生成到仓库根目录，即 GitHub Pages 发布根）:
    index.html         首页：分类导航 + 游戏卡片
    games/<slug>.html  每款游戏一个页面（Article + FAQPage Schema / iframe / 原创内容 / 相关游戏内链）
    sitemap.xml        全站 URL 清单（提交给 Search Console 用）
    robots.txt         允许全站抓取

工作流:
    1. 用 geo-content-optimizer 技能产出内容 → 填入 data/games.json
    2. 运行本脚本 → 生成全部页面
    3. git push → GitHub Pages 自动发布
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
    """HTML 转义，防止标题/正文中的引号与尖括号破坏页面。"""
    return html.escape(str(value), quote=True)


def load():
    with open(DATA, "r", encoding="utf-8-sig") as f:
        return json.load(f)


def slugify(title_en):
    """由英文标题生成 URL slug；失败时退化为拼音不可用时的时间戳。"""
    s = re.sub(r"[^a-z0-9]+", "-", title_en.lower()).strip("-")
    return s or "game"


# ---------- Schema ----------

def schema_article(game, site):
    url = f"{site['domain']}/games/{game['slug']}.html"
    date = game.get("date", datetime.date.today().isoformat())
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": f"{game['title']} 在线玩",
        "description": game.get("description", game.get("summary", "")),
        "url": url,
        "datePublished": date,
        "dateModified": date,
        "inLanguage": "zh-CN",
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


# ---------- 页面渲染 ----------

def related_games(game, all_games, n=3):
    """优先同分类，再补其他；排除自身。"""
    same = [g for g in all_games if g["category"] == game["category"] and g["slug"] != game["slug"]]
    others = [g for g in all_games if g["category"] != game["category"] and g["slug"] != game["slug"]]
    picked = (same + others)[:n]
    return picked


def render_game_page(game, site, all_games):
    title = f"{game['title']} 在线玩 - 免费"
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
        f"<h2>{esc(s['h2'])}</h2>\n<p>{esc(s['body'])}</p>"
        for s in game.get("sections", [])
    )

    faq_html = ""
    if game.get("faq"):
        faq_html = (
            '<h2>常见问题</h2>\n'
            + "\n".join(
                f"<h3>{esc(f['q'])}</h3>\n<p>{esc(f['a'])}</p>"
                for f in game["faq"]
            )
        )

    rel = related_games(game, all_games)
    rel_html = ""
    if rel:
        cards = "\n".join(
            f'<a class="card" href="games/{g["slug"]}.html">'
            f'<span class="tag">{esc(g["category"])}</span>'
            f'<strong>{esc(g["title"])}</strong></a>'
            for g in rel
        )
        rel_html = f"<h2>相关游戏</h2>\n<div class=\"card-grid\">{cards}</div>"

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
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
  <a class="brand" href="../index.html">{esc(site['name'])}</a>
  <span class="slogan">{esc(site['description'])}</span>
</header>
<main class="wrap">
  <article class="game-page">
    <h1>{esc(game['title'])} 在线玩</h1>
    <p class="lead">{esc(game.get('summary', ''))}</p>

    <div class="game-frame">
      <iframe src="{esc(game['embed_url'])}"
              title="{esc(game['title'])} 在线游戏"
              loading="lazy" allowfullscreen></iframe>
    </div>
    <p class="tip">提示：游戏由第三方平台提供，加载失败可刷新重试。</p>

    <div class="content">
{sections}
{faq_html}
    </div>
  </article>
{rel_html}
</main>
<footer class="site-footer">© {datetime.date.today().year} {esc(site['name'])} · 仅供娱乐 · 游戏版权归原平台所有</footer>
</body>
</html>
"""


def render_index(site, all_games):
    categories = {}
    for g in all_games:
        categories.setdefault(g["category"], []).append(g)

    nav = "".join(
        f'<a href="#cat-{esc(cat)}">{esc(cat)}</a>'
        for cat in categories
    )

    blocks = []
    for cat, games in categories.items():
        cards = "\n".join(
            f'<a class="card" href="games/{esc(g["slug"])}.html">'
            f'<span class="tag">{esc(g["category"])}</span>'
            f'<strong>{esc(g["title"])}</strong>'
            f'<em>{esc(g.get("summary", ""))[:60]}…</em></a>'
            for g in games
        )
        blocks.append(
            f'<h2 id="cat-{esc(cat)}">{esc(cat)}（{len(games)} 款）</h2>'
            f'<div class="card-grid">{cards}</div>'
        )

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(site['name'])} - 免费在线小游戏</title>
<meta name="description" content="{esc(site['description'])}">
<meta name="keywords" content="{esc(site['keywords'])}">
<link rel="canonical" href="{esc(site['domain'])}/">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site-header">
  <span class="brand">{esc(site['name'])}</span>
  <span class="slogan">{esc(site['description'])}</span>
</header>
<main class="wrap">
  <nav class="cat-nav">{nav}</nav>
  <p class="lead">共收录 {len(all_games)} 款游戏，持续更新中。</p>
{''.join(blocks)}
</main>
<footer class="site-footer">© {datetime.date.today().year} {esc(site['name'])} · 仅供娱乐 · 游戏版权归原平台所有</footer>
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

    print(f"[gen] 完成：{len(games)} 款游戏，共生成 {len(games) + 3} 个文件")


if __name__ == "__main__":
    sys.exit(main())
