# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

import random

MIN_ITEM = -50
MAX_ITEM = 120
SIZE = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
min_num = MAX_ITEM
max_num = MIN_ITEM

for i, item in enumerate(array):
    if item > max_num:
        max_num = item
        max_i = i
    if item < min_num:
        min_num = item
        min_i = i
array[min_i], array[max_i] = array[max_i], array[min_i]
print(array)
