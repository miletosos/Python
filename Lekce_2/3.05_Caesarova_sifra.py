# Definice fce caesar
def caesar(vstup):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    vysledek = ""
    abeceda = list(enumerate(abeceda))

    print(abeceda)
    print("Vstup je:", vstup)


# eliminace mezer a čísel.. ještě je problém s dalšími znaky ,.! atd.
    for znak in vstup:
        znak = znak.lower()

        if znak.isdigit() or znak.isspace():
            vysledek = str(vysledek + str(znak))


        for cislo, pismeno in abeceda:
            if znak == pismeno:
                #print(pismeno, cislo)

### posun znaku o danný počet míst buď + nebo -

                novy_znak = (cislo + 6) % len(abeceda)
                for cislo, pismeno in abeceda:
                    if novy_znak == cislo:
                        #print("Nový znak:", cislo, pismeno)
                        vysledek = str(vysledek) + str(pismeno)

    return(print("zašifrovaný text je:", vysledek))



# Zprava
message = 'Petr Juracka, datum narození 1993'

# Zavolani fce
caesar(message)






################### ŘEŠENÍ ENGETO #######################



# Definice fce caesar
def caesar(message, offset):
    # Abeceda
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Vysledna zprava
    encrypted=[]

    # For loop pro zpravu
    for char in message:

        # Pokud znak neni v abecede, nahrajeme ho jen tak
        if char.lower() not in alphabet:
            encrypted.append(char)
            continue

        # Zjisteni pozice pismene
        position = alphabet.index(char.lower())

        # Novy index pismene
        index = (position+offset) % len(alphabet)

        # Ziskani noveho pismene
        if char.isupper():
            new_char = alphabet[index].upper()
        else:
            new_char = alphabet[index]

        # Nahrani do vysledne zpravy
        encrypted.append(new_char)

    # Vraceni zpravy jako stringu
    return ''.join(encrypted)
# Zprava
message = 'abc def ghi jkl mno pqr stu vwx Yz'
# Zavolani fce
print(caesar(message,-2))š