s = input("Введите строку ")
d = {i: s.replace(" ", "").lower().count(i) for i in s.replace(" ", "").lower()
     if s.replace(" ", "").lower().count(i) == 1}
print(d)
