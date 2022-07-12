list = [4, 3, 2, 1]

list_2 = []

for num in list:
    list_2.append(num ** 2)

print(list_2)

sarasas = [4, 3, 2, 1]

def daugiau_nei_2(sarasas):
    sarasas_2 = []
    for skaicius in sarasas:
        if skaicius > 2:
            sarasas_2.append(skaicius)
    return sarasas_2

print(daugiau_nei_2(sarasas))

from functools import reduce

sarasas = [4, 3, 2, 1]
naujas = reduce(lambda x, y: x + y, sarasas)
print(naujas)

# 10
from functools import reduce

sarasas = [4, 3, 2, 1]
naujas = reduce(lambda x, y: x * y, sarasas)
print(naujas)

from statistics import mean, median

sarasas = [2, 9, 10, 39, 45]

print(mean(sarasas))

# 21

print(median(sarasas))

sarasas = list(range(20))
lyginiai = (x for x in sarasas if x % 2 == 0)

print(lyginiai)

sarasas = [4, 3, 2, 1, 5, 6, 7, 10, 9, 8]

sarasas.sort()
print(sarasas)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

naujas = sorted(sarasas)
print(naujas)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sarasas.sort(reverse=True)
print(sarasas)

# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

naujas = sorted(sarasas, reverse=True)
print(naujas)

# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
tuple_sarasas = (4, 3, 2, 1, 5, 6, 7, 10, 9, 8)

tuple_sarasas.sort()
# AttributeError: 'tuple' object has no attribute 'sort'

naujas = sorted(tuple_sarasas)
print(naujas)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]