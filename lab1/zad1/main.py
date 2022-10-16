print("Wprowadź nieparzystą wartość dla długości podstawy trójkąta: ")
podstawa = int(input())

if(podstawa % 2 == 0):
    print("Zadana podstawa jest parzysta, wprowadź wartość nieparzystą.")

else:
    x = int((podstawa + 1) / 2) #liczba rzędów
    for row in range(1, x + 1): #iteracja po rzędach
        for col in range(1, 2 * x): #iteracja po kolumnach
            if(row == 1 or row == col or col + row == podstawa + 1):
                print("*", end='')
            else:
                print(end=" ")
        print()