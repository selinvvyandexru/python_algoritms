# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

n = int(input('Введите целое число: '))
div = 1
ch = int(0)
nech = int(0)
for i in range(len(str(n))-1):
    div = div * 10
for i in range(len(str(n))):
    x = int(n // div)
    if x & 1 == 1:
        nech += 1
    else:
        ch +=1
    n = n % div
    div = div / 10
print('Четных цифр - ' + str(ch))
print(f'Нечетных цифр - {nech}')
