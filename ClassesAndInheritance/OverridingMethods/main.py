class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '"{}" by {}'.format(self.title, self.author)


class PaperBook(Book):
    def __init__(self, title, author, num_pages):
        Book.__init__(self, title, author)
        self.num_pages = num_pages


class EBook(Book):
    def __init__(self, title, author, file_size):
        Book.__init__(self, title, author)
        self.file_size = file_size


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_num_books(self):
        return len(self.books)


my_book = EBook('The Odyssey', 'Homer', 2)
my_paper_book = PaperBook('The Odyssey', 'Homer', 500)

print(my_book)
print(my_book.file_size)

print(my_paper_book)
print(my_paper_book.num_pages)

aadl = Library()
aadl.add_book(my_book)
aadl.add_book(my_paper_book)

print(aadl.get_num_books())

