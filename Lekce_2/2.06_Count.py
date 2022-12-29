# Definice funkce count
def my_count(vstup, seznam):
    i = 0
    for slovo in seznam:
        if vstup == slovo:
            i = i +1
    return i


# Nase data
names = ['Rob', 'Jim', 'Mark', 'Mark', 'Mark', 'Bob', 'Mark', 'Bob', 'Bob', 'Rob', 'Jim',
'Mark', 'Mark', 'Bob', 'Mark']

# Pouziti funkce count a tisk vysledku
prilkad = my_count("Bob", names)
print(prilkad)