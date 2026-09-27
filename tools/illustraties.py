#!/usr/bin/env python3
"""
Genereert alle illustraties voor Shiny Cleaning in de huisstijl van het logo:
doodle-stijl met dunne inktlijnen, vlakke vullingen (teal, geel, groen, lichtblauw)
en de kenmerkende vierpuntige sterretjes. Output: SVG-bestanden in ../images/ill/
"""
import os, math

OUT = os.path.join(os.path.dirname(__file__), "..", "images", "ill")
os.makedirs(OUT, exist_ok=True)

# ---- palet, afgeleid van het logo ---------------------------------------
INK    = "#1e2b31"
TEAL   = "#17a2a2"
TEAL_D = "#0f7f7f"
TEAL_L = "#8fdad6"
MINT   = "#d9f3f1"
YEL    = "#f6bf45"
YEL_D  = "#dfa02a"
ORANGE = "#f19a3e"
GRN    = "#86c94a"
GRN_D  = "#5f9e2f"
BLUE   = "#7dcdf0"
BLUE_L = "#cdeefb"
NAVY   = "#245a70"
WHITE  = "#ffffff"
GREY   = "#e3ebec"
GREY_D = "#b9c7ca"
CREAM  = "#f5ead7"
BRICK  = "#e9c9a6"
ALG    = "#9dbf6d"
MOSS   = "#6fa843"
TAN    = "#e6c489"

SW = 3          # standaard lijndikte
_seed = [7]

def stroke(w=SW, c=INK):
    return f'stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'

def svg(w, h, body, wobble=2.2, bg=None):
    """Wikkelt body in een SVG met hand-getekend 'wobble' filter."""
    _seed[0] += 1
    bgrect = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">
<defs>
  <filter id="w" x="-5%" y="-5%" width="110%" height="110%">
    <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="{_seed[0]}" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="{wobble}" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
