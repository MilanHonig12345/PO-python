def startscherm(): # hier geven we een stukje code een naam die we later aanroepen zodat het uitgevoerd kanworden
    print("=== EPIC ZOMBIE BATTLE ===")
    print("1. Uitleg")
    print("2. start")
    print("-----------------------------")

    kies = input("Kies 1 of 2: ")

    if kies == "2": # als de speeler 2 kiest, print het wat zinnen het gaat het door naar de volgende def
        print("--------------------------------")
        print("Het spel begint!")
        print("Probeer zoveel mogelijk te winnen!")
    
    else: # als het iets anders dan 2 is voert het deze regel uit
        print("--------------------------------")
        print("Er is een zombie-apocalyps uitgebroken.")
        print("De wereld zoals je die kende bestaat niet meer.")
        print("Jij staat oog in oog met een zombie.")

        print("Jij hebt vier levens en de zombie ook.")
        print("Verliezen kost je levens, maar winnen kost die van de zombie.")
        print("Als de levens van jou of de zombie op zijn, is het spel voorbij.")
        print("Zijn de levens van de zombie eerder op dan heb je gewonnen.")
        print("--------------------------------")
        input("Druk op enter om terug te gaan") 
        startscherm() # als je op enter drukt voert het code uit die we eerder hebben geschreven
    
startscherm() #hier wordt dus dat stukje code aangeroepen
speler_levens = 4
zombie_levens = 4
import random #zorgt dat het willekeurige keuzes kan maken in het volgende stukje code wanneer er random.choice wordt gebruikt
def raad_het_getal():
    def check_levens():
        global speler_levens, zombie_levens
        if speler_levens <= 0:
            sys.exit()
        elif zombie_levens <= 0:
            sys.exit()
        check_levens()
    global speler_levens, zombie_levens  # <-- hier vertel ik dat we de globale variabelen gebruiken
    print("------------------------------")
    print("Mini-game: Raad het getal (1 t/m 5)")
    geheim = random.choice([1,2,3,4,5])
    gok = int(input("Jouw gok: "))
    if gok == geheim:
        print("Goed geraden! Je wint.")
        zombie_levens -= 1
        
    else:
        print("Fout, het was", geheim)
        speler_levens -= 1
       
    
    print("Levens: Speler =", speler_levens, ", Zombie =", zombie_levens)
    if speler_levens <= 0:
         print("Game over! De zombie wint.")
    elif zombie_levens <= 0:
         print("Gefeliciteerd! Jij wint!")
    
    
raad_het_getal()
    

import random

def rekensommen():
    def check_levens():
        global speler_levens, zombie_levens
        if speler_levens <= 0:
           sys.exit()
        elif zombie_levens <= 0:
           sys.exit()
    check_levens()
    global speler_levens, zombie_levens
    print("-----------------------------------")
    print("Mini-game: Rekensommen")

    # SOM 1
    a = random.choice([1,2,3,4,5,6,7,8,9,10])
    b = random.choice([1,2,3,4,5,6,7,8,9,10])

    print(a, "+", b)
    antwoord = int(input("Antwoord: "))

    if antwoord != a + b:
        print("Fout, het was", a + b)
        speler_levens -= 1
        print("Levens: Speler =", speler_levens, ", Zombie =", zombie_levens)
        return False  # ← STOP meteen

    # SOM 2
    c = random.choice([1,2,3,4,5,6,7,8,9,10])
    d = random.choice([1,2,3,4,5,6,7,8,9,10])

    print(c, "*", d)
    antwoord = int(input("Antwoord: "))

    if antwoord != c * d:
        print("Fout, het was", c * d)
        speler_levens -= 1
        print("Levens: Speler =", speler_levens, ", Zombie =", zombie_levens)
        return False

    # SOM 3
    e = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    f = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

    print(e, "*", f)
    antwoord = int(input("Antwoord: "))

    if antwoord != e * f:
        print("Fout, het was", e * f)
        speler_levens -= 1
        print("Levens: Speler =", speler_levens, ", Zombie =", zombie_levens)
        return False

    print("Goed gedaan!")
    zombie_levens -= 1
    print("Levens: Speler =", speler_levens, ", Zombie =", zombie_levens)
    return True
