class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.borrowed_book = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_library_id(self):
        return self.__library_id

    def set_library_id(self, library_id):
        self.__library_id = library_id

    def set_borrowed_book(self, borrowed_book):
        self.borrowed_book.append(borrowed_book)

    def get_borrowed_book(self):
        return self.borrowed_book

    def remove_borrowed_book(self, borrowed_book):
        self.borrowed_book.remove(borrowed_book)

    def display_borrowed_books(self):
        if len(self.borrowed_book) == 0:
            print(f"No books borrowed. by {self.__name}")
        else:
            for book in self.borrowed_book:
                print(f"{self.__name} borrowed {book.get_title()}")
