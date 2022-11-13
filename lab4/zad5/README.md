Dyskutowane w zadaniu poprzednim rozwiązania mają pewne ograniczenia, jest to nowa funkcjonalność
w języku Python, która nadal nie obejmuje bardziej skomplikowanych zastosowań (np. przypadków
dziedziczenia). W tym zadaniu przyjrzymy się zewnętrznemu modułowi multipledispatch (prawdopodobnie
trzeba go najpierw zainstalować: pip install multipledispatch):
https://github.com/mrocklin/multipledispatch/

Przykład w pliku zadanie5.py to klasy Figura, Prostokat, Kwadrat i chodzi o to, aby definiując poniżej wersje
funkcji pole, różniące się argumentami oraz liczbą argumentów, wywołania wersji funkcji pole było
uzależnione właśnie od argumentów. Jeśli ta selekcja ma się odbywać na więcej niż jednym argumencie, można
właśnie użyc multipledispatch oraz dekorator @dispatch. Należy dopisać brakujący kod, aby testowe przykłady
działały. P.s. jeszcze inna opcja, to zewnętrzny moduł plum
https://wesselb.github.io/plum/intro.html
