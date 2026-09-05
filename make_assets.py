#!/usr/bin/env python3
"""Generates the site's image assets. Run after changing brand colours.

    python3 make_assets.py

Produces:
  assets/favicon.svg              — the energy device, pure geometry, legible at 16px
  assets/apple-touch-icon.png     — 180x180 of the same
  assets/og-exceptional-media.png — 1200x630 social card

NOTE: the display type here is DejaVu Sans Condensed Bold, not Bebas Neue — Bebas is not
installable in the build environment. The card reads on-brand because the structure carries
it (navy field, 30-degree gold energy lines, gold rule, letterspaced descriptor), but the
wordmark is a stand-in. Regenerate with real Bebas when a licensed file is on hand.
"""
import pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).parent
A = ROOT / "assets"; A.mkdir(exist_ok=True)

INK   = (0, 0, 0)
NAVY  = (44, 66, 100)
DEEP  = (30, 46, 69)
GOLD  = (205, 198, 140)
WHITE = (255, 255, 255)

COND = "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    try: return ImageFont.truetype(path, size)
    except Exception: return ImageFont.load_default()

def tracked(d, xy, text, f, fill, track=0):
    """Draw text with letter-spacing. Returns the width drawn."""
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + track
    return x - xy[0] - track

# ── favicon: black field, three gold 30-degree bars bleeding off both edges ──
# Pure geometry. No type — a letterform is unreadable at 16px and the device is not.
SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Exceptional Media">
  <rect width="64" height="64" fill="#000000"/>
  <g fill="#CDC68C">
    <polygon points="-14,50 4,14 20,14 2,50"/>
    <polygon points="14,50 32,14 48,14 30,50"/>
    <polygon points="42,50 60,14 76,14 58,50"/>
  </g>
</svg>
'''
(A / "favicon.svg").write_text(SVG)

def draw_bars(d, w, h, color, bar, gap, opacity=255, x0=None):
    """30 degrees, bottom-left to top-right, equal widths, bleeding off both edges."""
    import math
    dx = h / math.tan(math.radians(30))          # horizontal run over the full height
    x = (x0 if x0 is not None else -dx) - bar
    while x < w + dx:
        d.polygon([(x, h), (x + dx, 0), (x + dx + bar, 0), (x + bar, h)],
                  fill=color + (opacity,) if len(color) == 3 else color)
        x += bar + gap

# ── apple touch icon ──
ic = Image.new("RGB", (180, 180), INK)
dd = ImageDraw.Draw(ic)
draw_bars(dd, 180, 180, GOLD, 20, 32)
ic.save(A / "apple-touch-icon.png")

# ── open graph card ──
W, H = 1200, 630
im = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(im, "RGBA")

# energy lines confined to the right third — never behind the copy, per the standard
band = Image.new("RGBA", (W, H), (0, 0, 0, 0))
bd = ImageDraw.Draw(band)
draw_bars(bd, W, H, (255, 255, 255), 16, 46, opacity=26, x0=W * 0.60)
im.paste(Image.alpha_composite(im.convert("RGBA"), band).convert("RGB"), (0, 0))
d = ImageDraw.Draw(im, "RGBA")
d.rectangle([0, 0, W, 10], fill=GOLD)                       # top rule

f_word = font(COND, 108)
f_desc = font(SANS, 26)
f_lead = font(SANS, 34)
f_tag  = font(SANS, 22)

x, y = 84, 150
tracked(d, (x, y), "EXCEPTIONAL", f_word, WHITE, track=6)
y += 128
tracked(d, (x, y), "MEDIA", f_desc, GOLD, track=14)
y += 74
d.rectangle([x, y, x + 150, y + 7], fill=GOLD)              # accent rule
y += 52
d.text((x, y), "Books, podcasts, and a quarterly magazine", font=f_lead, fill=(233, 236, 242))
d.text((x, y + 46), "for people building something worth keeping.", font=f_lead, fill=(233, 236, 242))

tracked(d, (x, H - 78), "DESIGNED FOR EXCEPTIONAL.", f_tag, WHITE, track=3)
tracked(d, (x, H - 46), "LIFE. BUSINESS. WEALTH.", f_tag, GOLD, track=5)

im.save(A / "og-exceptional-media.png", optimize=True)
print("wrote favicon.svg, apple-touch-icon.png, og-exceptional-media.png")
for f in ("favicon.svg", "apple-touch-icon.png", "og-exceptional-media.png"):
    print(f"  {f:30} {(A / f).stat().st_size:>7,} bytes")
