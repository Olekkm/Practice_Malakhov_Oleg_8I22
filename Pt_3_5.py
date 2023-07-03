def sl(x):
    for i in range(2, int(abs(x) ** 0.5) + 1):
        if x % i == 0:
            return True
    return False


arr = [x for x in range(int(input("Начальное значение ")),
                        int(input("Конечное значение ")) + 1) if sl(x)]
print(arr)
