from itertools import product

K, M = list(map(int, input().split()))

list1 = []
for i in range(K):
    list1.append(map(lambda x: x ** 2, map(int, input().split(" ")[1:])))

list1 = list(product(*list1))
x = map(lambda x: x % M, map(sum, list1))

result = max(x)

print(result)
