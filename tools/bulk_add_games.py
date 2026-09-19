"""
批量从 GameMonetize feed 追加游戏到 games.json。
- 读 _feed_raw.json（feed API 原始 JSON）
- 读 data/games.json
- 按 embed_url 去重，跳过已上线
- 取前 N 款新游戏，自动生成英文条目
- 写回 games.json
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FEED_FILE = ROOT / "_feed_raw.json"
GAMES_JSON = ROOT / "data" / "games.json"
ADD_COUNT = 50


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-") or "game"


def clean_text(s: str) -> str:
    """去掉 feed description 里的 HTML 链接残留。"""
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"&[a-z#0-9]+;", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def summarize(desc: str, title: str) -> str:
    desc = clean_text(desc)
    # 截前 220 字符，在句号/空格处断
    if len(desc) > 220:
        cut = desc[:220]
        last = max(cut.rfind(". "), cut.rfind("! "), cut.rfind("? "))
        if last > 60:
            cut = cut[: last + 1]
        else:
            cut = cut[: cut.rfind(" ")] + "."
        desc = cut
    return desc


def make_sections(desc: str, howto: str, title: str, category: str) -> list:
    desc = clean_text(desc)
    howto = clean_text(howto)
    h2_a = {
        "puzzle": "How do you solve it?",
        "arcade": "How does the gameplay feel?",
        "racing": "How do you drive?",
        "adventure": "What is the goal?",
        "clicker": "How does the upgrade loop work?",
        "cooking": "How does the kitchen flow work?",
    }.get(category.lower(), "What is it about?")
    body_a = desc if desc else f"{title} is a {category} game playable right in your browser with no download."
    if len(body_a) > 600:
        body_a = body_a[:597].rsplit(" ", 1)[0] + "..."

    h2_b = "How do you control it?"
    body_b = howto if howto else "Use the mouse or tap the on-screen buttons. Keyboard players can usually use the arrow keys or WASD."
    if len(body_b) > 600:
        body_b = body_b[:597].rsplit(" ", 1)[0] + "..."

    return [{"h2": h2_a, "body": body_a}, {"h2": h2_b, "body": body_b}]


def make_faq(title: str, howto: str) -> list:
    howto = clean_text(howto)
    controls = (
        howto[:180] if len(howto) > 180 else howto
    ) or "Use the mouse or tap the on-screen buttons."
    return [
        {
            "q": f"Is {title} free to play?",
            "a": f"Yes. {title} runs in your browser with no download and no sign-up, supported by non-intrusive ads.",
        },
        {
            "q": "How do I control it?",
            "a": f"{controls} On mobile, touch buttons work the same way.",
        },
        {
            "q": "Can I play it offline or on my phone?",
            "a": "It needs an internet connection to load, but it runs on phones, tablets and desktops directly in the browser.",
        },
    ]


def main():
    feed = json.loads(FEED_FILE.read_text(encoding="utf-8-sig"))
    db = json.loads(GAMES_JSON.read_text(encoding="utf-8"))

    existing_urls = {g["embed_url"] for g in db["games"]}
    existing_slugs = {g["slug"] for g in db["games"]}

    added = 0
    for item in feed:
        if added >= ADD_COUNT:
            break
        url = item.get("url", "").strip()
        if not url or url in existing_urls:
            continue
        title = item.get("title", "").strip()
        if not title:
            continue
        slug = slugify(title)
        if slug in existing_slugs:
            continue
        # 防重：在 slug 后加数字
        base_slug = slug
        n = 2
        while slug in existing_slugs:
            slug = f"{base_slug}-{n}"
            n += 1

        cat = (item.get("category") or "arcade").strip().lower()
        thumb = item.get("thumb", "")
        if not thumb:
            m = re.search(r"gamemonetize\.co/([a-z0-9]+)/", url)
            if m:
                thumb = f"https://img.gamemonetize.com/{m.group(1)}/512x384.jpg"

        desc = item.get("description", "")
        howto = item.get("instructions", "")
        tags = item.get("tags", "") or ""
        kw = [w.strip().lower() for w in re.split(r"[,;]", tags) if w.strip()][:6]
        kw = kw + [f"{title.lower()} online", f"play {title.lower()} free"]

        entry = {
            "slug": slug,
            "title": title,
            "title_en": title,
            "category": cat,
            "embed_url": url,
            "thumbnail": thumb,
            "keywords": kw,
            "summary": summarize(desc, title),
            "description": f"Play {title} free online. {clean_text(desc)[:150]}",
            "sections": make_sections(desc, howto, title, cat),
            "faq": make_faq(title, howto),
            "related": [],
            "date": "2026-09-19",
        }
        db["games"].append(entry)
        existing_urls.add(url)
        existing_slugs.add(slug)
        added += 1
        print(f"  + {title}  [{cat}]  -> {slug}")

    GAMES_JSON.write_text(
        json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"DONE: added {added} new games, total {len(db['games'])}")


if __name__ == "__main__":
    main()
