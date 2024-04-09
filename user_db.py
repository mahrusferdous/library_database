from connect_db import connect_db


def fetch_user(name):
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM Users WHERE name = %s"
            cursor.execute(query, (name,))

            for row in cursor.fetchall():
                print(row)

        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


def fetch_users():
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM Users"
            cursor.execute(query)

            for row in cursor.fetchall():
                print(row)

        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


def add_users(name, library_id):
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = "INSERT INTO Users (name, library_id) VALUES (%s, %s)"

            cursor.execute(query, (name, library_id))
            conn.commit()
            print(f"order was succesfully added for Omen")
        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


def delete_users():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            name = ""
            library_id = ""
            query = "DELETE FROM Users WHERE name = %s AND library_id = %s"

            cursor.execute(query, (name, library_id))
            conn.commit()
            print("Your order was successfully deleted!")

        except Exception as e:
            print(f"and error occurred: {e}")

        finally:
            cursor.close()
            conn.close()


def update_users():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            name = ""
            library_id = ""
            query = "UPDATE Users SET name = %s WHERE library_id = %s"

            cursor.execute(query, (name, library_id))
            conn.commit()
            print("Your order was succesfully updated!")

        except Exception as e:
            print(f"and error occurred: {e}")

        finally:
            cursor.close()
            conn.close()
