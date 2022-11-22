class Baza(object):
    def __new__(cls, *args):
        print("-> Baza __new__", *args)
        nowy_obiekt = object.__new__(cls)
        print("<- Baza __new__")
        return nowy_obiekt

    def __init__(self, x):
        print("-> Baza __init__", x)
        super().__init__()
        print("-- Baza __init__")
        self.x = x
        print("<- Baza __init__")

    def __str__(self):
        return "{self.x}".format(self=self)

    def id(self):
        print("-Baza-")

class A(object):
    def __new__(cls, *args):
        print("-> A __new__", *args)
        nowy_obiekt = object.__new__(cls)
        print("<- A __new__")
        return nowy_obiekt

    def __init__(self, x):
        print("-> A __init__",x)
        super().__init__(x)
        print("-- A __init__")
        self.x = x
        print("<- A __init__")

    def __str__(self):
        return "{self.x}".format(self=self)

    def id(self):
        print("-A-")


class B(Baza):
    def __new__(cls, *args):
        print("-> B __new__", *args)
        nowy_obiekt = object.__new__(cls)
        print("<- B __new__")
        return nowy_obiekt

    def __init__(self, x):
        print("-> B __init__",x)
        super().__init__(x)
        print("-- B __init__")
        self.x = x
        print("<- B __init__")

    def __str__(self):
        return "{self.x}".format(self=self)

    def id(self):
        print("-B-")

class C(B):
    def __new__(cls, *args):
        print("-> C __new__", *args)
        nowy_obiekt = object.__new__(cls)
        print("<- C __new__")
        return nowy_obiekt

    def __init__(self, x):
        print("-> C __init__",x)
        super().__init__(x)
        print("-- C __init__")
        self.x = x
        print("<- C __init__")

    def __str__(self):
        return "{self.x}".format(self=self)

    def id(self):
        print("-C-")

class D(A, C, B, Baza):
    def __init__(self, x):
        print("-> D __init__",x)
        super().__init__(x)
        print("-- D __init__")
        self.x = x
        print("<- D __init__")

    def __str__(self):
        return "{self.x}".format(self=self)

    def id(self):
        print("-D-")

print("SCENARIUSZ 1")
### SCENARIUSZ 1: 
print(B.mro())
b = B(123)
print("------------")
b.id()
print("------------")
print(b)

print("\n\n\nSCENARIUSZ 2")
### SCENARIUSZ 2: 
print(C.mro())
c = C(456)
print("------------")
c.id()
print("------------")
print(c)

print("\n\n\nSCENARIUSZ 3")
### SCENARIUSZ 3: 
print(D.mro())
d = D(789)
print("------------")
d.id()
print("------------")
print(d)

print("\n\n\nSCENARIUSZ 4")
### SCENARIUSZ 4: 
# tak jak 3, tylko zobaczyć, co się dzieje podczas rzutowania:
# A(d),id() albo B(d),id() itp.
print(D.mro())
d = D(789)
print("------------")
B(d).id()
print("------------")
print(d)
