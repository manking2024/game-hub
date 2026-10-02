import json
import re
import sys
import urllib.request

PROXY = "http://127.0.0.1:7890"
BASE = "https://manking2024.github.io/game-hub/"


def fetch(url, timeout=20):
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({"http": PROXY, "https": PROXY})
    )
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 health-check"})
    with opener.open(req, timeout=timeout) as resp:
        return resp.status, resp.read().decode("utf-8", "ignore")


def main():
    # 1) 抓 sitemap，取全部 loc
    _, sm = fetch(BASE + "sitemap.xml")
    urls = re.findall(r"<loc>\s*(.*?)\s*</loc>", sm)
    print(f"SITEMAP_URLS={len(urls)}")

    # 2) 逐个请求，统计状态码
    from collections import Counter
    codes = Counter()
    bad = []
    for u in urls:
        try:
            c, _ = fetch(u)
            codes[c] += 1
            if c != 200:
                bad.append((c, u))
        except Exception as e:
            codes["ERR"] += 1
            bad.append(("ERR", u, str(e)))
        print(f"  {c if c in codes else 'ERR'}  {u}")
    print("STATUS_SUMMARY=" + dict(codes).__str__())
    if bad:
        print("BAD_URLS:")
        for b in bad:
            print("  ", b)
    else:
        print("ALL_OK")


if __name__ == "__main__":
    main()
