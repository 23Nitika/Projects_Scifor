class Book:
    def __init__(self, book_id, title, price):
        self.book_id = book_id
        self.title = title
        self.price = price

class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, price):
        book = Book(book_id, title, price)
        self.books.append(book)
        print("Book added successfully. ")
    
    def get_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None
    
    def get_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def get_book_by_price(self, price):
        for book in self.books:
            if book.price == price:
                return book
        return None 
    
    def show_all_books(self):
        if not self.books:
            print("No book available. ")
        else:
            print("Books available in the store: ")
            for book in self.books:
                print(f"ID: {book.book_id}, Title: {book.title}, Price: {book.price}")
    
    def delete_book(self, identifier):
        deleted = False
        for i, book in enumerate(self.books):
            if book.book_id == identifier or book.title == identifier or book.price == identifier:
                del self.books[i]
                print("Book deleted successfully. ")
                deleted = True
                break
        if not deleted:
            print("Book not found. ")

def main():
    bookstore = Bookstore()

    while True:
        print("\n Options:")
        print("1. Add a book")
        print("2. Get a book by ID")
        print("3. Get a book by title")
        print("4. Get a book by price")
        print("5. Show all books")
        print("6. Delete a book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            price = input("Enter book price: ")
            bookstore.add_book(book_id, title, price)
        elif choice == '2':
            book_id = input("Enter book ID: ")
            book = bookstore.get_book_by_id(book_id)
            if book:
                print(f"Book found - Title: {book.title}, Price: {book.price}")
            else:
                print("Book not found.")
        elif choice == '3':
             title = input("Enter book title: ")
             book = bookstore.get_book_by_title(title)
             if book:
                 print(f"Book found - ID: {book.book_id}, Price: {book.price}")
             else:
                 print("Book not found. ")
        elif choice == '4':
            bookstore.show_all_books()
        elif choice == '6':
            identifier = input("Enter book ID, title, or price to delete: ")
            bookstore.delete_book(identifier)
        elif choice == '7':
            print("Exited")
            break
        else:
            print("Invalid choice. Please choose again. ")

if __name__ == "__main__":
    main()


