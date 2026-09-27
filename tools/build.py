#!/usr/bin/env python3
"""
Bouwt alle Nederlandstalige landingspagina's van shinycleaning-kempen.be en houdt
header, footer, knoppen en versienummers op de bestaande pagina's gelijk.

    python3 tools/build.py

Inhoud staat in tools/inhoud/ (diensten, gemeenten, overige pagina's).
Bedrijfsgegevens staan hieronder in BIZ: vul ze één keer in, alles volgt.
"""
import hashlib, html, json, os, re, sys
from datetime import date
from urllib.parse import quote

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from inhoud import diensten as D, steden as S, overig as O   # noqa: E402

SITE = "https://www.shinycleaning-kempen.be"
TODAY = date.today().isoformat()

# ---------------------------------------------------------------- bedrijf --
BIZ = {
    "name": "Shiny Cleaning",
    "tel": "+32466307915",
    "tel_display": "0466 30 79 15",
    "wa": "32466307915",
    "email": "info@shinycleaning.be",
    "street": None,            # bv. "Voorbeeldstraat 12" — None = niet tonen
    "postcode": "2440",
    "city": "Geel",
    "vat": None,               # bv. "BE 0123.456.789" — verplicht op een bedrijfssite, invullen zodra gekend
    "hours": [("Maandag – vrijdag", "08.00 – 18.00"), ("Zaterdag", "09.00 – 13.00"), ("Zondag", "gesloten")],
    "geo": (51.1650, 4.9900),
}
ORG_ID = SITE + "/#organisatie"

def esc(s): return html.escape(s, quote=True)

def wa_url(text): return f"https://wa.me/{BIZ['wa']}?text={quote(text)}"

def asset_version():
    h = hashlib.sha1()
    for f in ("style.css", "site.js"):
        h.update(open(os.path.join(ROOT, f), "rb").read())
    return h.hexdigest()[:8]
V = asset_version()

# ------------------------------------------------------------------ iconen --
ICO_CHAT = ('<svg class="ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" '
            'd="M12 3C6.9 3 3 6.6 3 11c0 2.2 1 4.2 2.6 5.6L5 21l4.2-2.1c.9.2 1.8.3 2.8.3 5.1 0 9-3.6 9-8.1S17.1 3 12 3Zm-4 9.3a1.3 1.3 0 1 1 0-2.6 1.3 1.3 0 0 1 0 2.6Zm4 0a1.3 1.3 0 1 1 0-2.6 1.3 1.3 0 0 1 0 2.6Zm4 0a1.3 1.3 0 1 1 0-2.6 1.3 1.3 0 0 1 0 2.6Z"/></svg>')
ICO_PHONE = ('<svg class="ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" '
             'd="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1l-2.3 2.2Z"/></svg>')
