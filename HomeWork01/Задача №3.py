# coding=utf-8
# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти
# точки.
print('Введите координату Х для точки А')
xa = float(input())
print('Введите координату Y для точки А')
ya = float(input())
print('Введите координату Х для точки B')
xb = float(input())
print('Введите координату Y для точки B')
yb = float(input())
if xa == xb :
    if ya == yb:
        print('Прямой не существует')
    else:
        print(f'Любая точка будет лежать на прямой при Х = {xa}')
else:
    k: float
    k = (yb - ya) / (xb - xa)
    b: float
    b = yb - k * xb
    print("Уравнение прямой y = " + '%0.2f' % k + " * x + (" + '%0.2f' % b + ')')
