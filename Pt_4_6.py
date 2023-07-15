abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

text = input("Введите строку: ")
rot13 = ''.join([abc[(abc.find(i)+13)%33] for i in text])
print(rot13)