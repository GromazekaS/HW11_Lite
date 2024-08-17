from .utils import format_book_data


def generate_report(self):
    """Генерирует отчет по всем книгам в библиотеке."""
    report = ""
    for book in self.books:
        report += format_book_data(book) + "\n"
    return report.strip()
