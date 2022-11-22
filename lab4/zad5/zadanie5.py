from multipledispatch import dispatch

class Figura(object):
    def __init__(self):
        print("Figura init")

class Prostokat(Figura):
    # zdefiniuj __init__ i argumenty x, y
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Kwadrat(Prostokat):
    # __init__ i jeden argument x, wołanie __init__ bazowego
    def __init__(self, x):
        super().__init__(x, x)

@dispatch(Figura)
def pole(instance: Figura):
    print("Pole: Figura")
    return 0

@dispatch(Prostokat)
# zdefiniuj pole, zwróć x*y z instancji
def pole(arg):
    print("Pole prostokąta: ", end='')
    return arg.x * arg.y

@dispatch(Prostokat, int, int)
# funkcja pole, najpierw przypisz argumenty do x, y instancji, potem policz pole powierzchni
def pole(instance: Prostokat, a, b):
    poleProstokat = Prostokat(a, b)
    return pole(poleProstokat)

@dispatch(Kwadrat)
# funkcja pole
def pole(arg):
    print("Pole kwadratu: ", end='')
    return arg.x * arg.x

@dispatch(Kwadrat, int)
# funkcja pole z podanym argumentem boku
def pole(instance: Kwadrat, a):
    poleKwadrat = Kwadrat(a)
    return pole(poleKwadrat)
# testy

a, b, c = Figura(), Prostokat(2,4), Kwadrat(2)

bb = pole(b, 5, 6)
print(bb)
cc = pole(c, 7)
print(cc)


def polaPowierzchni(listaFigur):
    for i in listaFigur:
        print(pole(i)) # polymorphism at runtime

polaPowierzchni([a,b,c])