ICO_CHEVRON = ('<svg viewBox="0 0 12 12" aria-hidden="true" focusable="false"><path d="M2 4.5 6 8.5 10 4.5" fill="none" '
               'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
BRAND_MARK = ('<svg class="brand-mark" viewBox="0 0 64 64" aria-hidden="true" focusable="false">'
              '<path d="M26,6 Q26,32 50,32 Q26,32 26,58 Q26,32 2,32 Q26,32 26,6Z" fill="#f6bf45" stroke="#1e2b31" stroke-width="3" stroke-linejoin="round"/>'
              '<path d="M52,4 Q52,14 62,14 Q52,14 52,24 Q52,14 42,14 Q52,14 52,4Z" fill="#f6bf45" stroke="#1e2b31" stroke-width="2.2" stroke-linejoin="round"/></svg>')

# ------------------------------------------------------------- navigatie --
def nav_items():
    services = [(d["kort"], f"/{d['slug']}/") for d in D.DIENSTEN if not d.get("b2b")]
    services += [(g["kort"], f"/{g['slug']}/") for g in D.GIDSEN]
    b2b = [(d["kort"], f"/{d['slug']}/") for d in D.DIENSTEN if d.get("b2b")]
    b2b += [("Glasbewassing voor bedrijven", "/ruitenwasser/#bedrijven"), ("Werfopkuis voor aannemers", "/opleveringsschoonmaak/#werfopkuis")]
    return [
        ("Diensten", "/#diensten", services),
        ("Bedrijven", "/kantoorschoonmaak/", b2b),
        ("Particulieren", "/#particulieren", None),
        ("Prijzen", "/prijzen/", None),
        ("Werkgebied", "/werkgebied/", None),
        ("Over ons", "/#over-ons", None),
        ("FAQ", "/#faq", None),
    ]

def header(current="/"):
    lis = []
    for label, url, sub in nav_items():
        cur = ' aria-current="page"' if url == current else ""
        if sub:
            sid = "sub-" + re.sub(r"[^a-z]", "", label.lower())
            CUR = ' aria-current="page"'
            subs = "".join(f'<li><a href="{u}"{CUR if u == current else ""}>{esc(l)}</a></li>' for l, u in sub)
            lis.append(f'<li class="has-sub"><a href="{url}"{cur}>{esc(label)}</a>'
                       f'<button class="sub-toggle" type="button" aria-expanded="false" aria-controls="{sid}" '
                       f'aria-label="{esc(label)}: toon submenu">{ICO_CHEVRON}</button>'
                       f'<ul class="sub" id="{sid}">{subs}</ul></li>')
        else:
            lis.append(f'<li><a href="{url}"{cur}>{esc(label)}</a></li>')
    return f'''<header class="site-header" id="top">
  <div class="wrap header-inner">
    <a class="brand" href="/" aria-label="Shiny Cleaning — naar de homepagina">
      {BRAND_MARK}
      <span class="brand-text">
        <span class="brand-name">Shiny Cleaning</span>
        <span class="brand-tag">Glazen wassen &amp; schoonmaakservice</span>
      </span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav">
      <span class="nav-toggle-bars" aria-hidden="true"></span>
      <span class="nav-toggle-label">Menu</span>
    </button>
    <nav class="primary-nav" id="primary-nav" aria-label="Hoofdnavigatie">
      <ul class="nav-list">
        {"".join(lis)}
      </ul>
    </nav>
    <ul class="lang-switch" aria-label="Taalkeuze">
      <li><a class="is-current" href="/" hreflang="nl" lang="nl" aria-current="true">NL</a></li>
      <li><a href="/fr/" hreflang="fr" lang="fr">FR</a></li>
      <li><a href="/en/" hreflang="en" lang="en">EN</a></li>
    </ul>
    <div class="header-cta">
      <a class="btn btn-ghost btn-phone" href="tel:{BIZ['tel']}"><span class="btn-phone-label">Bel</span> {BIZ['tel_display']}</a>
      <a class="btn btn-primary" href="/#offerte">Gratis offerte</a>
    </div>
  </div>
</header>'''

# gemeenten in de footer (de rest staat op /werkgebied/ en in de gemeentelijsten op elke dienstpagina)
FOOTER_STEDEN = ["Geel", "Mol", "Turnhout", "Herentals", "Westerlo", "Heist-op-den-Berg", "Balen", "Laakdal", "Beringen", "Diest", "Aarschot"]

def footer():
    services = "".join(f'<li><a href="/{d["slug"]}/">{esc(d["kort"])}</a></li>' for d in D.DIENSTEN if not d.get("b2b"))
    services += "".join(f'<li><a href="/{g["slug"]}/">{esc(g["kort"])}</a></li>' for g in D.GIDSEN)
    b2b = "".join(f'<li><a href="/{d["slug"]}/">{esc(d["kort"])}</a></li>' for d in D.DIENSTEN if d.get("b2b"))
    b2b += '<li><a href="/ruitenwasser/#bedrijven">Glasbewassing voor bedrijven</a></li>'
    b2b += '<li><a href="/opleveringsschoonmaak/#werfopkuis">Werfopkuis voor aannemers</a></li>'
    b2b += '<li><a href="/prijzen/">Prijzen</a></li>'
    by = {c["naam"]: c for c in S.STEDEN}
    towns = "".join(f'<li><a href="/ruitenwasser/{by[n]["slug"]}/">Ruitenwasser {esc(n)}</a></li>' for n in FOOTER_STEDEN)
    street = f"{esc(BIZ['street'])}<br>" if BIZ["street"] else ""
    vat = f"<br>Ondernemingsnr. {esc(BIZ['vat'])}" if BIZ["vat"] else ""
    hours = "<br>".join(f"{esc(a)}: {esc(b)}" for a, b in BIZ["hours"])
    return f'''<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <img class="footer-logo" src="/images/logo-shiny-cleaning.png" alt="Shiny Cleaning" width="500" height="456" loading="lazy">
      <p class="footer-tagline">Glazenwasser en schoonmaakbedrijf uit Geel, voor particulieren, bedrijven, syndici en VME's in de Kempen, Antwerpen, Limburg en Vlaams-Brabant.</p>
    </div>
    <div class="footer-col">
      <p class="footer-title">Diensten</p>
      <ul class="footer-list">{services}</ul>
    </div>
    <div class="footer-col">
      <p class="footer-title">Voor bedrijven</p>
      <ul class="footer-list">{b2b}</ul>
    </div>
    <div class="footer-col">
      <p class="footer-title">Werkgebied</p>
      <ul class="footer-list">{towns}<li><a href="/werkgebied/">Alle gemeenten →</a></li></ul>
    </div>
    <div class="footer-col">
      <p class="footer-title">Contact</p>
      <address class="footer-address">
        <strong>{esc(BIZ['name'])}</strong><br>
        {street}{BIZ['postcode']} {esc(BIZ['city'])}, België<br><br>
        <a href="tel:{BIZ['tel']}">{BIZ['tel_display']}</a><br>
        <a href="{wa_url('Hallo Shiny Cleaning! ')}" rel="noopener">WhatsApp</a><br>
        <a href="mailto:{BIZ['email']}">{BIZ['email']}</a>{vat}
      </address>
      <p class="footer-hours">{hours}</p>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <p>&copy; <span id="jaar">{date.today().year}</span> Shiny Cleaning — Glazen wassen &amp; schoonmaakservice</p>
    <ul class="footer-legal">
      <li><a href="/privacy/">Privacybeleid</a></li>
      <li><a href="/privacy/#cookies">Cookies</a></li>
    </ul>
  </div>
</footer>'''

def mobile_bar(wa_text):
    return (f'<div class="mobile-bar" aria-label="Snel contact">'
            f'<a class="mobile-bar-btn mobile-bar-btn-wa" href="{wa_url(wa_text)}" rel="noopener">{ICO_CHAT} WhatsApp</a>'
            f'<a class="mobile-bar-btn" href="tel:{BIZ["tel"]}">{ICO_PHONE} Bellen</a>'
            f'<a class="mobile-bar-btn mobile-bar-btn-primary" href="/#offerte">Offerte</a></div>')

def float_wa(wa_text):
    return (f'<a class="float-wa" href="{wa_url(wa_text)}" rel="noopener" aria-label="Stuur ons een bericht via WhatsApp">'
            f'{ICO_CHAT}<span>WhatsApp ons</span></a>')

def buttons(wa_text, wa_label="Prijs via WhatsApp", size="btn-lg", outline=True):
    b = f'<a class="btn btn-wa {size}" href="{wa_url(wa_text)}" rel="noopener">{ICO_CHAT} {esc(wa_label)}</a>'
    b += f'<a class="btn {"btn-outline" if outline else "btn-ghost"} {size}" href="tel:{BIZ["tel"]}">{ICO_PHONE} Bel {BIZ["tel_display"]}</a>'
    return b

def cta_band(wa_text, title="Stuur een foto, krijg vandaag nog een prijs",
             text="Via WhatsApp gaat het het snelst: een paar foto's en uw gemeente volstaan meestal voor een vaste prijs."):
    return f'''<section class="cta-band" aria-labelledby="cta-band-title">
  <div class="wrap cta-band-inner">
    <div><h2 id="cta-band-title">{esc(title)}</h2><p>{esc(text)}</p></div>
    <div class="hero-actions">{buttons(wa_text)}</div>
  </div>
</section>'''

# ---------------------------------------------------------------- schema --
def org_node():
    addr = {"@type": "PostalAddress", "addressLocality": BIZ["city"], "postalCode": BIZ["postcode"],
            "addressRegion": "Antwerpen", "addressCountry": "BE"}
    if BIZ["street"]: addr["streetAddress"] = BIZ["street"]
    n = {"@type": ["LocalBusiness", "HomeAndConstructionBusiness", "CleaningService"], "@id": ORG_ID,
         "name": BIZ["name"], "url": SITE + "/", "telephone": BIZ["tel"], "email": BIZ["email"],
         "image": SITE + "/images/og-image.jpg", "logo": SITE + "/images/logo-shiny-cleaning.png",
         "priceRange": "€€", "address": addr,
         "geo": {"@type": "GeoCoordinates", "latitude": BIZ["geo"][0], "longitude": BIZ["geo"][1]}}
    if BIZ["vat"]: n["vatID"] = BIZ["vat"]
    return n

def crumbs_node(url, items):
    return {"@type": "BreadcrumbList", "@id": url + "#breadcrumbs", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)]}

