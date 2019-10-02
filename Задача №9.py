# Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).
print('Введите три разных числа:')
a = float(input())
b = float(input())
c = float(input())
if b > a > c or c > a > b:
    print('Среднее число: ' + str(a))
elif a > b > c or c > b > a:
    print('Среднее число: ' + str(b))
elif a > c > b or b > c > a:
    print('Среднее число: ' + str(c))
