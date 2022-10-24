list1 = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]
list2 = [1, [3], [2]]

counters = []

def get_depth_of_nested_lists(lista: list, count = 0):
    for i in lista:
        if(isinstance(i, list)):
            get_depth_of_nested_lists(i, count + 1)
    counters.append(count)
    return max(counters)

def extend_most_nested_lists(lista: list, most_nested: int, counter = 0):
    for i in lista:
        if(isinstance(i, list)):
            extend_most_nested_lists(i, most_nested, counter + 1)
        elif(counter == most_nested):
            lista.append(max(lista) + 1)
            counter += 1

def clear_list(counters: list):
    counters.clear()


print("Lista1 na początku: ", end=' ')
print(list1)
print("Lista1 po operacji: ", end=' ')
get_depth_of_nested_lists(list1)
extend_most_nested_lists(list1, max(counters))
clear_list(counters)
print(list1)

print()

print("Lista2 na początku: ", end=' ')
print(list2)
print("Lista2 po operacji: ", end=' ')
get_depth_of_nested_lists(list2)
extend_most_nested_lists(list2, max(counters))
clear_list(counters)
print(list2)