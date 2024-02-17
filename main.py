import sys

class Library:
    def __init__(self, filename = "books.txt"):
        self.filename = filename
        self.file = open(self.filename, "a+")
        
    def __del__(self):
        self.file.close()

    def listBooks(self):
        with open(self.filename) as books: bookList = books.read().splitlines()
        for book in bookList:
            bookInfo = book.split(",")
            print(f"Book Title: {bookInfo[0]}, Author: {bookInfo[1]}" )

    def addBook(self):
        title = input("Enter the book title: ").title()
        author = input("Enter the author of the book: ").title()

        while True:
            releaseYear = input("Enter the release year of the book: ")
            try:
                value = int(releaseYear)
                break
            except ValueError:
                print("The release year has to be a number.")
        while True:
            numberPages = input("Enter the number of pages: ")
            try:
                value = int(numberPages)
                break
            except ValueError:
                print("The number of pages has to be a number.") 

        bookInfo = f"{title}, {author}, {releaseYear}, {numberPages}\n"
        self.file.write(bookInfo)

    def removeBook(self):
        while True:
            removeThisBook = input("Enter the title of the book you want to remove: ").title()
            self.file.seek(0)
            books = self.file.read().splitlines()
            bookInfo = [book.split(",") for book in books]
            titles = [book[0] for book in bookInfo]
            if removeThisBook in titles:           
                updatedBooks = [book for book in books if removeThisBook != book.split(",")[0].title()]
                self.file.seek(0)
                self.file.truncate()
                for book in updatedBooks:
                    self.file.write(book + "\n")
                break
            else:
                print("There is no book of that title.Enter a title that is in books.txt")

while True:
    lib = Library()
    print("\n*** MENU*** ")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")

    choice = input("What is your choice? ")
    print("")
    if choice == "1":
        lib.listBooks()
    elif choice == "2":
        lib.addBook()
    elif choice == "3":
        lib.removeBook()
    elif choice == "q": 
        sys.exit(0)
    else: print("Invalid choice.Choose from the options.")