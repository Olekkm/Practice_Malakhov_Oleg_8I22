try:
    distance = int(input("Введите расстояние "))
    fuelperkm = int(input("Введите расход на 100 км "))
    fuel = int(input("Введите колличество топлива "))
    if distance / 100 * fuelperkm <= fuel:
        print("Можно ехать")
    else:
        print("Ехать не можно")
except ValueError:
    print("Ошибка ввода")
