# 4.Library Management System
# Description:
# Develop a Library Management System that includes multiple classes and
# relationships to represent the various entities within a library.
# It should include:
#
# Book Class: Holds details about individual books, including title, author, ISBN, availability status, etc.
#
# User Class: Represents library users (members) with information like name, member ID, current checkouts, etc.
#
# Librarian Class: A subclass of the user with additional privileges such as adding books, managing users, etc.
#
# Transaction Class: Represents a transaction in the library, such as checking out or returning a book.
# Includes details about the user, book, transaction type, date, etc.
#
# Library Class: The main class that combines all the others, containing lists of books, users, and librarians.
# It should have methods to perform various library tasks like searching books,
# checking out books, returning books, managing users, etc.

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.librarians = []
        self.transactions = []

    def search_book(self, isbn):
        for book in self.books:
            if book.get_isbn() == isbn:
                return book
            else:
                return None

    def add_book(self, book):
        self.books.append(book)

    def checkout_book(self, user, book):
        if book is None:
            exit()
        elif book.get_availability():
            transaction = Transaction(user, book, "checkout")
            self.transactions.append(transaction)
            book.set_availability()
            user.increment_checkouts()
            return f"{user.name} has checked out {book.get_title()}"
        else:
            return f"{book.get_title()} is unavailable for checkout!"

    def return_book(self, user, book):
        if book is None:
            exit()
        elif not book.get_availability():
            transaction = Transaction(user, book, "return")
            self.transactions.append(transaction)
            book.set_availability()
            user.decrement_checkouts()
            return f"{user.name} has returned {book.get_title()}"
        else:
            return f"{book.get_title()} is already in the library"

    def add_user(self, user):
        self.users.append(user)

    def add_librarian(self, employee):
        self.librarians.append(employee)


class Book:
    def __init__(self, title, author, isbn, availability=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_isbn(self):
        return self.isbn

    def get_availability(self):
        return self.availability

    def set_availability(self):
        if self.availability:
            self.availability = False
        else:
            self.availability = True


class User:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.number_of_checkouts = 0

    def increment_checkouts(self):
        self.number_of_checkouts += 1

    def decrement_checkouts(self):
        self.number_of_checkouts -= 1


class Librarian(User):
    def add_book(self, lib, title, author, isbn):
        new_book = Book(title, author, isbn)
        lib.add_book(new_book)
        return f"{self.name} has added {new_book.get_title()} to the library"


class Transaction:
    def __init__(self, user, book, transaction_type):
        self.user = user
        self.book = book
        self.transaction_type = transaction_type


library = Library()
librarian = Librarian("Marry", "10XG4")
library.add_librarian(librarian)

print(librarian.add_book(library, "1984", "George Orwell", "0X0014"))

user1 = User("John", "09XJD")
library.add_user(user1)

required_book = library.search_book("0X0014")
print(library.checkout_book(user1, required_book))

print(library.return_book(user1, required_book))

