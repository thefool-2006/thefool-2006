"""Turn your photo into a purple dotted-portrait SVG (the 'VISUAL.MAP' look).
Usage:  pip install pillow
        python tools/photo_to_dots.py my_photo.jpg assets/portrait_dots.svg
Tip: use a clear, front-facing, well-lit photo with a plain background."""
import sys, random
from PIL import Image, ImageOps

src, out = sys.argv[1], sys.argv[2]
W, H, STEP = 320, 340, 5                      # panel size and dot spacing
img = ImageOps.autocontrast(Image.open(src).convert("L"))
img = ImageOps.fit(img, (W // STEP, H // STEP))
random.seed(7)
dots = []
for y in range(img.height):
    for x in range(img.width):
        v = img.getpixel((x, y)) / 255          # 0 dark .. 1 bright
        if v > 0.18:                            # skip near-black (background)
            r = 0.6 + 1.6 * v
            dots.append(f'<circle cx="{x*STEP+STEP/2}" cy="{y*STEP+STEP/2}" r="{r:.2f}"/>')
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">'
       f'<g fill="#a78bfa" opacity=".9">{"".join(dots)}</g></svg>')
open(out, "w").write(svg)
print("saved", out, len(dots), "dots")
