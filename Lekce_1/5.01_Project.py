'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

uzivatele = {"bob":"123","ann":"pass123","mike":"password123","liz":"pass123"}

#smyčka na přihlášení
print("Vítejte.")
while True:
    jmeno = input("Zadejte Vaše přihlašovací jméno: ")
    heslo = input("Zadehte Vaše heslo: ")

    if jmeno in uzivatele and heslo == uzivatele.get(jmeno):
        print("Přihlášení úspěšné.")
        break
    else:
        print("Heslo nebo přihlašovací jméno nesouhlasí.")

# výběr textu
print("Na výběr máte ze 3 textů, prosím zadejte číslo vybraného: ")
vyber_cisla = int(input("Vaše volba: "))
vybrany_text = TEXTS[vyber_cisla - 1]


pocet_slov = print("Počet slov je: ", len(vybrany_text.split()))
jednotliva_slova = vybrany_text.split()


prvni_velke = 0
vse_velke = 0
vse_male = 0
cisla = 0

# smyčky na počítání slov.. musel jsem dekalrovat jednotliva_slova neustale dokola protože pop to smaže..
# je zde lepší řešení??
while jednotliva_slova:
    slovo = jednotliva_slova.pop()
    if slovo[0].isupper():
        prvni_velke += 1

jednotliva_slova = vybrany_text.split()
while jednotliva_slova:
    slovo = jednotliva_slova.pop()
    if slovo.isupper():
        vse_velke += 1

jednotliva_slova = vybrany_text.split()
while jednotliva_slova:
    slovo = jednotliva_slova.pop()
    if slovo.islower():
        vse_male += 1

jednotliva_slova = vybrany_text.split()
while jednotliva_slova:
    slovo = jednotliva_slova.pop()
    if slovo.isdigit():
        cisla += 1


print("Počet slov začínajícími velkým písmenem:", prvni_velke)
print("Počet slov, kde jsou všechna velká je: ", vse_velke)
print("Počet slov kde jsou všechna písmena malá je: ", vse_male)
print("Počet čísel v textu: ", cisla)

# sloupcový graf

z1 = 0
z2 = 0
z3 = 0
z4 = 0
z5 = 0
z6 = 0
z7 = 0
z8 = 0
z9 = 0
z10 = 0
z11 = 0
z12 = 0
z13 = 0
z14 = 0
z15 = 0
z16 = 0

jednotliva_slova = vybrany_text.split()

while jednotliva_slova:
    slovo = jednotliva_slova.pop()
    if len(slovo) == 1:
        z1 += 1
    elif len(slovo) == 2:
        z2 += 1
    elif len(slovo) == 3:
        z3 += 1
    elif len(slovo) == 4:
        z4 += 1
    elif len(slovo) == 5:
        z5 += 1
    elif len(slovo) == 6:
        z6 += 1
    elif len(slovo) == 7:
        z7 += 1
    elif len(slovo) == 8:
        z8 += 1
    elif len(slovo) == 9:
        z9 += 1
    elif len(slovo) == 10:
        z10 += 1
    elif len(slovo) == 11:
        z11 += 1
    elif len(slovo) == 12:
        z12 += 1
    elif len(slovo) == 13:
        z13 += 1
    elif len(slovo) == 14:
        z14 += 1
    elif len(slovo) == 15:
        z15 += 1
    elif len(slovo) == 16:
        z16 += 1




print("1", z1 * "*", int(z1) * 1)
print("2", z2 * "*", int(z2) * 1)
print("3", z3 * "*", int(z3) * 1)
print("4", z4 * "*", int(z4) * 1)
print("5", z5 * "*", int(z5) * 1)
print("6", z6 * "*", int(z6) * 1)
print("7", z7 * "*", int(z7) * 1)
print("8", z8 * "*", int(z8) * 1)
print("9", z9 * "*", int(z9) * 1)
print("10", z10 * "*", int(z10) * 1)
print("11", z11 * "*", int(z11) * 1)
print("12", z12 * "*", int(z12) * 1)
print("13", z13 * "*", int(z13) * 1)
print("14", z14 * "*", int(z14) * 1)
print("15", z15 * "*", int(z15) * 1)
print("16", z16 * "*", int(z16) * 1)


# součet čísel v textu

jednotliva_slova = vybrany_text.split()
soucet = 0
while jednotliva_slova:
    slovo = jednotliva_slova.pop()
    if slovo.isdigit():
        soucet = int(slovo) + int(soucet)

print(soucet)




###################################################################################
###################################################################################
###################################################################################
# Řešení ENGETO

# Registrovaná uživatelská jména s hesly:

# | USER |   PASSWORD  |

# -----------------------

# | bob  |     123     |

# | ann  |    pass123  |

# | mike | password123 |

# | liz  |    pass123  |

credentials = {'bob': '123', 'ann': 'pass123',

                'mike': 'password123', 'liz': 'pass123'}

# 1. Na začátku přivítá uživatele.

print('-' * 40)

print('Welcome to the app. Please log in:')

# 2. Vyžádá si od uživatele přihlašovací jméno a heslo.

user = input('USERNAME: ')

password = input('PASSWORD: ')

# 3. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.

if credentials.get(user) != password:

    print('ACCESS DENIED')

    print('Incorrect password or username')

    quit()

# 4. Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS.

print('-' * 40)

print('We have 3 texts to be analyzed.')

sel = int(input('Enter a number btw. 1 and 3 to select: '))

print('-' * 40)

text = TEXTS[sel-1]

dirty_words = text.split()

words = []

while dirty_words:

    word = dirty_words.pop()

    word = word.strip('.,:/;')

    if word: words.append(word)

# 5. Pro vybraný text spočítá následující statistiky:

#   - počet slov,<br>

#   - počet slov začínajících velkým písmenem,<br>

#   - počet slov psaných velkými písmeny,<br>

#   - počet slov psaných malými písmeny,<br>

#   - počet čísel (ne cifer!).

print('There are ' + str(len(words)) + ' words in the selected text.')

titlecase = 0

lowercase = 0

uppercase = 0

numeric   = 0

counts    = {}

num_sum   = 0

i = 0

while i < len(words):

    if words[i].istitle():

        titlecase = titlecase + 1

    elif words[i].isupper():

        uppercase = uppercase + 1

    elif words[i].islower():

        lowercase = lowercase + 1

    elif words[i].isnumeric():

        numeric = numeric + 1

        num_sum = num_sum + float(words[i])

    l = len(words[i])

    counts[l] = counts.get(l,0) + 1

    i = i + 1

print('There are ' + str(titlecase) + ' titlecase words')

print('There are ' + str(uppercase) + ' uppercase words')

print('There are ' + str(lowercase) + ' lowercase words')

print('There are ' + str(numeric) + ' numeric strings')

print('-' * 40)

# 6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:

#  1 * 1

#  2 *********** 11

#  3 *************** 15

#  4 ********* 9

#  5 ********** 10

lengths = sorted(counts)

i= 0

while i < len(lengths):

    length = lengths[i]

    frequency = counts[length]

    if len(str(length)) == 1:

        str_len = ' ' + str(length)

    else:

        str_len = str(length)

    print(str_len, '*' * frequency, frequency)

    i = i + 1

# 7. Spočítá součet všech čísel (ne cifer!) v textu. Výsledkem tohoto součtu v následujícím textu by teby bylo číslo 8500:

# "that rises sharply some 1000 feet above

# Twin Creek Valley to an elevation of more

# than 7500 feet above sea level. The butte

# is located just north of US 30N"

print('-' * 40)

print('If we summed all the numbers in this text we would get: ' + str(num_sum))

print('-' * 40)

