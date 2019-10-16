# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

def revnum(n, revn, div, LEN_N):
    if len(revn) == LEN_N:
        return revn
    x = int(n // div)
    n = n % div
    div = div / 10
    revn = str(x) + revn
    return revnum(n, revn, div, LEN_N)


n = int(input('Введите целое число: '))
div = 1
revn = ''
LEN_N = len(str(n))
for i in range(LEN_N - 1):
    div = div * 10
revn = revnum(n, revn, div, LEN_N)
print(revn)