rekensommen()

import random

def dobbelgevecht():
    def check_levens():
       global speler_levens, zombie_levens
       if speler_levens <= 0:
          sys.exit()
       elif zombie_levens <= 0:
          sys.exit()
    check_levens()
    global speler_levens, zombie_levens
    
    while True:
        print("-----------------------------------")
        print("Mini-game: Dobbelgevecht!")
        input("Druk op enter om te dobbelen:")

        speler = random.choice([1,2,3,4,5,6])
        zombie = random.choice([1,2,3,4,5,6])

        print(f"Jij gooit: {speler}")
        print(f"Zombie gooit: {zombie}")

        if speler > zombie:
            print("Je wint!")
            print("-----------------------")
            zombie_levens -= 1
            
        elif speler < zombie:
            print("Je verliest!")
            print("-----------------------")
            speler_levens -= 1
            
        else:
            print("Gelijkspel! Speel opnieuw")
            print("-----------------------")
            
        print("Levens: Speler =", speler_levens, ", Zombie =", zombie_levens)
        print("-----------------------------")
         
        if speler_levens <= 0:
            print("Game over! De zombie wint.")
            return True
        elif zombie_levens <= 0:
            print("Gefeliciteerd! Jij wint!")
            return True 
        else:
            return False 
    
dobbelgevecht()

def steenpapierschaar():
    def check_levens():
       global speler_levens, zombie_levens
       if speler_levens <= 0:
          sys.exit()
       elif zombie_levens <= 0:
          sys.exit()
    check_levens()
    while True:
        print("Mini-Game: STEEN, PAPIER, SCHAAR")
        print("kies:")
        print("1. steen")
        print("2. papier")
        print("3. schaar")
        
        kies2_speler = input("kies 1, 2 of 3: ")
        kies2_computer = random.choice(["1", "2", "3"])
        global speler_levens, zombie_levens
        
        print("zombie koos:", kies2_computer)
        
        if kies2_speler == kies2_computer:
            print("Gelijkspel!")
            print("-----------------------")
        elif (kies2_speler == "1" and kies2_computer == "3") or \
             (kies2_speler == "2" and kies2_computer == "1") or \
             (kies2_speler == "3" and kies2_computer == "2"):
            print("Je wint!")
            print("------------------------")
            zombie_levens -= 1
            
        else:
            print("Je verliest!")
            print("------------------------")

            speler_levens -= 1
        # Check opnieuw of het spel moet stoppen
        print("Levens: Speler =", speler_levens, ", Zombie =", zombie_levens)
        print("-----------------------------")

         
        if speler_levens <= 0:
            print("Game over! De zombie wint.")
            return True  # teruggeven dat het spel moet stoppen
        elif zombie_levens <= 0:
            print("Gefeliciteerd! Jij wint!")
            return True  # teruggeven dat het spel moet stoppen
        else:
            return False  # spel gaat door
            
    
steenpapierschaar()

import random

def raadhetwoord():
    def check_levens():
       global speler_levens, zombie_levens
       if speler_levens <= 0:
          sys.exit()
       elif zombie_levens <= 0:
          sys.exit()
    check_levens()
    global speler_levens, zombie_levens

    woorden = ["zombie","virus","beest","bloed","angst","chaos","vlucht",
               "schuil","kelder","bunker","radio","leger","mesje","bijl",
               "hamer","kogel","schot","alarm","gifgas","brand","motor",
               "truck","muur","poort","hek","water","eten","steek","grijp",
               "dood","graf","nacht","donker","rook","gevaar","redden"]

    woord = random.choice(woorden)
    geraden = ""
    pogingen = 8

    print("Mini-game: Raad het woord!")

    while pogingen > 0:
        goed = True
        print("Woord: ", end="")

        for letter in woord:
            if letter in geraden:
                print(letter, end=" ")
            else:
                print("_", end=" ")
                goed = False
        print()

        if goed:
            print(" Gewonnen! De zombie verliest een leven.")
            zombie_levens -= 1
            break

        gok = input("Raad een letter (1 letter per keer): ").lower()

        
        if len(gok) != 1:
            print("Voer **exact één letter** in!") # zo kan je niet meerdere letter in een keer gokken.
            continue  # gaat terug naar start van while
        elif gok in geraden:
            print("Je hebt deze letter al geprobeerd.")
            continue  

        # Voeg de letter toe aan geraden
        geraden += gok

        if gok in woord:
            print("Goed geraden!")
        else:
            print("Fout!")
            pogingen -= 1
            print("Nog", pogingen, "pogingen over")
            if pogingen == 0:
                speler_levens -= 1
                print("Game over! Het woord was:", woord)
                break

    # Toon levens na minigame
    print("Levens: Speler =", speler_levens, ", Zombie =", zombie_levens)

    # Check of spel stopt
    if speler_levens <= 0:
        print("Game over, je hebt verloren.")
        return True
    elif zombie_levens <= 0:
        print("Gefeliciteerd! Je hebt gewonnen.")
        return True
    else:
        return False
