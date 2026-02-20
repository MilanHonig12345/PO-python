# PO-python door Mayla Hinze en Milan Honig

**Onderwerp:**
Het spel heet “Epic Zombie Battle”. Het gaat over een zombie-apocalyps. Jij bent een speler die tegen een zombie moet vechten. Beide hebben vier levens. Het doel is om alle levens van de zombie te verliezen voordat jij zelf geen levens meer hebt.
Om dat te doen, speel je verschillende minigames. Elke minigame is een uitdaging, zoals raden, rekenen of geheugen testen. Als je een minigame wint, verliest de zombie een leven. Als je verliest, verlies jij een leven. Het spel stopt meteen als iemand geen levens meer heeft.

<b><u> Reflectie Mayla </u></b> <br>
Tijdens het maken van het spel “Epic Zombie Battle” heb ik veel geleerd over programmeren. Ik heb geleerd hoe je een spel stap voor stap opbouwt. Ook heb ik geleerd hoe je functies maakt en hoe je globale variabelen gebruikt om de levens van de speler en de zombie bij te houden. Zo blijft het spel logisch en overzichtelijk.
Een techniek die ik goed heb leren gebruiken is het maken van aparte functies voor elke minigame. Hierdoor werd mijn code overzichtelijker. Ook kon ik makkelijker fouten oplossen en het spel aanpassen. Ik heb geleerd hoe je het spel automatisch kunt stoppen als iemand geen levens meer heeft. Dat heb ik gedaan met sys.exit(). Hier zijn we op gekomen, doordat we ons probleem hadden voorgelegd aan chat gpt en die zei dat we dat konden gebruiken. 
Het moeilijkste vond ik ervoor zorgen dat het spel echt stopt als iemand geen levens meer heeft. Eerst ging het spel gewoon door. Ik heb dit opgelost door in elke functie te controleren of de speler of zombie levens over had. Als dat niet zo was, stopte het spel meteen. Ook het combineren van alle minigames was lastig. Ik heb dit opgelost door ze één voor één te testen en duidelijke prints te gebruiken.<br>
De samenwerking tussen mij en Milan verliep heel soepel. We hebben goed met elkaar overlegd over hoe we dingen gingen aanpakken. De taakverdeling is ook erg eerlijk gegaan, Milan en ik hebben beide verschillende mini-games gemaakt. Ook hebben we elkaars fouten verbeterd. 
Het programmeren van de minigames ging goed. Alles werkt zoals het moet en de levens worden goed bijgehouden. Tegelijk is dit ook wel een beetje waar we tegen aan liepen. Ik denk dat we tussen door meer vragen aan onze docent hadden moeten stellen. <br>
We hebben gekozen voor een zombie-thema. Ook hebben we gekozen dat het spel stopt als iemand geen levens meer heeft en dat de minigames in een vaste volgorde komen. We kozen zombies omdat het spannend is en veel mensen het leuk vinden. Het geeft een duidelijk doel: overleven en winnen van de zombie. Een belangrijke keuze is dat de speler en de zombie allebei vier levens hebben. Dit maakt het spel eerlijk en spannend. Zo kan je meerdere minigames spelen zonder dat het te snel voorbij is.<br>
Voor mijn gevoel heb ik goed aan dit project gezeten. Ook waren we al snel gelijk aan de slag gegaan, omdat we maar twee weken de tijd hadden.
Ik ben eigenlijk gewoon trots om het hele spel. In de lessen vond ik het hoofdstuk python erg moeilijk en had ik moeite met het onthouden van alle functies. Ik ben dus heel trots dat het toch is gelukt om een mooi spel neer te zetten. Echter, hadden we wel meer moeten vragen in de lessen en dat ga ik zeker onthouden voor de volgende keer.

<b><u> Reflectie Milan </u></b> <br>
Tijdens het maken van ons spel heb ik veel geleerd. In het begin vond ik programmeren met Python best moeilijk. Ik had moeite met het logische volgordes te doen. Door dit project heb ik geleerd dat je een spel stap voor stap moet opbouwen. Eerst één onderdeel maken dat goed werkt, en daarna pas verder gaan. Dat maakte het overzichtelijker en minder stressvol.

Een techniek die ik goed heb leren gebruiken is het werken met if, else en elif dingen ik snap deze ook super goed. Ik heb zelf een paar minigames gemaakt en daar aparte functies voor geschreven. Daardoor bleef de code duidelijk en kon ik fouten sneller vinden. Ook heb ik beter geleerd hoe je variabelen gebruikt om de levens van de speler en de zombie bij te houden. Zo bleef het spel logisch.

Wat ik lastig vond, was ervoor zorgen dat alles op elkaar aansloot. dus dat als de zombie geen levens meer had bijvoorbeeld dat het hele spel moest stoppen. Ook het samenvoegen van alle minigames vond ik moeilijk, maar door goed te testen is het gelukt.

De samenwerking met Mayla ging goed. We hebben de taken eerlijk verdeeld en ieder eigen minigames gemaakt. We hielpen elkaar als iets niet lukte. Wat beter had gekund, is dat we meer vragen aan de docent hadden gesteld.

We kozen voor een zombie-thema omdat dat spannend is. Een belangrijke keuze was dat beide vier levens hebben, zodat het spel eerlijk blijft. Ik ben trots dat het ons is gelukt om een werkend spel te maken. De volgende keer zou ik eerder om hulp vragen.

<b><u> bronnen</u></b> <br>
1. W3Schools – Python Functions

W3Schools. (z.d.). Python Functions. Geraadpleegd op 20 februari 2026, van
https://www.w3schools.com/python/python_functions.asp

Gebruikt voor uitleg over def, functies aanroepen en de opbouw van het spel.

2. W3Schools – Python Random Module

W3Schools. (z.d.). Python Random Module. Geraadpleegd op 20 februari 2026, van
https://www.w3schools.com/python/module_random.asp

Gebruikt voor random.choice() en random.sample() in de mini-games.

3. W3Schools – Python While Loops

W3Schools. (z.d.). Python While Loops. Geraadpleegd op 20 februari 2026, van
https://www.w3schools.com/python/python_while_loops.asp

Gebruikt voor herhalingen in mini-games zoals dobbelgevecht, woord raden en code kraken.

4. W3Schools – Python Strings

W3Schools. (z.d.). Python Strings. Geraadpleegd op 20 februari 2026, van
https://www.w3schools.com/python/python_strings.asp

Gebruikt bij het woordspel en het controleren van ingevoerde codes.

5. Informatica Baas – Python Basis

Informatica Baas. (z.d.). Python uitleg en programmeerbasis.

Gebruikt voor algemene uitleg over variabelen, condities en programmastructuur.

6. ChatGPT – Uitleg over sys.exit()

OpenAI. (2026). Uitleg over het gebruik van sys.exit() in Python. Verkregen via ChatGPT.

Gebruikte prompt:

“Hoe kan ik mijn Python-spel direct laten stoppen wanneer de speler of de zombie geen levens meer heeft?  En: Kun je uitleggen hoe sys.exit() werkt en hoe ik dat moet gebruiken in mijn code?”

Gebruikt om te begrijpen hoe import sys en sys.exit() het spel beëindigen bij game over.
