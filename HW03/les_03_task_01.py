# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
# каждому из чисел в диапазоне от 2 до 9

array = [i for i in range(2, 100)]
count_array = [0] * 8

for j in range(len(count_array)):
    spam = array[j]
    for item in array:
        if not item % spam:
            count_array[j] += 1
    print(f"{array[j]:>4} {count_array[j]:>4}")
