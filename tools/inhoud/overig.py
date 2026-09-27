# -*- coding: utf-8 -*-
"""Overige pagina's: prijzen, werkgebied, privacy. `body` krijgt de build-module mee (B)."""
from . import diensten as D, steden as S

OOK_IN = ["Hulshout", "Herenthout", "Grobbendonk", "Vorselaar", "Lille", "Oud-Turnhout", "Beerse", "Arendonk", "Nijlen", "Lier",
          "Mechelen", "Tessenderlo", "Ham", "Leopoldsburg", "Lommel", "Hasselt", "Scherpenheuvel-Zichem", "Tienen"]

PRIJS_RAMEN = [("Rijwoning, buitenzijde", "€55 – €70", "Per beurt, kaders en vensterbanken inbegrepen"),
               ("Halfopen bebouwing, buitenzijde", "€65 – €85", "Per beurt"),
               ("Open bebouwing, buitenzijde", "€85 – €115", "Per beurt"),
               ("Binnen- en buitenzijde", "€85 – €150", "Afhankelijk van het aantal ramen"),
               ("Rolluiken", "€12,50 – €20", "Per rolluik, samen met een beurt"),
               ("Veranda of glazen overkapping", "€120 – €280", "Glas, dak en profielen")]

# ------------------------------------------------------------------ PRIJZEN --
PRIJZEN_FAQ = [
 ("Wat kost ramen laten wassen?",
  "Voor de buitenzijde betaalt u €55 à €70 voor een rijwoning, €65 à €85 voor een halfopen en €85 à €115 voor een open bebouwing. Binnen én buiten ligt tussen €85 en €150. Met een vast schema betaalt u per beurt minder."),
 ("Wat vraagt een glazenwasser per raam?",
  "Wij rekenen per woning, niet per raam, maar omgerekend betaalt u voor de buitenzijde van een gewone rijwoning ongeveer €3 à €4 per raam. Grote raampartijen, ramen op hoogte en de binnenzijde tellen zwaarder door. Zo kent u vooraf één vaste prijs."),
 ("Wat rekent een glazenwasser per uur?",
  "Voor woningen rekenen we niet per uur maar per beurt, zodat u vooraf één vaste prijs kent. Voor kantoorschoonmaak en de schoonmaak van gemeenschappelijke delen rekenen we €30 à €45 per uur exclusief btw, of een vast maandbedrag."),
 ("Waarom staat er een prijsvork en geen vaste prijs?",
  "Omdat geen twee woningen hetzelfde zijn: het aantal ramen, de hoogte en de bereikbaarheid verschillen. De vork geeft u vooraf een eerlijk idee. Na een foto of plaatsbezoek krijgt u een vaste prijs, en die wijzigt niet meer."),
 ("Betaal ik verplaatsingskosten?",
  "Niet in ons standaard werkgebied, de Kempen. Daarbuiten kan een kleine verplaatsingsvergoeding gelden. Dat zeggen we altijd vooraf. Combineert u meerdere diensten op dezelfde dag, dan rekenen we één verplaatsing."),
 ("Is een offerte gratis?",
  "Ja, altijd en zonder verplichting. Voor de meeste klussen volstaan een paar foto's via WhatsApp. Voor grotere opdrachten komen we gratis ter plaatse kijken."),
 ("Hoe betaal ik?",
  "Na de beurt krijgt u een factuur, die u per overschrijving betaalt. Voor bedrijven en vaste contracten factureren we maandelijks."),
]

