class Book:
    def read(self):
        print("Reading a book 📖")

class Magazine:
    def read(self):
        print("Flipping through a magazine 📰")

class Newspaper:
    def read(self):
        print("Catching up with the news 🗞️")

# Polymorphism in action
publications = [Book(), Magazine(), Newspaper()]

for p in publications:
    p.read()

