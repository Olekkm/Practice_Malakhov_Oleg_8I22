count = 0

while True:
    try:
        a = int(input())
        if a >= 0:
            break
        count += a
    except ValueError:
        print("Ошибка ввода")
print(f"Итог суммы {count}")
