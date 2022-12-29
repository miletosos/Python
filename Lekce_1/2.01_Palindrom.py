# Vstup uzivatele
slovo = input("Zadejte slovo o kterém chcete zjistit zda je palindrom: ")

# Zkontroluj a odpovez, zda se jedna o palindrom.

prvni = slovo[0]
druhe = slovo[1]
posledni = slovo[len(slovo) - 1]
predposledni = slovo[len(slovo) - 2]

#print(prvni)
#print(posledni)
#print(druhe)
#print(predposledni)

if prvni == posledni and druhe == predposledni:
    print("Je to palindrom.")
else:
    print("Není to palindrom.")

#### Bere jen 4 písmena.. chybí mi cyklus???

    ###################################################################
#Řešení z engeto

# Vstup uzivatele

slovo = input("Zadej slovo:")

# Zkontroluj a odpověz, zda se jedná o palindrom.

### Neporovnává to jednotlivá písmena ale celý string.. [::-1] totiž otočí celý string
if slovo == slovo[::-1]:

    print("Slovo '" + slovo + "' je palindrom!.")

else:

    print("Slovo '" + slovo + "' není palindrom.")
