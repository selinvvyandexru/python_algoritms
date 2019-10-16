# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры

def summa(n, s, st, i):
    if i == n:
        return s
    i += 1
    st = st / (-2)
    s += st
    return summa(n, s, st, i)


n = int(input('Введите целое число: '))
s = summa(n, s=0, st=-2, i=0)
print(s)
