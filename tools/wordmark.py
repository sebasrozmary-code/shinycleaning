#!/usr/bin/env python3
"""Maakt de Shiny Cleaning-wordmarks (Lobster + Open Sans, tekst als vectorpaden)
in brand/: horizontaal en gestapeld, in kleur en in wit."""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = os.path.join(os.path.dirname(__file__), "..")
F = os.path.join(ROOT, "brand", "fonts")
OUT = os.path.join(ROOT, "brand")
LOB = TTFont(os.path.join(F, "Lobster-Regular.ttf"))
OPS = TTFont(os.path.join(F, "OpenSans-Regular.ttf"))

TEAL, INK, YEL, SOFT = "#17a2a2", "#1e2b31", "#f6bf45", "#46595f"

def text_path(font, s, size, x, y, tracking=0):
    """Tekst -> SVG path-data met basislijn op (x, y). Geeft (d, breedte)."""
    gs = font.getGlyphSet(); cmap = font.getBestCmap(); hmtx = font["hmtx"]
    upm = font["head"].unitsPerEm; k = size / upm
    kern = {}
    if "kern" in font and font["kern"].kernTables:
        kern = font["kern"].kernTables[0].kernTable
    pen = SVGPathPen(gs); cx = 0; prev = None
    for ch in s:
        g = cmap.get(ord(ch))
        if g is None: continue
        if prev and (prev, g) in kern: cx += kern[(prev, g)]
        tp = TransformPen(pen, (k, 0, 0, -k, x + cx * k, y))
        gs[g].draw(tp)
        cx += hmtx[g][0] + tracking / k
        prev = g
    return pen.getCommands(), cx * k

def width(font, s, size, tracking=0):
    return text_path(font, s, size, 0, 0, tracking)[1]

def sparkle(x, y, s, fill=YEL, ink=INK):
    d = f"M{x},{y-s} Q{x},{y} {x+s},{y} Q{x},{y} {x},{y+s} Q{x},{y} {x-s},{y} Q{x},{y} {x},{y-s}Z"
    return f'<path d="{d}" fill="{fill}" stroke="{ink}" stroke-width="{s*0.12:.2f}" stroke-linejoin="round"/>'

def svg(w, h, body, title):
    title = title.replace("&", "&amp;")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}" '
            f'role="img" aria-label="{title}"><title>{title}</title>\n{body}\n</svg>\n')

TAG = "Glazen wassen & schoonmaakservice"

def horizontal(name_col, tag_col, ink, tag=TAG):
    size = 96
    d, w = text_path(LOB, "Shiny Cleaning", size, 96, 104)
    tw = width(OPS, tag.upper(), 23, tracking=2.6)
    td, _ = text_path(OPS, tag.upper(), 23, 100, 150, tracking=2.6)
    W = 96 + max(w, tw) + 16
    body = (sparkle(40, 62, 30, ink=ink) + sparkle(72, 22, 11, ink=ink) + sparkle(76, 100, 8, ink=ink) +
            f'<path d="{d}" fill="{name_col}"/>' + f'<path d="{td}" fill="{tag_col}"/>')
    return svg(W, 170, body, "Shiny Cleaning — " + tag)

def stacked(name_col, tag_col, ink, tag=TAG):
    size = 120
    w1 = width(LOB, "Shiny", size); w2 = width(LOB, "Cleaning", size)
    tsz = 24; tw = width(OPS, tag.upper(), tsz, tracking=2.4)
    W = max(w1, w2, tw) + 80; cx = W / 2
    d1, _ = text_path(LOB, "Shiny", size, cx - w1 / 2, 150)
    d2, _ = text_path(LOB, "Cleaning", size, cx - w2 / 2, 262)
    td, _ = text_path(OPS, tag.upper(), tsz, cx - tw / 2, 322, tracking=2.4)
    body = (sparkle(cx + w1 / 2 + 22, 62, 22, ink=ink) + sparkle(cx + w1 / 2 + 52, 34, 9, ink=ink) +
            sparkle(cx - w2 / 2 - 6, 180, 10, ink=ink) +
            f'<path d="{d1}" fill="{name_col}"/><path d="{d2}" fill="{name_col}"/><path d="{td}" fill="{tag_col}"/>')
    return svg(W, 350, body, "Shiny Cleaning — " + tag)

files = {
    "shiny-cleaning-wordmark.svg":        horizontal(TEAL, SOFT, INK),
    "shiny-cleaning-wordmark-wit.svg":    horizontal("#ffffff", "#d7eeee", "#ffffff"),
    "shiny-cleaning-gestapeld.svg":       stacked(TEAL, SOFT, INK),
    "shiny-cleaning-gestapeld-wit.svg":   stacked("#ffffff", "#d7eeee", "#ffffff"),
}
for n, s in files.items():
    open(os.path.join(OUT, n), "w", encoding="utf-8").write(s)
    print(f"{n:36s} {len(s)/1024:5.1f} KB")
