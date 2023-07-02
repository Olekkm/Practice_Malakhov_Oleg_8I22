def armstrongnum(x):
    xstr = str(x)
    n = len(xstr)
    _sum = 0
    for i in xstr:
        _sum += int(i) ** n
    if _sum == x:
        return True
    return False


while True:
    try:
        a = int(input("Введите натуральное число "))
        if a < 0:
            raise ValueError
        elif armstrongnum(a):
            print(f"Число {a} является числом армрстронга\n")
        else:
            print(f"Число {a} не является числом армрстронга\n")
    except ValueError:
        print("Где-то ошибка наверное\n")
