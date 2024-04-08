from book_categories import Book_Categories
from user import User
from author import Author
from book import Book

books = {}

book1 = Book_Categories(
    "The Alchemist",
    "Paulo Coelho",
    "9780062315007",
    "April 25, 2006",
)
book2 = Book_Categories(
    "The Great Gatsby",
    "F. Scott Fitzgerald",
    "9780743273565",
    "September 30, 2004",
)
book3 = Book_Categories(
    "Harry Potter and the Philosopher's Stone",
    "J.K. Rowling",
    "9780743273565",
    "September 30, 2004",
)


user1 = User("Tom Cat", 1)
user2 = User("Jerry Mouse", 2)
user1.set_borrowed_book(book1)
user1.set_borrowed_book(book2)


author1 = Author(
    "Paulo Coelho",
    "Paulo Coelho was born in Rio de Janeiro, Brazil, in 1947.",
)
author2 = Author("F. Scott Fitzgerald", "F. Scott Fitzgerald was born in 1896.")

user_list = [user1, user2]
author_list = [author1, author2]
books = [book1, book2, book3]


def handle_choice():
    try:
        choice = int(input("Choose an option: "))
        return choice
    except ValueError:
        print("Invalid choice. Please choose a valid option.")
        return
    except Exception as e:
        print(e)
        return


# Book
def book_operations():
    print(
        "\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books"
    )
    choice = handle_choice()
    if choice == 1:
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        ISBN = input("Enter the ISBN of the book: ")
        publication_date = input("Enter the publication date of the book: ")
        book = Book(title, author, ISBN, publication_date)
        books.append(book)

    elif choice == 2:
        print()
        # Display all books
        for i in range(len(books)):
            if books[i].get_availability():
                print(f"{i+1}. {books[i].get_title()}")
        # Input
        try:
            book_num = int(
                input("Enter the title number of the book you want to borrow: ")
            )
            user_name = input("Enter your name: ")
        except ValueError:
            print("Invalid choice. Please choose a valid option.")
            return
        except Exception as e:
            print(e)
            return

        # if book available
        if books[book_num - 1].get_availability():
            # if user exists
            user = None
            for user_obj in user_list:
                if user_name == user_obj.get_name():
                    user = user_obj
                    break
        # borrow book
        if user:
            user.set_borrowed_book(books[book_num - 1])
            books[book_num - 1].borrow_book()
    elif choice == 3:
        print()
        try:

            in_book = input("Enter the title of the book you want to return: ")
            user_name = input("Enter your name: ")
            user = None
            for user_obj in user_list:
                if user_name == user_obj.get_name():
                    user = user_obj
                    break

            if user:
                for borrowed_book in user.get_borrowed_book():
                    if borrowed_book.get_title() == in_book:
                        user.remove_borrowed_book(borrowed_book)
                        borrowed_book.return_book()
                        break

        except Exception as e:
            print(e)
            return

    elif choice == 4:
        book = input("Enter the title of the book you want to search for: ")
        print()
        for i in range(len(books)):
            if book == books[i].get_title():
                print(
                    f"Book title: {books[i].get_title()}\nAuthor: {books[i].get_author()}\nISBN: {books[i].get_ISBN()}\nGenre: {books[i].get_genre()}\nPublication Date: {books[i].get_publication_date()}"
                )
                return
        print("Book not found.")

    elif choice == 5:
        print()
        for i in range(len(books)):
            print(f"{i}. {books[i].get_title()}")
        for book in user_list:
            book.display_borrowed_books()

    else:
        print("Invalid choice. Please choose a valid option.")
        return


# User
def user_operations():
    print(
        "\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users"
    )
    choice = handle_choice()
    if choice == 1:
        library_id = 0
        name = input("Enter the name of the user: ")
        library_id += 1
        user = User(name, library_id)
        user_list.append(user)
    elif choice == 2:
        for user in user_list:
            user.display_borrowed_books()
    elif choice == 3:
        for i in range(len(user_list)):
            print(f"{i+1}. {user_list[i].get_name()}")
    else:
        print("Invalid choice. Please choose a valid option.")
        return


# Author
def author_operations():
    print(
        "\nsAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors"
    )
    choice = handle_choice()
    if choice == 1:
        name = input("Enter the name of the user: ")
        biography = input("Write a little bit about the author: ")
        author = Author(name, biography)
        author_list.append(author)
    elif choice == 2:
        for author in author_list:
            print(
                f"Author's name is {author.get_name()} and Biography: {author.get_biography()}"
            )
    elif choice == 3:
        for i in range(len(author_list)):
            print(f"{i+1}. {author_list[i].get_name()}")
    else:
        print("Invalid choice. Please choose a valid option.")
        return


# Genre
def genre_operations():
    print(
        "\nGenre Operations:\n1. Add a new genre\n2. View genre details\n3. Display all genres"
    )
    choice = handle_choice()
    if choice == 1:
        title = input("Enter the title of the book you want to choose a category for: ")
        for book in books:
            if book.get_title() == title:
                book.choose_category()
    elif choice == 2:
        genre = input("Enter the genre you want to search for: ")
        for book in books:
            if book.get_categories() == genre:
                print(
                    f"Book title: {book.get_title()}\nAuthor: {book.get_author()}\nISBN: {book.get_ISBN()}\nGenre: {book.get_categories()}\nPublication Date: {book.get_publication_date()}"
                )
    elif choice == 3:
        for book in books:
            print(
                f"Book title: {book.get_title()}\nAuthor: {book.get_author()}\nISBN: {book.get_ISBN()}\nGenre: {book.get_categories()}\nPublication Date: {book.get_publication_date()}"
            )


# Main functionality
print("\nWelcome to the Library Management System!")
while True:
    print(
        "\nMain Menu\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit"
    )
    choice = handle_choice()
    if choice == 1:
        book_operations()
    elif choice == 2:
        user_operations()
    elif choice == 3:
        author_operations()
    elif choice == 4:
        pass
    elif choice == 5:
        print("Thank you for using the Library Management System!")
        break
    else:
        print("invalid choice. Please choose a valid option.")
