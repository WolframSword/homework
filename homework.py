class Library:
    """Библиотека"""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """
        Добавить книгу

        :param book: Книга
        """
        self.add_books(book)

    @property
    def books(self):
        return self._books
    
class Book:
    """Книга"""
    
    def __init__(self, title, author, book_id):
        self.title = title #название
        self.author = author #автор
        self.book_id = book_id #идентификатор книги

    def __str__(self):
        return f'Книга: {self.title}, Автор: {self.author}, ID: {book_id}'

class Rack:
    """Полка"""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """
        Добавить книгу

        :param book: Книга
        """
        if len(self.books) < 10:
            self.books.append(book)
        else:
            print(f"На полке отсутствует место под книгу '(book.title)'")

    def __str__(self):
        return ', '.join(str(book) for book in self.books)

class Shelf:
    """Стеллаж"""

    def __init__(self):
        """
        На стеллаже 10 полок

        :param rack: Полка
        """

        self.bookrack = [Rack() for _ in range(10)]
    
    def add_book(self, book, shelf_number):
        if 0 <= shelf_number < 10:  
            self.shelves[shelf_number].add_book(book)  
        else:
            print("Неверный номер полки.")
        
    def __str__(self):
        return '\n'.join(f"Полка {i+1}: {str(self.shelves[i])}" for i in range(10))

class Hall:
    """Зал"""
    
    def __init__(self):
        """
        В зале 10 стеллажей

        :param shelf: Стеллаж
        """
        self.bookshelf = [Shelf() for _ in range(10)]





    
