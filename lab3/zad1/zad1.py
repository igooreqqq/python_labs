import json
with open('tramwaje.json', "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

print(data["linia"][0]["przystanek"][0]["name"])
slownik = {}


for i in data["linia"]:
    przystanki = ()
    if("przystanek" in i):
        for j in i['przystanek']:
            nazwa = j['name'].split()
            nazwa.pop()
            przystanek = ' '.join(nazwa)
            przystanki = przystanki + (przystanek,)
            slownik[i['name']] = przystanki

print(slownik)

with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
    json.dump(slownik, file, ensure_ascii=False)

slownik_ilosc = {}
for i in slownik.items():
    liczba_przystankow = 0
    for k in i[1]:
        liczba_przystankow += 1
    slownik_ilosc[i[0]] = liczba_przystankow

#sortuje malejąco po ilości przystanków
sort = dict(sorted(slownik_ilosc.items(), key=lambda item: item[1], reverse=True))

for i in sort.items():
    print("Liczba przystanków dla linii " + str(i[0]) + ': \t' + str(i[1]))

print()
print()
print()

for i in slownik.items():
    for k in slownik.items():
        if(i[0] != k[0]):
            print("Linia " + str(i[0]) + " wspoldzieli nastepujące przystanki z linia " + str(k[0]))
            print(tuple(set(i[1]) & set(k[1])))