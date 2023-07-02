class SizeError(Exception):
    pass


try:
    a = list(map(int, input("Введите коэффициенты a, b, c через пробел ").split()))
    if len(a) != 3:
        raise SizeError
    D = a[1] ** 2 - 4 * a[0] * a[2]
    if D < 0:
        print("Решений нет")
    elif D == 0:
        print(f"x = {((-a[1]) / (2 * a[0])):.3f}")
    else:
        print(f"x1 = {((-a[1] + D ** 0.5) / (2 * a[0])):.3f}\nx2 = {((-a[1] - D ** 0.5) / (2 * a[0])):.3f}")
except ValueError:
    print("Ошибка ввода")
except SizeError:
    print("Необходимо указать 3 аргумента")
