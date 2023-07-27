print("Введите три числа")
while True:
    try:
        array = [int(input()) for i in range(3)]
        array.sort(reverse=True)
        print(f"Наибольшее число: {max(array)}\n{array}")
    except ValueError:
        print("Некоректное значение")
