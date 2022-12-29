# Ziskani nahodneho slova z listu 'ovoce'
import random
ovoce = ['Jablko', 'Banán', 'Hruška']
slovo = random.choice(ovoce)

# Pocet pokusu na uhodnuti
pocet_pokusu = 2

# Nastaveni pocitadla
i = 2

# While smycka s podminkou - napis podminku za while a před dvoujtecku.
while i:
    # Zadani tipu
    print("Oponent: ", slovo)
    tip = input('Vlož svůj tip: ')

    # Kontrola spravnosti slova - nastav podminku za if.
    if  tip == slovo:
        break


    # Zvetseni pocitadla
    i = i - 1
    print("Počet zbývajících pokusů", i)
# Podminka pro vyhru
if  i <= 0:
    print("Prohrál jsi")
else:
    print('Správně! Počet pokusů:', 3 - i )