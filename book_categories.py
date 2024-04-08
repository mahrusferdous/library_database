from book import Book


class Book_Categories(Book):
    def __init__(self, title, author, ISBN, genre, publication_date):
        super().__init__(title, author, ISBN, genre, publication_date)
        self.categories = "n/a"

    def choose_category(self):
        print("1. Fiction\n2. Non-fiction\n3. Mystery\n")
        try:
            category = int(input("Choose a category by picking a number: "))
        except ValueError:
            print("Invalid choice. Please choose a valid category.")
            return
        except Exception as e:
            print(e)
            return

        if category == 1:
            self.categories = "Fiction"
        elif category == 2:
            self.categories = "Non-fiction"
        elif category == 3:
            self.categories = "Mystery"
        else:
            print("Invalid choice. Please choose a valid category.")
            return

    def get_categories(self):
        return self.categories
