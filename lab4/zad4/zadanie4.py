import math
from functools import singledispatch, singledispatchmethod

@singledispatch
def pierwiastek(x):
    return "Argument o nieobsługiwanym typie."

@pierwiastek.register
def _(x: int):
    return math.sqrt(x)

@pierwiastek.register
def _(x: float):
    return math.sqrt(x)

@pierwiastek.register
def _(x: list):
    return [math.sqrt(i) for i in x]

@pierwiastek.register
def _(x: dict):
    for i, j in x.items():
        x[i] = math.sqrt(j)
    return x

print(pierwiastek(25))
print(pierwiastek(25.25))
print(pierwiastek([25, 36]))
print(pierwiastek({'pierwsza liczba': 25, 'druga liczba': 36}))
print(pierwiastek("25"), end='\n\n\n')

##################################################

class Potega:
    @singledispatchmethod
    def pot(self, x):
        return "Argument o nieobsługiwanym typie."

    @pot.register
    def _(self, x: int):
        return x**2

    @pot.register
    def _(self, x: float):
        return x**2

    @pot.register
    def _(self, x: list):
        return [i**2 for i in x]

    @pot.register
    def _(self, x: dict):
        for i, j in x.items():
            x[i] = j**2
        return x

potega = Potega()

print(potega.pot(5))
print(potega.pot(5.5))
print(potega.pot([5, 6]))
print(potega.pot({'pierwsza liczba': 5, 'druga liczba': 6}))
print(potega.pot("25"))