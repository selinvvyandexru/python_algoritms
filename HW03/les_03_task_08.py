# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

SIZE = 4
matrix = [[None for _ in range(SIZE)] for _ in range(SIZE+1)]

for i in range(SIZE + 1):
    sum_line = 0
    for j in range(SIZE):
        if j != (SIZE - 1):
            matrix[i][j] = int(input('Введите целое число: '))
            sum_line += matrix[i][j]
        else:
            matrix[i][j] = sum_line

print(*matrix, sep='\n')
