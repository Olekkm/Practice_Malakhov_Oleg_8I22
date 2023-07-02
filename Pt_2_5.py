from random import randint


class NotAnOption(Exception):
    pass


print("0 - Орел\n1 - Решка\n")
win = 0
loose = 0
count = 0
while True:
    try:
        c = int(input("Орел или решка? "))
        if (c != 0) and (c != 1):
            raise NotAnOption
        a = randint(0, 1)
        if c == a:
            count = 0
            win += 1
            print(f"Победа!\n\nПобед: {win}\nПоражений: {loose}\n")
        else:
            count += 1
            loose += 1
            print(f"Поражение...\n\nПобед: {win}\nПоражений: {loose}\n")
        if count == 3:
            print("Полное поражение")
            break
    except ValueError:
        print("Ошибка ввода\n")
    except NotAnOption:
        print("Ребро тут не выпадает\n")
