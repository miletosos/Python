def my_find(sekvence, prvek):
    for i, obj in enumerate(sekvence):
        if obj == prvek:
            return i
    return -1

### ŘEŠENÍ ENGETO !!!!!! ####
def my_find_1(seq, item):
	for i, obj in enumerate(seq):
		if obj == item:
			return i
	return -1



lst = ["a", "b", "c"]

nalez = my_find(lst, "b")
print("moje řešení: ", nalez)

nalez1 = my_find_1(lst, "b")
print(nalez1)
