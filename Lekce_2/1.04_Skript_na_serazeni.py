names = ['Michal', 'Pepa', 'Honza',
        'Pavel', 'Lukas', 'Matej',
        'Iva', 'Klara', 'Jana',
        'Honza', 'Vasek','Milan', 'Michal']

print(sorted(names))

usporadane = [names.pop()]

for name in names:
    for i,s_name in enumerate(usporadane):
        if name < s_name:
            usporadane.insert(i, name)
            break
    else:
        usporadane.append(name)

print(usporadane)


