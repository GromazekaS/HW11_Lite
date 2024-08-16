from .utils import validate_book_data


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_data):
        """Добавляет книгу в библиотеку после валидации."""
        if validate_book_data(book_data):
            self.books.append(book_data)
        else:
            raise ValueError("Некорректные данные книги")

    def remove_book(self, title):
        """Удаляет книгу по названию."""
        self.books = [book for book in self.books if book['title'] != title]

    def search_by_title(self, title):
        """Ищет книги по названию."""
        return [book for book in self.books if book['title'].lower() == title.lower()]

    def search_by_author(self, author):
        """Ищет книги по автору."""
        return [book for book in self.books if book['author'].lower() == author.lower()]

    def search_by_genre(self, genre):
        """Ищет книги по жанру."""
        return [book for book in self.books if book['genre'].lower() == genre.lower()]

    def view_all_books(self):
        """Возвращает все книги в библиотеке."""
        return self.books