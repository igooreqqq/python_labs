print('Enter length:')
y = int(input())

print('Enter width:')
x = int(input())

for i in range(x):
    for j in range(y):
        print('+---', end='')
        if(j == y - 1):
            print('+', end='')
    print()
    for k in range(y):
        print('|   ', end='')
        if (k == y - 1):
            print('|', end='')
    print()

for j in range(y):
    print('+---', end='')
    if(j == y - 1):
        print('+', end='')