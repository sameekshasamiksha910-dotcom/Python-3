class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def register_patron(self, patron):
        self.patrons.append(patron)

    def issue_book(self, book, patron):
        if book.available:
            book.available = False
            patron.borrowed_books.append(book)
            print("Book issued successfully")
        else:
            print("Book is not available")

    def return_book(self, book, patron):
        if book in patron.borrowed_books:
            book.available = True
            patron.borrowed_books.remove(book)
            print("Book returned successfully")



library = Library()

book = Book("Python Basics", "John Smith")
patron = Patron("Sam")

library.add_book(book)
library.register_patron(patron)

library.issue_book(book, patron)
library.return_book(book, patron)