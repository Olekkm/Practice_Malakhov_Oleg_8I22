def simple(x):
    x = abs(x)
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def _simple(i, j):  # Метод Решета Эратосфена (не подходит если есть и отрицательные числа)
    a = [x for x in range(i, j + 1)]
    a.remove(0), a.remove(1)
    for x in a:
        for h in a:
            if h % x == 0 and h != x:
                a.remove(h)
    return a


arr = []
for i in range(int(input("Введите начальное значение ")), int(input("Введите конечное значение ")) + 1):
    if simple(i):
        arr.append(i)
print(arr)
