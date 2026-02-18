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

        print("Jij hebt vijf levens en de zombie ook.")
        print("Verliezen kost je levens, maar winnen kost die van de zombie.")
        print("Als de levens van jou of de zombie op zijn, is het spel voorbij.")
        print("Zijn de levens van de zombie eerder op dan heb je gewonnen.")
        print("--------------------------------")
        input("Druk op Enter om terug te gaan...")
        startscherm()
    
startscherm()

import random 
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
<<<<<<< HEAD
    




    

=======
>>>>>>> a77b01a921eb154e59381b997c199327524f8b32

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