def faq_node(url, faq):
    return {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
        for q, a in faq]}

def webpage_node(url, title, about=None):
    n = {"@type": "WebPage", "@id": url, "url": url, "name": title, "inLanguage": "nl-BE",
         "isPartOf": {"@id": SITE + "/#website"}, "dateModified": TODAY}
    if about: n["about"] = {"@id": about}
    return n

def ld(nodes):
    return ('<script type="application/ld+json">\n' +
            json.dumps({"@context": "https://schema.org", "@graph": nodes}, ensure_ascii=False, indent=1) +
            "\n</script>")

# ------------------------------------------------------------ bouwstenen --
def breadcrumbs(items):
    lis = []
    for i, (n, u) in enumerate(items):
        if i == len(items) - 1:
            lis.append(f'<li><span aria-current="page">{esc(n)}</span></li>')
        else:
            lis.append(f'<li><a href="{u}">{esc(n)}</a></li>')
    return f'<nav class="breadcrumbs" aria-label="Kruimelpad"><ol class="wrap">{"".join(lis)}</ol></nav>'

def faq_html(faq, heading, hid="faq-titel"):
    items = "".join(f'<details class="faq-item"><summary>{esc(q)}</summary><div class="faq-answer"><p>{a}</p></div></details>'
                    for q, a in faq)
    return f'<section aria-labelledby="{hid}"><h2 id="{hid}">{esc(heading)}</h2><div class="faq">{items}</div></section>'

