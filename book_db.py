from connect_db import connect_db


def fetch_book(name):
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM Books WHERE title = %s"
            cursor.execute(query, (name,))

            # print(cursor.fetchall())
            return cursor.fetchall()

        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


def fetch_books():
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = "SELECT b.*, bb.borrow_date, bb.return_date FROM books b JOIN borrowed_books bb ON b.id = bb.book_id"
            cursor.execute(query)

            for row in cursor.fetchall():
                print(row)

        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


def add_books(title, isbn, publication_date, availability):
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = "INSERT INTO Books (title, isbn, publication_date, availability) VALUES (%s, %s, %s, %s)"

            cursor.execute(
                query,
                (title, isbn, publication_date, availability),
            )
            conn.commit()
        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


# def delete_books():
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()

#             title = ""
#             author_id = ""
#             genre_id = ""
#             isbn = ""
#             publication_date = "2022-03-15"
#             availability = ""
#             query = "DELETE FROM Books WHERE title = %s AND author_id = %s AND genre_id = %s AND isbn = %s AND publication_date = %s AND availability = %s"

#             cursor.execute(
#                 query,
#                 (title, author_id, genre_id, isbn, publication_date, availability),
#             )
#             conn.commit()
#             print("Your order was successfully deleted!")

#         except Exception as e:
#             print(f"and error occurred: {e}")

#         finally:
#             cursor.close()
#             conn.close()


def update_books(title, availability):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            query = "UPDATE Books SET availability = %s WHERE title = %s"
            cursor.execute(
                query,
                (availability, title),
            )
            conn.commit()

        except Exception as e:
            print(f"and error occurred: {e}")

        finally:
            cursor.close()
            conn.close()
