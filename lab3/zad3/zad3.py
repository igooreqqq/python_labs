def reverse_iter(L: list, left, right):
    L2 = L.copy()
    while(left != right & right > left):
        temp = L2[left]
        L2[left] = L2[right]
        L2[right] = temp
        left += 1
        right -= 1
    return L2

def reverse(Li: list):
    if len(Li) == 0:
        return Li
    else:
        return [Li[-1]] + reverse(Li[:-1])

def reverse_rec(L: list, left, right):
    first = L[:left]
    middle = L[left:right+1]
    end = L[right+1:]
    middle = reverse(middle)
    return first + middle + end


lista = [2, 4, 5, 6, 7]

print("Iteracyjnie:")
iteracyjnie = reverse_iter(lista, 3, 4)
print(iteracyjnie)
print()
print("Rekurencyjnie:")
rekurencyjnie = reverse_rec(lista, 1, 3)
print(rekurencyjnie)