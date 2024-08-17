def format_book_data(data: dict) -> str:
    """Форматирует данные книги для отчета."""
    return f"Title: {data['title']}, Author: {data['author']}, Genre: {data['genre']}"
