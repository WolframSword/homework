class Library:
    """Библиотека"""

    def __init__(self):
        self._hall = []

    def add_hall(self, name):
        """
        Добавить книгу

        :param name: Название
        """
        self.hall.append(Hall(name))

    @property
    def hall(self):
        return self._hall
    
    # def add_book(self, name, shelf_number, rack_number):
    #     for i in self.hall:
    #         if i.name == name:
    #             for j in i.bookshelf:
    #                 if j.shelf_number == shelf_number:
    #                     for k in k.bookrack:
    #                         if k.rack_number == rack_number:
                               
                        
    
class Book:
    """Книга"""
    
    def __init__(self, title, author, book_id):
        self.title = title #название
        self.author = author #автор
        self.book_id = book_id #идентификатор книги

    def __str__(self):
        return f'Книга: {self.title}, Автор: {self.author}, ID: {self.book_id}'

class Rack:
    """Полка"""

    def __init__(self, rack_number):
        self.rack_number = rack_number
        self.books = []

    def add_book(self, book):
        """
        Добавить книгу

        :param book: Книга
        """
        if len(self.books) < 10:
            self.books.append(book)
        else:
            print(f"На полке отсутствует место под книгу: {book.title}")

    def __str__(self):
        return ', '.join(str(book) for book in self.books)
    
    def remove_book(self, book_id):
        """
        Удалить книгу

        :param book: Книга
        """
        for i in self.books:
            if i.book_id == book_id:
                self.books.remove(i)


class Shelf:
    """Стеллаж"""

    def __init__(self, shelf_number):
        """
        На стеллаже 10 полок

        :param rack: Полка
        """
        self.shelf_number = shelf_number
        self.bookrack = [Rack(i) for i in range(10)]
    
class Hall:
    """Зал"""
    
    def __init__(self, name):
        """
        В зале 10 стеллажей

        :param shelf: Стеллаж
        """
        self.name = name
        self.bookshelf = [Shelf(i) for i in range(10)]