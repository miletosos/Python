cislo = 10
while cislo:
    print(cislo)
    cislo = cislo- 1
print("bla")

muj_string = 'while smyčKy můžOu být neKonečné'

while muj_string:

    if muj_string[0].isupper():

        print('Našel jsem velké písmeno:',muj_string[0])

    muj_string = muj_string[1:]

    # zadani stringu
    muj_string = 'while smyčky můžou být neKonečné'

    # while smycka
    while muj_string:
        if muj_string[0].isupper():
            print('Našel jsem velké písmeno:', muj_string[0])
            break
        muj_string = muj_string[1:]

        # kod po while
    print('Hotovo! V proměnné muj_string zbylo:', muj_string)