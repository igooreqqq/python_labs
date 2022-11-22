# podpunkt A) 
# zdefiniować w ramach klasy A funkcję foo(self, x), metodę klasy class_foo, metodę statyczną static_foo, 
# tak, żeby kod poniżej drukował treści jak w komentarzach

class A(object):
    def foo(self, x):
        print(f'wykonanie foo({self}, {x})')

    @classmethod
    def class_foo(cls, x):
        print(f'class_foo({cls}, {x})')

    @staticmethod
    def static_foo(x):
        print(f'wykonanie static_foo({x})')

a = A()
a.foo(123) # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
A.foo(a,123) # ditto
a.class_foo(123) # class_foo(<class '__main__.A'>, 123)
A.class_foo(123) # ditto
a.static_foo(123) # wykonanie static_foo(123)
A.static_foo(123) # ditto

# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu
from abc import ABC, abstractmethod

print('\n\npodpunkt B)')

class Zwierze(ABC):
    @abstractmethod
    def glos(self):
        pass

class Pies(Zwierze):
    def __init__(self, x):
        self.x = x

    def glos(self):
        return self.x

class Kot(Zwierze):
    def __init__(self, x):
        self.x = x

    def glos(self):
        return self.x

kot = Kot("Miau")
pies = Pies("Hau Hau")

print(kot.glos())
print(pies.glos())
# podpunkt C)
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez 
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu

print('\n\npodpunkt C)')

class Aukcja:
    def __init__(self):
        self.cena = 1140
        print(f'Początkowa cena wynosi: {self.cena}')

    @property
    def podbicie(self):
        print("Bieżąca cena produktu wynosi: ", end="")
        return self.cena

    @podbicie.setter
    def podbicie(self, nowaCena):
        if nowaCena > self.cena:
            print(f"Cena produktu zostaje podbita do: {nowaCena}")
            self.cena = nowaCena
        else:
            print("Oferta mniejsza od bieżącej ceny produktu.")

aukcja = Aukcja()
aukcja.podbicie = 1200
print(aukcja.podbicie)
aukcja.podbicie = 1199
print(aukcja.podbicie)
aukcja.podbicie = 1600
print(aukcja.podbicie)