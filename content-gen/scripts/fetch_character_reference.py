#!/usr/bin/env python3
"""
Automated Official Game Character Reference Fetcher
Persona: @CompetitiveAnalyst & @CreativeDirector
Searches official Fandom MediaWiki APIs (Mobile Legends, Free Fire, Honor of Kings, Valorant)
for high-resolution official splash arts / character renders, downloads them to
`assets/references/`, and converts WebP/other formats to standard JPEG/PNG cross-platform
(supporting Pillow, macOS `sips`, or direct binary write) so they can be passed directly
into `generate_image(MediaPaths=[...])`.
"""
import argparse
import json
import os
import shutil
import subprocess
import urllib.parse
import urllib.request

WIKI_ENDPOINTS = {
    "mobile-legends": "https://mobile-legends.fandom.com/api.php",
    "free-fire": "https://freefire.fandom.com/api.php",
    "honor-of-kings": "https://honor-of-kings.fandom.com/api.php",
    "valorant": "https://valorant.fandom.com/api.php",
}


def search_wiki_files(game: str, query: str, limit: int = 5):
    api_url = WIKI_ENDPOINTS.get(game, WIKI_ENDPOINTS["mobile-legends"])
    params = urllib.parse.urlencode({
        "action": "query",
        "generator": "search",
        "gsrsearch": f"File:{query}",
        "gsrnamespace": 6,
        "gsrlimit": limit,
        "prop": "imageinfo",
        "iiprop": "url|dimensions|mime",
        "format": "json",
    })
    req = urllib.request.Request(f"{api_url}?{params}", headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read())
    pages = data.get("query", {}).get("pages", {})
    results = []
    for p in pages.values():
        ii = (p.get("imageinfo") or [{}])[0]
        url = ii.get("url")
        width = ii.get("width", 0)
        height = ii.get("height", 0)
        if url and width >= 400:
            results.append({
                "title": p["title"],
                "url": url,
                "width": width,
                "height": height,
                "mime": ii.get("mime", ""),
            })
    results.sort(key=lambda x: x["width"] * x["height"], reverse=True)
    return results


def download_and_normalize(url: str, out_path: str):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()

    tmp_path = out_path + ".tmp"
    with open(tmp_path, "wb") as f:
        f.write(raw)

    fmt = "png" if out_path.lower().endswith(".png") else "jpeg"

    # Cross-platform format normalization:
    # 1. Try Pillow (PIL) if installed
    # 2. Try macOS sips if available
    # 3. Fallback to direct file rename/copy
    converted = False
    try:
        from PIL import Image
        with Image.open(tmp_path) as im:
            if fmt == "jpeg" and im.mode in ("RGBA", "P"):
                im = im.convert("RGB")
            im.save(out_path, format=fmt.upper())
            converted = True
    except ImportError:
        pass
    except Exception:
        pass

    if not converted and shutil.which("sips"):
        try:
            subprocess.run(["sips", "-s", "format", fmt, tmp_path, "--out", out_path], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            converted = True
        except Exception:
            pass

    if not converted:
        shutil.move(tmp_path, out_path)
    else:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

    return out_path


def main():
    parser = argparse.ArgumentParser(description="Fetch official character splash art reference.")
    parser.add_argument("--game", default="mobile-legends", choices=list(WIKI_ENDPOINTS.keys()))
    parser.add_argument("--query", required=True, help="Character or skin name (e.g. 'Mecha Maiden' or 'Cyber Cherubin')")
    parser.add_argument("--out", required=True, help="Output file path in assets/references/ (e.g. assets/references/ruby.jpg)")
    args = parser.parse_args()

    matches = search_wiki_files(args.game, args.query)
    if not matches:
        raise SystemExit(f"No official splash art found for query='{args.query}' on {args.game}")
    best = matches[0]
    saved = download_and_normalize(best["url"], args.out)
    print(json.dumps({"saved_path": os.path.abspath(saved), "source": best}, indent=2))


if __name__ == "__main__":
    main()
