# Розробити клас з інформацією про КНИГИ домашньої бібліотеки: автор, назва книги, видавництво, рік видання, кількість сторінок.
# Визначити конструктори, методи / властивості встановлення та читання значень полів даних.
# Вивести на екран список книг заданого автора, виданих після 2010 року.

class Book:
    def __init__(self, author, book_name, publishing_house, year_of_publishment, page_qty):
        self.author = author
        self.book_name = book_name
        self.publishing_house = publishing_house
        self.year_of_publishment = year_of_publishment
        self.page_qty = page_qty

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        if not isinstance(author, str):
            raise TypeError('Invalid type')

        if len(author) <= 1:
            raise ValueError('Author name must contain at least 2 characters')

        self.__author = author

    @property
    def book_name(self):
        return self.__book_name

    @book_name.setter
    def book_name(self, book_name):
        if not isinstance(book_name, str):
            raise TypeError('Invalid type')

        if len(book_name) <= 1:
            raise ValueError('Book name must contain at least 2 characters')

        self.__book_name = book_name

    @property
    def publishing_house(self):
        return self.__publishing_house

    @publishing_house.setter
    def publishing_house(self, publishing_house):
        if not isinstance(publishing_house, str):
            raise TypeError('Invalid type')

        if len(publishing_house) <= 1:
            raise ValueError('Publishing house must contain at least 2 characters')

        self.__publishing_house = publishing_house

    @property
    def year_of_publishment(self):
        return self.__year_of_publishment

    @year_of_publishment.setter
    def year_of_publishment(self, year_of_publishment):
        if not isinstance(year_of_publishment, int):
            raise TypeError('Invalid type for year of publishment')

        if year_of_publishment < 0 or year_of_publishment > 2021:
            raise ValueError("Invalid value for year of publishment")

        self.__year_of_publishment = year_of_publishment

    @property
    def page_qty(self):
        return self.__page_qty

    @page_qty.setter
    def page_qty(self, page_qty):
        if not isinstance(page_qty, int):
            raise TypeError('Invalid type for year of page_qty')

        if page_qty < 0:
            raise ValueError("Invalid value for year of page_qty")

        self.__page_qty = page_qty

    def __str__(self):
        return f'Author: {self.author}, book name: {self.book_name}, publishing house: {self.publishing_house}, year of ' \
               f'publishment: {self.year_of_publishment}, page qty: {self.page_qty}\n'


class BooksInLibrary:
    def __init__(self, books=list):
        self.books = books

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, books=list):
        if not isinstance(books, list):
            raise TypeError('Collection of books must be list')
        if not all(isinstance(item, Book) for item in books):
            raise TypeError("Books in collection must be instances of Book class")

        self.__books = books

    def get_books_since_2011(self, author):
        if not isinstance(author, str):
            raise TypeError("Cannot find books of non string author")

        author_books = []
        for book in self.books:
            if author is book.author and book.year_of_publishment > 2010:
                author_books.append(book)

        if not author_books:
            raise ValueError("No books with such author")

        return author_books


b1 = Book("John", "HGRIGHRU", "GEGR", 2012, 2012)
b2 = Book("John", "HGRIGHR3343U", "GEGR", 2013, 2012)
b3 = Book("Robert", "HGRIGHRU", "GEGR", 1997, 2012)
b4 = Book("John", "HGRIGHRUBGG", "GEGBGBR", 1997, 2011)

library = BooksInLibrary([b1, b2, b3, b4])
print("".join(map(str, library.get_books_since_2011("John"))))
