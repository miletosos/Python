def my_min(sekvence):
    min_prvek = sekvence[0]

    for prvek in sekvence[1:]:
        if min_prvek > prvek:
            min_prvek = prvek

    return (min_prvek)

def my_max(sekvence):
    max_prvek = sekvence[0]

    for prvek in sekvence[1:]:
        if max_prvek < prvek:
            max_prvek = prvek

    return(max_prvek)



sekvence = [1, 12, 55, 67, 44, 11, 99, 6]

min = my_min(sekvence)
print("Nejmenší prvek: ", min)

max = my_max(sekvence)
print("Největší prvek: ", max)
