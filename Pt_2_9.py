def f(n):
    _max = -1
    q = count = 0
    n = str(n)
    for i in n:
        count += 1
        if _max < int(i):
            _max = int(i)
            q = count
    return q


try:
    s = int(input())
    print(f"Номер от начала: {f(s)}\nНомер от конца {len(str(s)) - f(s) + 1}")
except ValueError:
    print("Ошибка ввода")
