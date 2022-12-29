def prestupny(datum):
    if int(datum) % 400 == 0 or (int(datum) % 4 == 0 and int(datum) % 100 != 0):
        return True
    else:
        return False


print(prestupny(2020))


### ŘEŠENÍ ENGETO ##


#možnost bez if else
# Definice fce
def is_leap(y):
    # Vrati True nebo False v zavislosti na tom, jestli je prestupny
    return ((y % 400 == 0) or (y % 4 == 0 and y % 100 != 0))