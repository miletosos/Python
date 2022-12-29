veta = "|{0:3}|{0:4}|".format(45)
print(veta)


 # vyplněno znakem $ a zarovnáno doprava
veta1 = "|{0:$>3}|{0:$>4}|".format(45)
print(veta1)

 # Uloha přesnost
print("|{0:.3}|{0:.4}|{0:.5}|".format(123.4567))
print("|{0:$<6.4}|".format(1.234))
print("|{0:.4}|".format("Hello"))
print("|{0:*>19,.14}|".format(123456789.123456))
print("|{0:*<6s}|".format("Hello"))

 # Konverze z desítkové na dvojkovou(b), osmičkové (o) a hexadecimální (x)
print("|{0:*<6b}|".format(280256650))
print("|{0:*<6o}|".format(28025652))
print("|{0:*<6x}|".format(2801261235165))

 #Další metody formátování
print("4".ljust(5,"x"))
print("2".rjust(5,"x"))
print("3".center(5,"x"))
print("5".zfill(5))