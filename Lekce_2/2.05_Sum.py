# Definice funkce sum
def my_sum(vstup):
    vysledek = 0
    for cislo in vstup:
        vysledek = vysledek + cislo
    return vysledek




# Data k secteni
data = [32,43,54,54,76,21,62,83,52,58]

# Pouziti a funkce sum na data a tisk vysledku
priklad = my_sum(data)
print(priklad)