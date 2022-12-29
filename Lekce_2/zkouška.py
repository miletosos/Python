
import random

slova = ["kolobezka", "automobil", "sibenice", "kolo"]

abeceda = "abcdefghijklmnopqrstuvwxyz"
abeceda = sorted(abeceda)

vybrane_slovo = random.choice(slova)

def vstup():
    for pismeno in vybrane_slovo:
        print("_", end=" ")
    print(" ")
    volba = input("Prosím zaadejte váš tip: ")
    if volba in vybrane_slovo:
        print(volba)


print(vstup())











### Řešení engeto

import random

### Funkce main()
# Definice funkce
def main(words):
    # Náhodný výběr hádaného slova
    word = random.choice(words)

    # My jme se rozhodli nastavit pocet pokusu na 1.6 delky slova
    guesses_available = int(len(word) * 1.6)

    # Promenna pro vizualizaci
    status = ['_'] * len(word)

    # Veta na uvod
    print('I am thinking of a word. What word is it?')
    # While loop
    while True:

        # Pouziti 2. funkce get_letter
        letter = get_letter(status, guesses_available)

        # Pouziti 3. funkce replace_letters
        replace_letters(letter, word, status)

        # Odecteni pokusu
        guesses_available -= 1

        # While konci pokud je vse uhadnuto
        if '_' not in status:
            print('\nCongatulations, you have won!\n')
            break

        # While konci pokud dojdou pokusy
        if not guesses_available:
            print('\nYou have lost. The word was:\n' + word)
            break


### Funkce get_letter()
# Definice funkce
def get_letter(status, guesses_available):
    # Vizualizace
    print(' '.join(status))

    # Ziskani vstupu od uzivatele
    letter = input('Guess a letter | guesses available: '
                   + str(guesses_available) + '\n')

    # Vraceni vstupu od uzivatele
    return letter


### Funkce replace_letters()
# Definice funkce
def replace_letters(letter, word, status):
    # Pocet nahrazeny pismen
    count_replaced = 0

    # For loop pro zjisteni poctu a nahrazeni uhadnuteho pismene
    for i, char in enumerate(word):
        if char == letter:
            status[i] = letter
            count_replaced += 1
    # Pokud jsme neco nahradili
    if count_replaced:
        print("Number of positions matched: " + str(count_replaced))
    # Pokud jsme nic nenahradili
    else:
        print('No, the letter ' + letter + ' is not in my word')


### Spuštění programu
# Nase slova
words = ['Hangman', 'available', 'increase']
# Spusteni fce main a vlozeni slov
main(words)


### moje řešení podle engeta

import random

def main(words):
    word = random.choice(words)
    pokusy = int(len(word) * 1.6)
    status = ["_"] * len(word)

    print("Myslím na nějaké slovo, dokážeš ho uhádnout?")

    while True:
        letter = get_letter(status, pokusy)

        replace_letters(letter, word, status)

        pokusy -= 1

        if  "_" not in status:
            print("\nBlahopřeji vyhrál jste!\n")
            break

        if not pokusy:
            print("\nProhrál jste. Slovo bylo: \n", + word)
            break




def get_letter(status, pokusy):
    print(" ".join(status))

    letter = input("Hádej písmeno | zbývající pokusy: "
                   + str(pokusy) + "\n")

    return letter

















