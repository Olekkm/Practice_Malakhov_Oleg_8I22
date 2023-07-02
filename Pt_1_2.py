while True:
    s = input("Введите имя ")
    s += " " + input("Введите фамилию ")
    if len(s.replace(" ", "")) < 1:
        print("Длина имени 0?\n")
    elif not s.replace(" ", "").isalpha():
        print("Не должно быть цифр в имени\n")
    else:
        print(f"Ваше имя {s}\nДлина полученной строки {len(s)}")
        break
