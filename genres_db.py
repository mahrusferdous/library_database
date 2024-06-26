from connect_db import connect_db


def fetch_genre(name=""):
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM Genres WHERE name = %s"
            cursor.execute(query, (name,))

            print(cursor.fetchall())

        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


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


def add_genres(name="", description="", category=""):
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = (
                "INSERT INTO Genres (name, description, category) VALUES (%s, %s, %s)"
            )

            cursor.execute(query, (name, description, category))
            conn.commit()
            print(f"Succesfully added for Genres")
        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


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
            print("Successfully deleted!")

        except Exception as e:
            print(f"and error occurred: {e}")

        finally:
            cursor.close()
            conn.close()


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
            print("Succesfully updated!")

        except Exception as e:
            print(f"and error occurred: {e}")

        finally:
            cursor.close()
            conn.close()
