#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)


result = ""

for i in range(m):
    for j in range(n):
        result += matrix[j][i]
        
result = re.compile(r"([A-Za-z0-9])[^A-Za-z0-9]+([A-Za-z0-9])").sub(r"\1 \2", "".join(result))
print(result)
