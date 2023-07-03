gl = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
st = input("Введите строку ")
d = {x: True if x in gl else False for x in st.replace(" ", "").lower()}
print(d)
