Rekurencyjne liczenie ciągu Fibonacciego jest naturalnym algorytmem, niemniej, wyliczanie każdego
kolejnego wyrazu ciągu „od początku” jest niepotrzebne. O wiele wydajniejszą metodą byłoby zastosowanie
czegoś w rodzaju buforu – pamięci podręcznej, w której zapamiętywalibyśmy poprzednio (wcześniej)
wyliczone wyrazy i z nich korzystali. Znacząco przyspieszy to obliczenia. Proszę napisać (uzupełnić poniższy
szkielet) kod tak, żeby powstawał słownik – pamięć podręczna z poprzednimi wyliczonymi wartościami i z nich
korzystać, a wyliczać nowe tylko gdy jeszcze nie były policzone wcześniej. Słownik proszę zrobić w dekoratorze.
```python
import functools
def pamiec(func):
@functools.wraps(func)
def wrapper(*args, **kwargs):
# tu powinien być kod tworzący słownik (element - wartość), który jest sprawdzany
# do obliczeń wyrazów ciągu - które by były wyliczane rekurencyjnie i wpisywane
# do słownika tylko gdy wcześniej nie były obliczone
# normalnie bez buforowania by było return func(*args, **kwargs)
return wrapper
@pamiec
def fibonacci(n):
return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)
for i in range(100):
print(fibonacci(i))
```