def prijzen_body(B):
    esc = B.esc
    wa = "Hallo Shiny Cleaning! Ik wil graag een prijs op maat voor: "
    blocks = []
    for d in D.DIENSTEN:
        blocks.append(f'<section id="prijs-{d["slug"]}" aria-labelledby="p-{d["slug"]}"><h2 id="p-{d["slug"]}">{esc(d["prijs_titel"])}</h2>'
                      f'<p>{d["prijs_intro"]}</p>{B.price_table(d["prijzen"], "Richtprijzen " + d["kort"])}'
                      f'<p><a class="link-more" href="/{d["slug"]}/">Meer over {esc(d["kort"].lower())} →</a></p></section>')
    toc = "".join(f'<li><a href="#prijs-{d["slug"]}">{esc(d["kort"])}</a></li>' for d in D.DIENSTEN)
    intro = f'''
<section aria-labelledby="waarom-t"><h2 id="waarom-t">Waarom wij onze prijzen gewoon op de site zetten</h2>
<p>Bijna geen enkel schoonmaakbedrijf in de Kempen toont zijn prijzen. Wij wel, omdat u vooraf wilt weten waar u aan toe bent.
Hieronder staan onze richtprijzen voor een normale situatie. U krijgt altijd een <strong>vaste prijs</strong> vóór we beginnen, en die wijzigt achteraf niet.</p>
<ul class="tick">
 <li>Prijzen voor particulieren zijn <strong>inclusief btw</strong>, prijzen voor bedrijven exclusief btw.</li>
 <li>Geen verplaatsingskosten in de Kempen. Meerdere diensten op dezelfde dag betekent één verplaatsing.</li>
 <li>Met een vast onderhoudsschema betaalt u per beurt minder dan bij een eenmalige opdracht.</li>
 <li>Een offerte is altijd gratis. Meestal volstaan een paar foto's via WhatsApp.</li>
</ul>
<nav class="callout" aria-label="Prijzen per dienst"><h3 class="callout-title">Spring naar</h3><ul class="pill-list">{toc}</ul></nav>
</section>'''
    voorbeeld = '''
<section id="rekenvoorbeeld" aria-labelledby="rv-t"><h2 id="rv-t">Rekenvoorbeeld: alles buiten in één beurt</h2>
<p>Een halfopen woning met twaalf zonnepanelen en 25 meter dakgoot, in één afspraak:</p>
<div class="table-scroll"><table class="price-table"><caption class="sr-only">Rekenvoorbeeld combinatiebeurt</caption>
<thead><tr><th scope="col">Onderdeel</th><th scope="col">Richtprijs</th><th scope="col">Berekening</th></tr></thead>
<tbody>
<tr><th scope="row">Ramen buitenzijde</th><td class="num">€65 – €85</td><td>Halfopen bebouwing</td></tr>
<tr><th scope="row">Zonnepanelen</th><td class="num">€75 – €120</td><td>12 × €5 à €10, minimum €75</td></tr>
<tr><th scope="row">Dakgoten</th><td class="num">€75 – €125</td><td>25 m × €3 à €5</td></tr>
<tr><th scope="row">Totaal</th><td class="num">€215 – €330</td><td>Eén verplaatsing, één factuur</td></tr>
</tbody></table></div>
<p>Welk bedrag het precies wordt, hangt af van de bereikbaarheid en hoe vuil alles is. Stuur ons foto's, dan krijgt u een vaste prijs.</p>
</section>'''
    faq = B.faq_html(PRIJZEN_FAQ, "Veelgestelde vragen over onze prijzen")
    hero = B.hero("Prijzen schoonmaak en glasbewassing", "Prijzen voor ramen wassen en schoonmaak:", "gewoon op de site",
                  "Ramen wassen, zonnepanelen, dakgoten, gevels, terrassen en kantoorschoonmaak: hier vindt u al onze richtprijzen. "
                  "U krijgt altijd een vaste prijs vóór we starten, zonder verrassingen achteraf.",
                  ["Ramen vanaf €55 per beurt", "Zonnepanelen €5 – €10 per paneel", "Offerte altijd gratis, meestal met één foto"],
                  wa, "factuur", "Factuur met vinkje en euromunt", ("Offerte gratis", "vaste prijs vóór we starten"))
    side = B.side_card("Prijs op maat", "gratis", "offerte, meestal dezelfde dag", wa, "Meer over elke dienst",
                       [(d["kort"], f"/{d['slug']}/") for d in D.DIENSTEN])
    return hero + f'<div class="wrap content-layout"><article class="prose">{intro}{"".join(blocks)}{voorbeeld}{faq}</article>{side}</div>'

# --------------------------------------------------------------- WERKGEBIED --
WERKGEBIED_FAQ = [
 ("In welke gemeenten werkt Shiny Cleaning?",
  "Onze thuisbasis is Geel. We werken dagelijks in de Kempen (onder meer Geel, Mol, Turnhout, Herentals, Westerlo, Heist-op-den-Berg, Herselt, Laakdal, Olen, Meerhout, Balen, Dessel, Retie en Kasterlee), wekelijks in de rest van de provincie Antwerpen, en op afspraak in Limburg en Vlaams-Brabant, zoals in Beringen, Diest en Aarschot."),
 ("Rekenen jullie verplaatsingskosten?",
  "Niet in de Kempen. Daarbuiten kan een kleine verplaatsingsvergoeding gelden, en dat zeggen we altijd vooraf. We bundelen afspraken per regio, zodat die vergoeding laag blijft of wegvalt."),
 ("Mijn gemeente staat er niet bij. Kunnen jullie toch komen?",
  "Vaak wel. Als we in de buurt zijn, rijden we graag even om. Stuur ons uw gemeente via WhatsApp of bel ons, dan zeggen we meteen wanneer we kunnen komen."),
]

