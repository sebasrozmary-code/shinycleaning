# -*- coding: utf-8 -*-
"""
Gemeentepagina's (/ruitenwasser/<gemeente>/). Zoekwoordfamilie per gemeente:
ruitenwasser / ramenwasser / glazenwasser / ramen wassen / schoonmaakbedrijf + gemeente.

Belangrijk voor Google: elke pagina moet echt iets eigens vertellen (deelgemeenten,
type woningen, wat er lokaal speelt). Kopieer dus nooit een pagina om er alleen
de naam in te vervangen — dat ziet Google als een 'doorway page'.
"""

STEDEN = [

dict(
 slug="geel", naam="Geel",
 title="Ruitenwasser Geel | Ramen wassen in Bel, Larum en Zammel",
 desc="Ruitenwasser en schoonmaakbedrijf in Geel, onze thuisbasis. Ramen, zonnepanelen, dakgoten en kantoren in Bel, Larum, Zammel, Punt en Stelen. Vanaf €55.",
 eyebrow="Ruitenwasser · ramenwasser · glazenwasser Geel",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Geel",
 lead=("Geel is onze thuisbasis. Van het centrum rond de Grote Markt tot Bel, Larum, Zammel en Ten Aard: we zijn hier elke werkdag op de baan. "
       "Dat betekent snel ingepland, geen verplaatsingskosten en elke keer dezelfde mensen aan uw ramen."),
 punten=["Onze thuisbasis: vaak dezelfde week ingepland", "Geen verplaatsingsvergoeding", "Ramen, zonnepanelen, dakgoten en kantoren"],
 ill="hero-ramen", ill_alt="Ruitenwasser wast een raam met trekker, emmer en sproeiflacon",
 secties=[
  ("om-de-hoek", "Uw ruitenwasser om de hoek", """
<p>Wie een ruitenwasser in Geel zoekt, wil vooral iemand die komt wanneer het is afgesproken. Omdat we hier wonen en werken, rijden we dagelijks door alle
wijken en gehuchten. Een extra rolluik, een veranda die er deze keer bij moet, of een dakgoot die na een storm vol ligt: dat regelen we meestal nog dezelfde week.</p>
<p>Geel is ook een gemeente van contrasten. Rond het centrum en de Sint-Dimpnakerk staan veel rijwoningen en appartementen. In Bel, Larum, Zammel,
Winkelomheide en Ten Aard zijn het vooral vrijstaande woningen met een grote tuin, veel glas en vaak een veranda. Voor elk type woning hebben we
een vaste prijs, zodat u vooraf weet waar u aan toe bent.</p>"""),
  ("bedrijven-geel", "Schoonmaak voor bedrijven in Geel", """
<p>Van winkels en praktijken in het centrum tot kantoren en werkplaatsen op de bedrijventerreinen rond Geel-West en Geel-Punt: voor bedrijven doen we de
<a href="/kantoorschoonmaak/">kantoorschoonmaak</a>, de glasbewassing van gevels en etalages, en periodieke dieptereiniging van vloeren en tapijt.
Met een vast team, een schriftelijk werkschema en een maandelijkse factuur. Omdat we in Geel gevestigd zijn, staan we er ook snel als er iets tussenkomt.</p>"""),
 ],
 diensten_lokaal={
  "ruitenwasser": "voor rijwoningen in het centrum en vrijstaande woningen in de gehuchten, op een vast schema.",
  "dakgoot-reinigen": "in de groene gehuchten met veel bomen raakt een goot snel vol. Plan een beurt in het najaar.",
  "kantoorschoonmaak": "voor winkels, praktijken en kantoren, van het centrum tot de bedrijventerreinen.",
 },
 deel_titel="In heel Geel, niet alleen in het centrum",
 deel_intro="We werken in alle wijken en gehuchten van Geel, overal zonder verplaatsingskosten. Onder meer in:",
 deelgemeenten=["Geel-Centrum", "Bel", "Larum", "Zammel", "Punt", "Stelen", "Ten Aard", "Winkelomheide", "Oosterlo", "Holven", "Elsum", "Sint-Dimpna"],
 prijs_tekst=("Omdat Geel onze thuisbasis is, rekent u hier nooit verplaatsingskosten. Voor een rijwoning in het centrum betaalt u doorgaans €55 à €70 per beurt "
              "voor de buitenzijde, voor een vrijstaande woning in de gehuchten €85 à €115. Met een vast schema betaalt u per beurt minder."),
 faq=[
  ("Hoe snel kan een ruitenwasser in Geel langskomen?",
   "Meestal binnen de week, in het voorjaar iets later. Omdat we elke werkdag in Geel werken, plannen we een extra beurt of een dringende opdracht vaak nog dezelfde week in."),
  ("Komen jullie ook naar Bel, Larum en Winkelomheide?",
   "Ja, we werken in heel Geel: van het centrum tot Bel, Larum, Zammel, Punt, Stelen, Ten Aard, Winkelomheide en Oosterlo. Overal zonder verplaatsingskosten."),
  ("Doen jullie ook kantoren en winkels in Geel?",
   "Ja. Voor winkels, praktijken en bedrijven doen we kantoorschoonmaak, glasbewassing van etalages en gevels, en periodieke dieptereiniging. Met een vast team en een maandelijkse factuur."),
 ],
 buren=["Mol", "Olen", "Westerlo", "Meerhout", "Laakdal", "Kasterlee"],
),

dict(
 slug="mol", naam="Mol",
 title="Ruitenwasser Mol | Ramen wassen in Ezaart, Gompel en Rauw",
 desc="Ruitenwasser in Mol: ramen, zonnepanelen en dakgoten in Mol-Centrum, Ezaart, Gompel, Achterbos, Millegem, Rauw en Postel. Vaste prijs vanaf €55 per beurt.",
 eyebrow="Ruitenwasser · ramenwasser · glazenwasser Mol",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Mol",
 lead=("Mol ligt midden in het groen: bossen, heide en de meren rond het Zilvermeer. Mooi om te wonen, maar dennennaalden en blad zitten snel in uw dakgoot, "
       "en in de schaduw krijgt een gevel sneller groene aanslag. Wij wassen uw ramen, kuisen uw goten en houden uw woning proper, in heel Mol."),
 punten=["Elke week in Mol aan het werk", "Ramen, dakgoten en zonnepanelen in één beurt", "Vaste prijs, zonder verplaatsingskosten"],
 ill="dienst-dakgoten", ill_alt="Dakgoot vol bladeren en naalden wordt leeggemaakt",
 secties=[
  ("groen", "Wonen in het groen vraagt ander onderhoud", """
<p>In wijken als Millegem, Ezaart, Rauw en rond Postel staan veel woningen tussen de bomen. Daar zien we elk jaar dezelfde drie dingen terugkomen:
dakgoten vol naalden en blad, groene aanslag op noordgevels en terrassen, en ramen die in de lente sneller vuil worden door stuifmeel.</p>
<p>Daarom stellen we in Mol vaak een combinatie voor: de <a href="/ruitenwasser/">ramen</a> op een vast schema, de <a href="/dakgoot-reinigen/">dakgoten</a>
in het najaar, en om de paar jaar de <a href="/gevelreiniging/">gevel</a> of het terras. Alles bij één firma, met één vaste prijs per beurt.</p>"""),
  ("centrum", "Van Mol-Centrum tot de Molse Meren", """
<p>In het centrum rond de Sint-Pieter-en-Pauwelkerk wassen we de ramen van rijwoningen, appartementen en winkels, etalages op vraag voor de openingstijd.
In Gompel, Achterbos en Sluis gaat het vaker om vrijstaande woningen met een veranda of zonnepanelen op het bijgebouw.
Voor appartementsgebouwen poetsen we ook de <a href="/gemeenschappelijke-delen/">gemeenschappelijke delen</a>, op een vast schema voor de syndicus.</p>"""),
 ],
 diensten_lokaal={
  "dakgoot-reinigen": "tussen de dennen van Millegem, Rauw en Postel een jaarlijkse must, liefst in het najaar.",
  "gevelreiniging": "groene aanslag op noordgevels onder de bomen, zacht verwijderd met softwash.",
  "zonnepanelen-reinigen": "stuifmeel en naalden van de bossen blijven aan de onderrand liggen. Een beurt in het voorjaar helpt.",
 },
 deel_titel="In alle wijken van Mol",
 deel_intro="We werken in heel Mol, van het centrum tot de gehuchten aan de rand. Onder meer in:",
 deelgemeenten=["Mol-Centrum", "Ezaart", "Gompel", "Achterbos", "Millegem", "Rauw", "Sluis", "Wezel", "Donk", "Ginderbuiten", "Postel"],
 prijs_tekst=("Mol ligt op een kwartier van onze basis in Geel en valt binnen ons standaard werkgebied: geen verplaatsingskosten. "
              "Voor een halfopen woning betaalt u doorgaans €65 à €85 per beurt voor de buitenzijde. Laat u de dakgoten meenemen in dezelfde beurt, "
              "dan betaalt u maar één verplaatsing."),
 faq=[
  ("Wanneer laat ik in Mol best mijn dakgoten uitkuisen?",
   "Eind oktober tot begin december, als de meeste bladeren gevallen zijn. Woont u tussen de naaldbomen, dan raden we een tweede beurt in het voorjaar aan."),
  ("Komen jullie ook in Postel en Millegem?",
   "Ja, we werken in heel Mol: van het centrum tot Ezaart, Gompel, Achterbos, Millegem, Rauw, Sluis en Postel."),
  ("Kunnen jullie ramen wassen en dakgoten reinigen in één beurt?",
   "Ja, en dat is ook voordeliger: u betaalt één verplaatsing. Veel klanten in Mol combineren ramen, dakgoten en zonnepanelen in één afspraak."),
 ],
 buren=["Geel", "Balen", "Dessel", "Retie", "Meerhout"],
),

dict(
 slug="herentals", naam="Herentals",
 title="Ruitenwasser Herentals | Ook in Noorderwijk en Morkhoven",
 desc="Ruitenwasser en schoonmaakbedrijf in Herentals, Noorderwijk en Morkhoven. Ramen, etalages, zonnepanelen en kantoorschoonmaak, met een vaste prijs vooraf.",
 eyebrow="Ruitenwasser · glazenwasser · schoonmaakbedrijf Herentals",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Herentals",
 lead=("Herentals combineert een levendig centrum rond de Grote Markt met bedrijventerreinen langs het Albertkanaal en rustige woonwijken in Noorderwijk en Morkhoven. "
       "Wij wassen ramen en etalages, poetsen kantoren en houden woningen proper, met een vast team."),
 punten=["Etalages en winkelpuien vóór openingstijd", "Kantoorschoonmaak met een vast team", "Woningen in Herentals, Noorderwijk en Morkhoven"],
 ill="bedrijven-kantoor", ill_alt="Kantoorgebouw met schoonmaakkar voor de deur",
 secties=[
  ("centrum", "Etalages en winkels in het centrum", """
<p>Een etalage is het eerste wat een klant ziet. Rond de Grote Markt en in de winkelstraten tussen de Zandpoort en de Bovenpoort wassen we etalages en
winkelpuien wekelijks of om de twee weken, 's morgens vroeg, zodat u bij openingstijd klaar bent. Horecazaken en praktijken helpen we met glas binnen en buiten,
en op vraag met de dagelijkse schoonmaak.</p>"""),
  ("wonen", "Woningen in Noorderwijk en Morkhoven", """
<p>Buiten het centrum wonen veel gezinnen in vrijstaande en halfopen woningen, vaak met een veranda, zonnepanelen en een grote tuin. Daar doen we de
<a href="/ruitenwasser/">ramen</a> op een vast schema, de <a href="/zonnepanelen-reinigen/">zonnepanelen</a> in het voorjaar en de dakgoten in het najaar.
Wie zijn terras voor de zomer weer proper wil, plant dat best in maart.</p>"""),
  ("bedrijven", "Kantoorschoonmaak op de bedrijventerreinen", """
<p>Voor kantoren en bedrijfsgebouwen langs het Albertkanaal en aan de rand van de stad verzorgen we de wekelijkse
<a href="/kantoorschoonmaak/">kantoorschoonmaak</a>, de glasbewassing van gevels en lichtstraten, en periodieke vloer- en tapijtreiniging.
Vast team, schriftelijk werkschema en maandelijks opzegbaar.</p>"""),
 ],
 diensten_lokaal={
  "ruitenwasser": "etalages en winkelpuien in het centrum, woningen in Noorderwijk en Morkhoven.",
  "kantoorschoonmaak": "voor kantoren, praktijken en bedrijfsgebouwen, buiten de werkuren.",
  "terras-oprit-reinigen": "terrassen en opritten klaar voor de zomer. Plan in februari of maart.",
 },
 deel_titel="In heel Herentals",
 deel_intro="We werken in het centrum en in beide deelgemeenten:",
 deelgemeenten=["Herentals-Centrum", "Noorderwijk", "Morkhoven"],
 prijs_tekst=("Herentals valt binnen ons standaard werkgebied, zonder verplaatsingskosten. Voor woningen gelden onze gewone richtprijzen hieronder. "
              "Voor etalages en kantoren maken we een prijs per beurt of per maand, op basis van de oppervlakte glas en hoe vaak we komen."),
 faq=[
  ("Kunnen jullie onze etalage wassen voor de winkel opengaat?",
   "Ja. We plannen etalages in Herentals vroeg in de ochtend, wekelijks of om de twee weken, zodat alles proper is bij openingstijd."),
  ("Werken jullie ook in Noorderwijk en Morkhoven?",
   "Ja, in heel Herentals: het centrum, Noorderwijk en Morkhoven."),
  ("Hoe snel kunnen jullie starten met een schoonmaakcontract?",
   "Na een plaatsbezoek en uw akkoord meestal binnen twee weken. Stapt u over van een andere firma, dan stemmen we de start af op uw opzegtermijn."),
 ],
 buren=["Olen", "Kasterlee", "Westerlo", "Geel", "Heist-op-den-Berg"],
),

dict(
 slug="westerlo", naam="Westerlo",
 title="Ruitenwasser Westerlo | Tongerlo, Oevel en Zoerle-Parwijs",
 desc="Ruitenwasser in Westerlo, Tongerlo, Oevel, Zoerle-Parwijs en Heultje. Ramen, zonnepanelen op woning en loods, dakgoten en gevels. Vaste prijs vanaf €55.",
 eyebrow="Ruitenwasser · ramenwasser Westerlo",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Westerlo",
 lead=("Westerlo combineert een gezellig centrum met landelijke deelgemeenten als Tongerlo, Oevel en Zoerle-Parwijs. Veel woningen hebben er ruimte, veel glas "
       "en zonnepanelen, vaak ook op een schuur of loods. Wij wassen uw ramen, reinigen uw zonnepanelen en houden uw gevel en dakgoten in orde."),
 punten=["Zonnepanelen op woning, schuur en loods", "Ramen op vast schema in alle deelgemeenten", "Op een kwartier van onze basis in Geel"],
 ill="dienst-zonnepanelen", ill_alt="Zonnepaneel wordt gereinigd met een zachte borstel",
 secties=[
  ("landelijk", "Landelijk wonen, meer onderhoud buiten", """
<p>Rond Tongerlo, Oevel en Zoerle-Parwijs staan veel vrijstaande woningen en boerderijen, met grote ramen, een veranda en zonnepanelen op het dak of het bijgebouw.
Naast akkers en weilanden worden ramen en panelen sneller stoffig, zeker in het voor- en najaar als het land bewerkt wordt. Een vast schema voor de
<a href="/ruitenwasser/">ramen</a> en een jaarlijkse beurt voor de <a href="/zonnepanelen-reinigen/">zonnepanelen</a> houden dat onder controle.</p>"""),
  ("loodsen", "Zonnepanelen op stallen en loodsen", """
<p>Op landbouwbedrijven en loodsen liggen vaak tientallen panelen. Stof van het land en uit stallen vormt er een hardnekkige laag die regen niet wegspoelt.
We reinigen ook grote installaties met osmosewater en een zachte borstel, zonder hogedruk. Voor grote aantallen maken we een prijs per paneel op maat,
na een plaatsbezoek of op basis van foto's.</p>"""),
  ("tongerlo", "Van het centrum tot bij de abdij van Tongerlo", """
<p>In het centrum van Westerlo wassen we de ramen van woningen, appartementen en winkels. In Tongerlo, rond de abdij, en in Heultje en Voortkapel gaat het
meer om woningen met tuin. Overal gelden dezelfde vaste prijzen.</p>"""),
 ],
 diensten_lokaal={
  "zonnepanelen-reinigen": "op woningen, schuren en loodsen, ook grote installaties met een prijs op maat.",
  "ruitenwasser": "om de zes à acht weken voor woningen naast akkers en weilanden.",
  "gevelreiniging": "voor boerderijen en vrijstaande woningen, zacht met softwash.",
 },
 deel_titel="In alle deelgemeenten van Westerlo",
 deel_intro="We werken in het centrum en in alle deelgemeenten en gehuchten:",
 deelgemeenten=["Westerlo-Centrum", "Tongerlo", "Oevel", "Zoerle-Parwijs", "Heultje", "Voortkapel"],
 prijs_tekst=("Westerlo ligt op een kwartier van Geel en valt binnen ons standaard werkgebied, zonder verplaatsingskosten. Voor een open bebouwing betaalt u doorgaans "
              "€85 à €115 per beurt voor de buitenzijde van de ramen. Zonnepanelen reinigen kost €5 à €10 per paneel."),
 faq=[
  ("Reinigen jullie ook zonnepanelen op een schuur of loods?",
   "Ja. Op landbouwgebouwen en loodsen reinigen we ook grote installaties, met osmosewater en een zachte borstel. Voor grote aantallen maken we een prijs op maat."),
  ("Komen jullie ook naar Heultje en Voortkapel?",
   "Ja, in heel Westerlo: het centrum, Tongerlo, Oevel, Zoerle-Parwijs, Heultje en Voortkapel."),
  ("Hoe vaak laat ik mijn ramen wassen als ik naast een akker woon?",
   "Om de zes à acht weken. Stof van het land zet zich snel op ramen vast, zeker in het voorjaar en na de oogst."),
 ],
 buren=["Geel", "Herentals", "Olen", "Laakdal", "Herselt", "Heist-op-den-Berg"],
),

dict(
 slug="laakdal", naam="Laakdal",
 title="Ruitenwasser Laakdal | Eindhout, Vorst, Veerle, Varendonk",
 desc="Ruitenwasser in Laakdal: ramen, zonnepanelen, dakgoten en terrassen in Eindhout, Vorst, Klein-Vorst, Veerle en Varendonk. Vaste prijs vooraf, vanaf €55.",
 eyebrow="Ruitenwasser · ramenwasser Laakdal",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Laakdal",
 lead=("Laakdal bestaat uit vier dorpen met elk een eigen karakter: Eindhout, Vorst, Veerle en Varendonk. Wij kennen ze allemaal. We wassen uw ramen, "
       "reinigen uw zonnepanelen en terras, en kuisen uw dakgoten uit, met een vaste prijs per beurt."),
 punten=["Vaste dag in alle vier de dorpen", "Ramen, zonnepanelen en terras in één beurt", "Zonder verplaatsingskosten"],
 ill="dienst-terras", ill_alt="Terrastegels worden gereinigd met een vlakreiniger",
 secties=[
  ("dorpen", "Vier dorpen, één vaste ruitenwasser", """
<p>In Laakdal wonen de meeste mensen in een vrijstaande of halfopen woning, vaak met een ruime tuin en een terras. We plannen onze beurten per dorp,
zodat we in Eindhout, Vorst, Veerle en Varendonk telkens op vaste momenten langskomen. Zo krijgt u een vaste dag, en rijden wij niet heen en weer.
Dat houdt de prijs laag.</p>"""),
  ("laak", "Terrassen en gevels in de vallei van de Laak", """
<p>Langs de Laak en de beboste stukken rond Veerle en Vorst is het vochtiger, en dat ziet u aan terrassen en noordgevels: groene aanslag komt er snel terug.
We reinigen <a href="/terras-oprit-reinigen/">terrassen en opritten</a> met een vlakreiniger, voegen opnieuw in met polymeerzand en behandelen
<a href="/gevelreiniging/">gevels</a> met softwash. Dat blijft jaren langer proper dan alleen een beurt met de hogedrukreiniger.</p>"""),
 ],
 diensten_lokaal={
  "terras-oprit-reinigen": "met vlakreiniger en polymeerzand, zodat de groene aanslag niet meteen terugkomt.",
  "ruitenwasser": "op een vaste dag per dorp: Eindhout, Vorst, Veerle en Varendonk.",
  "gevelreiniging": "voor noordgevels die in de vochtige Laakvallei groen worden.",
 },
 deel_titel="In alle dorpen van Laakdal",
 deel_intro="We plannen per dorp, zodat u een vaste dag krijgt:",
 deelgemeenten=["Eindhout", "Vorst", "Klein-Vorst", "Veerle", "Varendonk"],
 prijs_tekst=("Laakdal valt binnen ons standaard werkgebied, zonder verplaatsingskosten. Voor een vrijstaande woning betaalt u doorgaans €85 à €115 per beurt "
              "voor de buitenzijde van de ramen. Een terras reinigen kost €3 à €7 per m², met een forfait vanaf €170 voor kleine oppervlaktes."),
 faq=[
  ("Komen jullie in alle deelgemeenten van Laakdal?",
   "Ja: Eindhout, Vorst, Klein-Vorst, Veerle en Varendonk. We plannen per dorp, zodat u een vaste dag krijgt."),
  ("Waarom komt de groene aanslag op mijn terras zo snel terug?",
   "Door vocht en schaduw, en omdat na alleen hogedruk de sporen blijven zitten. Wij reinigen met een vlakreiniger, voegen in met polymeerzand en impregneren op vraag. Zo blijft het merkbaar langer proper."),
  ("Wanneer plan ik de terrasreiniging best?",
   "In februari of begin maart, dan is uw terras klaar voor de eerste warme dagen. In maart en april is onze planning snel vol."),
 ],
 buren=["Meerhout", "Geel", "Westerlo", "Herselt", "Diest"],
),

dict(
 slug="olen", naam="Olen",
 title="Ruitenwasser Olen | Ook in Sint-Jozef- en O.-L.-V.-Olen",
 desc="Ruitenwasser in Olen, onze buurgemeente: ramen, zonnepanelen, dakgoten en gevels in Olen-Centrum, Sint-Jozef-Olen en Onze-Lieve-Vrouw-Olen. Vanaf €55.",
 eyebrow="Ruitenwasser · ramenwasser Olen",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Olen",
 lead=("Olen grenst aan Geel, en dat merkt u: we zijn hier bijna dagelijks aan het werk. In Olen-Centrum, Sint-Jozef-Olen en Onze-Lieve-Vrouw-Olen "
       "wassen we ramen, reinigen we zonnepanelen en kuisen we dakgoten uit. Snel ingepland, met een vaste prijs."),
 punten=["Buurgemeente van Geel: bijna dagelijks in Olen", "Extra beurt vaak dezelfde week", "Geen verplaatsingskosten"],
 ill="dienst-ramen", ill_alt="Ramen wassen met een telescoopsteel aan een grote raampartij",
 secties=[
  ("buren", "Uw ruitenwasser uit de buurgemeente", """
<p>Olen ligt op tien minuten van onze basis. Daardoor kunnen we flexibel zijn: een extra beurt voor een feest, ramen na werken aan uw woning,
of een dakgoot die na een storm vol ligt, plannen we vaak nog dezelfde week. Vaste klanten krijgen een vaste dag, en een seintje de dag voordien.</p>"""),
  ("parochies", "Drie parochies, veel verschillende woningen", """
<p>Olen bestaat uit drie parochies: Olen-Centrum, Sint-Jozef-Olen en Onze-Lieve-Vrouw-Olen. U vindt er rijwoningen langs de dorpskernen, nieuwe verkavelingen
en vrijstaande woningen tussen het groen. Veel nieuwere woningen hebben grote raampartijen, schuiframen en zonnepanelen. Die houden we op een vast schema proper,
met osmosewater en zonder ladder. Voor bedrijven in Olen doen we ook <a href="/kantoorschoonmaak/">kantoorschoonmaak</a> en glasbewassing.</p>"""),
 ],
 diensten_lokaal={
  "ruitenwasser": "ook grote raampartijen en schuiframen, met osmosewater en zonder ladder.",
  "zonnepanelen-reinigen": "voor de vele nieuwere woningen met panelen, liefst in het voorjaar.",
 },
 deel_titel="In alle parochies van Olen",
 deel_intro="Olen is onze buurgemeente. We werken in:",
 deelgemeenten=["Olen-Centrum", "Sint-Jozef-Olen", "Onze-Lieve-Vrouw-Olen"],
 prijs_tekst=("Als buurgemeente van Geel valt Olen binnen ons standaard werkgebied: geen verplaatsingskosten. Voor een rijwoning betaalt u doorgaans €55 à €70 per beurt "
              "voor de buitenzijde, voor een vrijstaande woning €85 à €115."),
 faq=[
  ("Kunnen jullie in Olen snel een extra beurt inplannen?",
   "Meestal wel. Omdat Olen naast Geel ligt, zijn we er bijna dagelijks. Een extra beurt plannen we vaak nog dezelfde week."),
  ("Werken jullie in alle parochies van Olen?",
   "Ja, in Olen-Centrum, Sint-Jozef-Olen en Onze-Lieve-Vrouw-Olen."),
  ("Wassen jullie ook grote raampartijen en schuiframen?",
   "Ja. Grote raampartijen wassen we met osmosewater en een telescoopsteel, zonder ladder. Bij schuiframen nemen we op vraag ook de rails mee."),
 ],
 buren=["Geel", "Herentals", "Westerlo", "Kasterlee"],
),

dict(
 slug="meerhout", naam="Meerhout",
 title="Ruitenwasser Meerhout | Ook in Zittaart en Gestel",
 desc="Ruitenwasser en schoonmaakbedrijf in Meerhout, Zittaart en Gestel. Ramen, veranda's, zonnepanelen, dakgoten en gevels, met een vaste prijs vooraf vanaf €55.",
 eyebrow="Ruitenwasser · ramenwasser Meerhout",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Meerhout",
 lead=("Meerhout is een rustige gemeente tussen Geel, Mol en Laakdal, met veel ruim wonen in de gehuchten Zittaart en Gestel. "
       "Wij wassen uw ramen op een vast schema, reinigen zonnepanelen en gevels, en kuisen uw dakgoten uit voor de winter."),
 punten=["Vaste dag voor Meerhout, Zittaart en Gestel", "Ramen, veranda en zonnepanelen in één beurt", "Vaste prijs, zonder verplaatsingskosten"],
 ill="dienst-gevel", ill_alt="Gevel met groene aanslag die met softwash wordt gereinigd",
 secties=[
  ("ruim", "Ruim wonen, veel glas", """
<p>In Meerhout, Zittaart en Gestel staan veel vrijstaande woningen met grote ramen, een veranda of een serre. Dat geeft veel licht, en veel glas om proper te houden.
Met osmosewater en een telescoopsteel wassen we ook hoge en grote ruiten zonder ladder, en de veranda nemen we mee in dezelfde beurt:
glas, dak en profielen.</p>"""),
  ("nete", "Groene aanslag in de vallei van de Grote Nete", """
<p>Langs de Grote Nete en in de lager gelegen stukken is het vochtiger. Daar zien we meer groene aanslag op gevels en daken aan de noordkant.
Met <a href="/gevelreiniging/">softwash</a> verwijderen we die zonder de gevel te beschadigen, en met een
<a href="/dakreiniging/">anti-mosbehandeling</a> blijft uw dak jaren proper.</p>"""),
 ],
 diensten_lokaal={
  "ruitenwasser": "inclusief veranda's en serres, in dezelfde beurt.",
  "gevelreiniging": "voor gevels die in de vochtige Netevallei groen worden, zonder hogedruk.",
  "dakreiniging": "zacht ontmossen met een behandeling tegen hergroei.",
 },
 deel_titel="In heel Meerhout",
 deel_intro="We werken in het centrum en in de gehuchten:",
 deelgemeenten=["Meerhout-Centrum", "Zittaart", "Gestel"],
 prijs_tekst=("Meerhout valt binnen ons standaard werkgebied, zonder verplaatsingskosten. Voor een vrijstaande woning betaalt u doorgaans €85 à €115 per beurt "
              "voor de buitenzijde van de ramen. Een veranda kost €120 à €280 extra, afhankelijk van de grootte."),
 faq=[
  ("Wassen jullie ook de veranda in Meerhout?",
   "Ja: glas, dak en profielen. Dat kan in dezelfde beurt als de ramen, dan betaalt u maar één verplaatsing."),
  ("Komen jullie ook naar Zittaart en Gestel?",
   "Ja, in heel Meerhout: het centrum, Zittaart en Gestel."),
  ("Mijn noordgevel wordt groen, wat kan ik doen?",
   "Een softwashbehandeling verwijdert de aanslag zonder schade en doodt ook de sporen. Met een impregneermiddel nadien blijft de gevel langer proper."),
 ],
 buren=["Geel", "Laakdal", "Mol", "Balen"],
),

dict(
 slug="balen", naam="Balen",
 title="Ruitenwasser Balen | Ook in Olmen, Schoor en Hulsen",
 desc="Ruitenwasser in Balen, Olmen, Schoor en Hulsen: ramen, zonnepanelen, dakgoten en terrassen. Vaste prijs vooraf vanaf €55 per beurt, met planning per dorp.",
 eyebrow="Ruitenwasser · ramenwasser Balen",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Balen",
 lead=("Van het centrum van Balen tot Olmen, Schoor en Hulsen: wij wassen uw ramen, reinigen uw zonnepanelen en terras, en kuisen uw dakgoten uit. "
       "We plannen per dorp, zodat u een vaste dag heeft en de prijs scherp blijft."),
 punten=["Planning per dorp: een vaste dag", "Ramen, zonnepanelen en terras", "Vaste prijs vooraf"],
 ill="dienst-zonnepanelen", ill_alt="Zonnepanelen worden gereinigd met een zachte borstel",
 secties=[
  ("kernen", "Balen en Olmen: twee kernen, één planning", """
<p>Balen heeft twee grote kernen, Balen en Olmen, en daarrond gehuchten als Schoor en Hulsen. We combineren onze klanten per buurt.
Daardoor rijden we niet heen en weer, en kunnen we een vaste dag garanderen: om de vier, zes, acht of twaalf weken, met een seintje de dag voordien.</p>"""),
  ("bos-heide", "Tussen bos en heide rond de Keiheuvel", """
<p>Rond de Keiheuvel en de bossen richting Mol en Lommel staan veel woningen tussen het groen. Naalden en blad komen er snel in de dakgoot terecht,
en daken en terrassen in de schaduw krijgen mos. We <a href="/dakgoot-reinigen/">kuisen de goten uit</a> in het najaar, <a href="/dakreiniging/">ontmossen daken</a>
zacht en reinigen terrassen met een vlakreiniger. Zonnepanelen reinigen we in het voorjaar, vóór de zonnigste maanden.</p>"""),
 ],
 diensten_lokaal={
  "zonnepanelen-reinigen": "in het voorjaar, zodat uw panelen proper zijn voor de zonnigste maanden.",
  "dakgoot-reinigen": "voor woningen tussen de bossen: minstens één keer per jaar, in het najaar.",
  "ruitenwasser": "met een vaste dag per dorp in Balen, Olmen, Schoor en Hulsen.",
 },
 deel_titel="In heel Balen",
 deel_intro="We plannen per dorp en gehucht:",
 deelgemeenten=["Balen-Centrum", "Olmen", "Schoor", "Hulsen"],
 prijs_tekst=("Balen valt binnen ons werkgebied, zonder verplaatsingskosten. Door onze planning per dorp houden we de prijs scherp: voor een halfopen woning betaalt u "
              "doorgaans €65 à €85 per beurt voor de buitenzijde. Zonnepanelen reinigen kost €5 à €10 per paneel."),
 faq=[
  ("Komen jullie ook naar Olmen en Hulsen?",
   "Ja, in heel Balen: het centrum, Olmen, Schoor en Hulsen. We plannen per dorp, zodat u een vaste dag krijgt."),
  ("Hoe krijg ik een vaste dag voor mijn ramen?",
   "Met een vast schema. U kiest om de vier, zes, acht of twaalf weken, en krijgt een vaste dag met een seintje de dag voordien."),
  ("Kan ik zonnepanelen en dakgoten samen laten doen?",
   "Ja, in dezelfde beurt. Dan betaalt u maar één verplaatsing."),
 ],
 buren=["Mol", "Meerhout", "Dessel", "Beringen"],
),

dict(
 slug="dessel", naam="Dessel",
 title="Ruitenwasser Dessel | Ramen wassen in Dessel en Witgoor",
 desc="Ruitenwasser in Dessel en Witgoor: ramen, zonnepanelen, dakgoten en gevels, voor woningen en bedrijven. Vaste prijs vooraf vanaf €55, geen verplaatsingskosten.",
 eyebrow="Ruitenwasser · glazenwasser Dessel",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Dessel",
 lead=("Dessel is een compacte gemeente tussen Mol en Retie, met een gezellige dorpskern en de wijk Witgoor. Wij wassen uw ramen op een vast schema, "
       "reinigen zonnepanelen en gevels, en doen de glasbewassing en schoonmaak voor bedrijven in de buurt."),
 punten=["Vaste ronde samen met Mol en Retie", "Voor woningen én bedrijven", "Vaste prijs vooraf"],
 ill="hero-ramen", ill_alt="Ruitenwasser wast een raam met een trekker",
 secties=[
  ("ronde", "Een vaste ronde met Mol en Retie", """
<p>Dessel ligt op onze vaste ronde met Mol en Retie. Daardoor komen we hier geregeld langs, en kunnen we u een vaste dag voor uw ramen geven.
Nieuwe klanten plannen we in op de eerstvolgende ronde, meestal binnen één à twee weken.</p>"""),
  ("wonen", "Van de dorpskern tot Witgoor", """
<p>In de dorpskern gaat het vaak om rijwoningen en appartementen, in Witgoor en de verkavelingen daarrond om vrijstaande woningen met tuin.
Voor elke woning gelden dezelfde vaste prijzen. Staat er een veranda, een serre of zonnepanelen op het bijgebouw, dan nemen we die mee in dezelfde beurt.</p>"""),
  ("bedrijven", "Ook voor bedrijven in Dessel", """
<p>Voor bedrijven, winkels en praktijken in Dessel verzorgen we <a href="/ruitenwasser/#bedrijven">glasbewassing</a> en
<a href="/kantoorschoonmaak/">kantoorschoonmaak</a> met een vast team. U krijgt een maandelijkse factuur, en één contactpersoon die u kunt bellen
of een bericht kunt sturen.</p>"""),
 ],
 diensten_lokaal={
  "ruitenwasser": "op onze vaste ronde met Mol en Retie, meestal binnen één à twee weken ingepland.",
  "kantoorschoonmaak": "voor bedrijven, winkels en praktijken, met een vast team.",
 },
 deel_titel="In heel Dessel",
 deel_intro="We werken in de dorpskern en in Witgoor:",
 deelgemeenten=["Dessel-Centrum", "Witgoor"],
 prijs_tekst=("Dessel valt binnen ons werkgebied, zonder verplaatsingskosten. Voor een rijwoning betaalt u doorgaans €55 à €70 per beurt voor de buitenzijde, "
              "voor een vrijstaande woning €85 à €115."),
 faq=[
  ("Hoe snel kunnen jullie in Dessel beginnen?",
   "Meestal binnen één à twee weken, op de eerstvolgende ronde langs Mol, Dessel en Retie."),
  ("Werken jullie ook in Witgoor?",
   "Ja, in heel Dessel, ook in Witgoor."),
  ("Doen jullie ook glasbewassing voor bedrijven in Dessel?",
   "Ja. Voor bedrijven, winkels en praktijken wassen we etalages, gevelbeglazing en ramen op een vast schema, met een maandelijkse factuur exclusief btw."),
 ],
 buren=["Mol", "Retie", "Balen"],
),

dict(
 slug="retie", naam="Retie",
 title="Ruitenwasser Retie | Ramen wassen in Retie en Schoonbroek",
 desc="Ruitenwasser in Retie en Schoonbroek: ramen, zonnepanelen, dakgoten, daken en terrassen. Vaste prijs vooraf vanaf €55 per beurt, op een vaste ronde met Dessel.",
 eyebrow="Ruitenwasser · ramenwasser Retie",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Retie",
 lead=("Retie ligt midden in het groen, met het Prinsenpark en veel bos rondom. Heerlijk om te wonen, maar het vraagt ander onderhoud: dakgoten vol blad en naalden, "
       "mos op daken en terrassen, en ramen die in de lente sneller stoffig worden. Wij houden het proper, met een vaste prijs per beurt."),
 punten=["Ramen, dakgoten en daken in één beurt", "Vaste ronde met Dessel en Mol", "Vaste prijs vooraf"],
 ill="dienst-dak", ill_alt="Pannendak waarvan het mos met een borstel wordt verwijderd",
 secties=[
  ("groen", "Wonen tussen het groen rond het Prinsenpark", """
<p>In Retie en Schoonbroek staan veel woningen tussen de bomen. Dat merkt u vooral in de herfst: dakgoten lopen vol, en in de schaduw groeit mos op daken,
terrassen en opritten. We <a href="/dakgoot-reinigen/">kuisen dakgoten uit</a> in het najaar, <a href="/dakreiniging/">ontmossen daken</a>
met een zachte methode en een behandeling tegen hergroei, en reinigen <a href="/terras-oprit-reinigen/">terrassen</a> met een vlakreiniger.</p>"""),
  ("ronde", "Een vaste dag, samen met Dessel en Mol", """
<p>Retie ligt op onze vaste ronde met Dessel en Mol. Zo komen we geregeld langs en kunnen we u een vaste dag voor uw ramen geven, met een seintje de dag voordien.
Een extra beurt voor dakgoten of zonnepanelen plannen we op dezelfde ronde.</p>"""),
 ],
 diensten_lokaal={
  "dakgoot-reinigen": "tussen de bossen minstens één keer per jaar, eind oktober tot begin december.",
  "dakreiniging": "zacht ontmossen zonder hogedruk, met een behandeling tegen hergroei.",
  "terras-oprit-reinigen": "groene aanslag en mos weg met een vlakreiniger.",
 },
 deel_titel="In heel Retie",
 deel_intro="We werken in de dorpskern en in Schoonbroek:",
 deelgemeenten=["Retie-Centrum", "Schoonbroek"],
 prijs_tekst=("Retie valt binnen ons werkgebied, zonder verplaatsingskosten. Voor een vrijstaande woning betaalt u doorgaans €85 à €115 per beurt "
              "voor de buitenzijde van de ramen. Dakgoten reinigen kost €3 à €5 per lopende meter."),
 faq=[
  ("Werken jullie ook in Schoonbroek?",
   "Ja, in heel Retie: de dorpskern en Schoonbroek."),
  ("Hoe vaak moet ik mijn dakgoten laten uitkuisen als ik tussen de bomen woon?",
   "Minstens één keer per jaar, eind oktober tot begin december. Met veel naaldbomen raden we een tweede beurt in het voorjaar aan."),
  ("Kunnen jullie mijn dak ontmossen zonder hogedruk?",
   "Ja. We verwijderen mos met een borstel en lage druk, en behandelen het dak tegen hergroei. Hogedruk op oude pannen maakt ze ruw, en dan komt het mos juist sneller terug."),
 ],
 buren=["Dessel", "Mol", "Kasterlee", "Turnhout"],
),

dict(
 slug="kasterlee", naam="Kasterlee",
 title="Ruitenwasser Kasterlee | Ook in Lichtaart en Tielen",
 desc="Ruitenwasser in Kasterlee, Lichtaart en Tielen: ramen, dakgoten, zonnepanelen en schoonmaak van vakantiewoningen. Vaste prijs vooraf, vanaf €55 per beurt.",
 eyebrow="Ruitenwasser · ramenwasser Kasterlee",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Kasterlee",
 lead=("Kasterlee, Lichtaart en Tielen liggen in het hart van de bosrijke Kempen, met de Hoge Mouw en de Kabouterberg als bekendste plekken. "
       "Wij wassen de ramen van woningen, kuisen dakgoten uit en maken vakantiewoningen en B&B's klaar voor de volgende gasten."),
 punten=["Woningen, vakantiewoningen en B&B's", "Dakgoten en daken tussen de bossen", "Vaste prijs vooraf"],
 ill="dienst-oplevering", ill_alt="Emmer, zwabber en sleutels, klaar voor de wisselschoonmaak van een vakantiewoning",
 secties=[
  ("bos", "Wonen in de bossen: dakgoten en daken", """
<p>Rond Kasterlee, Lichtaart en Tielen staan veel woningen tussen dennen en loofbomen. Dennennaalden zijn verraderlijk: in de goot vormen ze een dichte mat
die het water tegenhoudt. We <a href="/dakgoot-reinigen/">kuisen dakgoten uit</a> in het najaar, en waar nodig ook in het voorjaar.
Daken en terrassen die groen worden, reinigen we zacht, zodat het mos niet meteen terugkomt.</p>"""),
  ("vakantie", "Vakantiewoningen, B&B's en tweede verblijven", """
<p>Kasterlee trekt veel toeristen, en veel eigenaars verhuren een vakantiewoning of B&B. Wij doen de wisselschoonmaak tussen gasten,
de grote kuis voor het seizoen en de <a href="/ruitenwasser/">ramen</a> op een vast schema. U geeft ons een sleutel of code,
en wij zorgen dat alles proper is voor de volgende gasten.</p>"""),
 ],
 diensten_lokaal={
  "dakgoot-reinigen": "dennennaalden vormen een dichte mat in de goot. Plan een beurt in het najaar, vaak ook in het voorjaar.",
  "opleveringsschoonmaak": "ook de wisselschoonmaak van vakantiewoningen en de grote kuis voor het seizoen.",
  "ruitenwasser": "voor woningen, B&B's en vakantiewoningen, op een vast schema.",
 },
 deel_titel="In heel Kasterlee",
 deel_intro="We werken in Kasterlee en in beide deelgemeenten:",
 deelgemeenten=["Kasterlee-Centrum", "Lichtaart", "Tielen"],
 prijs_tekst=("Kasterlee valt binnen ons werkgebied, zonder verplaatsingskosten. Voor een vrijstaande woning betaalt u doorgaans €85 à €115 per beurt "
              "voor de buitenzijde van de ramen. Voor de schoonmaak van vakantiewoningen maken we een vaste prijs per wissel."),
 faq=[
  ("Doen jullie ook de schoonmaak van vakantiewoningen in Kasterlee?",
   "Ja: de wisselschoonmaak tussen gasten, de grote kuis voor het seizoen en de ramen. Met een sleutel of code hoeft u er niet bij te zijn."),
  ("Komen jullie ook naar Lichtaart en Tielen?",
   "Ja, in heel Kasterlee: het centrum, Lichtaart en Tielen."),
  ("Waarom raakt mijn dakgoot zo snel verstopt?",
   "Dennennaalden vormen in een goot een dichte mat die water tegenhoudt, en blad en mos doen de rest. Tussen de bomen is een beurt in het najaar het minimum, vaak aangevuld met een beurt in het voorjaar."),
 ],
 buren=["Herentals", "Olen", "Geel", "Retie", "Turnhout"],
),
# ═══════════════════════════════════════════════ UITBREIDING (sept. 2026) ════
# regio="kempen": dagelijks, geen verplaatsingskosten.  regio="buiten": op afspraak,
# gebundeld per dag, eventuele verplaatsingsvergoeding altijd vooraf in de prijs.

dict(
 slug="turnhout", naam="Turnhout", regio="kempen",
 title="Ruitenwasser Turnhout | Ook in Zevendonk en Schorvoort",
 desc="Ruitenwasser en schoonmaakbedrijf in Turnhout, Zevendonk en Schorvoort: ramen, etalages, appartementsgebouwen en kantoren. Vaste prijs vooraf, vanaf €55.",
 eyebrow="Ruitenwasser · glazenwasser · schoonmaakbedrijf Turnhout",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Turnhout",
 lead=("Turnhout, de hoofdstad van de Kempen, is een echte winkelstad: een druk centrum rond de Grote Markt, veel appartementen boven en naast de handelspanden, "
       "en rustiger woonwijken als Zevendonk en Schorvoort. Wij wassen ramen en etalages, poetsen trappenhallen en kantoren, en houden woningen proper, met een vaste prijs per beurt."),
 punten=["Etalages en winkelpuien vóór openingstijd", "Appartementsgebouwen: glas en trappenhal in één ronde", "Geen verplaatsingskosten"],
 ill="dienst-vme", ill_alt="Appartementsgebouw met propere ramen, een emmer met zwabber en een checklist",
 secties=[
  ("eerste-indruk", "Winkelpuien, horeca en praktijken in het centrum", """
<p>In een winkelstad telt de eerste indruk. Een pui met strepen of een inkomdeur vol vingerafdrukken valt op, zeker naast een buur die wel blinkt.
We komen vóór openingstijd, zodat er geen emmer in de weg staat wanneer uw eerste klant binnenstapt. Horecazaken rond de Grote Markt helpen we
met terrasramen en glazen windschermen, praktijken en kantoren met het glas binnen en buiten en, op vraag, de wekelijkse
<a href="/kantoorschoonmaak/">kantoorschoonmaak</a>.</p>"""),
  ("appartementen", "Appartementsgebouwen: trappenhal en ramen samen", """
<p>Turnhout telt veel appartementsgebouwen, in het centrum en langs de invalswegen. Voor syndici en VME's poetsen we de
<a href="/gemeenschappelijke-delen/">gemeenschappelijke delen</a> op een vaste dag: inkomhal, trappen, lift, brievenbussen en kelders, met een kort rapport na elke beurt.
Het glas van de inkom en de traphal nemen we in dezelfde ronde mee. Bewoners die dat willen, laten hun eigen ramen op dezelfde dag wassen, met een eigen factuur.</p>"""),
  ("wijken", "Zevendonk, Schorvoort en de groene rand van de stad", """
<p>Verder van het centrum wordt Turnhout groener. In Zevendonk en Schorvoort, en richting Oud-Turnhout, Beerse en Vosselaar, staan meer vrijstaande en halfopen woningen,
vaak met zonnepanelen en een veranda. Daar wassen we de <a href="/ruitenwasser/">ramen</a> op een vast schema, reinigen we
<a href="/zonnepanelen-reinigen/">zonnepanelen</a> in het voorjaar en kuisen we <a href="/dakgoot-reinigen/">dakgoten</a> uit in het najaar.</p>"""),
 ],
 diensten_lokaal={
  "ruitenwasser": "etalages en winkelpuien in het centrum, appartementen en woningen in alle wijken.",
  "gemeenschappelijke-delen": "inkom, trappen en lift van appartementsgebouwen, met een rapport per beurt.",
  "kantoorschoonmaak": "kantoren en praktijken in het centrum en aan de rand van de stad, buiten de werkuren.",
 },
 deel_titel="In heel Turnhout en de buurgemeenten",
 deel_intro="We werken in het centrum en in alle wijken van Turnhout, en in de gemeenten errond:",
 deelgemeenten=["Turnhout-Centrum", "Zevendonk", "Schorvoort", "Oud-Turnhout", "Beerse", "Vosselaar"],
 prijs_tekst=("Turnhout hoort bij ons standaard werkgebied in de Kempen: u betaalt geen verplaatsingskosten. Voor een rijwoning betaalt u doorgaans €55 à €70 per beurt "
              "voor de buitenzijde van de ramen. Voor etalages en appartementsgebouwen maken we een prijs per beurt of per maand, op basis van het glas en hoe vaak we komen."),
 faq=[
  ("Wassen jullie ook de ramen van appartementen in Turnhout?",
   "Ja. Tot ongeveer de derde verdieping werken we met de telescoopsteel vanaf de grond. Hoger of moeilijk bereikbaar glas bekijken we per gebouw. Plannen we meerdere bewoners van hetzelfde gebouw op dezelfde dag, dan blijft de prijs per appartement laag."),
  ("Betaal ik verplaatsingskosten in Turnhout?",
   "Nee. Turnhout hoort bij ons standaard werkgebied in de Kempen. U betaalt alleen de beurt zelf. Combineert u ramen met zonnepanelen of dakgoten, dan komen we één keer voor alles."),
  ("Werken jullie ook in Oud-Turnhout, Beerse en Vosselaar?",
   "Ja. Die gemeenten nemen we mee op dezelfde ronde als Turnhout."),
 ],
 buren=["Kasterlee", "Retie", "Herentals"],
),

dict(
 slug="heist-op-den-berg", naam="Heist-op-den-Berg", regio="kempen",
 title="Ruitenwasser Heist-op-den-Berg | Booischot, Hallaar, Itegem",
 desc="Ruitenwasser in Heist-op-den-Berg, Booischot, Hallaar, Itegem, Schriek en Wiekevorst: ramen, veranda's, zonnepanelen en dakgoten. Vaste prijs vanaf €55.",
 eyebrow="Ruitenwasser · ramenwasser Heist-op-den-Berg",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Heist-op-den-Berg",
 lead=("Heist-op-den-Berg is een uitgestrekte gemeente in de Zuiderkempen, met zes deelgemeenten van Booischot tot Wiekevorst. "
       "Veel woningen staan er vrij, met een grote tuin, een veranda en zonnepanelen. Wij wassen uw ramen, reinigen uw zonnepanelen en kuisen uw dakgoten uit, "
       "met een vaste prijs per beurt."),
 punten=["Alle zes deelgemeenten, van Booischot tot Wiekevorst", "Ramen, veranda en zonnepanelen in één beurt", "Vaste prijs vooraf, vanaf €55"],
 ill="part-raam", ill_alt="Raam met een kalender ernaast: ramen wassen op een vast schema",
 secties=[
  ("zes-kernen", "Zes deelgemeenten, één planning", """
<p>Heist-Centrum, Booischot, Hallaar, Itegem, Schriek en Wiekevorst liggen ver uit elkaar. Daarom plannen we per deelgemeente: zo rijden we niet heen en weer tussen twee adressen,
en blijft de prijs scherp. U krijgt een vaste dag voor uw ramen en een seintje de dag voordien. Ook in de gehuchten, zoals Zonderschot en Pijpelheide, komen we langs.</p>"""),
  ("veel-glas", "Vrijstaande woningen met veel glas en zonnepanelen", """
<p>Rond het centrum op de Berg en in de deelgemeenten staan veel vrijstaande woningen en fermettes met grote raampartijen, een veranda en vaak een rij zonnepanelen
op het dak of op een bijgebouw. Een veranda wassen we volledig: glas, dak en profielen, binnen en buiten. <a href="/zonnepanelen-reinigen/">Zonnepanelen</a> reinigen we
met osmosewater en een zachte borstel. En in de vallei van de Grote Nete, waar het langer vochtig blijft, halen we
<a href="/groene-aanslag-verwijderen/">groene aanslag</a> van terrassen en noordgevels.</p>"""),
 ],
 diensten_lokaal={
  "ruitenwasser": "vrijstaande woningen en veranda's in alle zes deelgemeenten, op een vast schema.",
  "zonnepanelen-reinigen": "op het woonhuis of een bijgebouw, met osmosewater en een zachte borstel.",
  "terras-oprit-reinigen": "terrassen en opritten in klinkers of natuursteen, klaar voor de zomer.",
 },
 deel_titel="In alle deelgemeenten van Heist-op-den-Berg",
 deel_intro="We werken in het centrum en in alle deelgemeenten en gehuchten, onder meer in:",
 deelgemeenten=["Heist-Centrum", "Booischot", "Hallaar", "Itegem", "Schriek", "Wiekevorst", "Zonderschot", "Pijpelheide"],
 prijs_tekst=("Heist-op-den-Berg hoort bij ons werkgebied in de Kempen, zonder verplaatsingskosten. Voor een vrijstaande woning betaalt u doorgaans €85 à €115 per beurt "
              "voor de buitenzijde van de ramen. Een veranda of glazen overkapping kost €120 à €280, afhankelijk van de grootte."),
 faq=[
  ("Komen jullie in alle deelgemeenten van Heist-op-den-Berg?",
   "Ja: in Heist-Centrum, Booischot, Hallaar, Itegem, Schriek en Wiekevorst, en in gehuchten zoals Zonderschot en Pijpelheide. We plannen per deelgemeente, zodat u een vaste dag krijgt."),
  ("Wassen jullie ook de veranda en het glazen dak?",
   "Ja: glas, dak en profielen, binnen en buiten. Een glazen dak wassen we vanaf de grond met de telescoopsteel, zonder erop te lopen. Reken op €120 à €280, afhankelijk van de grootte en hoe vuil het dak is."),
  ("Hoe vaak laat ik mijn ramen wassen als ik landelijk woon?",
   "Naast akkers en onverharde wegen worden ramen sneller stoffig. Vier tot zes keer per jaar is dan een goed ritme, in het voorjaar iets vaker wanneer de velden bewerkt worden en de bomen stuiven."),
 ],
 buren=["Herselt", "Westerlo", "Herentals", "Aarschot"],
),

dict(
 slug="herselt", naam="Herselt", regio="kempen",
 title="Ruitenwasser Herselt | Ook in Ramsel en Blauberg",
 desc="Ruitenwasser en schoonmaakbedrijf in Herselt, Ramsel en Blauberg: ramen, zonnepanelen, dakgoten en groene aanslag op terras en gevel. Vaste prijs vooraf.",
 eyebrow="Ruitenwasser · glazenwasser Herselt",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Herselt",
 lead=("Herselt ligt op de grens van de Kempen en het Hageland, op een twintigtal minuten van onze basis in Geel. In Herselt, Ramsel en Blauberg wassen we ramen, "
       "reinigen we zonnepanelen en kuisen we dakgoten uit. Snel ingepland, met een vaste prijs per beurt en zonder verplaatsingskosten."),
 punten=["Herselt, Ramsel en Blauberg", "Ramen, dakgoten en terras in één afspraak", "Geen verplaatsingskosten"],
 ill="part-huis", ill_alt="Vrijstaande woning met blinkende ramen en sterretjes",
 secties=[
  ("grensstreek", "Tussen Kempen en Hageland", """
<p>Rond Herselt wisselen bos, weiland en glooiende akkers elkaar af. Mooi om te wonen, en dat ziet u ook aan de woningen: stof van de akkers op de ramen, blad en naalden
in de dakgoten, en groene aanslag op terrassen en noordgevels. We pakken het graag in één afspraak aan: de <a href="/ruitenwasser/">ramen</a>, de
<a href="/dakgoot-reinigen/">dakgoten</a> en, waar nodig, de <a href="/groene-aanslag-verwijderen/">groene aanslag</a> op uw terras of gevel.</p>"""),
  ("ronde", "Samen ingepland met Westerlo", """
<p>Herselt grenst aan Westerlo, waar we elke week aan het werk zijn, en ligt vlak bij Laakdal en Heist-op-den-Berg. Zo combineren we uw adres met klanten in de buurt,
en krijgt u een vaste dag voor uw ramen. Ook winkels, praktijken en kleine bedrijven in het centrum van Herselt helpen we, met glasbewassing en schoonmaak buiten de openingsuren.</p>"""),
 ],
 diensten_lokaal={
  "ruitenwasser": "woningen in Herselt, Ramsel en Blauberg, op een vast schema samen met Westerlo.",
  "dakgoot-reinigen": "tussen bos en akkers minstens één keer per jaar, in het najaar.",
  "terras-oprit-reinigen": "groene aanslag van terrassen en opritten, met een nabehandeling tegen hergroei.",
 },
 deel_titel="In heel Herselt",
 deel_intro="We werken in het centrum van Herselt en in de andere kernen:",
 deelgemeenten=["Herselt-Centrum", "Ramsel", "Blauberg"],
 prijs_tekst=("Herselt valt binnen ons werkgebied in de Kempen, zonder verplaatsingskosten. Voor een vrijstaande woning betaalt u doorgaans €85 à €115 per beurt "
              "voor de buitenzijde van de ramen. Dakgoten reinigen kost €3 à €5 per lopende meter, een terras reinigen €3 à €7 per m²."),
 faq=[
  ("Werken jullie ook in Ramsel en Blauberg?",
   "Ja, in heel Herselt: het centrum, Ramsel en Blauberg, overal zonder verplaatsingskosten."),
  ("Kan ik ramen, dakgoten en terras in één afspraak laten doen?",
   "Graag zelfs. We komen dan één keer, u krijgt één factuur en u regelt alles in één bericht. Een goed moment voor die combinatie is het najaar, als de bomen hun blad kwijt zijn."),
  ("Hoe krijg ik groene aanslag van mijn terras weg?",
   "Met een vlakreiniger en een nabehandeling die ook de sporen doodt. Zonder die nabehandeling is het groen na een paar maanden terug. Een gewone hogedrukreiniger spuit de voegen uit en ruwt de tegels op, waardoor nieuwe aanslag zich net sneller vastzet."),
 ],
 buren=["Westerlo", "Heist-op-den-Berg", "Laakdal", "Aarschot"],
),

dict(
 slug="beringen", naam="Beringen", regio="buiten",
 title="Ruitenwasser Beringen | Beverlo, Koersel en Paal",
 desc="Ruitenwasser en schoonmaakbedrijf in Beringen, Beverlo, Koersel en Paal: ramen, zonnepanelen, dakgoten en kantoren. Vaste prijs vooraf, vanaf €55 per beurt.",
 eyebrow="Ruitenwasser · glazenwasser Beringen",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Beringen",
 lead=("Beringen is een mijnstad in het westen van Limburg, met vier deelgemeenten: Beringen, Beverlo, Koersel en Paal. Van de mijnwijken rond be-MINE tot de nieuwere verkavelingen: "
       "wij wassen uw ramen, reinigen zonnepanelen en poetsen kantoren, met een vaste prijs die u vooraf kent."),
 punten=["Beringen, Beverlo, Koersel en Paal", "Woningen, kantoren en handelszaken", "Afspraken per dag gebundeld"],
 ill="over-ons-busje", ill_alt="Het busje van Shiny Cleaning met ladders op het dak",
 secties=[
  ("mijnstad", "Van de mijnwijken tot nieuwe verkavelingen", """
<p>Beringen is gegroeid rond de steenkoolmijn. In de wijken rond Beringen-Mijn staan veel rijwoningen en karakteristieke cité-woningen, in Beverlo, Koersel en Paal
vooral vrijstaande woningen en recente verkavelingen met grote glaspartijen. Elk type woning vraagt een eigen aanpak: kleine ruitjes en roedeverdeling doen we met trekker
en inwasser, grote ramen en veranda's aan de buitenkant met osmosewater en de telescoopsteel.</p>"""),
  ("bedrijven", "Kantoren en bedrijven langs het Albertkanaal", """
<p>Langs het Albertkanaal en de E313 liggen grote bedrijventerreinen, en rond be-MINE en in het centrum zitten winkels, praktijken en horeca.
Voor bedrijven doen we <a href="/kantoorschoonmaak/">kantoorschoonmaak</a> met een vast team, de glasbewassing van gevels en lichtstraten,
en de reiniging van <a href="/zonnepanelen-reinigen/">zonnepanelen op bedrijfsdaken</a>. Met een schriftelijk werkschema en een maandelijkse factuur.</p>"""),
  ("planning", "Hoe we plannen in Beringen", """
<p>Beringen ligt op ongeveer een halfuur van onze basis in Geel. We bundelen de afspraken in Beringen en omgeving op dezelfde dag, zodat de verplaatsing
laag blijft of helemaal wegvalt. Wat u betaalt, staat altijd vooraf in uw prijs.</p>"""),
 ],
 diensten_lokaal={
  "ruitenwasser": "van cité-woningen in Beringen-Mijn tot vrijstaande woningen in Beverlo, Koersel en Paal.",
  "kantoorschoonmaak": "voor kantoren, praktijken en handelszaken, met een vast team en een schriftelijk werkschema.",
  "zonnepanelen-reinigen": "op woningen en bedrijfsdaken, zacht en zonder hogedruk.",
 },
 deel_titel="In alle deelgemeenten van Beringen",
 deel_intro="We werken in de vier deelgemeenten en hun wijken, onder meer in:",
 deelgemeenten=["Beringen-Centrum", "Beringen-Mijn", "Beverlo", "Koersel", "Stal", "Paal"],
 prijs_tekst=("Voor woningen in Beringen gelden onze gewone richtprijzen hieronder. Omdat Beringen buiten ons dagelijkse werkgebied ligt, kan er een kleine verplaatsingsvergoeding bij komen. "
              "Die staat altijd vooraf in uw prijs, en valt vaak weg als we dezelfde dag al in de buurt werken."),
 faq=[
  ("Komen jullie ook naar Beverlo, Koersel en Paal?",
   "Ja, in heel Beringen: het centrum, Beringen-Mijn, Beverlo, Koersel met Stal, en Paal."),
  ("Betaal ik verplaatsingskosten in Beringen?",
   "Soms een kleine vergoeding, omdat Beringen buiten ons dagelijkse werkgebied ligt. U ziet ze altijd vooraf in uw prijs. Plannen we uw adres op een dag dat we al in de buurt zijn, dan valt ze meestal weg."),
  ("Doen jullie ook kantoorschoonmaak in Beringen?",
   "Ja. Voor kantoren, praktijken en handelszaken werken we met een vast team, een schriftelijk werkschema en een maandelijkse factuur. We starten altijd met een gratis plaatsbezoek."),
 ],
 buren=["Balen", "Laakdal", "Diest"],
),

dict(
 slug="diest", naam="Diest", regio="buiten",
 title="Ruitenwasser Diest | Schaffen, Webbekom en Molenstede",
 desc="Ruitenwasser en schoonmaakbedrijf in Diest, Schaffen, Webbekom, Molenstede, Deurne en Kaggevinne: ramen, oude gevels, dakgoten. Vaste prijs vooraf.",
 eyebrow="Ruitenwasser · glazenwasser Diest",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Diest",
 lead=("Diest combineert een historische binnenstad aan de Demer met rustige deelgemeenten als Schaffen, Webbekom en Molenstede. Van herenhuizen met hoge ramen "
       "tot vrijstaande woningen met zonnepanelen: wij wassen uw ramen en reinigen gevels en dakgoten, met een vaste prijs die u vooraf kent."),
 punten=["Binnenstad en alle deelgemeenten", "Hoge ramen en oude gevels, met de nodige zorg", "Afspraken per dag gebundeld"],
 ill="dienst-gevel", ill_alt="Oude bakstenen gevel die met lage druk wordt gereinigd",
 secties=[
  ("binnenstad", "Hoge ramen en oude gevels in de binnenstad", """
<p>In de binnenstad, tussen de Grote Markt, het begijnhof en de citadel, staan veel oude herenhuizen en handelspanden met hoge ramen en kleine ruitjes.
De buitenkant wassen we met de telescoopsteel vanaf de straat, zonder ladder tegen de gevel. Oude baksteen en natuursteen reinigen we alleen met
<a href="/gevelreiniging/">softwash op lage druk</a>: hogedruk spuit historisch voegwerk in één keer uit.</p>"""),
  ("deelgemeenten", "Schaffen, Webbekom en de andere deelgemeenten", """
<p>Buiten de stadskern wordt Diest landelijker. In Schaffen, Webbekom, Molenstede, Deurne en Kaggevinne staan veel vrijstaande woningen met een tuin, een terras en vaak zonnepanelen.
Daar plannen we de <a href="/ruitenwasser/">ramen</a> op een vast schema, de <a href="/dakgoot-reinigen/">dakgoten</a> in het najaar en het
<a href="/terras-oprit-reinigen/">terras</a> in het voorjaar. Handelszaken en praktijken in het centrum helpen we met etalages en glas, vroeg op de dag.</p>"""),
 ],
 diensten_lokaal={
  "ruitenwasser": "hoge ramen in de binnenstad, vrijstaande woningen in de deelgemeenten.",
  "gevelreiniging": "oude baksteen en natuursteen, altijd met lage druk.",
  "dakgoot-reinigen": "in het najaar, zodra het blad van de bomen is.",
 },
 deel_titel="In heel Diest",
 deel_intro="We werken in de binnenstad en in alle deelgemeenten:",
 deelgemeenten=["Diest-Centrum", "Schaffen", "Webbekom", "Molenstede", "Deurne", "Kaggevinne"],
 prijs_tekst=("Voor woningen in Diest gelden onze gewone richtprijzen hieronder. Diest ligt buiten ons dagelijkse werkgebied, op een halfuur van Geel, en daarom bundelen we "
              "de afspraken hier per dag. Een eventuele verplaatsingsvergoeding staat altijd vooraf in uw prijs."),
 faq=[
  ("Kunnen jullie de hoge ramen van een herenhuis wassen?",
   "Ja. Met de telescoopsteel werken we vanaf de straat tot ongeveer de derde verdieping, zonder ladder tegen uw gevel. Kleine ruitjes aan de binnenzijde doen we met de hand."),
  ("Werken jullie ook in Schaffen, Webbekom en Molenstede?",
   "Ja, in heel Diest: de binnenstad, Schaffen, Webbekom, Molenstede, Deurne en Kaggevinne."),
  ("Mag een oude gevel met hogedruk gereinigd worden?",
   "Liever niet. Hogedruk spuit oude kalkmortel uit de voegen en beschadigt zachte baksteen en natuursteen. Wij reinigen oude gevels met softwash: een middel doet het werk, en we spoelen af met lage druk."),
 ],
 buren=["Beringen", "Laakdal", "Aarschot", "Herselt"],
),

dict(
 slug="aarschot", naam="Aarschot", regio="buiten",
 title="Ruitenwasser Aarschot | Ook in Gelrode, Langdorp en Rillaar",
 desc="Ruitenwasser en schoonmaakbedrijf in Aarschot, Gelrode, Langdorp en Rillaar: ramen, gevels in ijzerzandsteen, dakgoten en zonnepanelen. Vaste prijs vooraf.",
 eyebrow="Ruitenwasser · glazenwasser Aarschot",
 h1="Ruitenwasser en schoonmaakbedrijf", hl="in Aarschot",
 lead=("Aarschot ligt aan de Demer, in het Hageland, met Gelrode, Langdorp en Rillaar als deelgemeenten. Wij wassen uw ramen, reinigen gevels en dakgoten "
       "en houden zonnepanelen proper, voor woningen en bedrijven, met een vaste prijs vooraf."),
 punten=["Aarschot, Gelrode, Langdorp en Rillaar", "IJzerzandsteen en oude gevels: zacht gereinigd", "Afspraken per dag gebundeld"],
 ill="werkgebied", ill_alt="Kaart met een centrale pin: we plannen de afspraken per regio",
 secties=[
  ("ijzerzandsteen", "Gevels in ijzerzandsteen en baksteen", """
<p>Het Hageland heeft zijn eigen bouwsteen: de bruine ijzerzandsteen van de Onze-Lieve-Vrouwekerk en van veel oudere huizen. Die steen is zacht en poreus,
en neemt vocht en groene aanslag makkelijk op. Met een hogedrukreiniger spuit u er zo de bovenlaag af. Wij reinigen zulke gevels met
<a href="/gevelreiniging/">softwash</a> op lage druk, en zeggen u eerlijk of impregneren bij uw gevel iets oplevert.</p>"""),
  ("hageland", "Van de Demervallei tot de heuvels van het Hageland", """
<p>Rond Aarschot wisselen de Demervallei, boomgaarden en beboste heuvels elkaar af. In Gelrode, Langdorp en Rillaar staan veel vrijstaande woningen met een grote tuin.
Daar wassen we de <a href="/ruitenwasser/">ramen</a> op een vast schema, kuisen we de <a href="/dakgoot-reinigen/">dakgoten</a> uit in het najaar
en reinigen we de <a href="/zonnepanelen-reinigen/">zonnepanelen</a> in het voorjaar.</p>"""),
 ],
 diensten_lokaal={
  "gevelreiniging": "ijzerzandsteen en oude baksteen, altijd met lage druk.",
  "ruitenwasser": "woningen in Aarschot, Gelrode, Langdorp en Rillaar, op een vast schema.",
  "zonnepanelen-reinigen": "zacht, met osmosewater, meestal vanaf de grond.",
 },
 deel_titel="In heel Aarschot",
 deel_intro="We werken in het centrum en in de drie deelgemeenten:",
 deelgemeenten=["Aarschot-Centrum", "Gelrode", "Langdorp", "Rillaar"],
 prijs_tekst=("Voor woningen in Aarschot gelden onze gewone richtprijzen hieronder. Aarschot ligt buiten ons dagelijkse werkgebied, dus plannen we de afspraken hier samen op één dag. "
              "Komt er een verplaatsingsvergoeding bij, dan ziet u die vooraf in uw prijs."),
 faq=[
  ("Hoe reinigen jullie een gevel in ijzerzandsteen?",
   "Met softwash: we brengen een middel aan dat algen en mos doodt, laten het inwerken en spoelen af met lage druk. Zo blijft de zachte bovenlaag van de steen heel. Hogedruk gebruiken we op ijzerzandsteen nooit."),
  ("Komen jullie ook naar Gelrode, Langdorp en Rillaar?",
   "Ja, in heel Aarschot: het centrum, Gelrode, Langdorp en Rillaar."),
  ("Hoe snel kunnen jullie in Aarschot langskomen?",
   "Meestal binnen twee weken, omdat we de afspraken in Aarschot en omgeving samen op één dag plannen. Voor een dringende klus, zoals een overlopende dakgoot, zoeken we een snellere oplossing."),
 ],
 buren=["Diest", "Herselt", "Heist-op-den-Berg"],
),
]

SLUG = {c["naam"]: c["slug"] for c in STEDEN}
