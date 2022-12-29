slova = ['Python', 'is', 'a', 'widely', 'used',
         'high-level', 'programming', 'language',
         'for', 'general-purpose', 'programming,',
         'created', 'by', 'Guido', 'van', 'Rossum',
         'and', 'first', 'released', 'in', '1991.']

nejdelsi = ("", 0)

while slova:
    slovo = slova.pop()
    if len(slovo) > nejdelsi[1]:
        nejdelsi = slovo, len(slovo)
print(nejdelsi)