def price_table(rows, caption):
    trs = "".join(f'<tr><th scope="row">{esc(a)}</th><td class="num">{esc(b)}</td><td>{esc(c)}</td></tr>' for a, b, c in rows)
    return (f'<div class="table-scroll"><table class="price-table"><caption class="sr-only">{esc(caption)}</caption>'
            f'<thead><tr><th scope="col">Wat</th><th scope="col">Richtprijs</th><th scope="col">Toelichting</th></tr></thead>'
            f'<tbody>{trs}</tbody></table></div>')

def hero(eyebrow, h1, hl, lead, points, wa_text, ill, ill_alt, badge=None, note=None):
    pts = "".join(f"<li>{p}</li>" for p in points)
    badge_html = (f'<figcaption class="hero-badge"><strong>{esc(badge[0])}</strong><span>{esc(badge[1])}</span></figcaption>'
                  if badge else "")
    note = note or 'Liever schriftelijk? <a href="/#offerte">Vul het offerteformulier in</a> — antwoord binnen 24 uur.'
    return f'''<section class="page-hero" aria-labelledby="page-title">
  <div class="wrap page-hero-inner">
    <div class="page-hero-copy">
      <p class="eyebrow">{esc(eyebrow)}</p>
      <h1 id="page-title">{esc(h1)} <span class="hl">{esc(hl)}</span></h1>
      <p class="lead">{lead}</p>
      <ul class="hero-points">{pts}</ul>
      <div class="hero-actions">{buttons(wa_text)}</div>
      <p class="hero-note">{note}</p>
    </div>
    <figure class="page-hero-media">
      <img src="/images/ill/{ill}.svg" alt="{esc(ill_alt)}" width="400" height="320" fetchpriority="high">
      {badge_html}
    </figure>
  </div>
</section>'''

