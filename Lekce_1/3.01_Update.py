# Cílem této úlohy je vložit cizí slovník do našeho hlavního slovníku.

databaze = {"id123": {}, "id124": {}, "id125": {}, "id126": {}}

PrvniSlovnik = {"jmeno": "Thomas", "vek": 45, "zeme": "Czechia", "mesto": "Brno"}
DruhySlovnik = {'jmeno': 'Daniel', 'vek': 34, 'zeme': 'Czechia', 'mesto': 'Prague'}
TretiSlovnik = {'jmeno': 'Eva', 'vek': 43, 'zeme': 'Czechia', 'mesto': 'Olomouc'}

#id je bez uvozovek!!
databaze.update(id123 = PrvniSlovnik)
databaze.update(id124 = DruhySlovnik)
databaze.update(id125 = TretiSlovnik)

print(databaze)











