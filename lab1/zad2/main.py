import sys
argv = sys.argv[1:]

for i in argv:
    x = int(i)
    print(str(x) + ' = ', end='')
    factors = []
    count = 0
    count2 = 0

    k = 2
    while(x > 1):
        while((x % k) == 0):
            #print(str(k) + ' ' + str())
            factors.append(k)
            x /= k
        k += 1

    for i in factors:
        if(factors[count2] != factors[count2 - 1]):
            count = factors.count(i)
            #print('Liczba ' + str(i) + ' wynosi: ' + str(count))

            count2 += 1
            if(count == 1):
                if(len(factors) == count2):
                    print(str(i), end='')
                else:
                    print(str(i) + ' * ', end='')
            else:
                print(str(i) + '^' + str(count) + ' * ', end='')
        else:
            count2 += 1
            continue
    print()