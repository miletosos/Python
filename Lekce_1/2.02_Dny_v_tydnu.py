# Vytvor list 'tyden' a uloz dny v tydnu v podobe stringu (vse malymi pismeny!).
tyden = ["pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota", "neděle"]

# Ziskej tip uzivatele.
tip_uzivatele = input("Jakým písmenem začíná jméno pátého dne v týdnu: ")

# Ziskej prvni pismeno z 'pátek'.
patek_pismeno = str(tyden[4])
patek_pismeno = str(patek_pismeno[0])
#print(patek_pismeno)

# Vysledek porovnani uloz do promenne 'vysledek'.
if patek_pismeno == tip_uzivatele:
    vysledek = True
else:
    vysledek = False

# Vytiskni vysledek porovnani promennych.
print(vysledek)