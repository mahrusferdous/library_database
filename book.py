class Book:
    def __init__(self, title, author, ISBN, publication_date):
        self.__title = title
        self.__author = author
        self.__ISBN = ISBN
        self.__publication_date = publication_date
        self.__availability = True

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_ISBN(self):
        return self.__ISBN

    def set_ISBN(self, ISBN):
        self.__ISBN = ISBN

    # def get_genre(self):
    #     return self.__genre

    # def set_genre(self, genre):
    #     self.__genre = genre

    def get_publication_date(self):
        return self.__publication_date

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def get_availability(self):
        return self.get_availability

    def return_book(self):
        self.__availability = True

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
