lst = []

while True:
    slovo = input("Prosím vložte slova, které chete porovnat, (break proukončení) : ")
    if slovo == "break":
        break
    lst.append(slovo)

def anagram(lst):
    prvni = lst.pop()

    for prvek in lst:

        if sorted(prvni) == sorted(prvek):
            return ("anagram")

        else:
            return ("není to anagram")

print(anagram(lst))




#### ŘEŠENÍ ENGETO


# Definice fce
def all_anagrams(words):
    if words:
        result = True
        seq= sorted(words.pop())
        for word in words:
            if sorted(word) != seq:
                result = False
            else:
                result = True
    else:
        result = False
    return result
# Slova
words = ['ship','hips','name']
# Volani fce
print(all_anagrams(words))
