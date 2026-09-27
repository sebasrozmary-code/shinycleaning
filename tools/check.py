#!/usr/bin/env python3
"""
SEO- en kwaliteitscontrole voor alle pagina's. Run na elke build:
    python3 tools/check.py
Controleert: titel- en descriptionlengte, unieke titels, één H1, canonical,
geldige JSON-LD, interne links en ankers, afbeeldingen, en overlap tussen
gemeentepagina's (te veel overlap = risico op 'doorway pages').
"""
import json, os, re, sys, itertools
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE = "https://www.shinycleaning-kempen.be"

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""; self._in_title = False; self.desc = None; self.canonical = None; self.robots = ""
        self.h1 = 0; self.ids = set(); self.links = []; self.imgs = []; self.ld = []; self._in_ld = False; self._buf = []
        self.text = []; self._skip = 0; self.stack = []; self.lang = None
    def handle_starttag(self, t, a):
        a = dict(a)
        if t == "html": self.lang = a.get("lang")
        if "id" in a: self.ids.add(a["id"])
        if t == "title": self._in_title = True
        if t == "meta" and a.get("name") == "description": self.desc = a.get("content", "")
        if t == "meta" and a.get("name") == "robots": self.robots = a.get("content", "")
        if t == "link" and a.get("rel") == "canonical": self.canonical = a.get("href")
        if t == "h1": self.h1 += 1
        if t == "a" and a.get("href"): self.links.append(a["href"])
        if t == "link" and a.get("rel") in ("stylesheet", "icon", "preload"): self.links.append(a["href"])
        if t in ("img", "script") and a.get("src"): self.imgs.append(a["src"])
        if t == "script" and a.get("type") == "application/ld+json": self._in_ld = True; self._buf = []
        if t in ("script", "style", "header", "footer", "nav"): self._skip += 1
    def handle_endtag(self, t):
        if t == "title": self._in_title = False
        if t == "script" and self._in_ld: self.ld.append("".join(self._buf)); self._in_ld = False
        if t in ("script", "style", "header", "footer", "nav"): self._skip = max(0, self._skip - 1)
    def handle_data(self, d):
        if self._in_title: self.title += d
        if self._in_ld: self._buf.append(d)
        if not self._skip: self.text.append(d)

def pages():
    for dp, dn, fn in os.walk(ROOT):
        if "/.git" in dp or "/tools" in dp or "/brand" in dp: continue
        for f in fn:
            if f.endswith(".html"): yield os.path.join(dp, f)

def url_of(fp):
    rel = os.path.relpath(fp, ROOT).replace(os.sep, "/")
    if rel.endswith("index.html"): rel = rel[:-10]
    return "/" + rel

def resolve(base_url, href):
    if href.startswith(("http://", "https://")):
        if not href.startswith(SITE): return None, None
        href = href[len(SITE):]
    if href.startswith(("mailto:", "tel:", "data:", "#")) and not href.startswith("#"): return None, None
    u = urlparse(href)
    path = u.path
    if not path:
        path = base_url
    elif not path.startswith("/"):
        base_dir = base_url if base_url.endswith("/") else base_url.rsplit("/", 1)[0] + "/"
        path = os.path.normpath(base_dir + path).replace(os.sep, "/") + ("/" if path.endswith("/") else "")
    fp = os.path.join(ROOT, unquote(path).lstrip("/"))
    if path.endswith("/") or os.path.isdir(fp): fp = os.path.join(fp, "index.html")
    return fp, u.fragment

def shingles(text, n=5):
    w = re.findall(r"[a-zà-ÿ0-9€]+", text.lower())
    return {" ".join(w[i:i + n]) for i in range(len(w) - n)}

def main():
    parsed = {}
    for fp in pages():
        p = P(); p.feed(open(fp, encoding="utf-8").read()); parsed[fp] = p
    errors, warns = [], []
    titles, descs = {}, {}
    rows = []
    for fp, p in sorted(parsed.items(), key=lambda x: url_of(x[0])):
        u = url_of(fp); noindex = "noindex" in p.robots
        tl, dl = len(p.title.strip()), len(p.desc or "")
        words = len(re.findall(r"\w+", " ".join(p.text)))
        rows.append((u, tl, dl, p.h1, words))
        if u.endswith("404.html"): continue
        if p.h1 != 1: errors.append(f"{u}: {p.h1}× H1")
        if not noindex:
            if tl > 60: warns.append(f"{u}: titel {tl} tekens (>60)")
            if not (110 <= dl <= 160): warns.append(f"{u}: description {dl} tekens")
            titles.setdefault(p.title.strip(), []).append(u); descs.setdefault(p.desc, []).append(u)
            if p.canonical != SITE + u: errors.append(f"{u}: canonical {p.canonical}")
        for block in p.ld:
            try: json.loads(block)
            except Exception as e: errors.append(f"{u}: JSON-LD ongeldig ({e})")
        for href in p.links + p.imgs:
            if href.startswith(("mailto:", "tel:")) or "wa.me" in href: continue
            tfp, frag = resolve(u, href.split("?")[0] if "?" in href and "#" not in href else href)
            if tfp is None: continue
            if not os.path.exists(tfp): errors.append(f"{u}: kapotte link {href}"); continue
            if frag and tfp in parsed and frag not in parsed[tfp].ids: errors.append(f"{u}: anker bestaat niet {href}")
    for t, us in titles.items():
        if len(us) > 1: errors.append(f"dubbele titel '{t}': {us}")
    for d, us in descs.items():
        if len(us) > 1: errors.append(f"dubbele description: {us}")

    print(f"{'URL':42s} {'titel':>5s} {'descr':>5s} {'H1':>3s} {'woorden':>8s}")
    for u, tl, dl, h1, w in rows: print(f"{u:42s} {tl:5d} {dl:5d} {h1:3d} {w:8d}")

    # overlap gemeentepagina's (alleen de lopende tekst in <main>)
    cities = {url_of(fp): shingles(" ".join(p.text)) for fp, p in parsed.items() if url_of(fp).startswith("/ruitenwasser/") and url_of(fp).count("/") == 3}
    worst = []
    for (a, sa), (b, sb) in itertools.combinations(cities.items(), 2):
        j = len(sa & sb) / max(1, len(sa | sb)); worst.append((j, a, b))
    worst.sort(reverse=True)
    if worst:
        print(f"\nOverlap gemeentepagina's (5-woord-shingles, Jaccard): max {worst[0][0]:.2f} ({worst[0][1]} ↔ {worst[0][2]}), "
              f"gemiddeld {sum(w[0] for w in worst)/len(worst):.2f}")
        if worst[0][0] > 0.45: warns.append("gemeentepagina's lijken te veel op elkaar (>0.45)")

    print(f"\n{len(parsed)} pagina's gecontroleerd — {len(errors)} fouten, {len(warns)} waarschuwingen")
    for e in errors: print("  FOUT  ", e)
    for w in warns: print("  LET OP", w)
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
