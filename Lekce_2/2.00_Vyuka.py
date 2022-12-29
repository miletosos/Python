def max(sekvence):
    max_prvek = sekvence[0]

    for prvek in sekvence[1:]:
        if max_prvek < prvek:
            max_prvek = prvek

    return max_prvek

max_cislo = max([32,2,4,1,4,54,23,12])
print(max_cislo)

# Hlavicka funkce
def soucet(prvni, posledni):

    # Pomocna promenna
    vysledek = 0

    # For loop
    for cislo in range(prvni, posledni):
        vysledek += cislo


    # Vraceni vysledku
    return vysledek

vysledek = soucet(1, 9999)
print(vysledek)



# Order  sequence
import random
def order_sequence(my_list):
    for i in range(1,len(my_list)):
        pos = i
        while pos > 0 and my_list[pos-1] > my_list[pos]:
            my_list[pos],my_list[pos-1] =  my_list[pos-1], my_list[pos]
            pos -= 1


def generate_random_list(size):
    lst = []
    for i in range(size):
        lst.append(random.randint(1,100))
    return lst

l = generate_random_list(10)
print('Before sorting:',l)
order_sequence(l)
print('After sorting:', l)