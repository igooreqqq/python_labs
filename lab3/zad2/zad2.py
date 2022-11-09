import sys

def na_rzymskie(liczba):
    if not isinstance(liczba, int):
        print("Podano niewłaściwe dane wejściowe. Należy wpisać liczbę.")
        sys.exit()
    if(liczba < 1 | liczba > 4000):
        print("Podana liczba nie mieści się w przedziale 1-3999")
        sys.exit()

    slownik = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
               'V': 5, 'IV': 4, 'I': 1}

    result = ""

    for i in slownik.items():
        while liczba >= i[1]:
            result += i[0]
            liczba -= i[1]
    return result

def na_arabskie(liczba):
    slownik = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in liczba:
        if i not in slownik.keys():
            print("Wprowadzona liczba w zapisie rzymskim zawiera niepoprawny zapis")
            sys.exit()

    result = 0

    for i in range(0, len(liczba)):
        if i + 1 == len(liczba) or slownik[liczba[i]] >= slownik[liczba[i + 1]]:
            result += slownik[liczba[i]]
        else:
            result -= slownik[liczba[i]]
    return result

arabska_to_rzymska = na_rzymskie(569)
print(arabska_to_rzymska)

rzymska_to_arabska = na_arabskie("DLXIX")
print(rzymska_to_arabska)