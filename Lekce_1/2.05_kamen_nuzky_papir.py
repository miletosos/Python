# Naimportuj modul random.
import random

# Vytvort list moznosti.
moznosti = ["kámen", "nůžky", "papír"]

# Vytvort promennou hrac.
hrac = input("Prosím zadejte vaši volbu (kámen, nůžky, papír): ")

# Vytvort promennou pocitac.
pocitac = random.choice(moznosti)

# Vytiskni volbu cloveka a pocitace.
print("Počítač:", pocitac)
print("Hráč:", hrac)

# Vytvor podminku, zda hrac zvolil neplatnou volbu.
if hrac != "kámen" and hrac != "nůžky" and hrac != "papír":
    print("Neplatná volba")
# Pokud je volba v poradku, muzeme provest zbytek programu.
else:
    if hrac == "kámen" and pocitac == "nůžky":
        print("Vyhrál jsi!")
    elif hrac == "kámen" and pocitac == "papír":
        print("Prohrál jsi!")
    elif hrac == "kámen" and pocitac == "kámen":
        print("Nerozhodně!")
    elif hrac == "nůžky" and pocitac == "kámen":
        print("Prohrál jsi!")
    elif hrac == "nůžky" and pocitac == "nůžky":
        print("Nerozhodně!")
    elif hrac == "nůžky" and pocitac == "papír":
        print("Vyhrál jsi!")
    elif hrac == "papír" and pocitac ==  "kámen":
        print("Vyhrál jsi!")
    elif hrac == "papír" and pocitac == "nůžky":
        print("Prohrál jsi!")
    elif hrac == "papír" and pocitac == "papír":
        print("Nerozhodně!")