from library_manager import *


def main():
# Создание библиотеки
    library = Library()

# Добавление книг
    library.add_book({'title': 'Book1', 'author': 'Author1', 'genre': 'Fiction'})
    library.add_book({'title': 'Book2', 'author': 'Author2', 'genre': 'Non-Fiction'})
    library.view_all_books()

# Удаление книги
    library.remove_book('Book1')

# Поиск книг
    print(library.search_by_author('Author2'))

# Генерация отчета
    report = generate_report(library)
    print(report)


if __name__ == main():
    main()
