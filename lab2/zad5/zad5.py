import sys

def fun(N):
    if(N < 1 or N > 2147483647):
        print("N jest poza dopuszczalnym zakresem")
        sys.exit()
    count = 0
    max = 0
    liczba = str(bin(N)[2:])
    for i in liczba:
        if(i == "1"):
            if(max < count):
                max = count
            count = 0
        if(i == "0"):
            count += 1
    print("Binarny zapis: " + liczba)
    print("Najdłuższa przerwa binarna: " + str(max))

fun(1041)