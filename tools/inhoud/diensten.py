# -*- coding: utf-8 -*-
"""
Dienstpagina's. Elke pagina mikt op één zoekwoordcluster (zie tools/SEO.md):
title ≤ 60 tekens, description ± 150 tekens, één H1, eigen FAQ.
Prijzen zijn richtprijzen — gelijk houden met de homepage en /prijzen/.
"""

TOWNS_INTRO = ("Onze thuisbasis is Geel. In de Kempen zijn we elke werkdag aan het werk en betaalt u geen verplaatsingsvergoeding. "
               "In de rest van de provincie Antwerpen, Limburg en Vlaams-Brabant bundelen we de afspraken per regio.")

DIENSTEN = [

# ═══════════════════════════════════════════════════════════════ RAMEN ════
dict(
 slug="ruitenwasser", kort="Ramen wassen", naam="Ruitenwasser en ramen wassen",
 kaart="Binnen en buiten, streeploos met osmosewater. Ook op hoogte, veranda's en etalages.",
 title="Ruitenwasser Kempen | Ramen wassen vanaf €55 per beurt",
 desc="Ruitenwasser nodig in de Kempen? Wij wassen uw ramen streeploos met osmosewater, ook op hoogte. Vaste prijs vanaf €55. Stuur een foto via WhatsApp.",
 eyebrow="Ruitenwasser · ramenwasser · glazenwasser",
 h1="Ruitenwasser voor woning en bedrijf", hl="in de Kempen",
 lead=("Of u nu ruitenwasser, ramenwasser of glazenwasser zegt: u wilt ramen waar u weer door kijkt. "
       "Shiny Cleaning wast uw ramen binnen en buiten met zuiver osmosewater. Geen strepen, geen kalkvlekken, "
       "en tot op de derde verdieping zonder ladder tegen uw gevel."),
 punten=["Vaste prijs vooraf, vanaf €55 per beurt", "Osmosewater: streeploos en langer proper",
         "Om de 4, 6, 8 of 12 weken, of één keer"],
 ill="dienst-ramen", ill_alt="Ramen wassen op hoogte met een telescoopsteel aan een glazen gevel",
 badge=("vanaf €55", "per beurt, rijwoning buitenzijde"), wa="ramen wassen",
 secties=[
  ("inbegrepen", "Wat zit er in een beurt ramen wassen?", """
<p>Een goede ruitenwasser wast meer dan het glas alleen. Bij elke beurt nemen we de <strong>kaders en vensterbanken aan de buitenkant</strong> mee.
Laten we die vuil, dan loopt het stof bij de eerste regenbui weer over uw schone ruiten.</p>
<ul class="tick">
 <li>Alle ramen aan de buitenzijde, inclusief kaders, profielen en vensterbanken</li>
 <li>Binnenzijde op vraag: met trekker en microvezel, zonder druppels op uw vensterbank</li>
 <li>Dakramen, koepels en lichtstraten die we veilig kunnen bereiken</li>
 <li>Veranda's, serres en glazen overkappingen, glas én profielen</li>
 <li>Rolluiken, screens, zonnewering en horren</li>
 <li>Etalages, winkelpuien en inkomdeuren, ook vóór openingstijd</li>
</ul>"""),
  ("osmose", "Osmosewater en telescoopsteel: streeploos tot de derde verdieping", """
<p>Voor de buitenkant werken we met <strong>osmosewater</strong>: kraanwater dat gefilterd is tot er geen kalk en geen mineralen meer in zitten.
Via een telescoopsteel met waterdoorvoer borstelen we het vuil los en spoelen we alles af met dat zuivere water.
Omdat er niets in het water zit, droogt het op zonder vlekken. Zeep hebben we niet nodig, en er blijft dus ook geen zeepfilm achter
die nieuw stof aantrekt. Daardoor blijven uw ramen merkbaar langer proper.</p>
<p>Het tweede voordeel is veiligheid. We werken vanaf de grond, tot ongeveer de derde verdieping. Er komt geen ladder tegen uw gevel of dakgoot,
en er loopt niemand over uw dak. Voor de binnenkant en kleine ruitjes gebruiken we de klassieke trekker en inwasser.</p>"""),
  ("frequentie", "Hoe vaak laat u uw ramen wassen?", """
<p>Dat hangt vooral af van waar u woont. Als richtlijn:</p>
<ul>
 <li><strong>Woningen:</strong> vier tot zes keer per jaar. Aan een drukke weg, naast een akker of onder bomen is om de zes weken beter.</li>
 <li><strong>Winkels en horeca:</strong> de etalage wekelijks of om de twee weken. Een vuile etalage kost klanten.</li>
 <li><strong>Kantoren:</strong> maandelijks of per kwartaal, afhankelijk van de ligging en het aantal bezoekers.</li>
</ul>
<p>Met een <strong>vast schema</strong> komen we automatisch langs. U hoeft er niet meer aan te denken, en de prijs per beurt ligt lager
dan bij een losse opdracht. Het voorjaar is onze drukste periode: wie in maart of april wil, vraagt best tijdig een plaats in de planning.</p>"""),
  ("bedrijven", "Ruitenwasser voor bedrijven, winkels en appartementsgebouwen", """
<p>Voor bedrijven werken we met een <strong>onderhoudscontract voor glasbewassing</strong>: een vaste dag, een vaste ploeg en een maandelijkse factuur
exclusief btw. We wassen gevelbeglazing, etalages, lichtstraten en de ramen van kantoorruimtes, waar nodig buiten de openingsuren.</p>
<p>Beheert u een appartementsgebouw? Dan combineren we het glas van de gemeenschappelijke delen met de wekelijkse schoonmaak van traphal en inkom.
Bewoners kunnen bovendien hun eigen ramen laten meenemen op dezelfde dag.
Lees meer over <a href="/kantoorschoonmaak/">kantoorschoonmaak</a> en de <a href="/gemeenschappelijke-delen/">schoonmaak van gemeenschappelijke delen</a>.</p>"""),
 ],
 prijs_titel="Wat kost ramen laten wassen?",
 prijs_intro=("We rekenen per woning, niet per raam: zo kent u vooraf één vaste prijs. Prijzen voor particulieren zijn inclusief btw. "
              "Bij een vast schema betaalt u per beurt minder dan bij een eenmalige opdracht."),
 prijzen=[("Rijwoning, buitenzijde", "€55 – €70", "Per beurt, kaders en vensterbanken inbegrepen"),
          ("Halfopen bebouwing, buitenzijde", "€65 – €85", "Per beurt"),
          ("Open bebouwing, buitenzijde", "€85 – €115", "Per beurt"),
          ("Binnen- en buitenzijde", "€85 – €150", "Afhankelijk van het aantal ramen"),
          ("Rolluiken", "€12,50 – €20", "Per rolluik, samen met een beurt"),
          ("Veranda of glazen overkapping", "€120 – €280", "Glas, dak en profielen")],
 prijs_na=("<p><strong>Wat bepaalt de prijs?</strong> Het aantal ramen en ruitjes, de bereikbaarheid (hoogte, achterkant, veranda), "
           "hoe vuil het glas is bij de eerste beurt, en hoe vaak we komen. De eerste beurt kan iets meer tijd vragen als er bouwstof of oude kalk op zit.</p>"),
 faq=[
  ("Wat kost ramen wassen per raam?",
   "Wij rekenen per woning, zodat u vooraf één vaste prijs kent. Omgerekend komt een gewone rijwoning met 15 à 20 ruiten aan de buitenzijde uit op ongeveer €3 à €4 per raam. Extra's zoals rolluiken, een veranda of de binnenzijde staan apart in onze prijstabel, zodat er achteraf geen verrassingen zijn."),
  ("Is ramen wassen met osmosewater beter dan met zeep?",
   "Voor de buitenkant wel. Osmosewater bevat geen kalk of mineralen en droogt dus zonder vlekken op. Er blijft geen zeepfilm achter die nieuw stof aantrekt, waardoor ramen langer proper blijven. Binnen gebruiken we de klassieke trekker."),
  ("Wassen jullie ook ramen op de tweede of derde verdieping?",
   "Ja. Met de telescoopsteel werken we vanaf de grond tot ongeveer de derde verdieping, zonder ladder en zonder stelling. Voor hogere gebouwen bekijken we samen met u de beste aanpak."),
  ("Moet ik thuis zijn als de ruitenwasser komt?",
   "Voor de buitenzijde niet. We hebben alleen toegang nodig tot alle kanten van de woning, bijvoorbeeld via een tuinpoort. Voor de binnenzijde spreken we een moment af, of u laat een sleutel achter."),
  ("Kan ik ramen wassen betalen met dienstencheques?",
   "Nee. Een losse beurt ramen wassen valt niet onder dienstencheques, ook niet bij een erkende onderneming: dat mag alleen als deel van het gewone huishoudelijke werk. Bij ons krijgt u een factuur met btw, en voor bedrijven is dat een aftrekbare kost."),
 ],
 faq_onderwerp="ramen wassen",
 towns_title="Ruitenwasser in uw gemeente", towns_intro=TOWNS_INTRO,
 gerelateerd=["zonnepanelen-reinigen", "dakgoot-reinigen", "gevelreiniging"],
 service_type="Glasbewassing", price_spec=(55, 150, "per beurt"),
),

# ═════════════════════════════════════════════════════════ ZONNEPANELEN ════
dict(
 slug="zonnepanelen-reinigen", kort="Zonnepanelen reinigen", naam="Zonnepanelen reinigen",
 kaart="Met zuiver water en een zachte borstel. Geen hogedruk, geen zeep, geen krassen.",
 title="Zonnepanelen reinigen | €5 – €10 per paneel, Kempen",
 desc="Zonnepanelen laten reinigen in de Kempen? Zacht, met osmosewater, zonder hogedruk of zeep. Vanaf €5 per paneel, minimum €75. Vraag uw prijs via WhatsApp.",
 eyebrow="Zonnepanelen laten reinigen",
 h1="Zonnepanelen reinigen", hl="zonder krassen of zeep",
 lead=("Stof, stuifmeel, bladresten en vogelpoep leggen een grijze laag op uw panelen, en aan de onderrand groeit na een paar jaar mos. "
       "Wij reinigen uw zonnepanelen met zuiver osmosewater en een zachte borstel, en kijken meteen of er iets mis is met de bevestiging of de randen."),
 punten=["€5 – €10 per paneel, minimum €75", "Osmosewater en zachte borstel, geen hogedruk",
         "Meestal vanaf de grond, zonder over uw dak te lopen"],
 ill="dienst-zonnepanelen", ill_alt="Zonnepaneel wordt gereinigd met een zachte borstel op een telescoopsteel",
 badge=("€5 – €10", "per paneel, minimum €75"), wa="zonnepanelen reinigen",
 secties=[
  ("zinvol", "Is zonnepanelen reinigen zinvol, of onzin?", """
<p>Eerlijk antwoord: dat verschilt per dak. Regen spoelt veel weg, maar niet alles. Vooral aan de <strong>onderrand</strong> blijft vuil liggen,
want daar verdampt het regenwater en blijft het stof achter. Na enkele jaren zie je er een groene of zwarte rand. Dat is mos, en dat groeit door.</p>
<p>Reinigen loont het meest als:</p>
<ul>
 <li>uw panelen een flauwe helling hebben, zodat regen minder goed afloopt;</li>
 <li>u naast een akker, een stal, een drukke weg of veel bomen woont;</li>
 <li>er vogels op uw dak zitten, want vogelpoep laat zich niet wegspoelen;</li>
 <li>u een groene of grijze rand onderaan uw panelen ziet.</li>
</ul>
<p>Twijfelt u? Vergelijk in de app van uw omvormer de opbrengst van deze maand met dezelfde maand vorig jaar. Of stuur ons een foto van uw panelen,
dan zeggen we u eerlijk of reinigen nu zin heeft.</p>"""),
  ("werkwijze", "Hoe wij uw zonnepanelen reinigen", """
<ol>
 <li><strong>Controle vooraf.</strong> We kijken hoe vuil de panelen zijn en of we veilig vanaf de grond kunnen werken.</li>
 <li><strong>Losweken en borstelen.</strong> Met osmosewater en een zachte borstel op een telescoopsteel. Geen hogedruk en geen agressieve middelen: daar zijn panelen en hun coating niet op gemaakt.</li>
 <li><strong>Randen en onderkant.</strong> Het mos aan de onderrand en tussen de panelen verwijderen we extra zorgvuldig.</li>
 <li><strong>Naspoelen.</strong> Het zuivere water droogt vlekkeloos op, u hoeft niets na te drogen.</li>
 <li><strong>Korte melding.</strong> Zien we losse kabels, beschadigd glas of vogelnesten onder de panelen, dan hoort u dat meteen.</li>
</ol>"""),
  ("hoe-vaak", "Hoe vaak laat u zonnepanelen reinigen?", """
<p>Voor de meeste woningen in de Kempen volstaat <strong>om de één à twee jaar</strong>. Woont u naast een landbouwbedrijf, een drukke weg of een bos,
dan is jaarlijks beter. Het beste moment is het voorjaar, van maart tot juni: dan staan uw panelen proper op het moment dat ze het meest opbrengen.</p>
<p>Combineer het gerust met <a href="/ruitenwasser/">ramen wassen</a> of <a href="/dakgoot-reinigen/">dakgoten uitkuisen</a>. Eén verplaatsing, één factuur.</p>"""),
  ("bedrijven", "Zonnepanelen op loodsen, stallen en bedrijfsdaken", """
<p>Grote installaties op loodsen, bedrijfshallen en landbouwgebouwen reinigen we ook. Bij stallen en bedrijven met veel stof zien we vaak een
hardnekkige laag die regen niet wegspoelt. Voor grote aantallen maken we een prijs per paneel op maat, na een plaatsbezoek of op basis van foto's
en het aantal panelen.</p>"""),
 ],
 prijs_titel="Wat kost zonnepanelen reinigen?",
 prijs_intro="U betaalt per paneel. Voor kleine installaties geldt een forfait, zodat de verplaatsing gedekt is. Prijzen inclusief btw voor particulieren.",
 prijzen=[("Per paneel", "€5 – €10", "Afhankelijk van bereikbaarheid en vervuiling"),
          ("Kleine installatie (tot 10 panelen)", "vanaf €75", "Forfait"),
          ("Loodsen, stallen en grote daken", "op maat", "Na plaatsbezoek of op basis van foto's")],
 prijs_na="<p><strong>Rekenvoorbeeld:</strong> 12 panelen op een woning, goed bereikbaar vanaf de grond: 12 × €5 à €10, dus tussen €60 en €120, met een minimum van €75.</p>",
 faq=[
  ("Hoe vaak moet je zonnepanelen reinigen?",
   "Om de één à twee jaar voor de meeste woningen. Jaarlijks als u naast een akker, stal, drukke weg of veel bomen woont, of als uw panelen een flauwe helling hebben. Het voorjaar is het beste moment."),
  ("Is het onzin om zonnepanelen te reinigen?",
   "Niet altijd, maar ook niet altijd nodig. Regen spoelt veel weg, maar aan de onderrand blijft vuil en groeit mos. Ziet u die rand, of zakt uw opbrengst tegenover vorig jaar, dan loont reinigen. Stuur een foto, dan zeggen we het u eerlijk."),
  ("Waarmee mag je zonnepanelen schoonmaken?",
   "Met zuiver water en een zachte borstel. Gebruik geen hogedrukreiniger, geen schuursponsjes en geen agressieve schoonmaakmiddelen. Gewoon kraanwater laat bovendien kalkvlekken achter, daarom werken wij met osmosewater."),
  ("Kan ik mijn zonnepanelen zelf reinigen?",
   "Als u ze veilig vanaf de grond bereikt, met een zachte borstel en regenwater: ja. Op het dak kruipen raden we af. Dat is gevaarlijk, en panelen breken sneller dan u denkt als u erop leunt."),
  ("Vervalt de garantie als ik mijn zonnepanelen laat reinigen?",
   "Reinigen met water en een zachte borstel is de methode die fabrikanten doorgaans aanraden. Kijk voor de zekerheid in de handleiding of de garantievoorwaarden van uw panelen. Wij gebruiken geen hogedruk en geen chemie."),
 ],
 faq_onderwerp="zonnepanelen reinigen",
 towns_title="Zonnepanelen reinigen in uw gemeente", towns_intro=TOWNS_INTRO,
 gerelateerd=["ruitenwasser", "dakgoot-reinigen", "dakreiniging"],
 service_type="Reiniging van zonnepanelen", price_spec=(5, 10, "per paneel"),
),

# ═══════════════════════════════════════════════════════════════ DAKGOOT ════
dict(
 slug="dakgoot-reinigen", kort="Dakgoten reinigen", naam="Dakgoten reinigen en uitkuisen",
 kaart="Goten en afvoerbuizen uitgekuist en doorgespoeld, vuil afgevoerd. Het najaar is het moment.",
 title="Dakgoot reinigen | Dakgoten uitkuisen vanaf €3 per meter",
 desc="Dakgoten laten reinigen in de Kempen? Wij kuisen goten en afvoerbuizen uit, voeren alles af en melden wat we zien. €3 – €5 per meter. WhatsApp een foto.",
 eyebrow="Dakgoot uitkuisen",
 h1="Dakgoot reinigen en ontstoppen", hl="in de Kempen",
 lead=("Bladeren, dennennaalden, mos en slib: in de bosrijke Kempen zit een dakgoot sneller vol dan u denkt. "
       "Wij kuisen uw dakgoten en afvoerbuizen grondig uit, voeren al het vuil af en laten u weten als er iets niet in orde is."),
 punten=["€3 – €5 per lopende meter", "Goten én afvoerbuizen doorgespoeld",
         "Waar het kan vanaf de grond, zonder ladder tegen uw gevel"],
 ill="dienst-dakgoten", ill_alt="Dakgoot vol bladeren wordt met de hand leeggemaakt",
 badge=("€3 – €5", "per lopende meter"), wa="dakgoten reinigen",
 secties=[
  ("waarom", "Waarom een verstopte dakgoot duur uitvalt", """
<p>Een volle dakgoot loopt bij de eerste stevige regenbui over. Dan loopt het water langs uw gevel in plaats van door de afvoer, met gevolgen die u pas later ziet:</p>
<ul>
 <li>vochtplekken en groene aanslag op de gevel;</li>
 <li>rottende boeidelen en houten dakoversteken;</li>
 <li>vorstschade als het water in de winter in de goot bevriest;</li>
 <li>water bij de fundering of in de kelder;</li>
 <li>een goot die doorzakt onder het gewicht van nat slib.</li>
</ul>
<p>Eén keer per jaar laten uitkuisen kost een fractie van één van die herstellingen.</p>"""),
  ("werkwijze", "Zo kuisen wij uw dakgoten uit", """
<ol>
 <li><strong>Leegmaken.</strong> Bladeren, naalden, mos en slib halen we uit de goot en voeren we af. U houdt er geen zakken vuil aan over.</li>
 <li><strong>Doorspoelen.</strong> We spoelen de goot en de afvoerbuizen door en controleren of het water vrij wegloopt.</li>
 <li><strong>Controle.</strong> We kijken naar gootbeugels, naden, aansluitingen en bladvangers.</li>
 <li><strong>Melding.</strong> Zien we lekken of losse stukken, dan hoort u dat meteen. Op vraag sturen we foto's van voor en na.</li>
</ol>
<p>Afhankelijk van de hoogte werken we met een gootreinigingsset op een telescoopsteel vanaf de grond, of met een ladder en de nodige beveiliging.</p>"""),
  ("wanneer", "Wanneer laat u uw dakgoot best reinigen?", """
<p><strong>Eind oktober tot begin december</strong>, als de bladeren gevallen zijn. Staan er naaldbomen of berken bij uw huis, wat in de Kempen vaak zo is,
dan is een tweede beurt in het voorjaar geen overbodige luxe. Na een zware storm kijken we graag even na of alles nog vrij is.</p>
<p>Tip: september en oktober zijn onze drukste maanden voor dakgoten. Wie in de zomer al een plaats vraagt, heeft voorrang.</p>"""),
  ("combineren", "Dakgoot reinigen combineren met dak of zonnepanelen", """
<p>Laat u uw <a href="/dakreiniging/">dak ontmossen</a>? Dan kuisen we de goten nadien sowieso uit, want het losgekomen mos komt er anders in terecht.
Ook met <a href="/zonnepanelen-reinigen/">zonnepanelen reinigen</a> of <a href="/ruitenwasser/">ramen wassen</a> is het handig om alles in één beurt te doen.</p>
<p>Wilt u minder vaak laten uitkuisen? Dan bekijken we of een gootrooster of een bladvanger op uw afvoer zinvol is.</p>"""),
 ],
 prijs_titel="Wat kost een dakgoot reinigen?",
 prijs_intro="U betaalt per lopende meter goot. Het doorspoelen van de afvoerbuizen zit erbij inbegrepen. Prijzen inclusief btw voor particulieren.",
 prijzen=[("Dakgoot reinigen", "€3 – €5", "Per lopende meter, afvoer doorgespoeld"),
          ("Minimumtarief", "van toepassing", "Voor kleine goten, zodat de verplaatsing gedekt is"),
          ("Samen met dak of zonnepanelen", "één verplaatsing", "Handig in dezelfde beurt")],
 prijs_na="<p><strong>Rekenvoorbeeld:</strong> een halfopen woning met 25 meter goot kost 25 × €3 à €5, dus tussen €75 en €125.</p>",
 faq=[
  ("Wat kost een dakgoot schoonmaken per meter?",
   "Bij ons tussen €3 en €5 per lopende meter, inclusief het doorspoelen van de afvoerbuizen en het afvoeren van het vuil. Voor een halfopen woning met 25 meter goot komt dat op €75 à €125."),
  ("Wat is de beste tijd om een dakgoot schoon te maken?",
   "Eind oktober tot begin december, als de bladeren gevallen zijn. Met naaldbomen of berken in de buurt is een extra beurt in het voorjaar aan te raden."),
  ("Kan een dakgoot gereinigd worden zonder ladder?",
   "Vaak wel. Met een gootreinigingsset op een telescoopsteel werken we vanaf de grond tot ongeveer de tweede verdieping. Is de goot hoger of moeilijk bereikbaar, dan werken we met een ladder en de nodige beveiliging."),
  ("Hoe weet ik of mijn dakgoot verstopt is?",
   "Water dat bij regen over de rand loopt, planten of mos die uit de goot groeien, vochtplekken op de gevel onder de goot, of een afvoerbuis die droog blijft terwijl het regent: dan is het tijd."),
  ("Moet ik thuis zijn als jullie de dakgoten komen reinigen?",
   "Nee, zolang we rond de woning kunnen. Na afloop sturen we een bericht, op vraag met foto's van voor en na."),
 ],
 faq_onderwerp="dakgoten reinigen",
 towns_title="Dakgoten reinigen in uw gemeente", towns_intro=TOWNS_INTRO,
 gerelateerd=["dakreiniging", "zonnepanelen-reinigen", "ruitenwasser"],
 service_type="Dakgootreiniging", price_spec=(3, 5, "per lopende meter"),
),

# ═════════════════════════════════════════════════════════════════ GEVEL ════
dict(
 slug="gevelreiniging", kort="Gevelreiniging", naam="Gevelreiniging met softwash",
 kaart="Groene aanslag weg met softwash, zonder uw voegen of crepi te beschadigen.",
 title="Gevelreiniging met softwash | €8 – €22 per m², Kempen",
 desc="Groene aanslag op uw gevel? Wij reinigen baksteen, crepi en sierpleister met softwash: lage druk, geen schade, langer proper. €8 – €22 per m². Gratis prijs.",
 eyebrow="Gevel reinigen zonder hogedruk",
 h1="Gevelreiniging met softwash", hl="in de Kempen",
 lead=("Groene en zwarte aanslag op een gevel zijn algen, mos en korstmos die zich vastzetten in vocht en schaduw. "
       "Wij verwijderen ze met softwash: een middel dat de aanslag tot in de wortel doodt, aangebracht en afgespoeld met lage druk. "
       "Uw voegwerk blijft heel, en de gevel blijft jaren langer proper."),
 punten=["€8 – €22 per m², vaste prijs vooraf", "Softwash: lage druk, geen uitgespoten voegen",
         "Optioneel impregneren tegen vocht en nieuwe aangroei"],
 ill="dienst-gevel", ill_alt="Bakstenen gevel met groene aanslag die met softwash wordt gereinigd",
 badge=("€8 – €22", "per m², afhankelijk van de gevel"), wa="gevelreiniging",
 secties=[
  ("softwash", "Softwash of hogedruk: waarom wij voor lage druk kiezen", """
<p>Met hogedruk krijg je een gevel snel proper, maar je betaalt het later terug. De straal spuit <strong>voegen</strong> uit, beschadigt
<strong>crepi en isolatiepleister</strong> en ruwt de oppervlakte op. In die ruwe poriën zet nieuwe aanslag zich sneller vast. En het water dat de muur
in wordt geperst, moet er ook weer uit.</p>
<p>Softwash werkt andersom. We brengen een reinigingsmiddel aan dat algen en mossporen doodt, laten het inwerken en spoelen af met lage druk.
Het resultaat ziet u niet altijd dezelfde dag helemaal: de dode aanslag spoelt in de weken daarna verder weg met de regen. Maar omdat ook de sporen
dood zijn, blijft de gevel veel langer schoon.</p>
<p>Hogedruk gebruiken we alleen waar het veilig kan: op beton, arduin en harde natuursteen. Wat groene aanslag precies is en wat u er zelf aan kunt doen,
leest u op onze pagina over <a href="/groene-aanslag-verwijderen/">groene aanslag verwijderen</a>.</p>"""),
  ("welke", "Welke gevels reinigen wij?", """
<ul class="tick">
 <li>Baksteen en gevelsteen, oud en nieuw</li>
 <li>Crepi, sierpleister en isolatiepleister (buitengevelisolatie)</li>
 <li>Natuursteen zoals blauwe steen en arduin</li>
 <li>Houten en kunststof gevelbekleding</li>
 <li>Betonnen plinten, tuinmuren, carports en tuinhuizen</li>
</ul>"""),
  ("werkwijze", "Onze werkwijze, van plaatsbezoek tot impregneren", """
<ol>
 <li><strong>Plaatsbezoek of foto's.</strong> We bekijken de ondergrond, de vervuiling en de oppervlakte, en u krijgt een vaste prijs.</li>
 <li><strong>Afdekken.</strong> Planten, ramen, schrijnwerk en verlichting beschermen we voor we beginnen.</li>
 <li><strong>Aanbrengen en inwerken.</strong> Het softwash-middel doet het werk, niet de druk.</li>
 <li><strong>Afspoelen met lage druk.</strong> Van boven naar beneden, zonder water de muur in te persen.</li>
 <li><strong>Impregneren (optioneel).</strong> Na het drogen brengen we een waterafstotende, dampopen laag aan.</li>
</ol>
<p>We werken bij droog, vorstvrij weer, bij voorkeur van het voorjaar tot de herfst.</p>"""),
  ("impregneren", "Gevel impregneren: zinvol of niet?", """
<p>Een impregneermiddel maakt de gevel waterafstotend. De muur blijft ademen, maar neemt minder regenwater op.
Daardoor krijgt aanslag minder kans, en is er minder risico op vorstschade. Het is zinvol voor baksteen en poreuze steen op een regenkant
of in de schaduw. Het is <strong>niet</strong> zinvol als de muur al behandeld is, of als het vocht van binnenuit komt: dan pakt u eerst de oorzaak aan.
We zeggen u eerlijk of het bij uw gevel iets oplevert.</p>
<p>Ook voor bedrijfsgebouwen en appartementsgebouwen reinigen we gevels. Voor syndici maken we een offerte die u zo aan de algemene vergadering kunt voorleggen.
Zie ook <a href="/gemeenschappelijke-delen/">schoonmaak voor VME's</a>.</p>"""),
 ],
 prijs_titel="Wat kost gevelreiniging per m²?",
 prijs_intro="De prijs hangt af van de ondergrond, de vervuiling en de bereikbaarheid. Na een plaatsbezoek of foto's krijgt u een vaste prijs. Prijzen inclusief btw voor particulieren.",
 prijzen=[("Baksteen en gevelsteen (softwash)", "€8 – €15", "Per m²"),
          ("Crepi, sierpleister, isolatiepleister", "€12 – €22", "Per m², vraagt meer zorg"),
          ("Impregneren na reiniging", "op maat", "Afhankelijk van de steensoort en oppervlakte")],
 prijs_na="<p><strong>Rekenvoorbeeld:</strong> een voorgevel van 60 m² in baksteen kost 60 × €8 à €15, dus tussen €480 en €900. Stellingen zijn bij softwash meestal niet nodig.</p>",
 faq=[
  ("Hoeveel kost gevelreiniging per m²?",
   "Bij ons tussen €8 en €22 per m². Baksteen zit onderaan die vork, crepi en isolatiepleister bovenaan omdat die meer zorg vragen. U krijgt altijd een vaste prijs na een plaatsbezoek of foto's."),
  ("Kan ik mijn gevel zelf reinigen?",
   "Een kleine muur of plint met een zachte borstel en een geschikt middel: ja. Een volledige gevel met een hogedrukreiniger raden we af, want u spuit makkelijk voegen uit en beschadigt crepi. Ook werken op hoogte is een risico."),
  ("Wat zijn de nadelen van het reinigen van een gevel?",
   "Met hogedruk: uitgespoten voegen, beschadigde pleister en snellere heraangroei. Met softwash zijn de nadelen klein. Planten moeten afgedekt worden, en het volledige resultaat ziet u soms pas na enkele regenbuien."),
  ("Is het verstandig om je gevel te impregneren?",
   "Bij poreuze baksteen op een regenkant of in de schaduw wel: de gevel neemt minder water op en blijft langer proper. Niet als de muur al behandeld is of als het vocht van binnenuit komt."),
  ("Hoe lang blijft een gevel proper na softwash?",
   "Meestal meerdere jaren. Een noordgevel of een gevel onder bomen krijgt sneller weer aanslag dan een zonnige zuidgevel. Impregneren verlengt die periode."),
 ],
 faq_onderwerp="gevelreiniging",
 towns_title="Gevelreiniging in uw gemeente", towns_intro=TOWNS_INTRO,
 gerelateerd=["dakreiniging", "terras-oprit-reinigen", "ruitenwasser"],
 service_type="Gevelreiniging", price_spec=(8, 22, "per m²"),
),

# ═════════════════════════════════════════════════════════════════ DAK ════
dict(
 slug="dakreiniging", kort="Dak ontmossen", naam="Dakreiniging en dak ontmossen",
 kaart="Mos van pannen en leien, behandeling tegen hergroei, goten nadien proper.",
 title="Dak ontmossen en dakreiniging | Anti-mos, vaste prijs",
 desc="Mos op uw dak houdt vocht vast, tilt pannen op en verstopt uw goten. Wij ontmossen pannen- en leien daken zacht, behandelen tegen hergroei en kuisen de goten.",
 eyebrow="Mos verwijderen van uw dak",
 h1="Dak ontmossen en dakreiniging", hl="in de Kempen",
 lead=("Een groen dak ziet er misschien romantisch uit, maar mos houdt vocht vast, duwt pannen omhoog en spoelt bij elke regenbui in uw dakgoot. "
       "Wij verwijderen het mos voorzichtig, behandelen het dak tegen hergroei en kuisen de goten nadien uit."),
 punten=["Vaste prijs na foto's of plaatsbezoek", "Zacht: borstel en lage druk, geen harde straal op oude pannen",
         "Anti-mosbehandeling en goten inbegrepen"],
 ill="dienst-dak", ill_alt="Pannendak waarvan het mos met een borstel wordt verwijderd",
 badge=("op maat", "vaste prijs na foto's of plaatsbezoek"), wa="dak ontmossen",
 secties=[
  ("probleem", "Waarom mos op uw dak een probleem is", """
<p>Mos werkt als een spons. Het houdt regenwater vast tegen uw pannen, waardoor ze langer nat blijven en bij vorst sneller barsten.
Groeit het tussen de overlappingen, dan tilt het pannen op en kan er regen onder komen. En bij elke bui spoelen stukjes mos in uw dakgoot,
die daardoor sneller verstopt.</p>
<p>In de Kempen, met veel bomen en een vochtig klimaat, zien we het vooral op daken aan de noordkant en op daken onder of naast bomen.
Mos op het dak is familie van de <a href="/groene-aanslag-verwijderen/">groene aanslag</a> op gevels en terrassen, en vraagt dezelfde aanpak: niet alleen wegborstelen, maar ook de sporen doden.</p>"""),
  ("werkwijze", "Zo ontmossen wij uw dak", """
<ol>
 <li><strong>Inspectie.</strong> Welk type dak is het, hoe oud zijn de pannen, en hoeveel mos zit er?</li>
 <li><strong>Mos verwijderen.</strong> Met een borstel of schraper, en waar de dakbedekking het toelaat met lage druk. Geen harde straal op oude of poreuze pannen: die maakt ze ruw, en dan komt het mos juist sneller terug.</li>
 <li><strong>Behandelen.</strong> Een anti-mosmiddel doodt de resterende sporen, zodat het dak veel langer proper blijft.</li>
 <li><strong>Goten uitkuisen.</strong> Het losgekomen mos halen we uit uw dakgoten en afvoerbuizen.</li>
</ol>"""),
  ("daken", "Welke daken ontmossen wij?", """
<ul class="tick">
 <li>Betonpannen en gebakken kleipannen</li>
 <li>Natuurleien en kunstleien (met extra voorzichtigheid)</li>
 <li>Platte daken met roofing of EPDM: mos en vuil verwijderen, afvoeren vrijmaken</li>
 <li>Veranda- en carportdaken in polycarbonaat of glas</li>
</ul>"""),
  ("coating", "Dakcoating: wel of niet?", """
<p>Na het ontmossen kan een dakcoating de pannen extra beschermen. Bij oudere betonpannen die poreus geworden zijn, kan dat de levensduur verlengen.
Bij pannen in goede staat is het meestal niet nodig. We zeggen u eerlijk of het bij uw dak zinvol is, want een coating die niets toevoegt, is weggegooid geld.</p>
<p>De beste periode om te ontmossen is het voorjaar of het najaar, bij droog en vorstvrij weer: de behandeling werkt dan het best.</p>"""),
 ],
 prijs_titel="Wat kost dak ontmossen?",
 prijs_intro=("Geen twee daken zijn hetzelfde. Daarom geven we een vaste prijs op basis van foto's of een plaatsbezoek. "
              "De verplaatsing en het uitkuisen van de goten zitten erbij inbegrepen."),
 prijzen=[("Dak ontmossen + anti-mosbehandeling", "op maat", "Vaste prijs vooraf"),
          ("Dakgoten uitkuisen na het ontmossen", "inbegrepen", "Anders verstoppen ze met het losse mos"),
          ("Dakcoating", "op maat", "Alleen als het echt iets toevoegt")],
 prijs_na=("<p><strong>Wat bepaalt de prijs?</strong> De oppervlakte en de helling van het dak, de bereikbaarheid, het type dakbedekking "
           "en hoeveel mos er zit. Stuur ons een paar foto's vanaf de straat en de tuin, dan krijgt u snel een prijs.</p>"),
 faq=[
  ("Wat kost dak ontmossen?",
   "Dat hangt af van de oppervlakte, de helling, het type pannen en hoeveel mos er zit. Op basis van enkele foto's of een plaatsbezoek krijgt u een vaste prijs, inclusief het uitkuisen van de goten."),
  ("Is hogedruk slecht voor mijn dak?",
   "Op oude of poreuze pannen wel. Een harde straal ruwt de oppervlakte op, waardoor mos en vuil zich nadien sneller vastzetten. Daarom werken wij met een borstel en lage druk, gevolgd door een anti-mosbehandeling."),
  ("Hoe vaak moet een dak ontmost worden?",
   "Met een goede anti-mosbehandeling blijft een dak meestal meerdere jaren proper. Op een noorddak of onder bomen komt het mos sneller terug dan op een zonnig zuiddak."),
  ("Komt het mos niet gewoon terug?",
   "Na alleen borstelen wel snel, want de sporen blijven zitten. Daarom behandelen we het dak na het ontmossen, zodat ook de sporen gedood worden."),
  ("Moeten mijn dakgoten daarna ook gekuist worden?",
   "Ja, en dat doen we standaard. Het losgekomen mos komt anders bij de eerste regenbui in uw goten en afvoer terecht."),
 ],
 faq_onderwerp="dak ontmossen",
 towns_title="Dak ontmossen in uw gemeente", towns_intro=TOWNS_INTRO,
 gerelateerd=["dakgoot-reinigen", "zonnepanelen-reinigen", "gevelreiniging"],
 service_type="Dakreiniging", price_spec=None,
),

# ═══════════════════════════════════════════════════════════ TERRAS/OPRIT ════
dict(
 slug="terras-oprit-reinigen", kort="Terras en oprit reinigen", naam="Terras en oprit reinigen",
 kaart="Klinkers, tegels en natuursteen met een vlakreiniger, opnieuw ingevoegd en beschermd.",
 title="Terras en oprit reinigen | Vanaf €3 per m² in de Kempen",
 desc="Groene aanslag, mos of onkruid op uw terras of oprit? Wij reinigen klinkers, tegels en natuursteen, voegen opnieuw in en impregneren. Vanaf €3 per m².",
 eyebrow="Hogedrukreiniging van terras en oprit",
 h1="Terras en oprit reinigen", hl="als nieuw, zonder strepen",
 lead=("Een terras of oprit wordt in een paar jaar groen, glad en vol onkruid. Wij reinigen klinkers, tegels en natuursteen met een vlakreiniger: "
       "geen strepen en geen uitgespoten voegen. Daarna voegen we opnieuw in, en op vraag beschermen we alles met een impregneermiddel."),
 punten=["€3 – €7 per m², forfait vanaf €170", "Vlakreiniger: gelijkmatig resultaat, voegen blijven heel",
         "Opnieuw invoegen en impregneren op vraag"],
 ill="dienst-terras", ill_alt="Terrastegels worden gereinigd: links groen, rechts weer proper",
 badge=("€3 – €7", "per m², forfait vanaf €170"), wa="terras of oprit reinigen",
 secties=[
  ("wat", "Wat we reinigen", """
<ul class="tick">
 <li>Betonklinkers, gebakken klinkers en kasseien</li>
 <li>Betontegels, keramische tegels en terrastegels</li>
 <li>Natuursteen zoals blauwe steen en porfier</li>
 <li>Gewassen grind en gepolierd beton</li>
 <li>Houten terrassen, met lage druk en een aangepast middel</li>
 <li>Tuinpaden, parkeerplaatsen en bedrijfsterreinen</li>
</ul>"""),
  ("werkwijze", "Zo pakken we uw terras of oprit aan", """
<ol>
 <li><strong>Onkruid en mos uit de voegen.</strong> Eerst mechanisch, zodat de wortels er echt uit zijn.</li>
 <li><strong>Reinigen met een vlakreiniger.</strong> Een ronddraaiende kap houdt de straal op een vaste afstand. U krijgt geen strepen, en de voegen spuiten niet leeg.</li>
 <li><strong>Naspoelen.</strong> Slib en vuil gaan de afvoer in, niet uw border.</li>
 <li><strong>Opnieuw invoegen.</strong> Met gewoon voegzand of met polymeerzand, dat hard wordt en onkruid tegenhoudt.</li>
 <li><strong>Impregneren (optioneel).</strong> Een beschermlaag tegen vlekken, olie en snelle heraangroei.</li>
</ol>"""),
  ("voegzand", "Voegzand of polymeerzand?", """
<p><strong>Gewoon voegzand</strong> is goedkoper, maar spoelt na verloop van tijd uit, en onkruid vindt er snel een weg in.
<strong>Polymeerzand</strong> wordt na bevochtigen hard en blijft zitten. Het is duurder, maar u heeft jaren minder onkruid tussen de klinkers.
Voor opritten en terrassen die veel gebruikt worden, raden we meestal polymeerzand aan.</p>"""),
  ("wanneer", "Het beste moment: begin van de lente", """
<p>De meeste mensen willen hun terras proper hebben voor de eerste warme dagen. Daardoor is <strong>maart en april</strong> onze drukste periode voor terrassen.
Wie in februari al een afspraak vastlegt, zit gegarandeerd goed. Een oprit kan eigenlijk het hele jaar door, zolang het niet vriest.</p>
<p>Combineer het gerust met <a href="/gevelreiniging/">gevelreiniging</a>: de aanslag op gevel en terras heeft vaak dezelfde oorzaak.
Meer over die oorzaken en over wat u zelf kunt doen, leest u bij <a href="/groene-aanslag-verwijderen/">groene aanslag verwijderen</a>.</p>"""),
 ],
 prijs_titel="Wat kost een terras of oprit reinigen?",
 prijs_intro="U betaalt per m². Voor kleine oppervlaktes geldt een forfait, zodat de verplaatsing en het materiaal gedekt zijn. Prijzen inclusief btw voor particulieren.",
 prijzen=[("Terras of oprit reinigen", "€3 – €7", "Per m², afhankelijk van ondergrond en vervuiling"),
          ("Kleine oppervlakte (tot ± 25 m²)", "vanaf €170", "Forfait"),
          ("Opnieuw invoegen en impregneren", "op maat", "Per m², afhankelijk van het product")],
 prijs_na="<p><strong>Rekenvoorbeeld:</strong> een oprit van 60 m² kost 60 × €3 à €7, dus tussen €180 en €420 voor het reinigen, zonder invoegen of impregneren.</p>",
 faq=[
  ("Wat kost een oprit reinigen per m²?",
   "Tussen €3 en €7 per m² voor het reinigen, afhankelijk van de ondergrond en hoe vuil de oprit is. Voor kleine oppervlaktes geldt een forfait vanaf €170. Invoegen en impregneren rekenen we apart."),
  ("Hoe verwijder je groene aanslag van een terras?",
   "Zelf kan dat met een harde borstel en een groene-aanslagreiniger, maar bij een groot terras is dat veel werk. Wij reinigen met een vlakreiniger en behandelen nadien, zodat de aanslag minder snel terugkomt."),
  ("Is een hogedrukreiniger slecht voor klinkers?",
   "Met een losse straal wel: te dichtbij spuit u voegen leeg en ruwt u de toplaag op. Met een vlakreiniger blijft de afstand gelijk, en krijgt u een gelijkmatig resultaat zonder schade."),
  ("Hoe lang blijft een terras proper na reinigen?",
   "Zonder behandeling een à twee jaar, afhankelijk van schaduw en bomen. Met impregneren en polymeerzand blijft het merkbaar langer proper."),
  ("Moet het voegzand altijd vervangen worden?",
   "Na een grondige reiniging spoelt er altijd wat voegzand uit. Opnieuw invoegen is daarom sterk aan te raden: anders schuiven klinkers en groeit onkruid sneller terug."),
 ],
 faq_onderwerp="terras en oprit reinigen",
 towns_title="Terras en oprit reinigen in uw gemeente", towns_intro=TOWNS_INTRO,
 gerelateerd=["gevelreiniging", "dakreiniging", "ruitenwasser"],
 service_type="Hogedrukreiniging van terras en oprit", price_spec=(3, 7, "per m²"),
),

# ════════════════════════════════════════════════════════════ TAPIJT/ZETEL ════
dict(
 slug="tapijt-zetelreiniging", kort="Tapijt en zetel reinigen", naam="Tapijt-, zetel- en matrasreiniging",
 kaart="Dieptereiniging aan huis of op kantoor. Vlekken, huisstofmijt en geurtjes eruit.",
 title="Zetelreiniging en tapijtreiniging aan huis | Kempen",
 desc="Zetel, tapijt of matras laten reinigen aan huis of op kantoor? Dieptereiniging met een extractiemachine: vlekken, huisstofmijt en geurtjes weg, snel droog.",
 eyebrow="Dieptereiniging aan huis",
 h1="Zetelreiniging en tapijtreiniging", hl="bij u thuis",
 lead=("Een zetel of tapijt vangt jarenlang stof, huidschilfers, vlekken en geurtjes op. Stofzuigen haalt alleen de bovenkant weg. "
       "Wij reinigen tot diep in de vezel met een extractiemachine, bij u thuis of op kantoor. Uw meubels blijven staan waar ze staan."),
 punten=["Bij u thuis of op kantoor", "Vlekbehandeling en dieptereiniging in één beurt", "Meestal dezelfde dag weer droog"],
 ill="dienst-tapijt", ill_alt="Zetel wordt gereinigd met een extractiemachine",
 badge=("op maat", "stuur een foto voor een prijs"), wa="zetel- of tapijtreiniging",
 secties=[
  ("wat", "Wat we reinigen", """
<ul class="tick">
 <li>Zetels, fauteuils en hoekbanken in stof en microvezel</li>
 <li>Vaste vloerbekleding, losse tapijten en trapbekleding</li>
 <li>Matrassen, met een behandeling tegen huisstofmijt</li>
 <li>Bureaustoelen en vergaderstoelen</li>
 <li>Autozetels en eetkamerstoelen met stoffen zitting</li>
</ul>
<p>Heeft u een lederen zetel of een bijzondere stof? Stuur ons een foto van het label. Dan bekijken we vooraf of en hoe we die kunnen reinigen.</p>"""),
  ("hoe", "Hoe dieptereiniging werkt", """
<ol>
 <li><strong>Stofzuigen en voorbehandelen.</strong> Los vuil eruit, vlekken krijgen een aangepaste voorbehandeling.</li>
 <li><strong>Sproei-extractie.</strong> De machine spuit warm water met een mild reinigingsmiddel diep in de vezel en zuigt het meteen, samen met het vuil, weer op.</li>
 <li><strong>Naborstelen.</strong> De vezels liggen weer mooi en drogen gelijkmatig.</li>
 <li><strong>Drogen.</strong> Meestal enkele uren. Met een open raam gaat het sneller.</li>
</ol>
<p>We testen altijd eerst op een onzichtbare plek, zodat er geen verkleuring of krimp ontstaat.</p>"""),
  ("allergie", "Voor mensen met allergie en huisdieren", """
<p>Huisstofmijt, huidschilfers en haren van huisdieren nestelen zich diep in zetels, matrassen en tapijt. Voor mensen met een allergie maakt een dieptereiniging
een merkbaar verschil. Heeft u huisdieren, dan pakken we ook geurtjes en haren aan. Op vraag werken we met ecologische producten.</p>"""),
  ("kantoor", "Tapijtreiniging op kantoor", """
<p>Kantoortapijt ziet veel voetstappen, koffie en straatvuil. We reinigen vaste vloerbekleding, bureaustoelen en vergaderruimtes buiten de kantooruren,
zodat alles de volgende ochtend droog en fris is. Dat kan als losse opdracht, of periodiek als deel van uw <a href="/kantoorschoonmaak/">schoonmaakcontract</a>.</p>"""),
 ],
 prijs_titel="Wat kost zetelreiniging of tapijtreiniging?",
 prijs_intro=("De prijs hangt af van het aantal zitplaatsen, het soort stof, de vlekken en de oppervlakte tapijt. "
              "Stuur een foto, dan krijgt u snel een vaste prijs. Prijzen inclusief btw voor particulieren."),
 prijzen=[("Zetel of hoekbank", "op maat", "Per zitplaats, afhankelijk van stof en vlekken"),
          ("Tapijt of vaste vloerbekleding", "op maat", "Per m²"),
          ("Matras", "op maat", "Inclusief behandeling tegen huisstofmijt")],
 prijs_na="<p>Laat u meerdere stukken tegelijk reinigen, bijvoorbeeld een zetel en een tapijt, dan betaalt u maar één verplaatsing.</p>",
 faq=[
  ("Hoe lang duurt het voor een zetel droog is?",
   "Meestal enkele uren, afhankelijk van de stof, de temperatuur en de ventilatie. Met een open raam of verwarming aan gaat het sneller. Doorgaans kunt u er dezelfde dag weer op zitten."),
  ("Gaan alle vlekken eruit?",
   "De meeste wel. Oude vlekken, inkt, verfresten of vlekken die al met een verkeerd middel behandeld zijn, gaan soms niet helemaal weg. Dat zeggen we u vooraf eerlijk."),
  ("Kan elke stof gereinigd worden?",
   "Bijna elke stof, maar niet elke stof op dezelfde manier. Het label op het kussen geeft aan wat mag. We testen altijd eerst op een onzichtbare plek."),
  ("Helpt dieptereiniging tegen huisstofmijt?",
   "Ja. Met sproei-extractie halen we huisstofmijt, uitwerpselen en huidschilfers diep uit zetel en matras. Voor mensen met een allergie maakt dat een merkbaar verschil."),
  ("Moet ik mijn zetel verplaatsen of wegbrengen?",
   "Nee, we reinigen bij u thuis of op kantoor. Maak alleen de ruimte rond de zetel of het tapijt vrij, de rest doen wij."),
 ],
 faq_onderwerp="zetel- en tapijtreiniging",
 towns_title="Zetelreiniging in uw gemeente", towns_intro=TOWNS_INTRO,
 gerelateerd=["opleveringsschoonmaak", "kantoorschoonmaak", "ruitenwasser"],
 service_type="Dieptereiniging van textiel", price_spec=None,
),

# ════════════════════════════════════════════════════════════ OPLEVERING ════
dict(
 slug="opleveringsschoonmaak", kort="Opleveringsschoonmaak", naam="Opleveringsschoonmaak en eerste opkuis",
 kaart="Eerste opkuis na nieuwbouw of renovatie, ramen inbegrepen. Altijd een vaste prijs.",
 title="Opleveringsschoonmaak en eerste opkuis | Vaste prijs",
 desc="Eerste opkuis na nieuwbouw of renovatie, werfopkuis of verhuisschoonmaak? Wij maken uw pand instapklaar, ramen inbegrepen. Altijd een vaste prijs vooraf.",
 eyebrow="Eerste opkuis · werfopkuis · verhuisschoonmaak",
 h1="Opleveringsschoonmaak", hl="en eerste opkuis",
 lead=("Na de laatste aannemer ligt er overal bouwstof: in kasten, op radiatoren, in stopcontacten en op elke ruit. "
       "Wij maken uw nieuwbouw, renovatie of huurwoning instapklaar. De ramen zitten erbij inbegrepen, want dat is ons vak. "
       "U krijgt altijd een vaste prijs, nooit een open rekening per uur."),
 punten=["Vaste prijs vooraf, nooit per uur achteraf", "Ramen binnen en buiten inbegrepen",
         "Voor particulieren, aannemers en projectontwikkelaars"],
 ill="dienst-oplevering", ill_alt="Verhuisdozen, emmer met zwabber en sleutels voor een opleveringsschoonmaak",
 badge=("vaste prijs", "na plaatsbezoek of foto's"), wa="een opleveringsschoonmaak",
 secties=[
  ("eerste-opkuis", "Eerste opkuis na nieuwbouw of renovatie", """
<p>Bouwstof is fijn en zit overal. Een gewone poetsbeurt verplaatst het vooral. Bij een <strong>eerste opkuis</strong> werken we ruimte per ruimte, van boven naar beneden:</p>
<ul class="tick">
 <li>Cementsluier van tegels en voegen, zonder de voegen aan te tasten</li>
 <li>Verf-, pleister- en siliconenresten van ramen, deuren en sanitair</li>
 <li>Stickers en beschermfolie van ramen en schrijnwerk</li>
 <li>Kasten en keukenkasten binnen en buiten</li>
 <li>Radiatoren, stopcontacten, schakelaars en ventilatieroosters</li>
 <li>Ramen binnen en buiten, inclusief kaders en rails van schuiframen</li>
 <li>Vloeren gezogen en gedweild, trappen en plinten</li>
</ul>"""),
  ("werfopkuis", "Werfopkuis voor aannemers en projectontwikkelaars", """
<p>Voor aannemers en projectontwikkelaars doen we de <strong>werfopkuis</strong> bij de oplevering van woningen en appartementen, ook gefaseerd per blok of per verdieping.
U krijgt één aanspreekpunt, een planning die aansluit op uw oplevering, en een factuur exclusief btw. Zo staat elke woning sleutelklaar
op het moment dat de koper binnenkomt.</p>"""),
  ("verhuis", "Verhuisschoonmaak en eindschoonmaak van een huurwoning", """
<p>Verhuist u of loopt uw huurcontract af? Dan maken we de woning leeg en proper klaar voor de plaatsbeschrijving. We doen extra aandacht aan de plekken
die bij een plaatsbeschrijving altijd bekeken worden: oven, dampkap, koelkast, kalk in de badkamer, ramen en vensterbanken.</p>
<p>Voor verhuurders doen we ook de wisselschoonmaak tussen twee huurders.</p>"""),
  ("vaste-prijs", "Vaste prijs, geen uurtje-factuurtje", """
<p>Bij een opleveringsschoonmaak weet u vooraf niet hoeveel uur het wordt, en dat is precies waarom wij met een <strong>vaste prijs</strong> werken.
Na een plaatsbezoek, of op basis van foto's en de oppervlakte, weet u wat het kost. Duurt het langer dan gedacht, dan is dat ons probleem, niet het uwe.</p>
<p>Na de opkuis blijven de ramen het mooist als u ze op een vast schema laat <a href="/ruitenwasser/">wassen</a>.</p>"""),
 ],
 prijs_titel="Wat kost een eerste opkuis van een nieuwbouw?",
 prijs_intro="Elke werf is anders. Daarom geven we altijd een vaste prijs na een plaatsbezoek of op basis van foto's. Prijzen inclusief btw voor particulieren, exclusief btw voor bedrijven.",
 prijzen=[("Eerste opkuis woning of appartement", "vaste prijs", "Op basis van oppervlakte en hoeveelheid bouwstof"),
          ("Werfopkuis projecten", "vaste prijs", "Per woning of per blok, planning volgens oplevering"),
          ("Verhuis- of eindschoonmaak", "vaste prijs", "Inclusief ramen, keuken en badkamer")],
 prijs_na=("<p><strong>Wat bepaalt de prijs?</strong> De oppervlakte, hoeveel bouwstof en resten er liggen, het aantal ramen en kasten, "
           "en de termijn waarin het klaar moet zijn.</p>"),
 faq=[
  ("Wat kost een eerste opkuis van een nieuwbouwwoning?",
   "Dat hangt af van de oppervlakte, de hoeveelheid bouwstof, het aantal ramen en kasten. We werken altijd met een vaste prijs na een plaatsbezoek of op basis van foto's, nooit met een open rekening per uur."),
  ("Wanneer plan ik de eerste opkuis?",
   "Na de laatste werken en voor u de meubels binnenzet. Zijn er nog stellingen, dan wachten we met de buitenkant van de ramen tot ze weg zijn. Zo moet niets twee keer."),
  ("Zijn de ramen inbegrepen?",
   "Ja, binnen en buiten, inclusief stickers, folie, cement- en verfresten en de rails van schuiframen. Ramen zijn tenslotte ons vak."),
  ("Werken jullie ook voor aannemers en projectontwikkelaars?",
   "Ja. We doen werfopkuis bij de oplevering van woningen en appartementen, ook gefaseerd per blok of verdieping, met een factuur exclusief btw."),
  ("Hoeveel tijd hebben jullie nodig?",
   "Een gemiddelde woning doen we meestal in één à twee dagen, afhankelijk van de grootte en de hoeveelheid bouwstof. Bij het plaatsbezoek krijgt u een duidelijke planning."),
 ],
 faq_onderwerp="de opleveringsschoonmaak",
 towns_title="Opleveringsschoonmaak in uw gemeente", towns_intro=TOWNS_INTRO,
 gerelateerd=["ruitenwasser", "tapijt-zetelreiniging", "kantoorschoonmaak"],
 service_type="Opleveringsschoonmaak", price_spec=None,
),

# ═════════════════════════════════════════════════════════ KANTOOR (B2B) ════
dict(
 slug="kantoorschoonmaak", kort="Kantoorschoonmaak", naam="Kantoorschoonmaak en schoonmaakcontracten", b2b=True,
 kaart="Vast team, schriftelijk werkschema, maandelijks opzegbaar. Voor kantoren, praktijken en winkels.",
 title="Kantoorschoonmaak Kempen | Schoonmaakbedrijf vanaf €30/u",
 desc="Schoonmaakbedrijf voor kantoren, praktijken en winkels in de Kempen. Vast team, schriftelijk werkschema, maandelijks opzegbaar. Vanaf €30 per uur excl. btw.",
 eyebrow="Schoonmaakbedrijf voor bedrijven",
 h1="Kantoorschoonmaak in de Kempen,", hl="met een vast team",
 lead=("Een schoonmaakbedrijf dat niet komt opdagen, of elke week andere mensen stuurt, kost u meer dan het oplevert. "
       "Wij werken met een vast team per klant, een schriftelijk werkschema en één contactpersoon die opneemt. "
       "Voor kantoren, praktijken, winkels en magazijnen in de hele Kempen."),
 punten=["Vanaf €30 per uur excl. btw", "Vast team en één vast aanspreekpunt",
         "Maandelijks opzegbaar na de eerste drie maanden"],
 ill="bedrijven-kantoor", ill_alt="Kantoorgebouw met een schoonmaakkar voor de deur",
 badge=("vanaf €30/u", "excl. btw, afhankelijk van frequentie"), wa="kantoorschoonmaak",
 tussen_cta="Wilt u een prijs voor uw kantoor? Stuur ons de oppervlakte en hoe vaak u schoonmaak wilt.",
 secties=[
  ("contract", "Een schoonmaakcontract dat gewoon werkt", """
<ul class="tick">
 <li><strong>Vast team.</strong> Dezelfde mensen die uw gebouw kennen, met een vaste vervanger bij ziekte of verlof.</li>
 <li><strong>Schriftelijk werkschema.</strong> Per ruimte staat wat er gebeurt, en hoe vaak. U weet waarvoor u betaalt.</li>
 <li><strong>Eén contactpersoon.</strong> Bereikbaar op gsm en via WhatsApp, niet via een callcenter.</li>
 <li><strong>Buiten de kantooruren.</strong> 's Morgens vroeg of 's avonds, zodat uw mensen er niets van merken.</li>
 <li><strong>Alles inbegrepen.</strong> Producten, materiaal en machines zitten in de prijs.</li>
 <li><strong>Maandelijks opzegbaar.</strong> Na de eerste drie maanden. We houden klanten met ons werk, niet met kleine lettertjes.</li>
</ul>"""),
  ("voor-wie", "Voor wie wij schoonmaken", """
<ul>
 <li><strong>Kantoren en KMO's:</strong> bureaus, vergaderzalen, sanitair, keuken en koffiehoek.</li>
 <li><strong>Medische praktijken, apotheken en kinderopvang:</strong> vaste desinfectieroutine voor contactpunten en aparte materialen per zone.</li>
 <li><strong>Winkels, showrooms en horeca:</strong> vloeren, sanitair en etalages, vóór de openingstijd.</li>
 <li><strong>Magazijnen en productie:</strong> machinaal schrobben, kantine, kleedkamers en hoge ramen.</li>
</ul>"""),
  ("beurt", "Wat een onderhoudsbeurt omvat", """
<p>Een typisch werkschema voor een kantoor ziet er zo uit. We passen het aan uw gebouw en uw wensen aan.</p>
<ul class="tick">
 <li>Bureaus en werkplekken afstoffen en reinigen, schermen voorzichtig afnemen</li>
 <li>Sanitair grondig reinigen en ontkalken, verbruiksartikelen aanvullen</li>
 <li>Keuken en koffiehoek: aanrecht, toestellen aan de buitenkant, vaatwasser in- en uitladen op vraag</li>
 <li>Vloeren stofzuigen en dweilen, harde vloeren periodiek machinaal</li>
 <li>Afval ledigen en sorteren volgens uw afvalbeleid</li>
 <li>Deurklinken, lichtschakelaars en trapleuningen ontsmetten</li>
 <li>Binnenglas en glazen deuren streeploos</li>
</ul>
<p>Periodiek werk, zoals <a href="/ruitenwasser/">glasbewassing buiten</a>, <a href="/tapijt-zetelreiniging/">tapijtreiniging</a> en machinaal schrobben, plannen we in hetzelfde contract.</p>"""),
  ("overstappen", "Overstappen van schoonmaakfirma", """
<p>Bent u niet tevreden over uw huidige schoonmaakbedrijf? De meeste contracten hebben een <strong>opzegtermijn van één tot drie maanden</strong>.
Bezorg ons uw huidige overeenkomst, dan kijken we samen na wanneer u kunt overstappen. We plannen de start zo dat er geen week zonder schoonmaak tussenvalt.</p>
<p>Een schoonmaakbedrijf is voor uw onderneming een beroepskost. U krijgt een maandelijkse factuur met btw.</p>"""),
 ],
 prijs_titel="Wat kost een schoonmaakbedrijf per uur?",
 prijs_intro=("Voor kantoorschoonmaak rekenen we tussen €30 en €42 per uur exclusief btw. Hoe vaker we komen, hoe lager het uurtarief. "
              "Na een plaatsbezoek rekenen we het aantal uren per week uit, en u krijgt een vast maandbedrag."),
 prijzen=[("Kantoorschoonmaak op contract", "€30 – €42", "Per uur excl. btw, lager bij hogere frequentie"),
          ("Vast maandbedrag", "op maat", "Na plaatsbezoek, alles inbegrepen"),
          ("Periodiek werk (glas, tapijt, vloeren)", "op maat", "In hetzelfde contract")],
 prijs_na=("<p><strong>Rekenvoorbeeld:</strong> een kantoor van 250 m² met 15 werkplekken, twee keer per week schoonmaak van twee uur: "
           "vier uur per week, of ongeveer 17 uur per maand. Aan €30 à €42 per uur is dat tussen €520 en €730 per maand, exclusief btw.</p>"),
 faq=[
  ("Wat kost een schoonmaakbedrijf per uur?",
   "Bij ons tussen €30 en €42 per uur exclusief btw, afhankelijk van hoe vaak we komen en het type gebouw. Producten, materiaal en machines zitten erbij inbegrepen."),
  ("Wat kost kantoorschoonmaak per m²?",
   "Dat hangt af van hoe vaak en hoe grondig u wilt laten schoonmaken. We rekenen uit hoeveel uur per week uw kantoor nodig heeft, en zetten dat om naar een vast maandbedrag. Zo vergelijkt u eerlijk."),
  ("Hoe vaak moet een kantoor schoongemaakt worden?",
   "Voor een klein kantoor volstaan vaak een of twee beurten per week. Sanitair en keuken vragen meer aandacht dan werkplekken. Bij veel bezoekers of personeel is dagelijks beter. We stellen samen een werkschema op."),
  ("Werken jullie buiten de kantooruren?",
   "Ja, 's morgens vroeg of 's avonds, zodat uw medewerkers er niets van merken. Voor winkels komen we voor de openingstijd."),
  ("Hoe zeg ik mijn huidig schoonmaakcontract op?",
   "Kijk in uw contract naar de opzegtermijn, meestal één tot drie maanden, en zeg schriftelijk op. Bezorg ons uw overeenkomst, dan plannen we de overstap zo dat er geen week zonder schoonmaak valt."),
 ],
 faq_onderwerp="kantoorschoonmaak",
 towns_title="Kantoorschoonmaak in uw regio",
 towns_intro="Voor bedrijven werken we in de hele Kempen, en voor contracten ook in Turnhout, Lier, Mechelen, Hasselt en Leuven.",
 gerelateerd=["gemeenschappelijke-delen", "ruitenwasser", "tapijt-zetelreiniging"],
 service_type="Kantoorschoonmaak", price_spec=(30, 42, "per uur excl. btw"),
),

# ═══════════════════════════════════════════════════════ VME / SYNDICUS ════
dict(
 slug="gemeenschappelijke-delen", kort="Gemeenschappelijke delen", naam="Schoonmaak van gemeenschappelijke delen", b2b=True,
 kaart="Traphallen, lift en inkom op vast schema, met rapport per beurt. Voor syndici en VME's.",
 title="Schoonmaak gemeenschappelijke delen | Syndicus en VME",
 desc="Traphallen, lift, inkomhal en kelders van uw appartementsgebouw proper op een vast schema. Voor syndici en VME's, vanaf één gebouw, met rapport per beurt.",
 eyebrow="Voor syndici en VME's",
 h1="Schoonmaak gemeenschappelijke delen", hl="voor appartementsgebouwen",
 lead=("Een propere inkomhal en traphal is het visitekaartje van een appartementsgebouw, en het eerste waar bewoners over klagen als het misloopt. "
       "Wij poetsen de gemeenschappelijke delen op een vaste dag, volgens een checklist, met een kort rapport na elke beurt. "
       "Voor syndici en zelfbeheerde VME's, al vanaf één gebouw."),
 punten=["€30 – €45 per uur excl. btw, of vast maandbedrag", "Rapport met foto's na elke beurt",
         "Defecten meteen gemeld aan de syndicus"],
 ill="dienst-vme", ill_alt="Appartementsgebouw met emmer, zwabber en een checklist",
 badge=("€30 – €45/u", "excl. btw, of vast maandbedrag"), wa="de schoonmaak van gemeenschappelijke delen",
 tussen_cta="Syndicus of VME? Stuur ons het adres en het aantal verdiepingen, dan krijgt u een offerte voor de algemene vergadering.",
 secties=[
  ("wat", "Wat we poetsen in een appartementsgebouw", """
<ul class="tick">
 <li>Inkomhal, brievenbussen, deurbelpaneel en inkomdeur (glas binnen en buiten)</li>
 <li>Traphallen: trappen, leuningen, plinten en overlopen</li>
 <li>Lift: vloer, wanden, spiegel, knoppen en liftdeuren op elke verdieping</li>
 <li>Gangen, kelders, bergingen en fietsenberging</li>
 <li>Vuilnislokaal: vloer en containers</li>
 <li>Ondergrondse parking: vegen en vuil opruimen</li>
 <li>Glas van de gemeenschappelijke delen en het buitenschrijnwerk</li>
</ul>"""),
  ("rapport", "Vast schema, checklist en rapport per beurt", """
<p>We komen op een vaste dag, werken een checklist af en sturen na elke beurt een kort rapport, op vraag met foto's.
Zien we een kapotte lamp, een deur die niet meer sluit, een lek of vandalisme? Dan meldt ons team dat meteen aan de syndicus.
Zo heeft u ogen in het gebouw, en iets concreets in handen voor de algemene vergadering.</p>"""),
  ("syndicus", "Voor syndici én zelfbeheerde VME's", """
<p>We werken voor professionele syndici en voor VME's die hun gebouw zelf beheren. Voor de algemene vergadering maken we een duidelijke offerte
met het werkschema en de prijs per maand, die u zo kunt voorleggen. Eén gebouw is voor ons geen te kleine opdracht.</p>"""),
  ("glas", "Ramen van de bewoners in dezelfde beurt", """
<p>Naast het glas van de gemeenschappelijke delen kunnen bewoners hun eigen ramen laten wassen op dezelfde dag. Wie meedoet, betaalt enkel voor
zijn eigen appartement, en rechtstreeks aan ons. Voor de syndicus geen extra werk, voor de bewoners een voordeel. Meer over onze
<a href="/ruitenwasser/">ruitenwasser-service</a> en <a href="/gevelreiniging/">gevelreiniging</a> voor appartementsgebouwen.</p>"""),
 ],
 prijs_titel="Wat kost het poetsen van gemeenschappelijke delen?",
 prijs_intro=("We rekenen tussen €30 en €45 per uur exclusief btw, of een vast bedrag per maand. De prijs hangt af van het aantal verdiepingen, "
              "de lift, de kelders en parking, en hoe vaak we komen."),
 prijzen=[("Wekelijkse schoonmaak gemeenschappelijke delen", "€30 – €45", "Per uur excl. btw"),
          ("Vast maandbedrag", "op maat", "Handig voor het budget van de VME"),
          ("Glas gemeenschappelijke delen", "op maat", "In hetzelfde contract")],
 prijs_na=("<p><strong>Rekenvoorbeeld:</strong> een gebouw met twaalf appartementen, vier verdiepingen en een lift, wekelijks anderhalf uur: "
           "ongeveer 6,5 uur per maand, of tussen €195 en €295 per maand exclusief btw.</p>"),
 faq=[
  ("Wat kost het poetsen van gemeenschappelijke delen van een appartement?",
   "Bij ons tussen €30 en €45 per uur exclusief btw, of een vast maandbedrag. Voor een gebouw met twaalf appartementen en een lift, wekelijks anderhalf uur, komt dat op ongeveer €195 à €295 per maand."),
  ("Hoe vaak worden gemeenschappelijke delen gepoetst?",
   "In de meeste gebouwen wekelijks. Voor kleine gebouwen met weinig bewoners kan om de twee weken volstaan. Inkom en lift vragen vaak meer aandacht dan de kelders."),
  ("Wie beslist over het schoonmaakbedrijf: de syndicus of de VME?",
   "Dat staat in de statuten en de afspraken van uw VME. Meestal legt de syndicus offertes voor aan de algemene vergadering. Wij maken daarvoor een duidelijke offerte met werkschema en prijs."),
  ("Kunnen bewoners ook hun eigen ramen laten wassen?",
   "Ja. Op dezelfde dag als de gemeenschappelijke delen wassen we de ramen van bewoners die dat willen. Ze betalen rechtstreeks aan ons, voor hun eigen appartement."),
  ("Werken jullie ook voor één klein gebouw?",
   "Ja. Eén gebouw is voor ons geen te kleine opdracht, ook niet als uw VME in zelfbeheer werkt."),
 ],
 faq_onderwerp="de schoonmaak van gemeenschappelijke delen",
 towns_title="Schoonmaak voor VME's in uw regio",
 towns_intro="We werken voor appartementsgebouwen in de hele Kempen, en op afspraak ook in Turnhout, Lier, Mechelen en Hasselt.",
 gerelateerd=["kantoorschoonmaak", "ruitenwasser", "gevelreiniging"],
 service_type="Schoonmaak van gemeenschappelijke delen", price_spec=(30, 45, "per uur excl. btw"),
),
]

