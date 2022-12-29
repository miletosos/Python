cisla = []

while True:
    cislo = input("Prosím zadejte číslo: ")
    if cislo == "break":
        break
    cisla.append(cislo)

print(cisla)

min_prvek = cisla[0]
for prvek in cisla[1:]:
    if min_prvek > prvek:
        min_prvek = prvek

print("Nejmenší  číslo je: ", min_prvek)

