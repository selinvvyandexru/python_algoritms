# Определить, какое число в массиве встречается чаще всего.
# Т.к. аналоги sum договорились не использовать, то метод .count() исключаем

import random

MIN_ITEM = 1
MAX_ITEM = 3
SIZE = 15
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
norepeats_array = []
count_array = []
max_count = 0
print(array)

for item in array:
    if item in norepeats_array:
        j = norepeats_array.index(item)
        count_array[j]+=1
        if max_count < count_array[j]:
            max_count = count_array[j]
    else:
        norepeats_array.append(item)
        count_array.append(1)
print(f'Число {norepeats_array[count_array.index(max_count)]} встречается {max_count} раз.')
