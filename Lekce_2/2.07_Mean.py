# Definice funkce mean
def my_mean(vstup):
    vysledek = 0
    for cislo in vstup:
        vysledek += cislo
    vysledek = vysledek / len(vstup)
    return vysledek


# Nase data
data = [35, 14, 26, 48, 49, 26, 18, 25, 16, 16, 39, 17, 10, 29, 30]

# Pouziti a funkce mean a tisk vysledku

priklad = my_mean(data)
print(priklad

      ## ENGETO ŘEŠENÍ :)

def mean(values):
    return sum(values)/len(values)