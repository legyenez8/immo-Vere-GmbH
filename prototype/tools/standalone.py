"""Build a single self-contained HTML file (images embedded) from prototype/index.html.

Usage: python3 prototype/tools/standalone.py OUTPUT.html
Requires Pillow (pip install pillow) to shrink the embedded photos.
"""
import base64
import io
import json
import pathlib
import re
import sys

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
out = pathlib.Path(sys.argv[1])
out.write_text(html, encoding="utf-8")
print(f"{out} written, {out.stat().st_size / 1e6:.1f} MB")
