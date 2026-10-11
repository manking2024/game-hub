import json
import re

with open("data/games.json", encoding="utf-8-sig") as f:
    d = json.load(f)

for slug in ["box-press-puzzle", "slime-buffet", "ragdoll-rush-3d-sky-race", "geometry-vibes", "unite-words"]:
    with open(f"games/{slug}.html", encoding="utf-8") as fh:
        html = fh.read()
    faq_count = len(re.findall(r'"@type": "Question"', html))
    secs = len(re.findall(r'<section class="content-block">', html))
    print(slug, "| FAQ schema questions:", faq_count, "| content sections:", secs)

# index checks
with open("index.html", encoding="utf-8") as fh:
    idx = fh.read()
print("index | picks:", len(re.findall(r'class="picks-mins"', idx)), "| site FAQ:", len(re.findall(r'class="faq-item"', idx)), "| FAQPage schema:", '"@type": "FAQPage"' in idx)
