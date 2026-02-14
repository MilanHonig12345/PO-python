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
    geheim = random.randint(1, 5)
    gok = int(input("Jouw gok: "))

    if gok == geheim:
        print("Goed geraden! Je wint.")
        return True
    else:
        print("Fout, het was", geheim)
        return False

raad_het_getal()
def rekensommen():
    print("-----------------------------------")
    print("Mini-game: Rekensommen")
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    antwoord = int(input(f" {a} + {b} = "))
    if antwoord !=  a + b:
        print("Fout, het was", a + b)
        return False
    
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    antwoord2 = int(input(f"{c} * {d} = "))
    if antwoord2 == c * d:
        print("Goed gedaan! Je wint!")
        return True
    else:
        print ("Fout, het was", c * d)
rekensommen()

def dobbelgevecht():
    
    while True:
        print("-----------------------------------")
        print("Mini-game: Dobbelgevecht!")
        input("Druk op Enter om te dobbelen...")

        speler = random.randint(1, 6)
        zombie = random.randint(1, 6)

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
        print("STEEN, PAPIER, SCHAAR")
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

    
    


    

