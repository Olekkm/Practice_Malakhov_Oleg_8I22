try:
    a = float(input())
    if a < 0:
        raise ArithmeticError
    b = int(a ** 0.5) + 1
    print(f"{b}^2 > {a}")
except ValueError:
    print("Ошибка ввода")
except ArithmeticError:
    print("Число меньше 0")
