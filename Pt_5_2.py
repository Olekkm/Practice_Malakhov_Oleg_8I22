import csv


def extend_library(file_name: str):
    n = int(input('сколько записей лобавить в список? '))
    if n < 1:
        return
    books = []

    print("Введите данные (Книга; автор; год выхода)")
    c = 0
    while c != n:
        entry = input(f'{c + 1}. ').split('; ')
        if len(entry) != 3 or entry[2] == '':
            print("Некоректный ввод")
        else:
            books.append(entry)
            c += 1

    with open(file_name, 'a') as file:
        w = csv.writer(file, delimiter=';')
        w.writerows(books)


def find_books(library: str, author: str) -> list:
    found = []

    with open(library) as file:
        books = list(csv.DictReader(file, delimiter=';'))
    for i in books:
        if i['Author'] == author:
            found.append(i)

    return found


file = 'books.csv'
try:
    extend_library(file)
except ValueError:
    print("Ошибка ввода")

author = input('Введите имя автора для поиска: ')
result = find_books(file, author)
# If no book was found
if len(result) == 0:
    print('Книг этого автора не найдено')
else:
    print(f'{author}:')
    for i in result:
        print(f'Название: {i["Book"]} | Дата выхода: {i["Release date"]}')
