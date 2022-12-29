seq = [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]
slovnik = {}

for i in seq:
    slovnik[str(i)] = slovnik.setdefault(str(i),0) + 1

print(slovnik)
