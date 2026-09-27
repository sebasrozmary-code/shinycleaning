# Shiny Cleaning — huisstijl

## Lettertypes
| Gebruik | Lettertype | Bestand |
|---|---|---|
| Merknaam "Shiny Cleaning", accenten | **Lobster** | `fonts/Lobster-Regular.ttf` |
| Alle andere tekst | **Open Sans** (Regular / SemiBold / Bold) | `fonts/OpenSans-*.ttf` |

Beide zijn gratis Google Fonts onder de SIL Open Font License (zie `fonts/OFL-*.txt`):
vrij te gebruiken in Word, Canva, drukwerk, belettering van de bestelwagen en op de website.
Installeren op Mac: dubbelklik op het `.ttf`-bestand → *Installeer lettertype*.

## Kleuren
| Naam | HEX | Gebruik |
|---|---|---|
| Teal | `#17A2A2` | merknaam, knoppen, accenten |
| Donker teal | `#0A4D4D` | donkere vlakken, footer |
| Geel | `#F6BF45` | sterretjes, highlights |
| Groen | `#86C94A` | illustraties, vinkjes |
| Inkt | `#1E2B31` | tekst, lijnen in illustraties |
| Mint | `#EEF8F8` | lichte achtergronden |

## Wordmarks
Tekst omgezet naar vectorpaden: altijd scherp, lettertype niet nodig.

| Bestand | Wanneer |
|---|---|
| `shiny-cleaning-wordmark.svg/.png` | brieven, offertes, e-mailhandtekening, website |
| `shiny-cleaning-gestapeld.svg/.png` | vierkante plekken: social media, stickers, visitekaartje |
| `…-wit.svg/.png` | op donkere of teal achtergrond |

PNG's zijn 2400 px breed met transparante achtergrond. Gebruik voor drukwerk altijd de SVG.
Het ronde illustratielogo (`../images/logo-shiny-cleaning.png`) blijft bruikbaar vanaf ongeveer 150 px breed.
Kleiner wordt het onleesbaar: gebruik daar de wordmark.

Opnieuw genereren: `python3 tools/wordmark.py` (daarna PNG's opnieuw exporteren).
