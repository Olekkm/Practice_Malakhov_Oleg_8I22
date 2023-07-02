try:
    a = int(input("Введите колличество баллов "))
    if a == 3:
        print("Win")
    elif a == 1:
        print("Tie")
    elif a == 0:
        print("Lose")
    else:
        print("idk")
except ValueError:
    print("Input error")
