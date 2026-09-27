# Shiny Cleaning — website

Statische drietalige one-pager voor Shiny Cleaning (Geel, Kempen).
Live op https://www.shinycleaning-kempen.be — gehost bij Hostinger, gedeployed vanuit deze repo.

```
index.html        NL (hoofdtaal)
fr/index.html     FR
en/index.html     EN
style.css         gedeeld door alle talen
images/ill/       huisstijl-illustraties (SVG), gegenereerd door tools/illustraties.py
images/           logo + og-image
sitemap.xml · robots.txt · .htaccess · 404.html
```

## Aanpassen
- **Teksten**: rechtstreeks in de drie `index.html`-bestanden. Secties en klassen zijn identiek in NL/FR/EN.
- **Stijl**: `style.css`, alle kleuren staan bovenaan als custom properties.
- **Illustraties**: pas `tools/illustraties.py` aan en run `python3 tools/illustraties.py` — schrijft alle SVG's opnieuw.

## Nog in te vullen vóór livegang
- BTW-nummer en straatadres: zoek op `todo` in de drie HTML-bestanden (footer + JSON-LD).
- Prijzen in de tabel en in de JSON-LD zijn marktrichtprijzen — bevestigen met de zaakvoerder.
- Formulier: `action="#"` koppelen aan een mailscript of formulierdienst.
- Privacybeleid, algemene voorwaarden en cookiebeleid schrijven (links staan al in de footer).
