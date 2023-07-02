def ArmstrongNum(x):
    xstr = str(x)
    n = len(xstr)
    sum = 0
    for i in xstr:
        sum += int(i) ** n
    if sum == x:
        return True
    return False


while True:
    try:
        a = int(input("Введите натуральное число "))
        if a < 0:
            raise ValueError
        elif ArmstrongNum(a):
            print(f"Число {a} является числом армрстронга\n")
        else:
            print(f"Число {a} не является числом армрстронга\n")
    except ValueError:
        print("Где-то ошибка наверное¯\_(ツ)_/¯\n")
