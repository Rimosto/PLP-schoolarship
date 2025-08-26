# Parent Class
class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f"'{self.title}' by {self.author}"
    

# Child Class inheriting from Publication
class Book(Publication):
    def __init__(self, title, author, pages, genre):
        super().__init__(title, author)  # call parent constructor
        self.pages = pages
        self.genre = genre
        self.__is_borrowed = False  # encapsulated attribute

    def borrow(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return f"You borrowed {self.title} 📖"
        return f"{self.title} is already borrowed ❌"

    def return_book(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            return f"You returned {self.title} ✅"
        return f"{self.title} was not borrowed ❌"

    def book_info(self):
        return f"{self.info()} | {self.pages} pages | Genre: {self.genre}"
    

# Example Usage
b1 = Book("Python Mastery", "Patrick Rimosto", 350, "Programming")
print(b1.book_info())  
print(b1.borrow())      
print(b1.borrow())      # second time borrowing should fail
print(b1.return_book())

