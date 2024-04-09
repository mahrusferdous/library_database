from connect_db import connect_db


def fetch_author(name=""):
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM Authors WHERE name = %s"
            cursor.execute(query, (name,))

            for row in cursor.fetchall():
                print(row)

        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


def fetch_authors():
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM Authors"
            cursor.execute(query)

            for row in cursor.fetchall():
                print(row)

        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


def add_author(name, biography):
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = "INSERT INTO Authors (name, biography) VALUES (%s, %s)"
            cursor.execute(query, (name, biography))

            conn.commit()
            print(f"Succesfully added for Author")
        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


def delete_author():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            name = ""
            biography = ""
            query = "DELETE FROM Authors WHERE name = %s AND biography = %s"

            cursor.execute(query, (name, biography))
            conn.commit()
            print("Your order was successfully deleted!")

        except Exception as e:
            print(f"and error occurred: {e}")

        finally:
            cursor.close()
            conn.close()


def update_author():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            name = ""
            biography = ""
            query = "UPDATE Authors SET biography = %s WHERE name = %s"

            cursor.execute(query, (biography, name))
            conn.commit()
            print("Your order was succesfully updated!")

        except Exception as e:
            print(f"and error occurred: {e}")

        finally:
            cursor.close()
            conn.close()
