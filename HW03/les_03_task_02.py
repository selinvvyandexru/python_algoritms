# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
# надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

MIN_ITEM = 0
MAX_ITEM = 120
SIZE = 15
first_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
second_array = []
print(first_array)

for i, item in enumerate(first_array):
    if not item & 1:
        second_array.append(i)
print(second_array)
