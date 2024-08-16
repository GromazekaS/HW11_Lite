from .utils import format_book_data


def generate_report(library):
    """Генерирует отчет по всем книгам в библиотеке."""
    report = ""
    for book in library.view_all_books():
        report += format_book_data(book) + "\n"
    return report.strip()