def werkgebied_body(B):
    esc = B.esc
    wa = "Hallo Shiny Cleaning! Komen jullie ook naar mijn gemeente? Ik woon in: "
    def kaart(c):
        return (f'<article class="related-card"><img src="/images/ill/{c["ill"]}.svg" alt="" width="84" height="68" loading="lazy">'
                f'<div><h3><a href="/ruitenwasser/{c["slug"]}/">Ruitenwasser {esc(c["naam"])}</a></h3>'
                f'<p>{esc(", ".join(c["deelgemeenten"][:4]))}</p></div></article>')
    cards = "".join(kaart(c) for c in S.STEDEN if c.get("regio", "kempen") == "kempen")
    cards_buiten = "".join(kaart(c) for c in S.STEDEN if c.get("regio", "kempen") != "kempen")
    ook = "".join(f"<li><span>{esc(t)}</span></li>" for t in OOK_IN)
    hero = B.hero("Werkgebied", "Ruitenwasser en schoonmaak", "in de hele Kempen",
                  "Vanuit Geel werken we elke dag in de Kempen, wekelijks in de rest van de provincie Antwerpen, en op afspraak in Limburg en Vlaams-Brabant. "
                  "In de Kempen betaalt u geen verplaatsingskosten.",
                  ["Kempen: elke werkdag", "Provincie Antwerpen: wekelijks", "Limburg en Vlaams-Brabant: op afspraak"],
                  wa, "werkgebied", "Kaart met een grote pin in het midden en vier regio's rondom", ("Kempen", "zonder verplaatsingskosten"))
    body = f'''
<section class="section" aria-labelledby="kempen-t">
  <div class="wrap">
    <div class="section-head"><h2 id="kempen-t">De Kempen: hier zijn we elke werkdag</h2>
      <p class="section-intro">In deze gemeenten werken we het vaakst. Per gemeente leest u wat we er doen, in welke deelgemeenten we komen en wat het kost.</p></div>
    <div class="related-grid">{cards}</div>
  </div>
</section>
<section class="section section-alt" aria-labelledby="buiten-t">
  <div class="wrap">
    <div class="section-head"><h2 id="buiten-t">Limburg en Vlaams-Brabant: op afspraak</h2>
      <p class="section-intro">Buiten de Kempen bundelen we de afspraken per regio en per dag. Zo blijft een eventuele verplaatsingsvergoeding klein,
      en staat ze altijd vooraf in uw prijs.</p></div>
    <div class="related-grid">{cards_buiten}</div>
  </div>
</section>
<section class="section" aria-labelledby="ook-t">
  <div class="wrap">
    <div class="section-head"><h2 id="ook-t">Ook in deze gemeenten</h2>
      <p class="section-intro">Wekelijks in de rest van de provincie Antwerpen, en op afspraak in Limburg en Vlaams-Brabant.
      Staat uw gemeente er niet bij? Vraag het gerust: als we in de buurt zijn, rijden we graag even om.</p></div>
    <ul class="pill-list">{ook}</ul>
  </div>
</section>
<section class="section section-alt" aria-labelledby="wg-faq"><div class="wrap narrow">{B.faq_html(WERKGEBIED_FAQ, "Vragen over ons werkgebied", "wg-faq")}</div></section>'''
    return hero + body

