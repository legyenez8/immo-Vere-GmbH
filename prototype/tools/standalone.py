"""Build a single self-contained HTML file (images and fonts embedded) from prototype/index.html.

Usage: python3 prototype/tools/standalone.py OUTPUT.html
Requires Pillow (pip install pillow) to shrink the embedded photos.
Fonts are downloaded from Google Fonts at build time (latin + latin-ext only);
if that fails, the file keeps the normal Google Fonts link and needs internet.
"""
import base64
import io
import json
import pathlib
import re
import ssl
import sys
import urllib.request

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
html = (ROOT / "index.html").read_text(encoding="utf-8")


def data_uri(path: pathlib.Path) -> str:
    im = Image.open(path).convert("RGB")
    im.thumbnail((1800, 1800) if path.stem == "hero" else (1300, 1300))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=72, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


images = {p.stem: data_uri(p) for p in sorted((ROOT / "assets").glob("*.jpg"))}

# Static <img> tags: swap the file path for a key, filled in by script at start-up.
html = re.sub(r'src="assets/([\w-]+)\.jpg"', r'data-img-key="\1"', html)
helper = "const img = name => `assets/${name}.jpg`;"
assert helper in html
html = html.replace(
    helper,
    "const IMG = " + json.dumps(images) + ";\n"
    "const img = name => IMG[name];\n"
    "document.querySelectorAll('[data-img-key]').forEach(el => { el.src = IMG[el.dataset.imgKey]; });",
)


def fetch(url: str) -> bytes:
    ctx = ssl.create_default_context()
    for ca in ("/root/.ccr/ca-bundle.crt",):
        if pathlib.Path(ca).exists():
            ctx.load_verify_locations(ca)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"})
    with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
        return r.read()


def embed_fonts(doc: str) -> str:
    m = re.search(r'<link rel="stylesheet" href="(https://fonts\.googleapis\.com/css2[^"]+)">', doc)
    if not m:
        return doc
    try:
        css = fetch(m.group(1).replace("&amp;", "&")).decode()
        blocks = re.findall(r"/\* ([\w-]+) \*/\s*(@font-face \{.*?\})", css, re.S)
        keep, cache = [], {}
        for subset, block in blocks:
            if subset not in ("latin", "latin-ext"):
                continue
            url = re.search(r"url\((https://[^)]+\.woff2)\)", block).group(1)
            if url not in cache:
                cache[url] = "data:font/woff2;base64," + base64.b64encode(fetch(url)).decode()
            keep.append(block.replace(url, cache[url]))
        if not keep:
            raise ValueError("no font blocks found")
    except Exception as exc:  # keep the online link as a fallback
        print(f"fonts not embedded ({exc}); the file will load them from Google Fonts")
        return doc
    print(f"fonts embedded: {len(keep)} faces, {len(cache)} files")
    doc = re.sub(r'<link rel="preconnect" href="https://fonts\.(googleapis|gstatic)\.com"( crossorigin)?>\n', "", doc)
    return doc.replace(m.group(0), "<style>\n" + "\n".join(keep) + "\n</style>")


html = embed_fonts(html)
out = pathlib.Path(sys.argv[1])
out.write_text(html, encoding="utf-8")
print(f"{out} written, {out.stat().st_size / 1e6:.1f} MB")
