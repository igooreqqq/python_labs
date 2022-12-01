s = list(input())

lower = []
upper = []
odd = []
even = []

for i in s:
    if str(i).islower():
        lower.append(i)
    if str(i).isupper():
        upper.append(i) 
    if str(i).isdigit():
        i = int(i)
        if(i % 2 == 0):
            even.append(i)
        if(i % 2 != 0):
            odd.append(i)
        
lower = sorted(lower)
upper = sorted(upper)
odd = sorted(odd)
even = sorted(even)

result = lower + upper + odd + even

for i in result:
    print(i, end='')
