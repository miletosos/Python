# Zadani slova
slovo = input("Prosím zadejte vaše slovo: ")

# Zjisteni delky
znaky = len(slovo)

# Podminka a tisk delky slova
if znaky > 4:
    print(slovo, "obsahuje", znaky, "znaků.")
else:
    print(slovo, "obsahuje", znaky, "znaky")