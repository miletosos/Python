# Nas slovnik
data = {
    "uzivatel1": "heslo",
    "Marek": "1234",
    "Danko": "qwert",
            }
# Zeptej se na uzivatelske jmeno a heslo.
jmeno = input("Prosím zadejte Vaše uživatelské jméno: ")
heslo = input("Prosím zadejte Vaše heslo: ")
print(jmeno)
print(heslo)

# Podminkovy vyraz
if jmeno in data.keys() and heslo in data.values():
    ##    if data.get(username) == password:   Takhle to řešili oni
    ## Přidal jsem tam keys and values.. pokud zadám jen data tak bere jen klíče ne hodnoty
    ## stačilo by tedy jen values ale pro lepší ukázku..
    print("Vítejte.")
else:
    print("Uživatelské jméno nebo heslo nebylo zadáno správně.")