# ═══════════════════════════════════════════════════ ONDERWERPPAGINA'S ════
# Pagina's rond een probleem waar veel op gezocht wordt, niet rond één dienst.
# Zelfde opbouw als een dienstpagina, maar niet in de dienstkaarten op de homepage.
GIDSEN = [
dict(
 slug="groene-aanslag-verwijderen", kort="Groene aanslag verwijderen", naam="Groene aanslag verwijderen",
 kaart="Algen en mos weg van gevel, terras, oprit en dak, met een behandeling tegen hergroei.",
 title="Groene aanslag verwijderen van gevel, terras of dak",
 desc="Groene aanslag op uw gevel, terras of dak? Wat werkt, wat u beter niet doet en wat laten verwijderen kost. Vanaf €3 per m², met behandeling tegen hergroei.",
 eyebrow="Algen, mos en korstmos",
 h1="Groene aanslag verwijderen", hl="van gevel, terras en dak",
 lead=("Groene aanslag is een laagje algen en mos dat groeit waar steen lang vochtig blijft: aan de noordkant, onder bomen en op plekken waar de zon weinig komt. "
       "Het ziet er vuil uit, maakt terrassen glad en tast op termijn voegen en pleister aan. Hier leest u wat werkt, wat u beter niet doet, en wanneer u het beter laat doen."),
 punten=["Gevels, terrassen, opritten, daken en tuinmuren", "Behandeling tot in de sporen: komt veel trager terug",
         "Vanaf €3 per m², vaste prijs vooraf"],
 ill="dienst-terras", ill_alt="Terrastegels met groene aanslag: links groen, rechts weer proper",
 badge=("vanaf €3", "per m², terras of oprit"), wa="groene aanslag verwijderen",
 secties=[
  ("wat-is-het", "Wat is groene aanslag, en waarom komt het terug?", """
<p>Wat we groene aanslag noemen, is meestal een mengsel van <strong>algen</strong> (het groene laagje), <strong>mos</strong> (de donkergroene kussentjes in voegen en hoeken)
en <strong>korstmos</strong> (grijze en zwarte vlekjes die zich stevig vastzetten). Ze hebben drie dingen nodig: vocht, een beetje licht en een ruwe of poreuze ondergrond.
Stuifmeel en stof van de weg dienen als voeding.</p>
<p>Daarom zit het op een noordgevel, onder een boom of naast een lekkende dakgoot, en bijna nooit op een zonnige zuidmuur. En daarom komt het terug als u alleen
de bovenkant wegspuit: de sporen blijven in de poriën van de steen zitten, en na één vochtig seizoen is het groen er weer.</p>"""),
  ("zelf-doen", "Zelf groene aanslag verwijderen: wat werkt en wat niet", """
<ul>
 <li><strong>Hogedrukreiniger:</strong> het resultaat is meteen zichtbaar, maar de straal spuit voegen leeg en ruwt steen en tegels op. In die ruwe poriën zet nieuwe aanslag zich net sneller vast. Gebruik hem alleen op hard materiaal zoals beton en arduin, en liefst met een vlakreiniger.</li>
 <li><strong>Chloor of bleekwater:</strong> bleekt het groen weg, maar beschadigt planten en gras, kan natuursteen verkleuren en komt via de afvoer in het water terecht. Wij raden het af.</li>
 <li><strong>Groene-aanslagreiniger uit de winkel:</strong> werkt wel, maar traag. Het middel doodt de aanslag, de regen spoelt hem in de weken daarna weg. Volg de gebruiksaanwijzing en werk niet bij vorst of vlak voor regen.</li>
 <li><strong>Azijn of kristalsoda:</strong> huismiddeltjes met een tijdelijk effect. Azijn tast kalkhoudende steen en voegen aan, soda laat witte uitslag achter als u niet grondig naspoelt.</li>
 <li><strong>Borstel en voegenkrabber:</strong> prima voor een klein stuk of de voegen van een tuinpad, maar zwaar werk voor een volledig terras.</li>
</ul>
<p>Voor een tuinpad of een paar tegels komt u er zelf dus vaak wel. Voor een volledige gevel, een groot terras, alles op hoogte of een oude, zachte steen loont het om het te laten doen.</p>"""),
  ("aanpak", "Zo verwijderen wij groene aanslag, per ondergrond", """
<ul class="tick">
 <li><strong>Gevels:</strong> met softwash. Een middel doodt algen en sporen, we spoelen af met lage druk, en uw voegwerk blijft heel. Zie <a href="/gevelreiniging/">gevelreiniging</a>.</li>
 <li><strong>Terrassen en opritten:</strong> onkruid en mos uit de voegen, reinigen met een vlakreiniger, nabehandelen en opnieuw invoegen. Zie <a href="/terras-oprit-reinigen/">terras en oprit reinigen</a>.</li>
 <li><strong>Daken:</strong> mos zacht verwijderen, een behandeling tegen hergroei en de goten nadien proper. Zie <a href="/dakreiniging/">dak ontmossen</a>.</li>
 <li><strong>Tuinmuren, carports, tuinhuizen en bloembakken:</strong> vaak in dezelfde beurt als gevel of terras.</li>
 <li><strong>De onderrand van zonnepanelen:</strong> daar groeit na enkele jaren mos, dat we zacht verwijderen. Zie <a href="/zonnepanelen-reinigen/">zonnepanelen reinigen</a>.</li>
</ul>
<p>Planten, ramen en schrijnwerk dekken we af voor we beginnen, en we werken bij droog, vorstvrij weer, zodat het middel zijn werk kan doen.</p>"""),
  ("voorkomen", "Groene aanslag voorkomen: vijf dingen die helpen", """
<ol>
 <li><strong>Laat licht en lucht binnen.</strong> Snoei struiken en takken die tegen de gevel of boven het terras hangen.</li>
 <li><strong>Laat water weglopen.</strong> Een overlopende of lekkende <a href="/dakgoot-reinigen/">dakgoot</a> is de nummer één oorzaak van een groene streep op een gevel.</li>
 <li><strong>Veeg het terras geregeld.</strong> Blad en aarde die blijven liggen, houden vocht vast en voeden nieuwe aanslag.</li>
 <li><strong>Behandel na het reinigen.</strong> Een nabehandeling die de sporen doodt, houdt het oppervlak veel langer proper.</li>
 <li><strong>Impregneer waar het zinvol is.</strong> Poreuze baksteen en tegels nemen dan minder water op. We zeggen u eerlijk of het bij uw ondergrond iets oplevert.</li>
</ol>"""),
 ],
 tussen_cta="Stuur ons een foto van de groene plek, dan krijgt u vandaag nog een prijs.",
 prijs_titel="Wat kost groene aanslag laten verwijderen?",
 prijs_intro=("De prijs hangt af van de ondergrond, de oppervlakte en hoe dik de aanslag zit. U krijgt altijd een vaste prijs vooraf, "
              "na foto's of een plaatsbezoek. Prijzen inclusief btw voor particulieren."),
 prijzen=[("Terras of oprit", "€3 – €7", "Per m², forfait vanaf €170"),
          ("Gevel in baksteen", "€8 – €15", "Per m², met softwash"),
          ("Gevel in crepi of sierpleister", "€12 – €22", "Per m², vraagt meer zorg"),
          ("Dak ontmossen", "op maat", "Vaste prijs na foto's of plaatsbezoek"),
          ("Tuinmuur, carport of tuinhuis", "op maat", "Vaak samen met gevel of terras")],
 prijs_na=("<p><strong>Rekenvoorbeeld:</strong> een achtergevel van 40 m² in baksteen kost 40 × €8 à €15, dus €320 à €600. Laat u in dezelfde afspraak ook een terras "
           "van 60 m² reinigen (€180 à €420), dan rekenen we één verplaatsing.</p>"),
 faq=[
  ("Wat is het verschil tussen groene en zwarte aanslag?",
   "Groene aanslag bestaat vooral uit algen en mos en zit vrij los. Zwarte aanslag is meestal korstmos of zwarte algen: die zetten zich veel steviger vast, hebben meer inwerktijd nodig en soms een tweede behandeling."),
  ("Is groene aanslag schadelijk?",
   "Niet voor uw gezondheid, wel voor uw woning. Een groen terras wordt glad, een groene gevel blijft langer nat, waardoor voegen en pleister sneller vergaan en vorst meer schade doet. Mos op het dak spoelt bovendien in uw dakgoot."),
  ("Wat is het beste middel tegen groene aanslag?",
   "Een middel dat ook de sporen doodt en lang genoeg kan inwerken, bij droog weer en zonder vorst. Alleen wegspuiten helpt maar een paar maanden. Chloor of bleekwater raden we af: het schaadt planten en kan steen verkleuren."),
  ("Wanneer verwijdert u groene aanslag het best?",
   "In het voorjaar of in het begin van de herfst, bij droog en vorstvrij weer. Na de behandeling is een droge dag ideaal, zodat het middel niet meteen wegspoelt."),
  ("Hoe lang blijft een oppervlak proper na een behandeling?",
   "Een gevel meestal meerdere jaren, een terras in de schaduw iets korter. Hoe zonniger en luchtiger de plek, hoe langer het duurt voor het groen terugkomt. Regelmatig vegen en impregneren verlengen die periode."),
 ],
 faq_onderwerp="groene aanslag",
 towns_title="Groene aanslag verwijderen in uw gemeente", towns_intro=TOWNS_INTRO,
 gerelateerd=["gevelreiniging", "terras-oprit-reinigen", "dakreiniging"],
 service_type="Verwijderen van groene aanslag", price_spec=(3, 22, "per m²"),
),
]
