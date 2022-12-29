# Vstupni hodnoty
jmeno = input("Zadejte prosím vaše jméno: ")
vyska = input("Zadejte prosím vaši výšku v cm!: ")
vaha = input("Zadejte prosím vaši váhu: ")
# Vypocet
bmi = int(vaha) / (int(vyska) ** 2 * 0.0001)
#print(bmi)

# Vytvor promennou kategorie a prirad ji pomoci podminek.
kategorie = ""
if bmi <= 18.5:
    kategorie = "Podvýživa"
elif bmi > 18.5 and bmi <= 25:
    kategorie = "Zdravá váha"
elif bmi > 25 and bmi<= 30:
    kategorie = "Mírná nadváha"
elif bmi > 30 and bmi<= 40:
    kategorie = "Obezita"
elif bmi > 40:
    kategorie = "Těžká obezita"

# Vytiskni odpoved s vysledkem.

print("Tvé BMI je:",int(bmi) , "což spadá do kategorie", kategorie)