raadhetwoord()

def algemene_quiz():
    def check_levens():
       global speler_levens, zombie_levens
       if speler_levens <= 0:
          sys.exit()
       elif zombie_levens <= 0:
          sys.exit()
    check_levens()
    global speler_levens, zombie_levens
    
    print("-----------------------")
    print("Mini-game: Quizen!")
    
    vragen = [
        {
            "vraag": "Wat is de hoofdstad van Frankrijk?",
            "opties": ["1. Parijs", "2. Londen", "3. Berlijn"],
            "antwoord": "1"
        },
        {
            "vraag": "Hoeveel dagen heeft een schrikkeljaar?",
            "opties": ["1. 365", "2. 366", "3. 364"],
            "antwoord": "2"
        },
        {
            "vraag": "Wie schilderde de Mona Lisa?",
            "opties": ["1. Michelangelo", "2. Leonardo da Vinci", "3. Picasso"],
            "antwoord": "2"
        },
        {
            "vraag": "Wat is H2O?",
            "opties": ["1. Zuurstof", "2. Water", "3. Helium"],
            "antwoord": "2"
        },
        {
            "vraag": "Hoeveel continenten zijn er op aarde?",
            "opties": ["1. 5", "2. 6", "3. 7"],
            "antwoord": "3"
        },
        {
            "vraag": "Wie schreef 'Romeo en Julia'?",
            "opties": ["1. William Shakespeare", "2. J.K. Rowling", "3. Charles Dickens"],
            "antwoord": "1"
        },
        {
            "vraag": "Wat krijg je als je rood en geel mengt?",
            "opties": ["1. Paars", "2. Oranje", "3. Groen"],
            "antwoord": "2"
        },
        {
            "vraag": "Welke van deze dieren is een zoogdier?",
            "opties": ["1. Krokodil", "2. Walvis", "3. Haai"],
            "antwoord": "2"
        },
        {
            "vraag": "Wat is 12 x 12?",
            "opties": ["1. 144", "2. 124", "3. 154"],
            "antwoord": "1"
        },
        {
            "vraag": "Wat is de grootste planeet in ons zonnestelsel?",
            "opties": ["1. Aarde", "2. Jupiter", "3. Mars"],
            "antwoord": "2"
        }
    ]
    
    score = 0
    
    # Kies 5 random vragen
    gekozen_vragen = random.sample(vragen, 5)
    
    for q in gekozen_vragen:
        print(" " + q["vraag"])
        for optie in q["opties"]:
            print(optie)
        
        gok = input("Kies 1, 2 of 3: ")
        
        if gok == q["antwoord"]:
            print("Goed!")
            score += 1
        else:
            print("Fout!")
        print("-----------------------")
    
    # Minigame resultaat
    if score >= 3:
        print(f"Je hebt {score} van de 5 vragen goed! Je wint deze minigame!")
        zombie_levens -= 1
    else:
        print(f"Je hebt {score} van de 5 vragen goed. Je verliest deze minigame!")
        speler_levens -= 1
    
    # Levens tonen na minigame
    print("Levens: Speler =", speler_levens, ", Zombie =", zombie_levens)
    print("-----------------------------")
    
    # Check of het spel stopt
    if speler_levens <= 0:
        print("Game over! De zombie wint.")
        return True
    elif zombie_levens <= 0:
        print("Gefeliciteerd! Jij wint!")
        return True
    else:
        return False

