class Error(Exception):
    pass


class More(Error):
    pass


class Less(Error):
    pass


def _less(number):
    if number >= 10:
        return True
    raise Less


def _more(number):
    if number <= 20:
        return True
    raise More


while True:
    try:
        a = int(input("Введите число от 10 до 20\n"))
        if _less(a) and _more(a):
            print("Спасибо")
            break
    except More as e:
        print("Число больше требуемого диапазона")
    except Less:
        print("Число меньше требуемого диапазона")
    except ValueError:
        print("Ошибка ввода")
