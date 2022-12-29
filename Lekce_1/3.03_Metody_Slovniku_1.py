# Vytvor prazdne slovniky do slovníků.
muj_slovnik = {}
novy_slovnik = {}

# Vloz klice 'jméno', 'přijmení' do 'muj_slovnik' a přidej libovolne hodnoty.
muj_slovnik['jméno'] 	= "Petr"
muj_slovnik['přijmení'] 	= "Juracka"

# Vytvor z tuple 'muj_tuple' slovnik do slovniku 'novy_slovnik'.
muj_tuple = 'věk', 'email'
novy_slovnik = novy_slovnik.fromkeys(muj_tuple)

# Dopln muj_slovnik o novy_slovnik.
muj_slovnik.update(novy_slovnik)

# Vypln klice 'věk' a 'mail'.
muj_slovnik["věk"] = 25
muj_slovnik["email"] = "petr@gmail.com"
print(muj_slovnik)

# TADY NIC NEPIŠ. Slouží pro kontrolu. :-)
if (len(muj_slovnik) + 1) % 5 == 0 and '@' in muj_slovnik['email']:
	print('Paráda, metody slovníků ovládáš na jedničku, blahopřejeme!')
else:
	print('Bohužel máš někde chybu. \nPodívej se ještě jednou na tabulku s metodami.\n\npozn. Obsahuje tvůj email "@"?')