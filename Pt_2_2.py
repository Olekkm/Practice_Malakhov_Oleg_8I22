a = ["новости" + str(i) for i in range(1, 6)]
for i in a:
    print(i)
try:
    a.insert(int(input("\nПоставить на позицию ")) - 1, input("Передачу "))
    print("\n")
    for i in a:
        print(i)
except ValueError:
    print("Где-то ошибка наверное")
