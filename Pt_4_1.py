a = [int(i) for i in input("Введите число ")]
a.sort(reverse=True)
a = int(''.join(map(str, a)))
print(f"Максимальное число из данного набора: {a}")
