import csv


def years_range() -> tuple:
    check = True
    while check:
        _range = input('Введите промежуток ГГГГ-ГГГГ ').split('-')

        try:
            if len(_range) != 2 or _range[0] > _range[1]:
                raise ValueError
            _range = tuple(map(int, _range))
            check = False
        except ValueError:
            print('Некорректный ввод')

    return _range


def search_in_yrange(lib: str, start: int, end: int) -> list:
    found_books = []

    with open(lib) as file:
        books = list(csv.DictReader(file, delimiter=';'))

    for book in books:
        if start <= int(book['Release date']) <= end:
            found_books.append(book)

    return found_books


file = 'books.csv'

yrange = years_range()
found_books = search_in_yrange(file, yrange[0], yrange[1])

if len(found_books) == 0:
    print('Книг за данные года не найдено')
else:
    print('Found books:')
    for i in found_books:
        print("Название: {} | Автор: {} | Дата выхода: {}".format(*i.values()))
