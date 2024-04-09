from connect_db import connect_db


def fetch_genres():
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM Genres"
            cursor.execute(query)

            for row in cursor.fetchall():
                print(row)

        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    fetch_genres()


def add_genres():
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            name = ""
            description = ""
            category = ""
            query = (
                "INSERT INTO Genres (name, description, category) VALUES (%s, %s, %s)"
            )

            cursor.execute(query, (name, description, category))
            conn.commit()
            print(f"order was succesfully added for Omen")
        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    add_genres()


def delete_genres():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            name = ""
            description = ""
            category = ""
            query = "DELETE FROM Genres WHERE name = %s AND description = %s AND category = %s"

            cursor.execute(query, (name, description, category))
            conn.commit()
            print("Your order was successfully deleted!")

        except Exception as e:
            print(f"and error occurred: {e}")

        finally:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    delete_genres()


def update_genres():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            name = ""
            description = ""
            category = ""
            query = (
                "UPDATE Genres SET category = %s WHERE name = %s AND description = %s"
            )

            cursor.execute(query, (category, name, description))
            conn.commit()
            print("Your order was succesfully updated!")

        except Exception as e:
            print(f"and error occurred: {e}")

        finally:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    update_genres()
