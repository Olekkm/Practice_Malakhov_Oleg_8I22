while True:
    s = input("Введите имя ")
    if len(s) < 1:
        print("Длина имени 0?\n")
    elif not s.isalpha():
        print("Не должно быть цифр в имени\n")
    else:
        print(len(s))
        break
