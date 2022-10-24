#x, y, z, n = 1, 1, 2, 3
print("Podaj wartość x: ")
x = int(input())
print("Podaj wartość y: ")
y = int(input())
print("Podaj wartość z: ")
z = int(input())
print("Podaj wartość n: ")
n = int(input())

list1 = []

for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
                list2 = []
                list2.append(i)
                list2.append(j)
                list2.append(k)
                list1.append(list2)

result_List = [x for x in list1 if sum(x) != n]

print(result_List)