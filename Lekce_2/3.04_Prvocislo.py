
#generuje seznam prvočísel v námi požadovaném rozsahu
def list_primes():
    seznam = []
    prvocisla = set()
    for cislo in range(int(input("Proosím zadejte číslo: ")) +1):
        if cislo >=2:
            seznam.append(cislo)
    print(seznam)
    while seznam:
        prvek = seznam.pop(0)
        prvocisla.add(prvek)
        for n in seznam:
            if n % prvek == 0:
                seznam.remove(n)

    prvocisla = sorted(prvocisla)
    return print(prvocisla)


#zavolání fce
list_primes()


##### ŘEŠENÍ ENEGETO ##########

# Definice fce list_primes
def list_primes1(n):

    # Vygenerovani listu k projiti
    nums = list(range(2,n+1))

    # Pomocna promenna pro ukladani prvocisel
    result = set()

    # While loop pro prochazeni listu
    while nums:

        # Prvocislo
        i = nums.pop(0)

        # Pridani prvocislo do vysledku
        result.add(i)

        # For loop pro odstraneni nasobku prvocisla
        for num in nums:
            if num % i==0:
                nums.remove(num)

    # Vraceni vysledku
    return result


print(list_primes1(100))




## funkce na zjištění jestli danné číslo je prvočíslo.. pracuje s předchozí fcí
## v mém případě jem neměl povinnou proměnou u první fce takže mi nefungovala druhá
## řešení v mém případě??
# Definice fce is_prime
def is_prime1(n):
    # Vraceni boolean hodnoty
    return n in list_primes1(n)

# Volani fce is_prime
print(is_prime1(23))

