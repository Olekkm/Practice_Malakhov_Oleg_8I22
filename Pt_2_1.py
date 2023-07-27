from random import randint as r

a = {"Фиолетовый": "подсказка фио*етовый", "Желтый": "подсказка ж*лтый", "Синий": "Подсказка с*ний",
     "Зеленый": "подсказка зелен*й", "Оранжевый": "подсказка о*анжевый"}
arr = str(a.keys())[11:-2].replace("'", "").split(", ")

print("Варианты:")
for i in arr:
    print(i)

ccolor = arr[r(0, len(arr) - 1)]
color = input("\nВыберите цвет ").capitalize()
while color != ccolor:
    print(a[ccolor])
    color = input("\nВыберите цвет ").capitalize()
else:
    print("Отлично!")
