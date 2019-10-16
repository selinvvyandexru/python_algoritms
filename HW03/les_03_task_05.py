# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

MIN_ITEM = -100
MAX_ITEM = 30
SIZE = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
max_negative = MIN_ITEM
print(array)

for i, item in enumerate(array):
    if item < 0:
        if item > max_negative:
            max_negative = item
            num_i = i
print(f'Наибольшее отрицательное число {max_negative} в позиции {num_i}.')