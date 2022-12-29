nums = input("Prosím zadejte čísla oddělená čárkou: ")
vysledek = []
nums = nums.split(",")

for cislo in nums:
    cislo = cislo.strip()
    vysledek.append(cislo)

print(vysledek)