</defs>
{bgrect}<g filter="url(#w)" fill="none" {stroke()}>
{body}
</g>
</svg>
'''

# ---- bouwstenen ----------------------------------------------------------
def sparkle(x, y, s, fill=YEL, sw=2.2):
    p = f"M{x},{y-s} Q{x},{y} {x+s},{y} Q{x},{y} {x},{y+s} Q{x},{y} {x-s},{y} Q{x},{y} {x},{y-s}Z"
    return f'<path d="{p}" fill="{fill}" {stroke(sw)}/>'

def dot(x, y, r, fill=BLUE, sw=1.8):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" {stroke(sw)}/>'

def drop(x, y, s, fill=BLUE, sw=2):
    return (f'<path d="M{x},{y-s} C{x+s*0.9},{y+s*0.1} {x+s*0.7},{y+s} {x},{y+s} '
            f'C{x-s*0.7},{y+s} {x-s*0.9},{y+s*0.1} {x},{y-s}Z" fill="{fill}" {stroke(sw)}/>')

def blob(x, y, rx, ry, fill=MINT):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="none"/>'

def rect(x, y, w, h, fill, rx=6, sw=SW, c=INK):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {stroke(sw, c)}/>'

def line(x1, y1, x2, y2, c=INK, sw=SW, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {stroke(sw, c)}{d}/>'

def path(d, fill="none", sw=SW, c=INK, extra=""):
    return f'<path d="{d}" fill="{fill}" {stroke(sw, c)} {extra}/>'

def bucket(x, y, w=90, h=80, fill=TEAL, foam=True):
    """x,y = linksboven van de emmerrand."""
    b = []
    b.append(f'<path d="M{x},{y} L{x+w},{y} L{x+w-w*0.14},{y+h} L{x+w*0.14},{y+h}Z" fill="{fill}" {stroke()}/>')
    b.append(rect(x-4, y-10, w+8, 16, TEAL_D, rx=5))
    b.append(path(f"M{x+w*0.18},{y-10} Q{x+w/2},{y-h*0.75} {x+w*0.82},{y-10}", sw=3.5))
    if foam:
        for i, (dx, r) in enumerate([(0.25, 11), (0.45, 13), (0.66, 10), (0.82, 8)]):
            b.append(dot(x + w*dx, y - 12 - r*0.4, r, WHITE, 2))
    return "\n".join(b)

def spray_bottle(x, y, h=90, body=GRN, cap=TEAL):
    """x,y = linksonder van de fles."""
    w = h*0.42
    b = []
    b.append(rect(x, y-h*0.62, w, h*0.62, body, rx=8))
    b.append(path(f"M{x+w*0.3},{y-h*0.62} L{x+w*0.3},{y-h*0.8} L{x+w*0.7},{y-h*0.8} L{x+w*0.7},{y-h*0.62}", fill=body))
    # trekker + kop
    b.append(path(f"M{x+w*0.3},{y-h*0.8} L{x+w*0.3},{y-h} L{x+w*1.05},{y-h} L{x+w*1.05},{y-h*0.86} L{x+w*0.7},{y-h*0.86} L{x+w*0.7},{y-h*0.8}Z", fill=cap))
    b.append(path(f"M{x+w*0.72},{y-h*0.86} Q{x+w*0.95},{y-h*0.72} {x+w*0.78},{y-h*0.62}", sw=2.8))
    # nevel
    nx = x+w*1.15; ny = y-h*0.93
    for i, (dx, dy, r) in enumerate([(12, -8, 2.5), (22, -2, 3), (18, 8, 2.5), (30, -12, 2), (32, 6, 2.2)]):
        b.append(dot(nx+dx, ny+dy, r, BLUE, 1.5))
    b.append(rect(x+w*0.12, y-h*0.5, w*0.76, h*0.26, WHITE, rx=4, sw=2))
    return "\n".join(b)

def glove(x, y, s=1.0, fill=YEL, angle=0):
    """Wantvormige handschoen, pols onderaan bij (x,y)."""
    d = (f"M{-22*s},{0} L{-22*s},{-40*s} Q{-22*s},{-70*s} {0},{-72*s} Q{22*s},{-70*s} {22*s},{-40*s} "
         f"L{22*s},{0}Z")
    thumb = f"M{-22*s},{-30*s} Q{-44*s},{-40*s} {-40*s},{-58*s} Q{-34*s},{-66*s} {-24*s},{-52*s}"
    return (f'<g transform="translate({x},{y}) rotate({angle})">'
            f'<path d="{thumb}" fill="{fill}" {stroke()}/>'
            f'<path d="{d}" fill="{fill}" {stroke()}/>'
            f'<line x1="{-22*s}" y1="{-8*s}" x2="{22*s}" y2="{-8*s}" {stroke(2.2)}/>'
            f'</g>')

def squeegee(x, y, angle, L=150):
    """Trekker: handvat begint bij (x,y), blad aan het andere eind, gedraaid om angle graden."""
    return (f'<g transform="translate({x},{y}) rotate({angle})">'
            f'<rect x="0" y="-9" width="{L*0.62}" height="18" rx="9" fill="{YEL}" {stroke()}/>'
            f'<rect x="{L*0.6}" y="-7" width="{L*0.16}" height="14" rx="4" fill="{GREY_D}" {stroke()}/>'
            f'<rect x="{L*0.74}" y="-42" width="12" height="84" rx="4" fill="{GREY_D}" {stroke()}/>'
            f'<rect x="{L*0.82}" y="-46" width="8" height="92" rx="3" fill="{INK}" {stroke(2)}/>'
            f'</g>')

def brush_head(x, y, angle, w=70, teal=TEAL):
    return (f'<g transform="translate({x},{y}) rotate({angle})">'
            f'<rect x="{-w/2}" y="-10" width="{w}" height="20" rx="8" fill="{teal}" {stroke()}/>'
            f'<path d="M{-w/2+4},10 L{-w/2+4},30 M{-w/2+16},10 L{-w/2+16},32 M{-w/2+28},10 L{-w/2+28},31 '
            f'M{-w/2+40},10 L{-w/2+40},32 M{-w/2+52},10 L{-w/2+52},30 M{-w/2+64},10 L{-w/2+64},31" {stroke(4, YEL)}/>'
            f'<path d="M{-w/2+4},10 L{-w/2+4},30 M{-w/2+16},10 L{-w/2+16},32 M{-w/2+28},10 L{-w/2+28},31 '
            f'M{-w/2+40},10 L{-w/2+40},32 M{-w/2+52},10 L{-w/2+52},30 M{-w/2+64},10 L{-w/2+64},31" {stroke(1.4, INK)} opacity=".6"/>'
            f'</g>')

def leaf(x, y, s, fill=GRN, angle=0):
    return (f'<g transform="translate({x},{y}) rotate({angle})">'
            f'<path d="M0,{-s} Q{s*0.9},{-s*0.3} 0,{s} Q{-s*0.9},{-s*0.3} 0,{-s}Z" fill="{fill}" {stroke(2)}/>'
            f'<line x1="0" y1="{-s*0.6}" x2="0" y2="{s*0.7}" {stroke(1.5)}/></g>')

def sun(x, y, r):
    rays = []
    for i in range(8):
        a = math.radians(i*45)
        rays.append(line(x+math.cos(a)*(r+8), y+math.sin(a)*(r+8), x+math.cos(a)*(r+20), y+math.sin(a)*(r+20), sw=3))
    return dot(x, y, r, YEL, 3) + "".join(rays)

def foam_streaks(x, y, w, h, n=6):
    """Zeepstrepen: golvende lichtblauwe lijnen + witte belletjes."""
    out = []
    for i in range(n):
        yy = y + h*(i+0.5)/n
        out.append(path(f"M{x+6},{yy} q{w*0.18},-8 {w*0.36},0 t{w*0.36},0 t{w*0.2},0", sw=3, c=BLUE, extra='opacity=".85"'))
    for (dx, dy, r) in [(0.2, 0.15, 7), (0.55, 0.3, 5), (0.35, 0.6, 8), (0.75, 0.72, 6), (0.15, 0.85, 5)]:
        out.append(dot(x+w*dx, y+h*dy, r, WHITE, 1.8))
    return "\n".join(out)

def shine(x, y, w, h):
    """Twee diagonale glansstrepen op schoon glas."""
    return (path(f"M{x+w*0.55},{y+h*0.08} L{x+w*0.25},{y+h*0.92}", sw=7, c=WHITE, extra='opacity=".9"') +
            path(f"M{x+w*0.75},{y+h*0.08} L{x+w*0.62},{y+h*0.45}", sw=5, c=WHITE, extra='opacity=".9"'))

# =========================================================================
#  ILLUSTRATIES
# =========================================================================
FILES = {}

# ---- HERO: raam half gewassen ------------------------------------------
def hero():
    b = [blob(300, 290, 270, 200, MINT)]
    fx, fy, fw, fh = 150, 56, 300, 290
    b.append(rect(fx, fy, fw, fh, TEAL_D, rx=10, sw=3.5))
    gx, gy, gw, gh = fx+18, fy+18, fw-36, fh-36
    b.append(rect(gx, gy, gw, gh, BLUE_L, rx=4, sw=2.5))
    # linkerhelft nog zeep
    b.append(f'<clipPath id="cl"><rect x="{gx}" y="{gy}" width="{gw*0.5}" height="{gh}"/></clipPath>')
    b.append(f'<g clip-path="url(#cl)">{foam_streaks(gx, gy, gw*0.55, gh, 7)}</g>')
    # rechterhelft schoon
    b.append(shine(gx+gw*0.5, gy, gw*0.5, gh))
    # kruis
    b.append(line(gx+gw/2, gy, gx+gw/2, gy+gh, TEAL_D, 12))
    b.append(line(gx, gy+gh*0.5, gx+gw, gy+gh*0.5, TEAL_D, 12))
    b.append(line(gx+gw/2, gy, gx+gw/2, gy+gh, INK, 2))
    b.append(line(gx, gy+gh*0.5, gx+gw, gy+gh*0.5, INK, 2))
    # vensterbank
    b.append(rect(fx-22, fy+fh-4, fw+44, 22, GREY, rx=5))
    # trekker: handvat rechtsonder, blad op de grens zeep/schoon midden op het glas
    b.append(squeegee(440, 335, -128, 165))
    b.append(glove(452, 356, 1.05, YEL, -38))
    # sterretjes rechts
    for (x, y, s) in [(400, 110, 13), (425, 190, 9), (380, 160, 7), (500, 80, 10), (520, 250, 8)]:
        b.append(sparkle(x, y, s))
    for (x, y, r) in [(470, 130, 4), (540, 170, 3.5), (110, 120, 4)]:
        b.append(dot(x, y, r, BLUE))
    # emmer + fles
    b.append(bucket(60, 400, 105, 88))
    b.append(spray_bottle(470, 490, 105, GRN, TEAL))
    b.append(sparkle(590, 420, 8))
    return svg(640, 520, "\n".join(b))
FILES["hero-ramen.svg"] = hero

# ---- DIENST: ramen op hoogte (telescoopsteel) --------------------------
def d_ramen():
    b = [blob(200, 160, 170, 120, MINT)]
    # glazen gevel: 3 rijen x 2 panelen
    for r in range(3):
        for c in range(2):
            x = 150 + c*95; y = 30 + r*82
            b.append(rect(x, y, 88, 74, BLUE_L, rx=3, sw=2.5))
            if r == 0 or (r == 1 and c == 1):
                b.append(shine(x, y, 88, 74))
            else:
                b.append(f'<clipPath id="c{r}{c}"><rect x="{x}" y="{y}" width="88" height="74"/></clipPath>')
                b.append(f'<g clip-path="url(#c{r}{c})">{foam_streaks(x, y, 88, 74, 4)}</g>')
    b.append(rect(146, 26, 194, 250, "none", rx=6, sw=3.5))
    b.append(line(243, 26, 243, 276, TEAL_D, 8)); b.append(line(146, 108, 340, 108, TEAL_D, 8)); b.append(line(146, 190, 340, 190, TEAL_D, 8))
    # telescoopsteel van linksonder naar het paneel middenrechts
    b.append(line(30, 290, 250, 150, GREY_D, 9)); b.append(line(30, 290, 250, 150, INK, 2.2))
    b.append(line(30, 290, 140, 220, YEL, 5))
    b.append(brush_head(262, 142, -33, 62))
    b.append(glove(46, 300, 0.7, YEL, 32))
    for (x, y, s) in [(365, 60, 10), (100, 60, 8), (360, 250, 7), (120, 130, 6)]:
        b.append(sparkle(x, y, s))
    b.append(dot(70, 110, 4, BLUE)); b.append(dot(378, 150, 3.5, BLUE))
    return svg(400, 320, "\n".join(b))
FILES["dienst-ramen.svg"] = d_ramen

# ---- DIENST: zonnepanelen ---------------------------------------------
def d_zonnepanelen():
    b = [blob(200, 190, 185, 110, MINT), sun(330, 62, 26)]
    # paneel, licht scheef
    b.append(f'<g transform="translate(60,110) skewX(-14)">')
    b.append(rect(0, 0, 250, 150, NAVY, rx=6, sw=3.5))
    for c in range(1, 4): b.append(line(c*62.5, 0, c*62.5, 150, TEAL_L, 2))
    for r in range(1, 3): b.append(line(0, r*50, 250, r*50, TEAL_L, 2))
    # schone cellen glanzen (rechts), vuile cellen (links) stofvlekken
    b.append(path("M175,12 L150,138", sw=6, c=WHITE, extra='opacity=".85"'))
    b.append(path("M235,12 L222,60", sw=5, c=WHITE, extra='opacity=".85"'))
    b.append(blob(30, 30, 16, 10, "#8aa3ad")); b.append(blob(90, 110, 20, 11, "#8aa3ad")); b.append(blob(40, 120, 12, 8, "#8aa3ad"))
    b.append('</g>')
    # borstel op steel vanuit linksonder
    b.append(line(20, 300, 160, 195, GREY_D, 8)); b.append(line(20, 300, 160, 195, INK, 2))
    b.append(brush_head(170, 187, -37, 66))
    b.append(glove(34, 312, 0.65, YEL, 40))
    # druppels
    for (x, y, s) in [(205, 250, 7), (230, 268, 6), (185, 275, 5)]:
        b.append(drop(x, y, s))
    for (x, y, s) in [(280, 150, 11), (250, 120, 7), (350, 140, 8), (300, 230, 6)]:
        b.append(sparkle(x, y, s))
    return svg(400, 320, "\n".join(b))
FILES["dienst-zonnepanelen.svg"] = d_zonnepanelen

# ---- DIENST: dakgoten -------------------------------------------------
def d_dakgoten():
    b = [blob(200, 150, 190, 120, MINT)]
    # dakpannen: 3 rijen bogen
    for r in range(3):
        y = 40 + r*34
        for i in range(9):
            x = 20 + i*42 + (21 if r % 2 else 0)
            b.append(path(f"M{x},{y+30} L{x},{y+8} Q{x+21},{y-14} {x+42},{y+8} L{x+42},{y+30}", fill=TEAL_D, sw=2.5))
    b.append(rect(14, 130, 372, 12, GREY, rx=3))
    # goot als halve buis
    b.append(path("M30,150 L30,170 Q30,200 60,200 L340,200 Q370,200 370,170 L370,150", fill=GREY_D, sw=3.5))
    b.append(path("M30,150 L370,150", sw=3.5))
    # bladeren + slib in goot
    b.append(path("M60,198 Q120,178 190,190 Q260,200 336,186 L340,198Z", fill="#7a6a4a", sw=0))
    for (x, y, s, f, a) in [(90, 178, 13, YEL, 20), (140, 172, 12, ORANGE, -30), (200, 175, 12, GRN, 60),
                             (250, 168, 13, YEL, -15), (300, 176, 11, ORANGE, 35), (120, 120, 11, GRN, 80), (330, 112, 10, YEL, -60)]:
        b.append(leaf(x, y, s, f, a))
    # afvoerbuis rechts
    b.append(path("M370,175 L370,195 Q370,215 350,215 L340,215 L340,300", fill="none", sw=12, c=GREY_D))
    b.append(path("M370,175 L370,195 Q370,215 350,215 L340,215 L340,300", fill="none", sw=2.5))
    b.append(drop(340, 312, 6)); b.append(drop(352, 296, 4.5))
    # handschoen die van onderuit (ladder) in de goot grijpt
    b.append(glove(236, 266, 0.95, YEL, -8))
    for (x, y, s) in [(40, 250, 9), (300, 250, 8), (60, 20, 7), (380, 24, 9)]:
        b.append(sparkle(x, y, s))
    return svg(400, 320, "\n".join(b))
FILES["dienst-dakgoten.svg"] = d_dakgoten

# ---- DIENST: gevel softwash -------------------------------------------
def d_gevel():
    b = [blob(200, 170, 190, 120, MINT)]
    wx, wy, ww, wh = 40, 30, 320, 250
    b.append(rect(wx, wy, ww, wh, BRICK, rx=4, sw=3.5))
    # voegen
    for r in range(8):
        y = wy + 31*(r+1)
        b.append(line(wx, y, wx+ww, y, "#c9a882", 2))
        off = 0 if r % 2 else 40
        for c in range(5):
            x = wx + off + c*80
            if wx < x < wx+ww: b.append(line(x, y-31, x, y, "#c9a882", 2))
    # raam in de gevel
    b.append(rect(230, 70, 90, 100, TEAL_D, rx=4)); b.append(rect(240, 80, 70, 80, BLUE_L, rx=2, sw=2)); b.append(shine(240, 80, 70, 80))
    # algen links
    b.append(f'<clipPath id="cg"><rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" rx="4"/></clipPath>')
    b.append('<g clip-path="url(#cg)" opacity=".85">')
    for (x, y, rx, ry) in [(70, 250, 55, 34), (120, 200, 40, 26), (60, 160, 36, 30), (110, 262, 48, 22), (150, 240, 30, 18), (80, 110, 26, 20)]:
        b.append(blob(x, y, rx, ry, ALG))
    b.append('</g>')
    # lans met nevel vanuit rechtsonder
    b.append(line(390, 310, 250, 235, GREY_D, 9)); b.append(line(390, 310, 250, 235, INK, 2.2))
    b.append(line(390, 310, 330, 278, YEL, 5))
    b.append(path("M246,233 L232,225", sw=8, c=INK))
    for (x, y, r) in [(215, 215, 3.5), (200, 228, 3), (205, 205, 2.5), (188, 218, 2.5), (195, 240, 3), (178, 230, 2), (182, 205, 2)]:
        b.append(dot(x, y, r, BLUE, 1.5))
    b.append(glove(372, 318, 0.6, YEL, 30))
    for (x, y, s) in [(200, 50, 10), (180, 120, 7), (300, 210, 9), (330, 250, 6), (380, 20, 8)]:
        b.append(sparkle(x, y, s))
    return svg(400, 320, "\n".join(b))
FILES["dienst-gevel.svg"] = d_gevel

# ---- DIENST: dak ontmossen --------------------------------------------
def d_dak():
    b = [blob(200, 190, 190, 110, MINT)]
    # dakvlak (trapezium) + schoorsteen
    b.append(rect(290, 40, 34, 60, BRICK, rx=2))
    b.append(path("M40,230 L140,70 L360,70 L380,230Z", fill=TEAL_D, sw=3.5))
    b.append(f'<clipPath id="cd"><path d="M40,230 L140,70 L360,70 L380,230Z"/></clipPath>')
    b.append('<g clip-path="url(#cd)">')
    for r in range(6):
        y = 92 + r*26
        for i in range(12):
            x = 20 + i*36 + (18 if r % 2 else 0)
            b.append(path(f"M{x},{y+22} L{x},{y+6} Q{x+18},{y-10} {x+36},{y+6} L{x+36},{y+22}", fill="none", sw=2, c="#0a5f5f"))
    # mos links
    for (x, y, rx, ry) in [(110, 130, 26, 16), (90, 180, 32, 18), (150, 200, 22, 13), (130, 105, 16, 10), (70, 215, 20, 12), (175, 160, 18, 11)]:
        b.append(blob(x, y, rx, ry, MOSS))
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="none" {stroke(1.8, GRN_D)}/>')
    b.append('</g>')
    b.append(rect(30, 226, 360, 14, GREY, rx=3))
    # handborstel
    b.append(f'<g transform="translate(228,150) rotate(-28)">'
             f'<rect x="-40" y="-12" width="80" height="24" rx="9" fill="{TEAL}" {stroke()}/>'
             f'<rect x="38" y="-7" width="60" height="14" rx="7" fill="{YEL}" {stroke()}/>'
             f'<path d="M-34,12 L-34,30 M-22,12 L-22,32 M-10,12 L-10,31 M2,12 L2,32 M14,12 L14,30 M26,12 L26,31" {stroke(4, YEL)}/>'
             f'</g>')
    for (x, y, s) in [(300, 120, 11), (330, 170, 8), (270, 200, 7), (60, 40, 8), (380, 30, 7)]:
        b.append(sparkle(x, y, s))
    for (x, y) in [(200, 250), (230, 262), (215, 275)]:
        b.append(blob(x, y, 6, 4, MOSS))
    return svg(400, 320, "\n".join(b))
FILES["dienst-dak.svg"] = d_dak

# ---- DIENST: terras / oprit hogedruk ----------------------------------
def d_terras():
    b = [blob(200, 200, 190, 110, MINT)]
    # tegels: 4 rijen x 5
    for r in range(4):
        for c in range(6):
            x = 20 + c*62; y = 130 + r*46
            clean = (c + r*0.6) > 2.6
            b.append(rect(x, y, 56, 40, CREAM if clean else "#cfd9b3", rx=3, sw=2.4))
            if not clean:
                b.append(blob(x+18, y+14, 12, 7, ALG)); b.append(blob(x+38, y+28, 10, 6, ALG))
    # lans
    b.append(line(385, 40, 265, 150, GREY_D, 9)); b.append(line(385, 40, 265, 150, INK, 2.2))
    b.append(line(385, 40, 340, 82, YEL, 5))
    b.append(path("M262,152 L250,163", sw=8))
    # waterwaaier
    b.append(path("M250,163 L170,236 L215,258Z", fill=BLUE, sw=2.2, extra='opacity=".85"'))
    for (x, y, r) in [(175, 215, 3), (162, 245, 3), (200, 262, 3), (150, 228, 2.5), (185, 268, 2.5)]:
        b.append(dot(x, y, r, BLUE, 1.5))
    b.append(glove(376, 44, 0.6, YEL, 138))
    # grassprietjes
    for x in [60, 120, 350]:
        b.append(path(f"M{x},128 q-4,-14 -2,-22 M{x},128 q2,-16 8,-20 M{x},128 q-8,-8 -12,-12", sw=2.2, c=GRN_D))
    for (x, y, s) in [(300, 220, 10), (340, 280, 8), (260, 300, 7), (80, 60, 9), (140, 40, 7)]:
        b.append(sparkle(x, y, s))
    return svg(400, 320, "\n".join(b))
FILES["dienst-terras.svg"] = d_terras

# ---- DIENST: tapijt / zetel -------------------------------------------
def d_tapijt():
    b = [blob(200, 190, 190, 110, MINT)]
    # tapijt
    b.append(rect(20, 250, 360, 40, YEL, rx=6))
    for x in range(40, 380, 30): b.append(line(x, 258, x, 282, YEL_D, 2.5))
    # zetel
    b.append(rect(40, 150, 240, 90, TEAL, rx=14, sw=3.5))          # zitting/basis
    b.append(rect(58, 110, 204, 60, TEAL_L, rx=12))                # rugleuning
    b.append(rect(40, 150, 40, 90, TEAL_D, rx=12)); b.append(rect(240, 150, 40, 90, TEAL_D, rx=12))
    b.append(rect(84, 170, 82, 48, TEAL_L, rx=10)); b.append(rect(172, 170, 66, 48, "#6fbdb8", rx=10))
    b.append(line(60, 240, 60, 262, INK, 5)); b.append(line(262, 240, 262, 262, INK, 5))
    # vlekken op rechter kussen
    b.append(blob(200, 190, 12, 7, "#8fa0a5")); b.append(blob(222, 204, 8, 5, "#8fa0a5"))
    # machine (zoals stofzuiger in logo)
    b.append(rect(300, 200, 80, 70, GRN, rx=18, sw=3.5))
    b.append(rect(310, 186, 60, 24, YEL, rx=10))
    b.append(dot(340, 236, 12, YEL_D, 2.5)); b.append(dot(318, 274, 9, INK, 2)); b.append(dot(362, 274, 9, INK, 2))
    # slang naar zuigmond op zitting
    b.append(path("M320,190 C300,120 230,110 200,160", sw=10, c=GREY_D)); b.append(path("M320,190 C300,120 230,110 200,160", sw=2.5))
    b.append(rect(184, 158, 40, 14, GREY_D, rx=4))
    for (x, y, s) in [(120, 195, 10), (100, 130, 7), (150, 150, 6), (60, 80, 9), (340, 120, 8), (370, 160, 6)]:
        b.append(sparkle(x, y, s))
    return svg(400, 320, "\n".join(b))
FILES["dienst-tapijt.svg"] = d_tapijt

# ---- DIENST: oplevering / verhuis --------------------------------------
def d_oplevering():
    b = [blob(200, 190, 190, 110, MINT)]
    # dozen
    b.append(rect(60, 170, 130, 110, TAN, rx=4, sw=3.5)); b.append(line(60, 200, 190, 200, "#c9a15c", 2.5))
    b.append(rect(110, 170, 30, 30, YEL_D, rx=2, sw=2))                 # tape
    b.append(rect(80, 96, 100, 76, TAN, rx=4, sw=3.5)); b.append(rect(118, 96, 24, 22, YEL_D, rx=2, sw=2))
    b.append(path("M96,150 L164,150 M96,160 L140,160", sw=2.5, c="#a98550"))
    # emmer + zwabber
    b.append(bucket(226, 208, 90, 74, TEAL, foam=True))
    b.append(line(300, 230, 336, 60, YEL, 7)); b.append(line(300, 230, 336, 60, INK, 2))
    b.append(path("M322,60 L350,60 Q360,70 356,88 L344,88 Q338,74 322,60Z", fill=GREY_D))
    # sleutelbos
    b.append(f'<g transform="translate(40,60)">'
             f'<circle cx="0" cy="0" r="16" fill="{YEL}" {stroke()}/><circle cx="0" cy="0" r="6" fill="{WHITE}" {stroke(2)}/>'
             f'<rect x="12" y="-5" width="40" height="10" rx="3" fill="{YEL}" {stroke()}/>'
             f'<rect x="36" y="5" width="6" height="8" fill="{YEL}" {stroke(2)}/><rect x="46" y="5" width="6" height="6" fill="{YEL}" {stroke(2)}/>'
             f'</g>')
    for (x, y, s) in [(360, 150, 11), (230, 80, 9), (380, 250, 7), (30, 130, 7), (200, 140, 6)]:
        b.append(sparkle(x, y, s))
    b.append(dot(210, 300, 4, BLUE)); b.append(dot(60, 296, 3.5, BLUE))
    return svg(400, 320, "\n".join(b))
FILES["dienst-oplevering.svg"] = d_oplevering

# ---- B2B: kantoorgebouw + schoonmaakkar --------------------------------
def b2b_kantoor():
    b = [blob(200, 250, 190, 140, MINT)]
    b.append(rect(90, 40, 240, 300, GREY, rx=6, sw=3.5))
    b.append(rect(90, 40, 240, 22, TEAL_D, rx=4))
    for r in range(3):
        for c in range(3):
            x = 112 + c*70; y = 82 + r*70
            b.append(rect(x, y, 50, 48, BLUE_L, rx=3, sw=2.4)); b.append(shine(x, y, 50, 48))
            b.append(line(x+25, y, x+25, y+48, TEAL_D, 3)); b.append(line(x, y+24, x+50, y+24, TEAL_D, 3))
    b.append(rect(186, 290, 48, 50, TEAL_D, rx=4)); b.append(dot(224, 316, 3, YEL, 1.5))
    b.append(rect(20, 340, 360, 12, GREY_D, rx=3))
    # kar (gele zak zoals in logo)
    b.append(f'<g transform="translate(24,200)">'
             f'<rect x="10" y="60" width="90" height="86" rx="8" fill="{YEL}" {stroke(3.2)}/>'
             f'<path d="M20,60 L90,60 M18,150 L18,166 M92,150 L92,166" {stroke(3)}/>'
             f'<rect x="0" y="48" width="110" height="14" rx="4" fill="{GREY_D}" {stroke()}/>'
             f'<circle cx="24" cy="176" r="9" fill="{INK}" {stroke(2)}/><circle cx="86" cy="176" r="9" fill="{INK}" {stroke(2)}/>'
             f'<rect x="14" y="14" width="34" height="34" rx="5" fill="{TEAL}" {stroke()}/>'         # emmer
             f'<rect x="56" y="24" width="18" height="24" rx="5" fill="{GRN}" {stroke(2.5)}/>'      # flesjes
             f'<rect x="78" y="20" width="18" height="28" rx="5" fill="{BLUE}" {stroke(2.5)}/>'
             f'<line x1="100" y1="50" x2="118" y2="-30" {stroke(7, YEL_D)}/><line x1="100" y1="50" x2="118" y2="-30" {stroke(2)}/>'
             f'<path d="M112,-30 L130,-30 Q136,-22 132,-8 L120,-8Z" fill="{GREY_D}" {stroke()}/>'
             f'</g>')
    for (x, y, s) in [(350, 70, 11), (370, 150, 8), (60, 120, 8), (30, 60, 6), (340, 260, 7)]:
        b.append(sparkle(x, y, s))
    return svg(400, 380, "\n".join(b))
FILES["bedrijven-kantoor.svg"] = b2b_kantoor

# ---- VME: appartementsgebouw met inkomhal ------------------------------
def d_vme():
    b = [blob(200, 190, 185, 120, MINT)]
    # gebouw
    b.append(rect(70, 30, 200, 250, CREAM, rx=4, sw=3.5))
    b.append(rect(70, 30, 200, 18, TEAL_D, rx=3))
    for r in range(3):
        for c in range(3):
            x = 88 + c * 60; y = 62 + r * 58
            b.append(rect(x, y, 44, 40, BLUE_L, rx=2, sw=2.4))
            if (r + c) % 2 == 0: b.append(shine(x, y, 44, 40))
            b.append(rect(x - 4, y + 38, 52, 6, GREY, rx=2, sw=1.8))      # balkonrandje
    # inkomhal met glazen deur
    b.append(rect(140, 234, 60, 46, TEAL_D, rx=3))
    b.append(rect(148, 240, 44, 40, BLUE_L, rx=2, sw=2)); b.append(shine(148, 240, 44, 40))
    b.append(line(170, 240, 170, 280, TEAL_D, 3))
    b.append(rect(100, 248, 26, 18, GREY, rx=2, sw=2))                     # brievenbussen
    b.append(line(100, 257, 126, 257, INK, 1.5)); b.append(line(113, 248, 113, 266, INK, 1.5))
    b.append(rect(40, 280, 320, 12, GREY_D, rx=3))
    # emmer + zwabber rechts
    b.append(bucket(282, 218, 70, 60, TEAL))
    b.append(line(300, 238, 330, 110, YEL, 7)); b.append(line(300, 238, 330, 110, INK, 2))
    b.append(path("M318,110 L344,110 Q352,120 348,136 L336,136 Q330,122 318,110Z", fill=GREY_D))
    # klembord met vinkjes (rapport voor de syndicus)
    b.append(f'<g transform="translate(18,150) rotate(-8)">'
             f'<rect x="0" y="0" width="54" height="70" rx="6" fill="{WHITE}" {stroke(3)}/>'
             f'<rect x="16" y="-6" width="22" height="12" rx="3" fill="{YEL}" {stroke(2.2)}/>'
             f'<path d="M10,22 L15,27 L24,16 M10,40 L15,45 L24,34 M10,58 L15,63 L24,52" {stroke(2.6, TEAL)}/>'
             f'<path d="M30,22 L44,22 M30,40 L44,40 M30,58 L44,58" {stroke(2.4, GREY_D)}/>'
             f'</g>')
    for (x, y, s) in [(300, 60, 11), (330, 170, 7), (40, 60, 8), (365, 250, 7), (250, 20, 6)]:
        b.append(sparkle(x, y, s))
    return svg(400, 320, "\n".join(b))
FILES["dienst-vme.svg"] = d_vme

# ---- OVER ONS: het busje ----------------------------------------------
def busje():
    b = [blob(270, 230, 250, 90, MINT)]
    # weg
    b.append(line(20, 300, 520, 300, GREY_D, 5)); b.append(line(60, 316, 480, 316, GREY_D, 3, dash="18 14"))
    # carrosserie
    b.append(path("M70,270 L70,150 Q70,120 100,120 L330,120 Q400,120 440,170 L470,200 L470,270Z", fill=WHITE, sw=3.5))
    b.append(path("M70,215 L470,215 L470,270 L70,270Z", fill=TEAL, sw=3.5))                   # onderband
    b.append(path("M70,150 Q70,120 100,120 L330,120 Q400,120 440,170 L470,200", fill="none", sw=3.5))
    # ramen
    b.append(path("M338,132 L390,132 Q430,150 448,196 L338,196Z", fill=BLUE_L, sw=3)); b.append(shine(340, 134, 100, 60))
    b.append(rect(255, 132, 70, 64, BLUE_L, rx=6, sw=3)); b.append(shine(255, 132, 70, 64))
    b.append(rect(185, 132, 62, 64, BLUE_L, rx=6, sw=3))
    b.append(line(330, 120, 330, 270, INK, 2.5))                                           # deur
    b.append(rect(300, 220, 22, 8, INK, rx=3, sw=1.5))
    # logo-cirkel op de zijkant
    b.append(dot(140, 190, 46, WHITE, 3.5)); b.append(dot(140, 190, 38, MINT, 0))
    b.append(sparkle(140, 186, 22, YEL, 3)); b.append(sparkle(162, 208, 8)); b.append(sparkle(118, 170, 7))
    # ladder op dak
    b.append(line(60, 108, 350, 108, YEL, 7)); b.append(line(60, 108, 350, 108, INK, 2))
    b.append(line(60, 96, 350, 96, YEL, 7)); b.append(line(60, 96, 350, 96, INK, 2))
    for x in range(85, 350, 34): b.append(line(x, 96, x, 108, INK, 2.5))
    b.append(rect(110, 108, 14, 14, GREY_D, rx=2, sw=2)); b.append(rect(300, 108, 14, 14, GREY_D, rx=2, sw=2))
    # wielen
    for cx in (140, 400):
        b.append(dot(cx, 275, 30, INK, 3)); b.append(dot(cx, 275, 15, GREY, 2.5)); b.append(dot(cx, 275, 4, INK, 1))
    # lichten
    b.append(dot(465, 205, 8, YEL, 2.5)); b.append(dot(75, 230, 6, "#e0504a", 2.2))
    # vaart
    b.append(line(20, 190, 50, 190, INK, 3)); b.append(line(10, 215, 48, 215, INK, 3)); b.append(line(28, 240, 52, 240, INK, 3))
    for (x, y, s) in [(490, 120, 11), (510, 170, 8), (40, 80, 9), (200, 60, 7)]:
        b.append(sparkle(x, y, s))
    return svg(540, 340, "\n".join(b))
FILES["over-ons-busje.svg"] = busje

# ---- WERKGEBIED: pinnen op een kaart -----------------------------------
def werkgebied():
    def pin(x, y, s, fill):
        return (f'<path d="M{x},{y} C{x-s*0.9},{y-s*1.1} {x-s*0.8},{y-s*2.2} {x},{y-s*2.2} '
                f'C{x+s*0.8},{y-s*2.2} {x+s*0.9},{y-s*1.1} {x},{y}Z" fill="{fill}" {stroke(3)}/>'
                f'<circle cx="{x}" cy="{y-s*1.45}" r="{s*0.36}" fill="{WHITE}" {stroke(2.2)}/>')
    b = [blob(200, 200, 180, 170, MINT)]
    for (x, y, rx, ry, f) in [(120, 130, 80, 60, "#e7f6f5"), (300, 120, 70, 55, "#e7f6f5"), (110, 290, 75, 55, "#e7f6f5"), (300, 290, 85, 60, "#e7f6f5")]:
        b.append(blob(x, y, rx, ry, f)); b.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="none" {stroke(2, TEAL_L)} stroke-dasharray="8 8"/>')
    # wegen
    b.append(path("M200,200 Q150,150 110,120 M200,200 Q250,150 300,110 M200,200 Q150,250 110,280 M200,200 Q260,250 300,280", sw=3, c=GREY_D, extra='stroke-dasharray="10 9"'))
    b.append(pin(110, 130, 16, YEL)); b.append(pin(300, 118, 16, GRN)); b.append(pin(110, 292, 16, BLUE)); b.append(pin(300, 290, 16, ORANGE))
    b.append(pin(200, 212, 30, TEAL))
    b.append(sparkle(238, 150, 12)); b.append(sparkle(160, 240, 8)); b.append(sparkle(350, 200, 7)); b.append(sparkle(50, 210, 6))
    # klein busje op de weg
    b.append(f'<g transform="translate(232,236) scale(.9)">'
             f'<path d="M0,20 L0,4 Q0,0 4,0 L36,0 Q46,0 52,10 L58,18 L58,20Z" fill="{WHITE}" {stroke(2.5)}/>'
             f'<path d="M0,14 L58,14 L58,20 L0,20Z" fill="{TEAL}" {stroke(2.5)}/>'
             f'<rect x="38" y="3" width="12" height="8" rx="2" fill="{BLUE_L}" {stroke(1.8)}/>'
             f'<circle cx="14" cy="22" r="5" fill="{INK}"/><circle cx="46" cy="22" r="5" fill="{INK}"/></g>')
    return svg(400, 400, "\n".join(b))
FILES["werkgebied.svg"] = werkgebied

# ---- FACTUUR (dienstencheques-sectie) ----------------------------------
def factuur():
    b = [blob(200, 150, 170, 110, MINT)]
    b.append(path("M90,30 L260,30 L310,80 L310,270 L90,270Z", fill=WHITE, sw=3.5))
    b.append(path("M260,30 L260,80 L310,80", fill=GREY, sw=3))
    for (y, w) in [(110, 130), (135, 160), (160, 110), (185, 150)]:
        b.append(line(115, y, 115+w, y, GREY_D, 5))
    b.append(rect(115, 60, 70, 12, TEAL_L, rx=4, sw=0))
    b.append(line(115, 215, 285, 215, INK, 2.5))
    b.append(rect(215, 228, 70, 22, MINT, rx=5, sw=2.2))
    # euromunt
    b.append(dot(300, 210, 40, YEL, 3.5)); b.append(dot(300, 210, 30, YEL_D, 0))
    b.append(path("M312,194 Q294,188 288,206 Q286,226 306,228 M282,204 L304,204 M280,214 L302,214", sw=4, c=INK))
    # stempel vinkje
    b.append(dot(110, 220, 34, TEAL, 3.5)); b.append(path("M92,220 L106,234 L130,204", sw=6, c=WHITE))
    for (x, y, s) in [(340, 60, 11), (60, 70, 9), (350, 250, 7), (40, 160, 6)]:
        b.append(sparkle(x, y, s))
    return svg(400, 300, "\n".join(b))
FILES["factuur.svg"] = factuur

# ---- CONTACT: telefoon met foto + prijs ---------------------------------
def contact():
    b = [blob(160, 220, 130, 170, MINT)]
    b.append(rect(80, 30, 160, 340, INK, rx=24, sw=3.5))
    b.append(rect(92, 54, 136, 292, WHITE, rx=12, sw=2.5))
    b.append(rect(130, 40, 60, 6, "#4b5b62", rx=3, sw=0))
    # bubbel 1 (klant, foto)
    b.append(path("M110,90 L200,90 Q210,90 210,100 L210,160 Q210,170 200,170 L124,170 L108,184 L110,170 Q100,170 100,160 L100,100 Q100,90 110,90Z", fill=GREY, sw=2.5))
    b.append(rect(112, 100, 86, 58, BLUE_L, rx=4, sw=2)); b.append(path("M116,152 L140,124 L160,142 L172,130 L194,152Z", fill=GRN, sw=2)); b.append(dot(180, 114, 7, YEL, 2))
    # bubbel 2 (Shiny, prijs)
    b.append(path("M130,200 L210,200 Q222,200 222,212 L222,262 Q222,274 210,274 L214,290 L196,274 L130,274 Q118,274 118,262 L118,212 Q118,200 130,200Z", fill=TEAL, sw=2.5))
    b.append(path("M182,224 Q160,216 154,236 Q152,258 176,260 M146,234 L172,234 M144,246 L170,246", sw=4.5, c=WHITE))
    b.append(sparkle(200, 216, 8, YEL, 2))
    # invoerbalk
    b.append(rect(104, 304, 96, 24, GREY, rx=12, sw=2)); b.append(dot(214, 316, 12, GRN, 2.2)); b.append(path("M208,316 L220,316 M216,311 L221,316 L216,321", sw=2.5, c=WHITE))
    for (x, y, s) in [(270, 80, 12), (280, 200, 8), (50, 120, 9), (40, 300, 7), (275, 330, 6)]:
        b.append(sparkle(x, y, s))
    b.append(dot(60, 60, 4, BLUE)); b.append(dot(290, 270, 3.5, BLUE))
    return svg(320, 400, "\n".join(b))
FILES["contact.svg"] = contact

# =========================================================================
#  ICONEN (120x120)
# =========================================================================
def icon(body):
    return svg(120, 120, body, wobble=1.6)

def ic_prijslabel():
    return icon(blob(60, 62, 46, 44, MINT) +
        path("M30,28 L70,28 L96,54 L60,92 L22,54Z", fill=YEL, sw=3) + dot(44, 44, 6, WHITE, 2.2) +
        path("M74,60 Q62,56 58,66 Q57,78 70,78 M54,64 L68,64 M53,71 L66,71", sw=3.2) + sparkle(96, 26, 8) + sparkle(24, 96, 6))
def ic_schild():
    return icon(blob(60, 62, 46, 44, MINT) +
        path("M60,18 L94,30 L92,62 Q88,88 60,102 Q32,88 28,62 L26,30Z", fill=TEAL, sw=3) +
        path("M44,60 L56,72 L78,46", sw=6, c=WHITE) + sparkle(98, 24, 8) + sparkle(22, 92, 6))
def ic_badge():
    return icon(blob(60, 62, 46, 44, MINT) +
        rect(24, 34, 72, 56, WHITE, rx=8, sw=3) + rect(24, 34, 72, 14, TEAL, rx=6, sw=3) +
        dot(44, 68, 10, YEL, 2.5) + line(62, 62, 86, 62, GREY_D, 4) + line(62, 74, 82, 74, GREY_D, 4) +
        path("M52,34 L52,24 Q60,18 68,24 L68,34", sw=3) + sparkle(100, 30, 8) + sparkle(20, 96, 6))
def ic_factuur():
    return icon(blob(60, 62, 46, 44, MINT) +
        path("M32,20 L74,20 L90,36 L90,100 L32,100Z", fill=WHITE, sw=3) + path("M74,20 L74,36 L90,36", fill=GREY, sw=2.5) +
        line(42, 50, 78, 50, GREY_D, 4) + line(42, 62, 72, 62, GREY_D, 4) +
        dot(74, 84, 13, TEAL, 2.5) + path("M67,84 L72,89 L81,78", sw=3.5, c=WHITE) + sparkle(100, 60, 8) + sparkle(20, 40, 6))

def ic_stap_vraag():
    return icon(blob(60, 62, 46, 44, MINT) +
        rect(30, 14, 46, 92, INK, rx=10, sw=3) + rect(35, 24, 36, 70, WHITE, rx=5, sw=2) +
        path("M62,44 L98,44 Q104,44 104,50 L104,72 Q104,78 98,78 L70,78 L62,88 L64,78 Q56,78 56,72 L56,50 Q56,44 62,44Z", fill=TEAL, sw=2.5) +
        rect(66, 52, 28, 18, BLUE_L, rx=2, sw=1.8) + path("M68,68 L76,58 L84,66 L92,58 L92,68Z", fill=GRN, sw=1.5) + sparkle(24, 40, 7))
def ic_stap_offerte():
    return icon(blob(60, 62, 46, 44, MINT) +
        path("M28,20 L70,20 L86,36 L86,100 L28,100Z", fill=WHITE, sw=3) + path("M70,20 L70,36 L86,36", fill=GREY, sw=2.5) +
        line(38, 50, 74, 50, GREY_D, 4) + line(38, 62, 66, 62, GREY_D, 4) + line(38, 74, 70, 74, GREY_D, 4) +
        path("M66,84 Q56,80 52,90 Q51,102 64,102 M48,88 L62,88 M47,95 L60,95", sw=3) +
        path("M78,96 L104,58 L112,64 L86,102 L76,104Z", fill=YEL, sw=2.5) + sparkle(20, 34, 7))
def ic_stap_plan():
    return icon(blob(60, 62, 46, 44, MINT) +
        rect(22, 30, 76, 68, WHITE, rx=8, sw=3) + rect(22, 30, 76, 18, TEAL, rx=6, sw=3) +
        line(40, 24, 40, 38, INK, 4) + line(80, 24, 80, 38, INK, 4) +
        "".join(rect(x, y, 10, 8, GREY, rx=2, sw=1.5) for x in (32, 48, 64, 80) for y in (56, 70, 84)) +
        dot(72, 78, 16, YEL, 2.5) + path("M64,78 L70,84 L81,70", sw=4, c=INK) + sparkle(104, 26, 7))
def ic_stap_controle():
    return icon(blob(60, 62, 46, 44, MINT) +
        dot(50, 50, 28, BLUE_L, 3.5) + dot(50, 50, 20, WHITE, 0) + line(70, 70, 98, 98, INK, 9) + line(70, 70, 98, 98, YEL, 5) +
        sparkle(50, 48, 14, YEL, 2.5) + sparkle(20, 92, 6) + sparkle(100, 26, 7))
def ic_stap_herhaal():
    return icon(blob(60, 62, 46, 44, MINT) +
        path("M26,14 L62,14 L76,28 L76,66 L26,66Z", fill=WHITE, sw=3) + path("M62,14 L62,28 L76,28", fill=GREY, sw=2.5) +
        line(36, 40, 66, 40, GREY_D, 4) + line(36, 52, 58, 52, GREY_D, 4) +
        path("M60,80 A20,20 0 1 1 96,72", sw=4, c=TEAL) + path("M96,58 L98,74 L82,72", sw=3.5, c=TEAL) +
        path("M96,90 A20,20 0 1 1 60,98", sw=4, c=TEAL) + path("M60,112 L58,98 L74,100", sw=3.5, c=TEAL) + sparkle(20, 92, 6))

def ic_part_raam():
    return icon(blob(60, 62, 46, 44, MINT) +
        rect(20, 24, 66, 72, TEAL_D, rx=5, sw=3) + rect(28, 32, 50, 56, BLUE_L, rx=2, sw=2) + shine(28, 32, 50, 56) +
        line(53, 32, 53, 88, TEAL_D, 5) + line(28, 60, 78, 60, TEAL_D, 5) +
        rect(70, 66, 36, 34, WHITE, rx=5, sw=2.5) + rect(70, 66, 36, 9, YEL, rx=4, sw=2.5) + path("M78,84 L84,90 L96,80", sw=3, c=TEAL) + sparkle(100, 24, 8))
def ic_part_huis():
    return icon(blob(60, 62, 46, 44, MINT) +
        path("M24,60 L60,26 L96,60", sw=3.5) + path("M32,58 L32,98 L88,98 L88,58", fill=CREAM, sw=3) +
        path("M30,60 L60,30 L90,60Z", fill=TEAL_D, sw=3) + rect(52, 74, 16, 24, TEAL, rx=2, sw=2.5) +
        rect(38, 66, 12, 12, BLUE_L, rx=1, sw=2) + rect(70, 66, 12, 12, BLUE_L, rx=1, sw=2) +
        sparkle(18, 40, 8) + sparkle(104, 42, 9) + sparkle(100, 96, 6) + sparkle(20, 92, 6) + sparkle(60, 12, 7))
def ic_part_grotekuis():
    return icon(blob(60, 62, 46, 44, MINT) +
        rect(20, 56, 56, 44, TAN, rx=3, sw=3) + rect(40, 56, 16, 12, YEL_D, rx=1, sw=1.8) + line(20, 72, 76, 72, "#c9a15c", 2) +
        line(84, 96, 100, 22, YEL, 6) + line(84, 96, 100, 22, INK, 2) + path("M74,96 L98,96 Q104,104 100,116 L78,116 Q72,104 74,96Z", fill=GREY_D, sw=2.5) +
        sparkle(28, 30, 9) + sparkle(64, 36, 6))
def ic_part_vakantie():
    return icon(blob(60, 62, 46, 44, MINT) + sun(92, 30, 12) +
        path("M18,66 L50,36 L82,66", sw=3.5) + path("M26,64 L26,100 L74,100 L74,64", fill=CREAM, sw=3) +
        path("M24,66 L50,40 L76,66Z", fill=TEAL_D, sw=3) + rect(44, 78, 12, 22, TEAL, rx=2, sw=2.5) +
        f'<g transform="translate(90,84)"><circle cx="0" cy="0" r="10" fill="{YEL}" {stroke(2.5)}/><circle cx="0" cy="0" r="3.5" fill="{WHITE}" {stroke(1.5)}/>'
        f'<rect x="8" y="-3" width="22" height="6" rx="2" fill="{YEL}" {stroke(2.2)}/><rect x="20" y="3" width="4" height="5" fill="{YEL}" {stroke(1.5)}/></g>' +
        sparkle(18, 30, 7))

ICONS = {
    "icon-prijs.svg": ic_prijslabel, "icon-verzekerd.svg": ic_schild, "icon-team.svg": ic_badge, "icon-factuur.svg": ic_factuur,
    "stap-vraag.svg": ic_stap_vraag, "stap-offerte.svg": ic_stap_offerte, "stap-plan.svg": ic_stap_plan,
    "stap-controle.svg": ic_stap_controle, "stap-herhaal.svg": ic_stap_herhaal,
    "part-raam.svg": ic_part_raam, "part-huis.svg": ic_part_huis, "part-grotekuis.svg": ic_part_grotekuis, "part-vakantie.svg": ic_part_vakantie,
}
FILES.update(ICONS)

if __name__ == "__main__":
    total = 0
    for name, fn in FILES.items():
        s = fn()
        p = os.path.join(OUT, name)
        with open(p, "w", encoding="utf-8") as f: f.write(s)
        total += len(s.encode())
        print(f"{name:28s} {len(s.encode())/1024:5.1f} KB")
    print(f"\n{len(FILES)} bestanden, {total/1024:.0f} KB totaal")
