def startscherm():
    print("=== EPIC ZOMBIE BATTLE ===")
    print("1. Uitleg")
    print("2. start")
    print("-----------------------------")

    kies = input("Kies 1 of 2: ")

    if kies == "2":
        print("--------------------------------")
        print("Het spel begint!")
        print("Probeer zoveel mogelijk te winnen!")
    
    else:
        print("--------------------------------")
        print("Er is een zombie-apocalyps uitgebroken.")
        print("De wereld zoals je die kende bestaat niet meer.")
        print("Jij staat oog in oog met een zombie.")

        print("Jij hebt vier levens en de zombie ook.")
        print("Verliezen kost je levens, maar winnen kost die van de zombie.")
        print("Als de levens van jou of de zombie op zijn, is het spel voorbij.")
        print("Zijn de levens van de zombie eerder op dan heb je gewonnen.")
        print("--------------------------------")
        input("Druk op Enter om terug te gaan...")
        startscherm()
    
startscherm()

import random
import time 
def raad_het_getal():
    print("------------------------------")
    print("Mini-game: Raad het getal (1 t/m 5)")
    geheim = random.choice([1,2,3,4,5])
    gok = int(input("Jouw gok: "))

    if gok == geheim:
        print("Goed geraden! Je wint.")
        return True
    else:
        print("Fout, het was", geheim)
        return False

raad_het_getal()

import random

def rekensommen():
    print("-----------------------------------")
    print("Mini-game: Rekensommen")

    a = random.choice([1,2,3,4,5,6,7,8,9,10])
    
    b = random.choice([1,2,3,4,5,6,7,8,9,10])

    print(a, "+", b)
    antwoord = int(input("Antwoord: "))

    if antwoord != a + b:
        print("Fout, het was", a + b)
        return False
    c = random.choice([1,2,3,4,5,6,7,8,9,10])
    d = random.choice([1,2,3,4,5,6,7,8,9,10])

    print(c, "*", d)
    antwoord = int(input("Antwoord: "))

    if antwoord != c * d:
        print("Fout, het was", c * d)
        return False
    
    e = random.choice([1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15])
    f = random.choice([1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15])

    print(e, "*", f)
    antwoord = int(input("Antwoord: "))

    if antwoord != e * f:
        print("Fout, het was", e * f)
        return True
    else:
        print("Goed gedaan!")
    
rekensommen()

import random

def dobbelgevecht():
    
    while True:
        print("-----------------------------------")
        print("Mini-game: Dobbelgevecht!")
        input("Druk op Enter om te dobbelen...")

        speler = random.choice([1,2,3,4,5,6])
        zombie = random.choice([1,2,3,4,5,6])

        print(f"Jij gooit: {speler}")
        print(f"Zombie gooit: {zombie}")

        if speler > zombie:
            print("Je wint!")
            print("-----------------------")
            break
        elif speler < zombie:
            print("Je verliest!")
            print("-----------------------")
            break
        else:
            print("Gelijkspel! Speel opnieuw")
            print("-----------------------")
dobbelgevecht()

def steenpapierschaar():
    
    while True:
        print("MIni-Game: STEEN, PAPIER, SCHAAR")
        print("kies:")
        print("1. steen")
        print("2. papier")
        print("3. schaar")
        
        kies2_speler = input("kies 1, 2 of 3: ")
        kies2_computer = random.choice(["1", "2", "3"])
        
        print("zombie koos:", kies2_computer)
        
        if kies2_speler == kies2_computer:
            print("Gelijkspel!")
            print("-----------------------")
        elif (kies2_speler == "1" and kies2_computer == "3") or \
             (kies2_speler == "2" and kies2_computer == "1") or \
             (kies2_speler == "3" and kies2_computer == "2"):
            print("Je wint!")
            print("------------------------")
            break
        else:
            print("Je verliest!")
            print("------------------------")
            break
    
steenpapierschaar()

import random

def raadhetwoord():

    woorden = ["zombie","virus","beest","bloed","angst","chaos","vlucht",
               "schuil","kelder","bunker","radio","leger","mesje","bijl",
               "hamer","kogel","schot","alarm","gifgas","brand","motor",
               "truck","muur","poort","hek","water","eten","steek","grijp","dood","graf","nacht","donker",
               "rook","gevaar","redden"]

    woord = random.choice(woorden)
    
    geraden = ""
    pogingen = 8

    print("MiniRaad het woord!")

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
            print("gewonnen!")
            return

        gok = input("Mini-Game: Raad een letter (kies 1 letter per keer): ")

        if gok in woord:
            print("Goed!")
        else:
            print("Fout!")
            pogingen = pogingen - 1
            print("Nog", pogingen, "pogingen over")

        geraden = geraden + gok

    print("game over. Het woord was:", woord)
    
raadhetwoord()

def algemene_quiz():
    
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
        },
        {
            "vraag": "In welk land ligt de Eiffeltoren?",
            "opties": ["1. Italië", "2. Spanje", "3. Frankrijk"],
            "antwoord": "3"
        },
        {
            "vraag": "Hoeveel minuten zitten er in een uur?",
            "opties": ["1. 50", "2. 60", "3. 70"],
            "antwoord": "2"
        },
        {
            "vraag": "Welke kleur krijg je als je blauw en geel mengt?",
            "opties": ["1. Groen", "2. Paars", "3. Oranje"],
            "antwoord": "1"
        },
        {
            "vraag": "Wat is het snelste landdier?",
            "opties": ["1. Leeuw", "2. Jachtluipaard", "3. Paard"],
            "antwoord": "2"
        },
        {
            "vraag": "Hoeveel zijden heeft een driehoek?",
            "opties": ["1. 3", "2. 4", "3. 5"],
            "antwoord": "1"
        },
        {
            "vraag": "Wat is de uitkomst van 9 x 8?",
            "opties": ["1. 72", "2. 81", "3. 64"],
            "antwoord": "1"
        },
        {
            "vraag": "Welke oceaan ligt tussen Europa en Amerika?",
            "opties": ["1. Indische Oceaan", "2. Atlantische Oceaan", "3. Stille Oceaan"],
            "antwoord": "2"
        }

    ]
    
    score = 0
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
    
    print(f"Je hebt {score} van de 5 vragen goed!")
    
    if score >= 3:
        print("Je wint deze minigame!")
        return True
    else:
        print("Je verliest deze minigame!")
        return False
    
algemene_quiz()

import random

def coderaden():

    print("-----------------------")
    print("Mini-game: Raad De Code!")
    print("voer een nummer-code in en raad in 10 beurten wat de code is")
    print("kies uit de nummers 1, 2, 3, 4 en 5")
    print("de code bestaat uit 4 cijfers")
    
    code = ""
    for i in range(4):
        code += str(random.choice(["1","2","3","4","5"]))


    beurten = 10

    while beurten > 0:
        gok = input("code (4 cijfers): ")

        if len(gok) != 4:
            print("vul 4 cijfers in.")
            continue

        if gok == code:
            print("Goed gedaan!")
            return

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
        print("nog", beurten, "beurten over")
        print("-----------------------")

    print("Helaas! De code was:", code)
    
coderaden()
