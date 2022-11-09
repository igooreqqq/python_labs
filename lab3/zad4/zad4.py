import functools

def pamiec(func):
    slownik = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # tu powinien być kod tworzący słownik (element - wartość), który jest sprawdzany
        # do obliczeń wyrazów ciągu - które by były wyliczane rekurencyjnie i wpisywane
        # do słownika tylko gdy wcześniej nie były obliczone
        # normalnie bez buforowania by było return func(*args, **kwargs)

        if args in slownik:
            print("Odczytano fib(" + str(*args) + ") z pamięci")
            return slownik[args]

        print("Wykonuję fib(" + str(*args) + ")")
        result = func(*args, **kwargs)

        print("Dodano fib(" + str(*args) + ") do pamięci")
        slownik[args] = result
        return result
    return wrapper

@pamiec
def fibonacci(n):
    return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

for i in range(100):
    print(fibonacci(i))