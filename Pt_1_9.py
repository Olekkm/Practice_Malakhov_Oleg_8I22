while True:
    try:
        a = int(input("a "))
        b = int(input("b "))
        print(f"{a} x {b} = {a * b}\n")
    except ValueError:
        pass
