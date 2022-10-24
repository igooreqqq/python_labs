sentence = "Zdanie testowe zawierające 11 słów, 5 cyfer, a także 44 liter"
sentence = sentence.lower() #aby nie zliczać osobno dużych i małych liter

lista = sentence.split()
lista2 = []
sumaCyfr = 0
sumaLiter = 0

for i in sentence.replace(" ", ""):
    lista2.append(i)

for j in lista2:
    if(j.isdigit()):
        sumaCyfr += 1
    if(j.isalpha()):
        sumaLiter += 1

print("Ilość słów: " + str(len(lista)))
print("Ilość cyfr: " + str(sumaCyfr))
print("Ilość liter: " + str(sumaLiter))
print()

lista3 = []
for k in lista2:
    if(k.isdigit()):
        if(lista3.__contains__(k)):
            continue
        else:
            lista3.append(k)
            print("Cyfra " + str(k) + " występuje " + str(lista2.count(k)) + " razy.")
    elif(k.isalpha()):
        if(lista3.__contains__(k)):
            continue
        else:
            lista3.append(k)
            print("Litera " + str(k) + " występuje " + str(lista2.count(k)) + " razy.")