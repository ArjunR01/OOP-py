from datetime import *

class Book:
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies_available = copies
        self.book_id = None

class Patron:
    def __init__(self, name):
        self.name = name
        self.books_checked_out = []
        self.time=None
        self.patron_id = None

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title, author, year, copies):
        book = Book(title, author, year, copies)
        book.book_id = len(self.books) + 1
        self.books.append(book)


    def add_patron(self, name):
        patron = Patron(name)
        patron.patron_id = len(self.patrons) + 1
        self.patrons.append(patron)


    def check_out_book(self, patron_id, book_id):          
        patron = self.patrons[patron_id - 1]
        book = self.books[book_id - 1]


        if book.copies_available > 0:
            patron.books_checked_out.append(book_id)
            book.copies_available -= 1
            patron.time=datetime.now()
            print(f"Book '{book.title}' checked out by patron '{patron.name}' at {patron.time}.")
        else:
            print(f"Book '{book.title}' is not available.")



    def check_in_book(self, patron_id, book_id):          
        patron = self.patrons[patron_id - 1]
        book = self.books[book_id - 1]

        patron.books_checked_out.pop()
        book.copies_available += 1
        patron.time=datetime.now()
        print(f"Book '{book.title}' checked in by patron '{patron.name}' at {patron.time}.")

    def display_books(self):
        print("\nBooks in the library:\n")
        for book in self.books:
            print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Copies available: {book.copies_available}")

    def display_patrons(self):
        print("\nPatrons in the library:\n")
        for patron in self.patrons:
            print(f"Patron ID: {patron.patron_id}, Name: {patron.name}, Books checked out: {len(patron.books_checked_out)} recent checked out time is {patron.time}.")


def main():
    library = Library()
    while(1):
        n=int(input("\n1.Add books to library\n2.Add Patron or student details\n3.Display the books available in library\n4.Display the patrons\n5.Check out a book\n6.Check in a book\nPress '0' to exit\nENter your choice to proceed="))
        match(n):
         case 1:
            name=input("Enter the name of the book you want to add=")
            author=input(f"Enter the name of the author of book {name}=")
            year=int(input("Enter the Publish year of the book="))
            copies=int(input("Enter the number of copies available="))
            library.add_book(name,author,year,copies)
         case 2:
            student_name=input("Enter the student name=")
            library.add_patron(student_name)
         case 3:
            library.display_books()
         case 4:
            library.display_patrons()
         case 5:
            student_id=int(input("Enter the student ID to proceed="))
            book_id=int(input("Enter the book ID to proceed="))
            library.check_out_book(student_id,book_id)

         case 6:
             student_id=int(input("Enter the student ID to proceed="))
             book_id=int(input("Enter the book ID to proceed="))
             library.check_in_book(student_id,book_id)
                     
            
         case _:
                exit()

    

if __name__ == "__main__":
    main()