# Prevodni pomery
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

# Pocet jednotek, ktery ma byt preveden.
kg_pocet = 80
km_pocet = 54
l_pocet = 5

# Vypocty pro prevod.
kg_vysledek = kg_pocet * kg_lb
km_vysledek = km_mile * km_pocet
l_vysledek = l_gal * l_pocet

# Vysledne odpovedi.
print("80 kg je:", kg_vysledek, "liber.")
print("54 km je:", km_vysledek, "mílí.")
print("5 litrů je:", l_vysledek, "galonů.")