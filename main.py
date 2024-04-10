from book_categories import Book_Categories
from user import User
from author import Author
from book import Book

from genres_db import fetch_genre, add_genres, fetch_genres
from author_db import fetch_authors, add_author, fetch_author
from user_db import fetch_users, add_users, fetch_user

from book_db import fetch_books, fetch_book, add_books, update_books


# books = {}

# book1 = Book_Categories(
#     "The Alchemist",
#     "Paulo Coelho",
#     "9780062315007",
#     "April 25, 2006",
# )
# book2 = Book_Categories(
#     "The Great Gatsby",
#     "F. Scott Fitzgerald",
#     "9780743273565",
#     "September 30, 2004",
# )
# book3 = Book_Categories(
#     "Harry Potter and the Philosopher's Stone",
#     "J.K. Rowling",
#     "9780743273565",
#     "September 30, 2004",
# )


# user1 = User("Tom Cat", 1)
# user2 = User("Jerry Mouse", 2)
# user1.set_borrowed_book(book1)
# user1.set_borrowed_book(book2)


# author1 = Author(
#     "Paulo Coelho",
#     "Paulo Coelho was born in Rio de Janeiro, Brazil, in 1947.",
# )
# author2 = Author("F. Scott Fitzgerald", "F. Scott Fitzgerald was born in 1896.")

# user_list = [user1, user2]
# author_list = [author1, author2]
# books = [book1, book2, book3]


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
        # author = input("Enter the author of the book: ")
        ISBN = input("Enter the ISBN of the book: ")
        publication_date = input("Enter the publication date of the book: ")
        # book = Book(title, author, ISBN, publication_date)
        add_books(title, ISBN, publication_date, True)

    elif choice == 2:
        book_title = input("Enter the title of the book you want to borrow: ")
        book_info = fetch_book(book_title)
        if book_info is not None:
            id, title, author_id, genre_id, isbn, publication_date, availability = (
                book_info[0]
            )
            if availability:
                update_books(title, False)
                print(f"You have borrowed '{title}'. Enjoy your reading!")
            else:
                print("Sorry, the book is currently not available.")
        else:
            print(
                "Book not found in the library. Please check the title and try again."
            )

    elif choice == 3:
        book = input("Enter the title of the book you want to return: ")
        book_info = fetch_book(book)
        if book_info is not None:
            id, title, author_id, genere_id, isbn, publication_date, availability = (
                book_info[0]
            )
            if not availability:
                update_books(title, True)
                print(f"Thank you for returning '{title}'.")
            else:
                print("The book is already available in the library.")
        else:
            print(
                "Book not found in the library. Please check the title and try again."
            )

    elif choice == 4:
        book = input("Enter the title of the book you want to search for: ")
        main_book = fetch_book(book)
        if main_book is not None:
            print(main_book[0])
        else:
            print(
                "Book not found in the library. Please check the title and try again."
            )

    elif choice == 5:
        fetch_books()

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
        count = 1
        library_id = f"LIB{count}"
        count += 1
        name = input("Enter the name of the user: ")
        add_users(name, library_id)
    elif choice == 2:
        user = input("Enter the user you want to search for: ")
        fetch_user(user)
    elif choice == 3:
        fetch_users()
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
        add_author(name, biography)
    elif choice == 2:
        author = input("Enter the author you want to search for: ")
        fetch_author(author)
    elif choice == 3:
        fetch_authors()
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
        name = input("Enter the name of the book: ")
        description = input("Enter the description of the book: ")
        category = input("Enter the genre of the book: ")
        add_genres(name, description, category)
    elif choice == 2:
        genre = input("Enter the genre you want to search for: ")
        fetch_genre(genre)
    elif choice == 3:
        fetch_genres()


# Main functionality
print("\nWelcome to the Library Management System!")
while True:
    print(
        "\nMain Menu\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Genre Operations\n5. Quit"
    )
    choice = handle_choice()
    if choice == 1:
        book_operations()
    elif choice == 2:
        user_operations()
    elif choice == 3:
        author_operations()
    elif choice == 4:
        genre_operations()
    elif choice == 5:
        print("Thank you for using the Library Management System!")
        break
    else:
        print("invalid choice. Please choose a valid option.")
