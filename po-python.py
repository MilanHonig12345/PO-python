def startscherm():
    print("=== BUNKER SURVIVAL ===")
    print("1. Uitleg")
    print("2. start")
    print("-----------------------------")

    kies = input("Kies 1 of 2: ")

    if kies == "2":
        print("Het spel begint")
    else:
        print("--------------------------------")
        print("Er is een zombie-apocalyps uitgebroken.")
        print("De wereld zoals je die kende bestaat niet meer.")
        print("Jij hebt een bunker gevonden, maar veilig ben je nog niet.")

        print("In dit spel moet je de juiste keuzes maken om te overleven.")
        print("Verkeerde keuzes kosten levens.")
        print("Als je levens op zijn, is het spel voorbij.")
        print("Je kunt naar buiten voor spullen, maar daar zijn zombies.")
        print("--------------------------------")
        input("Druk op Enter om terug te gaan...")
        startscherm()
    
startscherm()