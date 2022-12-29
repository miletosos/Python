    # Vytvoreni kandidatu
    kandidati = []

    # Tisk kandidatu na zacatku
    print("Kandidáti na začátku:", kandidati)

    # Vytvoreni zamestnancu
    zamestnanci = ["František", "Anna", "Jakub", "Klára"]

    # Tisk zamestnancu na zacatku
    print("Zaměstnanci na začátku", zamestnanci)

    # Pridani novych kandidatu
    kandidati.append("Bruno")
    kandidati.append("Anežka")

    # Tisk novych kandidatu
    print("Nová jména přidána do kandidáti:", kandidati)
    # Vypsání bez hranatých závorek, nemusí být záporné indexy můžeme jít i od 0
    print("Nová jména přidána do kandidati: " + kandidati[-2] + ", " + kandidati[-1])

    # Vlozeni jmena
    zamestnanci.insert(1, "Bruno")

    # Tisk listu zamestnanci po vlozeni noveho jmena
    print("Nová jména vložena do zaměstnanci:", zamestnanci)


    ##################################################################################
    # Výsledky z minulé úlohy
    #kandidati = ['Bruno', 'Anežka']
    #zamestnanci = ['František', 'Bruno', 'Anna', 'Jakub', 'Klára']


    # Odstraneni jmena z kandidati
    kandidati.remove("Bruno")

    # Tisk zbylych kandidatu
    print("Bruno odstraněn z kandidati:" + str(kandidati))

    # Opakovani prvku
    kandidati = kandidati * 3

    # Tisk opakovani prvku v listu kandidati
    print("Opakování prvku v listu kandidáti:" + str(kandidati))

    # Spojeni listu
    zamestnanci = zamestnanci + kandidati

    # Tisk spojenych listu
    print("Spojení zaměstnanci a kandidáti:" + str(zamestnanci))

    # Index 2
    print("Na pozici 2 se nachází:" + str(kandidati[2]))

    # Zjisteni posledniho indexu a prirazeni do promenne
    posledni_index = len(zamestnanci)
    posledni_index = posledni_index - 1
    print("Poslední index je: " + str(posledni_index))
    # Posledni index
    print("Na pozici " + str(posledni_index) + " se nachází: " + str(zamestnanci[posledni_index]))

    # Interval 2-5
    print("Na intervalu 2-5 se nachází: " + str(zamestnanci[2:6]))

    # Kazdy treti
    print("Každý třetí: " + str(zamestnanci[::3]))

    # Ulozeni indexu
    jakub_index = zamestnanci.index("Jakub")
    # Jakub index
    print("Jakub je na indexu: " + str(jakub_index))

    # Anezka pocet
    anezka_pocet = zamestnanci.count("Anežka")
    print("Anezka je tam: " + str(anezka_pocet))