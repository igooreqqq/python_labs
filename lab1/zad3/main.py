print('Enter length:')
x = int(input())

for i in range(x):
    print('|....', end='')
    if(i == x-1):
        print('|')

for i in range(x+1):
    if(i == 9):
        print(i, end='   ')
    elif(len(str(i)) == 1):
        print(i, end='    ')
    if (i == 99):
        print(i, end='  ')
    elif(len(str(i)) == 2):
        print(i, end='   ')
    if(len(str(i)) == 3):
        print(i, end='  ')