
max = 0

def function(l: list):
    k = 0
    for i in l:
        if(isinstance(i, list)):
            print(i)
            list2 = i
            function(i)




list1 = [1, 2, [3, 4, [5, 6], 5, [7, 8, [1, 2]]], 3, [4, 5]]

function(list1)

