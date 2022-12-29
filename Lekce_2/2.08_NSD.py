def nsd(prvni, druhe):
    while True:
        vysledek = prvni % druhe
        print("mezisoučet:", vysledek)
        if vysledek != 0:
            prvni = druhe
            druhe = vysledek
        else:
            break
    return druhe

cislo1 = int(98545698)
cislo2 = int(9855)

priklad = nsd(cislo1, cislo2)
print(priklad)

## ENGETO ŘEŠENÍ

def my_gcd(a,b):
	while b > 1:
		remainder = a % b
		if not remainder:
			break
		a,b = b,remainder
	return b