# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

MIN_ITEM = -10
MAX_ITEM = 120
SIZE = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
min_1 = MAX_ITEM
min_2 = MAX_ITEM

for item in array:
    if item < min_1:
        min_1 = item
    else:
        if item < min_2:
            min_2 = item
print(f'Два минимальных элемента равны {min_1}' if min_1 == min_2 else f'Минимальные элементы равны {min_1} и {min_2}')
