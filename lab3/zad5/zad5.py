class Bug:
    """ Klasa Bug"""
    licznik = 0

    def __init__(self):
        """Wraz z wywołaniem funkcji rośnie licznik"""
        Bug.licznik += 1
        self.id = Bug.licznik

    def __del__(self):
        """Wraz z wywołaniem funkcji maleje licznik"""
        Bug.licznik -= 1
        self.id = Bug.licznik
        print(f'Koniec = {Bug.licznik} ID={self.id}')

    def __str__(self):
        """Funkcja wypisuje licznik i ID"""
        return f'Bug count = {Bug.licznik} ID={self.id}'

bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])
