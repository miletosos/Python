# Funkce my_all(), která imituje built-in funkci all().
# Funkce bude brát sekvenci a vrátí True,
# pokud mají všechny prvky v sekvenci boolean hodnotu True
# nebo pokud je sekvence prázdná. Jinak fuknce vrací False.

def my_all(sekvence):
    for prvek in sekvence:
        if not prvek:
            return False
    return True

# Funkce my_any(), která imituje built-in funkci any().
# Funkce bude brát sekvenci a vrátí True,
# pokud má aspoň jeden prvek v sekvenci boolean hodnotu True.
# V opačném případě a také pokud je sekvence prázdná vrací fuknce False.

def my_any(sekvence):
    for prvek in sekvence:
        if prvek:
            return True
    return False


lst = [0]

all = my_all(lst)
print("my all: ", all)

any = my_any(lst)
print("my any: ", any)