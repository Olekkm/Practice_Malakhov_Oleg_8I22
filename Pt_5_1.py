import csv

books = [
    ('Crime and Punishment', 'Fyodor Dostoevsky', '1866'),
    ('Fight Club', 'Chuck Palahniuk', '1996'),
    ('Fahrenheit 451', 'Ray Bradbury', '1953')
]

with open('books.csv', 'w') as file:
    w = csv.writer(file, delimiter=';')
    w.writerow(('Book', 'Author', 'Release date'))
    w.writerows(books)
