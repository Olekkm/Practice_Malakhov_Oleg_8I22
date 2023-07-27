f = lambda x: sum(x) / len(x)
try:
    a = list(map(int, input("Введите значения через пробел ").split()))
    print(f"Среднее значение: {f(a):.3f}")
except ValueError:
    print("Ошибка ввода")
except ZeroDivisionError:
    print("Необходимо минимум одно число")