# ------------------------------------------------------------------ PRIVACY --
def privacy_body(B):
    biz = B.BIZ
    adres = (f"{B.esc(biz['street'])}, " if biz["street"] else "") + f"{biz['postcode']} {biz['city']}"
    vat = f", ondernemingsnummer {B.esc(biz['vat'])}" if biz["vat"] else ""
    return f'''
<section class="page-hero" aria-labelledby="page-title"><div class="wrap narrow" style="padding-top:1rem">
  <p class="eyebrow">Privacy</p><h1 id="page-title">Privacybeleid</h1>
  <p class="lead">Hoe Shiny Cleaning omgaat met de gegevens die u ons bezorgt. Kort en duidelijk.</p>
</div></section>
<div class="wrap narrow legal" style="padding-block:2rem 4rem">
<p><em>Laatst bijgewerkt: {B.TODAY}</em></p>

<h2>Wie is verantwoordelijk?</h2>
<p>Shiny Cleaning, {adres}{vat}. Vragen over uw gegevens stuurt u naar <a href="mailto:{biz['email']}">{biz['email']}</a> of via
WhatsApp naar {biz['tel_display']}.</p>

<h2>Welke gegevens verwerken wij?</h2>
<p>Alleen wat u ons zelf bezorgt als u een prijs vraagt of klant wordt: uw naam, telefoonnummer, e-mailadres, adres of gemeente, eventueel uw bedrijfsnaam,
de omschrijving van de klus en de foto's die u ons stuurt. Voor klanten komen daar facturatiegegevens bij.</p>

<h2>Hoe komen die gegevens bij ons?</h2>
<p>Het offerteformulier op deze website slaat zelf niets op. Wanneer u op verzenden klikt, opent uw eigen WhatsApp of e-mailprogramma met een bericht
dat u zelf verstuurt. Uw gegevens komen dus rechtstreeks bij ons terecht via WhatsApp of e-mail, net zoals wanneer u ons belt of een bericht stuurt.</p>

<h2>Waarvoor gebruiken wij ze?</h2>
<ul>
 <li>Om uw vraag te beantwoorden en u een prijs te bezorgen (stappen vóór een overeenkomst).</li>
 <li>Om de afgesproken werken te plannen, uit te voeren en te factureren (uitvoering van de overeenkomst).</li>
 <li>Om onze boekhouding te voeren (wettelijke verplichting).</li>
</ul>
<p>We gebruiken uw gegevens niet voor reclame van derden, en we verkopen ze nooit.</p>

<h2>Hoe lang bewaren wij ze?</h2>
<p>Een prijsvraag die geen opdracht wordt, verwijderen we uiterlijk na twaalf maanden. Gegevens van klanten bewaren we zolang u klant bent, en facturen zolang de wet
dat vraagt (in België zeven jaar).</p>

<h2>Met wie delen wij ze?</h2>
<p>Alleen met partijen die we nodig hebben om ons werk te doen: onze boekhouder, de aanbieder van onze e-mail en WhatsApp (Meta), en onze websitehost (Hostinger),
die technische logbestanden bijhoudt om de website veilig te laten werken.</p>

<h2 id="cookies">Cookies</h2>
<p>Deze website gebruikt <strong>geen tracking- of advertentiecookies</strong> en geen analysediensten. De lettertypes staan op onze eigen server,
dus uw browser maakt geen verbinding met Google Fonts. Onze host kan technisch noodzakelijke gegevens verwerken om de website snel en veilig te leveren.
Daarvoor is geen toestemming nodig. Voegen we later een analysedienst toe, dan passen we dit beleid aan en vragen we waar nodig eerst uw toestemming.</p>

<h2>Uw rechten</h2>
<p>U kunt uw gegevens altijd inkijken, laten verbeteren of laten verwijderen, en u kunt bezwaar maken tegen het gebruik ervan. Stuur daarvoor een bericht naar
<a href="mailto:{biz['email']}">{biz['email']}</a>. We antwoorden binnen een maand. Bent u het niet eens met hoe we met uw gegevens omgaan,
dan kunt u klacht indienen bij de Gegevensbeschermingsautoriteit (www.gegevensbeschermingsautoriteit.be).</p>
</div>'''

PAGINAS = [
 dict(path="/prijzen/", crumb="Prijzen", prio="0.9",
      title="Prijzen: wat kost ramen wassen, zonnepanelen en dakgoten?",
      desc="Al onze richtprijzen op één pagina: ramen wassen vanaf €55, zonnepanelen €5 – €10 per paneel, dakgoten €3 – €5 per meter, gevels, terrassen en kantoren.",
      wa="Hallo Shiny Cleaning! Ik wil graag een prijs op maat voor: ", body=prijzen_body, faq=PRIJZEN_FAQ),
 dict(path="/werkgebied/", crumb="Werkgebied", prio="0.8",
      title="Werkgebied: ruitenwasser in de Kempen, Antwerpen en Limburg",
      desc="Ruitenwasser en schoonmaakbedrijf in Geel, Mol, Turnhout, Herentals en de hele Kempen, zonder verplaatsingskosten. Op afspraak in Limburg en Vlaams-Brabant.",
      wa="Hallo Shiny Cleaning! Komen jullie ook naar mijn gemeente? Ik woon in: ", body=werkgebied_body, faq=WERKGEBIED_FAQ),
 dict(path="/privacy/", crumb="Privacybeleid", robots="noindex, follow",
      title="Privacybeleid en cookies | Shiny Cleaning",
      desc="Hoe Shiny Cleaning omgaat met uw gegevens: welke gegevens we gebruiken, waarom, hoe lang we ze bewaren en welke rechten u heeft. Geen trackingcookies.",
      wa="Hallo Shiny Cleaning! Ik heb een vraag over mijn gegevens: ", body=privacy_body),
]
