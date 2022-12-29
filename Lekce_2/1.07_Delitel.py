start = input("Prosím zadjete úvodní číslo: ")
stop = input("Prosím zadejte koncové číslo: ")
delitel = input("Prosím zadejte dělitele: ")

start = int(start)
stop = int(stop) + 1
delitel = int(delitel)
list = []

if delitel == 0:
    print("Nulou nelze dělit")
else:
    for i in range(start, stop):
        if i % delitel == 0:
            list.append(i)
            print(i)

print(list)