def side_card(title, price, price_sub, wa_text, links_title=None, links=None):
    links_html = ""
    if links:
        li = "".join(f'<li><a href="{u}">{esc(l)}</a></li>' for l, u in links)
        links_html = f'<nav class="side-links" aria-label="{esc(links_title)}"><h2>{esc(links_title)}</h2><ul>{li}</ul></nav>'
    return f'''<aside class="side-cta" aria-label="Prijs en contact">
  <div class="side-card">
    <p class="eyebrow">{esc(title)}</p>
    <p class="side-price">{esc(price)}</p>
    <p class="side-price-sub">{esc(price_sub)}</p>
    <a class="btn btn-wa" href="{wa_url(wa_text)}" rel="noopener">{ICO_CHAT} Foto sturen via WhatsApp</a>
    <a class="btn btn-outline" href="tel:{BIZ['tel']}">{ICO_PHONE} Bel {BIZ['tel_display']}</a>
    <ul class="tick"><li>Vaste prijs vóór we starten</li><li>Verzekerd werk, met factuur</li><li>Antwoord binnen 24 uur</li></ul>
  </div>
  {links_html}
</aside>'''

# Lange samenstellingen mogen in smalle kaarten netjes afbreken (zachte koppeltekens, enkel in zichtbare kaarttitels)
SOFT = {"Opleveringsschoonmaak": "Opleverings&shy;schoonmaak", "Kantoorschoonmaak": "Kantoor&shy;schoonmaak",
        "Gemeenschappelijke": "Gemeenschap&shy;pelijke", "Zonnepanelen": "Zonne&shy;panelen"}
def soft(text):
    h = esc(text)
    for k, v in SOFT.items(): h = h.replace(k, v)
    return h

def related(slugs):
    by = {d["slug"]: d for d in D.DIENSTEN + D.GIDSEN}
    cards = []
    for s in slugs:
        d = by[s]
        cards.append(f'<article class="related-card"><img src="/images/ill/{d["ill"]}.svg" alt="" width="84" height="68" loading="lazy">'
                     f'<div><h3><a href="/{s}/">{soft(d["kort"])}</a></h3><p>{esc(d["kaart"])}</p></div></article>')
    return f'''<section class="section" aria-labelledby="related-title">
  <div class="wrap">
    <h2 id="related-title">Vaak gecombineerd in dezelfde beurt</h2>
    <div class="related-grid">{"".join(cards)}</div>
  </div>
</section>'''

def towns_block(title, intro, current=None):
    pills = "".join(
        f'<li><a href="/ruitenwasser/{c["slug"]}/">{esc(c["naam"])}</a></li>' for c in S.STEDEN if c["slug"] != current)
    extra = "".join(f"<li><span>{esc(t)}</span></li>" for t in O.OOK_IN)
    return f'''<section class="section section-alt" aria-labelledby="towns-title">
  <div class="wrap">
    <div class="section-head"><h2 id="towns-title">{esc(title)}</h2><p class="section-intro">{intro}</p></div>
    <ul class="pill-list">{pills}{extra}</ul>
    <p class="section-foot"><a class="link-more" href="/werkgebied/">Bekijk ons volledige werkgebied →</a></p>
  </div>
</section>'''

