from math import log, sin, tan, exp


def func1(x, y, z):
    return (53 * z ** 2 - sin(z) - 77) / (90 * z ** 8 - 17 * z ** 5 - 89) + \
           log(40 * z) + y ** 3 - \
           (sin(z) + 56 * z ** 7 + 64) / (sin(x) + 42 * x ** 8 + 38)


def func2(x):
    if x < 82:
        return 53 * x ** 2 - sin(x) - 77
    elif 82 <= x < 148:
        return 90 * x ** 8 - 17 * x ** 5 - 89
    elif 148 <= x < 218:
        return tan(x ** 2) + x ** 532
    elif 218 <= x < 292:
        return 4 * x ** 6 - 66 * x ** 5
    elif x >= 292:
        return exp(x ** 3 - sin(x)) - (x ** 7) / 26


def func3(n, m):
    res1 = 0
    res2 = 0
    for i in range(1, n + 1):
        res1 += 53 * i ** 2 - sin(i) - 77
        for j in range(1, m + 1):
            res2 += 80 * i ** 2 - 17 * j ** 5
    return 56 * res1 - 7 * res2


def func4(n):
    if n == 0:
        return 4
    elif n == 1:
        return 2
    elif n < 0:
        return None
    else:
        return 0.04 * func4(n - 1) - tan(func4(n - 1))


print('%.2e' % func1(int(input('Введите x: ')), int(input('Введите y: ')), int(input('Введите z: '))))
print('%.2e' % func2(int(input('Введите x: '))))
print('%.2e' % func3(int(input('Введите n: ')), int(input('Введите m: '))))
print('%.2e' % func4(int(input('Введите n: '))))
