try:
    print(f"Привет {input('Введите имя ')}! Тебе уже {int(input('Введите возраст '))} лет")
except ValueError:
    print("Ошибка ввода")
