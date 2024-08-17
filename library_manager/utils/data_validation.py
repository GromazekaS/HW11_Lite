def validate_book_data(data: dict) -> bool:
    """Проверяет, что данные книги корректны."""
    required_fields = ['title', 'author', 'genre']
    for field in required_fields:
        if field not in data or not isinstance(data[field], str) or not data[field].strip():
            return False
    return True
