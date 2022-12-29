#####   ŘEŠENÍ ENGETO

def num_days(date1, date2):
    # Chronologicke serazeni dat
    if date1 > date2:
        date1, date2 = date2, date1
    # Pocitadlo
    num_days = 0
    # Zvysujeme dat1 dokud je mensi nez date2
    while date1 < date2:
        date1 = increase(date1)
        num_days += 1
    # Vraceni dnu
    return num_days

# Definice fce
def increase(date):
    # Rozdeleni datumu do jednotlivych promennych
    y,m,d = date
    # Unor
    if m == 2 and d in [28,29]:
        if is_leap(y) and d == 28:
            date =(y,m,d+1)
        else:
            date =(y,m+1,1)
    # Konec mesice
    elif (m in [1,3,5,7,8,10] and d == 31) \
        or (m in [4,6,9,11] and d == 30):
        date =(y,m+1,1)
    # Konec roku
    elif m == 12 and d == 31:
        date = (y+1,1,1)
    # Uvnitr mesice
    else:
        date = (y,m,d+1)
    # Vraceni upraveneho data
    return date

def is_leap(y):
    # Vraceni vysledku testu
    return ((y % 400 == 0) or (y % 4 == 0 and y % 100 != 0))

def weekday(date,relative_date=(1970,1,1), relative_weekday=4):
    # Vracime -1, pokud je datum mensi nez 1.1.1970
    if date < relative_date:
        return -1
    # Vracime 'Non-existent date' pokud datum neexistuje
    elif not is_leap(date[0]) and date[1:] == (2,29):
        print('Non-existent date')
        return 0
    # Pocitani dnu
    days = num_days(relative_date, date)
    # Zjisteni dne - priklad uvedeny vyse v popisu
    weekday = (days + relative_weekday)%7
    print(weekday)
    return weekday

# Datum - vychazi na patek - 5
date = (1993,10,13)
# Spusteni main
weekday(date)