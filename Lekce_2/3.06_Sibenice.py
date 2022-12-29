import random

def main(words):
    word = random.choice(words)
    pokusy = int(len(word) * 1.6)
    status = ["_"] * len(word)
    print("Myslím si slovo, zkus ho uhádnout.")

    while True:
        letter = get_letter(status, pokusy)
        replace_letters(letter, word, status)
        pokusy -= 1

        if "_" not in status:
            print("Blahopřeji vyhrál jste!")
            break

        if not pokusy:
            print("Prohrál jste!")
            print("Slovo bylo: ", slovo)
            break

def get_letter(status, pokusy):
    print(" ".join(status))
    letter = input("Hádej písmeno | zbývajíci pokusy: " + str(pokusy) + "\n")
    return letter

def replace_letters(letter, word, status):
    count_replaced = 0

    for i, char in enumerate(word):
        if char == letter:
            status[i] = letter
            count_replaced += 1

    if count_replaced:
        print("Počet nahrazrných písmen: " + str(count_replaced))

    else:
        print("Ne písmeno: " + letter + "není ve slově")

words = ["zabijak", "balik", "prdelka", "praha"]

main(words)








