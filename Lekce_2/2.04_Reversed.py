def my_reversed(vstup):
    lst = list(vstup[::-1])
    return lst

def my_reversed1(vstup):
    lst = []
    for i in vstup:
        lst.insert(0, i)
    return lst



# musí být tuple, když dám hranaté závorky tak to funguje ale ne se stringem
x = "Petr"

priklad = my_reversed(x)
print(priklad)

priklad1 = my_reversed1(x)
print("druha varianta: ", priklad1)