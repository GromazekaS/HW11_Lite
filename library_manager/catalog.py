from .utils import validate_book_data


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_data: dict):
        """Добавляет книгу в библиотеку после валидации."""
        if validate_book_data(book_data):
            self.books.append(book_data)
        else:
            raise ValueError("Некорректные данные книги")

    def remove_book(self, title: str):
        """Удаляет книгу по названию."""
        self.books = [book for book in self.books if book['title'] != title]

    def search_by_title(self, title: str) -> list:
        """Ищет книги по названию."""
        return [book for book in self.books if book['title'].lower() == title.lower()]

    def search_by_author(self, author: str) -> list:
        """Ищет книги по автору."""
        return [book for book in self.books if book['author'].lower() == author.lower()]

    def search_by_genre(self, genre: str) -> list:
        """Ищет книги по жанру."""
        return [book for book in self.books if book['genre'].lower() == genre.lower()]

    def view_all_books(self):
        """Возвращает все книги в библиотеке."""
        for item in self.books:
            print(item)
