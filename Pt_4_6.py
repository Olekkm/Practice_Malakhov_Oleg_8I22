abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

text = input("Введите строку: ")
rot13 = ''.join(
    [abc[(abc.find(i) + 13) % 33] if i.islower() else abc[(abc.find(i.lower()) + 13) % 33].capitalize() for i in text])
print(rot13)
