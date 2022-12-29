cas = input("Prosím  zadejte čas: ")
cas = cas.split(":")
hodiny = cas[0]
minuty = cas[1]

upraveny = int(hodiny) - 12
print(upraveny)
if int(upraveny == 0):
    print("Opravený čas je", upraveny, ":", minuty, "AM")
elif int(hodiny)> 12:
    print("Opravený čas je", upraveny, ":", minuty, "PM")
else:
    print("Opravený čas je", hodiny, ":", minuty, "AM")


########################################################################
##########################################################################
######################################################################
# ŘEŠENÍ ENGETO

# Získej vstup uživatele do proměnné 'time'
time = input('Please enter your time: ')

# Rozděl do listu vstup od uživatele do proměnné 'hours` a `mins`.
hours, mins = time.split(':')

# Uprav proměnou 'hours' tak, aby se do proměnné 'adjusted_hours' místo 24 hodinového formátu (např.: 17) uložil formát anglický (např.: 5).
adjusted_hours = hours if int(hours)==12 else str(int(hours) % 12)

# Do proměnné 'daytime' vyber odpovídající string z dvojčlenného listu ['AM', 'PM']
# Dosáhneš toho pomocí výrazu, který vrátí index 0 (=False), nebo 1 (=True).
daytime = ['AM','PM'][int(hours)>=12]

# Vytiskni převedený čas.
print('Converted to English format: ' + adjusted_hours + ':' + mins + ' ' + daytime)