# Test aanroepen
algemene_quiz()
import random

def coderaden():
    def check_levens():
       global speler_levens, zombie_levens
       if speler_levens <= 0:
          sys.exit()
       elif zombie_levens <= 0:
          sys.exit()
    check_levens()
    global speler_levens, zombie_levens

    print("-----------------------")
    print("Mini-game: Raad De Code!")
    print("Voer een nummer-code in en raad in 10 beurten wat de code is")
    print("Kies uit de nummers 1, 2, 3, 4 en 5")
    print("De code bestaat uit 4 cijfers")
    
    # Genereer willekeurige 4-cijfer code
    code = ""
    for i in range(4):
        code += str(random.choice(["1","2","3","4","5"]))

    beurten = 10
    gewonnen = False

    while beurten > 0:
        gok = input("Code (4 cijfers): ")

        if len(gok) != 4:
            print("Vul precies 4 cijfers in.")
            continue

        if gok == code:
            print("Goed gedaan! Je hebt de code geraden!")
            zombie_levens -= 1
            gewonnen = True
            break  # minigame direct stoppen als correct geraden

        goed = 0
        fout = 0

        for i in range(4):
            if gok[i] == code[i]:
                goed += 1
            elif gok[i] in code:
                fout += 1

        print("Juist cijfer en juiste plek:", goed)
        print("Juist cijfer maar verkeerde plek:", fout)

        beurten -= 1
        print("Nog", beurten, "beurten over")
        print("-----------------------")

    if not gewonnen:
        print("Helaas! De code was:", code)
        speler_levens -= 1  # speler verliest een leven bij verlies
        print("Je verliest 1 leven!")

    # Levens tonen na minigame
    print("Levens: Speler =", speler_levens, ", Zombie =", zombie_levens)
    print("-----------------------------")

    # Check of het spel stopt
    if speler_levens <= 0:
        print("Game over! De zombie wint.")
        return True
    elif zombie_levens <= 0:
        print("Gefeliciteerd! Jij wint!")
        return True
    else:
        return False


coderaden()
import random
def geheugentest():
    def check_levens():
       global speler_levens, zombie_levens
       if speler_levens <= 0:
          sys.exit()
       elif zombie_levens <= 0:
          sys.exit()
    check_levens()
    global speler_levens, zombie_levens
    print("-----------------------")
    print("Mini-game: Geheugen Test")

    rondes = 3
    gehaald = 0

    while rondes > 0:
        print("\nNieuwe ronde!")

        # maak code van 4 cijfers
        code = ""
        for i in range(4):
            code += random.choice(["1", "2", "3", "4", "6"])

        print("Onthoud deze code:")
        print(code)

        time.sleep(2)
        print("\n" * 20)

        gok = input("Wat was de code? (voer 4 cijfers in) ")

        # Controle dat speler echt 4 cijfers invoert
        if len(gok) != 4:
            print("Je moet precies 4 cijfers invoeren!")
            continue

        if gok == code:
            print("Goed!")
            gehaald += 1
        else:
            print("Fout! Het was", code)

        rondes -= 1

    print("\nJe had", gehaald, "van de 3 goed.")

    # Levens aanpassen afhankelijk van resultaat
    if gehaald >= 2:
        print("Je wint de minigame!")
        zombie_levens -= 1  # zombie verliest een leven
    else:
        print("Je verliest de minigame!")
        speler_levens -= 1  # speler verliest een leven

    # Levens tonen
    print("Levens: Speler =", speler_levens, ", Zombie =", zombie_levens)
    print("-----------------------------")

    # Check of het spel stopt
    if speler_levens <= 0:
        print("Game over! De zombie wint.")
        return True
    elif zombie_levens <= 0:
        print("Gefeliciteerd! Jij wint!")
        return True
    else:
        return False


geheugentest()