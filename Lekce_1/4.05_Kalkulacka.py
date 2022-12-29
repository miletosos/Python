
while True:
    print("Pro ukončení napište exit.")
    hodnota_1 = int(input("Prosím zadejte první hodnotu: "))
    hodnota_2 = int(input("Prosím zadejte druhou hodnotu: "))
    symbol = input("Prosím zadejte operaci *,/,-,+ :")
    vysledek = 0
    if symbol == ("*"):
        vysledek = hodnota_1 * hodnota_2
        print(vysledek)
    elif symbol == ("/"):
        vysledek = hodnota_1 / hodnota_2
        print(vysledek)
    elif symbol == ("+"):
        vysledek = hodnota_1 + hodnota_2
        print(vysledek)
    elif symbol == ("-"):
        vysledek = hodnota_1 - hodnota_2
        print(vysledek)
    elif symbol == ("exit"):
        break
    else:
        print("Zadanou operaci nebylo možné provést, prosím opakujte operaci.")


#### Řešení ENGETO:

# Pozdrav uživatele a umožni mu zapsat dvě vstupní proměnné.
print('Ahoj, nejprve vyber dve cisla! :)')
print()
number01 = int(input('Prosim zadajte prvni cislo: '))
number02 = int(input('Prosim zadajte druhe cislo: '))

# Tento text nechceme opakovat, proto patří před smyčku while.
print('Nyni vyber operaci, kterou chces s cisly provest: ')
print()

# Zapiš nekonečnou smyčku.
# Mód kalkulačky je ON.
# Podmínka nekonečne smyčky.
mod = True
while mod == True:

# Vypiš, jaké operace může uživatel provádět, a dej mu možnost zapsat input().
	choice = str(input('''
------------------------
Scitani:	"sci",
Odcitani:	"odc",
Nasobeni:	"nas",
Deleni:		"del",
Ukonci:		"off",
----------------------
Vyber si operaci: '''))

    # Sem zapiš podmínky, které spojí tebou nabízené operace a následný print() výsledku.
	if choice == 'sci':
		print('		>>> ' + str(number01)+ ' + ' + str(number02) + ' = ' + str(number01 + number02))
	elif choice == 'odc':
		print('		>>> ' + str(number01) + ' - ' + str(number02) + ' = ' + str(number01 - number02))
	elif choice == 'nas':
		print('		>>> ' + str(number01) + ' * ' + str(number02) + ' = ' + str(number01 * number02))
	elif choice == 'del':
		print('		>>> ' + str(number01) + ' / ' + str(number02) + ' = ' + str(number01 / number02))
	elif choice == 'off': # prepnu mod OFF
		print('Poctum zdar, brachu!')
		mod = False