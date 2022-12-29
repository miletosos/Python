#vstup od uživatele
karta = input("Prosím vložte číslo Vaší karty: ")

print(karta)

#obrácení pořadí čísel
obracene = []
for n in karta[:: -1]:
    obracene.append(n)

print(obracene)


# Definice fce
def luhn(num):
    suda = []
    licha = []

    #rozdělení na sudá a lichá
    for i, n in enumerate(num):
        i += 1
        if i % 2 == 0:
            suda.append(n)
        else:
            licha.append(n)
    print("suda", suda)
    print("licha", licha)

    s1 = 0
    s2 =0
    suda2= []

    #součet lichých
    for n in licha:
        n = int(n)
        s1 = n + s1
    print("suma licha", s1)

    #vynásobení suchých
    for n in suda:
        n = int(n)
        n = n * 2
        suda2.append(n)
    print("suda2", suda2)

    #součet sudých
    for n in suda2:
        if n <= 9:
            s2 = s2 + n
        else:
            n = n - 9
            s2 = s2 + n
    print("suma suda:", s2)

    s= 0
    s = s1 + s2

    if s % 10 == 0:
        print("Vaše karta je platná.")
    else:
        print("Neplatná karta!")

print(luhn(obracene))

