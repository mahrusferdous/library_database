from connect_db import connect_db


def fetch_books():
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM Books"
            cursor.execute(query)

            for row in cursor.fetchall():
                print(row)

        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


fetch_books()


def add_books():
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            title = ""
            author_id = 1
            genre_id = 3
            isbn = ""
            publication_date = "2022-03-15"
            availability = True
            query = "INSERT INTO Books (title, author_id, genre_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s, %s)"

            cursor.execute(
                query,
                (title, author_id, genre_id, isbn, publication_date, availability),
            )
            conn.commit()
            print(f"order was succesfully added for Omen")
        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


# add_books()


def delete_books():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            title = ""
            author_id = ""
            genre_id = ""
            isbn = ""
            publication_date = "2022-03-15"
            availability = ""
            query = "DELETE FROM Books WHERE title = %s AND author_id = %s AND genre_id = %s AND isbn = %s AND publication_date = %s AND availability = %s"

            cursor.execute(
                query,
                (title, author_id, genre_id, isbn, publication_date, availability),
            )
            conn.commit()
            print("Your order was successfully deleted!")

        except Exception as e:
            print(f"and error occurred: {e}")

        finally:
            cursor.close()
            conn.close()


delete_books()


def update_books():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            title = ""
            author_id = ""
            genre_id = ""
            isbn = ""
            publication_date = "2022-03-15"
            availability = ""
            query = "UPDATE Books SET availability = %s WHERE title = %s AND author_id = %s AND genre_id = %s AND isbn = %s AND publication_date = %s"

            cursor.execute(
                query,
                (availability, title, author_id, genre_id, isbn, publication_date),
            )
            conn.commit()
            print("Your order was succesfully updated!")

        except Exception as e:
            print(f"and error occurred: {e}")

        finally:
            cursor.close()
            conn.close()


update_books()
