# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE = 4
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE+1)]
print(*matrix, sep='\n')

min_column = [MAX_ITEM] * len(matrix[0])
min_row = [0] * SIZE
max_num = MIN_ITEM

for i, line in enumerate(matrix):
    for j, item in enumerate(line):
        if item < min_column[j]:
            min_column[j] = item
            min_row[j]  = i

print('Минимумы столбцов:')
print(min_column)

for item in min_column:
    if item > max_num:
        max_num = item

pos = min_column.index(max_num)
print(f'Максмальное значение среди минимальных {max_num}')
print(f'Элемент находится в {min_row[pos]} строке и {pos} столбце.')
