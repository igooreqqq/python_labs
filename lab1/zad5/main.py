def union(set1, set2):
    set = []
    for i in set1:
        set.append(i)
    for i in set2:
        if(set.__contains__(i)):
            continue
        set.append(i)
    return set

def intersection(set1:list, set2:list):
    set = []

    if(len(set1) < len(set2)):
        for i in set1:
            if(set2.__contains__(i)):
                set.append(i)

    else:
        for i in set2:
            if(set1.__contains__(i)):
                set.append(i)
    return set

set_1 = ["element1", "1", "element2", "element3", "2"]
set_2 = ["element3", "element4", "2"]

set_union = union(set_1, set_2)
set_inter = intersection(set_1, set_2)

print("Suma elementów: " + str(set_union))
print("Część wspólna: " + str(set_inter))