# ------------------------------------------------------------------ pagina --
def page(path, title, desc, body, wa_text, nodes, current, og_type="website", robots="index, follow, max-image-preview:large"):
    url = SITE + path
    doc = f'''<!DOCTYPE html>
<html lang="nl-BE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{robots}">
<meta name="geo.region" content="BE-VAN">
<meta name="geo.placename" content="Geel">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="nl_BE">
<meta property="og:site_name" content="Shiny Cleaning">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/images/logo-shiny-cleaning.png" type="image/png">
<link rel="preload" href="/fonts/opensans.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css?v={V}">
</head>
<body>
<a class="skip-link" href="#main">Naar hoofdinhoud</a>
{header(current)}
<main id="main">
{body}
</main>
{cta_band(wa_text)}
{footer()}
{mobile_bar(wa_text)}
{float_wa(wa_text)}
<script src="/site.js?v={V}" defer></script>
{ld(nodes)}
</body>
</html>
'''
    out = os.path.join(ROOT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(doc)
    return path

# ------------------------------------------------------------ dienstpagina --
def render_dienst(d):
    path = f"/{d['slug']}/"; url = SITE + path
    wa = f"Hallo Shiny Cleaning! Ik wil graag een prijs voor {d['wa']}. Mijn gemeente is: "
    items = [("Home", "/"), (d["kort"], path)]
    secties = "".join(f'<section id="{sid}" aria-labelledby="{sid}-t"><h2 id="{sid}-t">{esc(h)}</h2>{body}</section>'
                      for sid, h, body in d["secties"])
    prijs = (f'<section id="prijs" aria-labelledby="prijs-t"><h2 id="prijs-t">{esc(d["prijs_titel"])}</h2>'
             f'<p>{d["prijs_intro"]}</p>{price_table(d["prijzen"], "Richtprijzen " + d["kort"])}'
             f'{d.get("prijs_na", "")}'
             f'<p><a class="link-more" href="/prijzen/">Alle prijzen en rekenvoorbeelden →</a></p></section>')
    cta = (f'<div class="inline-cta"><p>{esc(d.get("tussen_cta", "Twijfelt u over de prijs? Stuur ons een foto, dan weet u het vandaag nog."))}</p>'
           f'<a class="btn btn-wa" href="{wa_url(wa)}" rel="noopener">{ICO_CHAT} WhatsApp</a></div>')
    others = [(x["kort"], f"/{x['slug']}/") for x in D.DIENSTEN if x["slug"] != d["slug"]]
    body = (breadcrumbs(items) +
            hero(d["eyebrow"], d["h1"], d["hl"], d["lead"], d["punten"], wa, d["ill"], d["ill_alt"], d.get("badge")) +
            f'<div class="wrap content-layout"><article class="prose">{secties}{cta}{prijs}'
            f'{faq_html(d["faq"], "Veelgestelde vragen over " + d["faq_onderwerp"])}</article>'
            f'{side_card("Richtprijs", d["badge"][0], d["badge"][1], wa, "Andere diensten", others)}</div>' +
            towns_block(d.get("towns_title", f"{d['kort']} in uw gemeente"), d["towns_intro"]) +
            related(d["gerelateerd"]))
    service = {"@type": "Service", "@id": url + "#dienst", "name": d["naam"], "serviceType": d["service_type"],
               "description": re.sub(r"<[^>]+>", "", d["lead"]), "provider": {"@id": ORG_ID}, "url": url,
               "areaServed": [{"@type": "AdministrativeArea", "name": n} for n in ("Kempen", "Provincie Antwerpen", "Limburg", "Vlaams-Brabant")]
                             + [{"@type": "City", "name": c["naam"]} for c in S.STEDEN]}
    if d.get("price_spec"):
        lo, hi, unit = d["price_spec"]
        service["offers"] = {"@type": "Offer", "priceCurrency": "EUR",
                             "priceSpecification": {"@type": "UnitPriceSpecification", "minPrice": lo, "maxPrice": hi,
                                                    "priceCurrency": "EUR", "unitText": unit}}
    nodes = [org_node(), service, webpage_node(url, d["title"], url + "#dienst"), crumbs_node(url, items), faq_node(url, d["faq"])]
    return page(path, d["title"], d["desc"], body, wa, nodes, path)

# ---------------------------------------------------------- gemeentepagina --
def render_stad(c):
    path = f"/ruitenwasser/{c['slug']}/"; url = SITE + path
    wa = f"Hallo Shiny Cleaning! Ik woon in {c['naam']} en wil graag een prijs voor: "
    items = [("Home", "/"), ("Ramen wassen", "/ruitenwasser/"), (c["naam"], path)]
    secties = "".join(f'<section id="{sid}" aria-labelledby="{sid}-t"><h2 id="{sid}-t">{esc(h)}</h2>{body}</section>'
                      for sid, h, body in c["secties"])
    # diensten in deze gemeente: korte lijst met links (lokale zin waar opgegeven)
    lokaal = c.get("diensten_lokaal", {})
    lis = "".join(
        f'<li><a href="/{d["slug"]}/"><strong>{esc(d["kort"])}</strong></a> — {lokaal.get(d["slug"], esc(d["kaart"]))}</li>'
        for d in D.DIENSTEN)
    diensten = (f'<section id="diensten-{c["slug"]}" aria-labelledby="dl-t"><h2 id="dl-t">Onze diensten in {esc(c["naam"])}</h2>'
                f'<ul>{lis}</ul></section>')
    deel = "".join(f"<li><span>{esc(x)}</span></li>" for x in c["deelgemeenten"])
    deel_html = (f'<section id="deelgemeenten" aria-labelledby="dg-t"><h2 id="dg-t">{esc(c["deel_titel"])}</h2>'
                 f'<p>{c["deel_intro"]}</p><ul class="pill-list">{deel}</ul></section>')
    prijs = (f'<section id="prijs" aria-labelledby="prijs-t"><h2 id="prijs-t">Wat kost een ruitenwasser in {esc(c["naam"])}?</h2>'
             f'<p>{c["prijs_tekst"]}</p>'
             f'{price_table(O.PRIJS_RAMEN, "Richtprijzen ramen wassen in " + c["naam"])}'
             f'<p><a class="link-more" href="/prijzen/">Alle prijzen: zonnepanelen, dakgoten, gevels en meer →</a></p></section>')
    cta = (f'<div class="inline-cta"><p>Woont u in {esc(c["naam"])}? Stuur een foto van uw woning, dan krijgt u vandaag een vaste prijs.</p>'
           f'<a class="btn btn-wa" href="{wa_url(wa)}" rel="noopener">{ICO_CHAT} WhatsApp</a></div>')
    buren = [(f"Ruitenwasser {b}", f"/ruitenwasser/{S.SLUG[b]}/") for b in c["buren"]]
    body = (breadcrumbs(items) +
            hero(c["eyebrow"], c["h1"], c["hl"], c["lead"], c["punten"], wa, c["ill"], c["ill_alt"],
                 ("Ramen vanaf €55", f"in {c['naam']}, rijwoning buitenzijde")) +
            f'<div class="wrap content-layout"><article class="prose">{secties}{diensten}{cta}{deel_html}{prijs}'
            f'{faq_html(c["faq"], "Vragen uit " + c["naam"])}</article>'
            f'{side_card("Ramen wassen in " + c["naam"], "vanaf €55", "per beurt, rijwoning buitenzijde", wa, "Ruitenwasser in de buurt", buren)}</div>' +
            towns_block("Ook in de buurt van " + c["naam"], "Vanuit Geel werken we in de hele Kempen en daarbuiten. Per gemeente leest u wat we er doen, waar we komen en wat het kost.", c["slug"]) +
            related(["ruitenwasser", "zonnepanelen-reinigen", "dakgoot-reinigen"]))
    service = {"@type": "Service", "@id": url + "#dienst", "name": f"Ruitenwasser en schoonmaakbedrijf in {c['naam']}",
               "serviceType": "Glazenwassen en schoonmaak", "provider": {"@id": ORG_ID}, "url": url,
               "areaServed": [{"@type": "City", "name": c["naam"]}] + [{"@type": "Place", "name": x} for x in c["deelgemeenten"]]}
    nodes = [org_node(), service, webpage_node(url, c["title"], url + "#dienst"), crumbs_node(url, items), faq_node(url, c["faq"])]
    return page(path, c["title"], c["desc"], body, wa, nodes, path)

# ------------------------------------------------------------ vrije pagina --
def render_vrij(p):
    path = p["path"]; url = SITE + path
    items = [("Home", "/"), (p["crumb"], path)]
    body = breadcrumbs(items) + p["body"](sys.modules[__name__])
    nodes = [org_node(), webpage_node(url, p["title"]), crumbs_node(url, items)]
    if p.get("faq"): nodes.append(faq_node(url, p["faq"]))
    return page(path, p["title"], p["desc"], body, p["wa"], nodes, path, robots=p.get("robots", "index, follow, max-image-preview:large"))

# ------------------------------------------- bestaande pagina's bijwerken --
def inject(path, marker, content):
    fp = os.path.join(ROOT, path); s = open(fp, encoding="utf-8").read()
    pat = re.compile(rf"(<!-- BUILD:{marker} -->).*?(<!-- /BUILD:{marker} -->)", re.S)
    if not pat.search(s): raise SystemExit(f"marker {marker} ontbreekt in {path}")
    s = pat.sub(lambda m: m.group(1) + "\n" + content + "\n" + m.group(2), s)
    open(fp, "w", encoding="utf-8").write(s)

def bump_assets(path, prefix):
    fp = os.path.join(ROOT, path); s = open(fp, encoding="utf-8").read()
    s = re.sub(r'href="[./]*style\.css(\?v=[^"]*)?"', f'href="{prefix}style.css?v={V}"', s)
    s = re.sub(r'src="[./]*site\.js(\?v=[^"]*)?"', f'src="{prefix}site.js?v={V}"', s)
    open(fp, "w", encoding="utf-8").write(s)

def sitemap(paths):
    alt = ('<xhtml:link rel="alternate" hreflang="nl-be" href="{s}/"/><xhtml:link rel="alternate" hreflang="fr-be" href="{s}/fr/"/>'
           '<xhtml:link rel="alternate" hreflang="en" href="{s}/en/"/><xhtml:link rel="alternate" hreflang="x-default" href="{s}/"/>').format(s=SITE)
    urls = []
    for p, prio in paths:
        a = alt if p in ("/", "/fr/", "/en/") else ""
        urls.append(f"  <url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{prio}</priority>{a}</url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(xml)

def main():
    built = [("/", "1.0"), ("/fr/", "0.7"), ("/en/", "0.7")]
    for d in D.DIENSTEN: built.append((render_dienst(d), "0.9"))
    for g in D.GIDSEN: built.append((render_dienst(g), "0.8"))
    for c in S.STEDEN: built.append((render_stad(c), "0.8"))
    for p in O.PAGINAS:
        path = render_vrij(p)
        if not p.get("robots", "").startswith("noindex"): built.append((path, p.get("prio", "0.6")))
    # homepage: header, footer, knoppen en dienstkaarten gelijk trekken
    home_wa = "Hallo Shiny Cleaning! Ik wil graag een prijs voor: "
    inject("index.html", "HEADER", header("/"))
    inject("index.html", "HEROCTA",
           f'<div class="hero-actions">{buttons(home_wa, "Stuur een foto via WhatsApp")}</div>\n'
           f'      <p class="hero-note">Prijs meestal dezelfde dag. Liever schriftelijk? <a href="#offerte">Vul het offerteformulier in</a>.</p>')
    cards = []
    for d in D.DIENSTEN:
        if d.get("b2b"): continue
        cards.append(f'''      <article class="service">
        <figure class="service-media"><img src="/images/ill/{d["ill"]}.svg" alt="" width="400" height="320" loading="lazy"></figure>
        <div class="service-body">
          <h3><a href="/{d["slug"]}/">{soft(d["kort"])}</a></h3>
          <p>{esc(d["kaart"])}</p>
          <p class="service-price"><strong>{esc(d["badge"][0])}</strong> · {esc(d["badge"][1])}</p>
          <span class="service-more" aria-hidden="true">Prijzen en werkwijze →</span>
        </div>
      </article>''')
    inject("index.html", "DIENSTEN", "\n".join(cards))
    inject("index.html", "FOOTER", footer() + "\n" + mobile_bar(home_wa) + "\n" + float_wa(home_wa))
    bump_assets("index.html", "/"); bump_assets("404.html", "/")
    bump_assets("fr/index.html", "../"); bump_assets("en/index.html", "../")
    sitemap(built)
    print(f"{len(built)} URL's in sitemap, assets v={V}")

if __name__ == "__main__":
    main()
