from connect_db import connect_db


def fetch_author():
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


fetch_author()


def add_author():
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            name = ""
            biography = ""
            query = "INSERT INTO Authors (name, biography) VALUES (%s, %s)"

            cursor.execute(query, (name, biography))
            conn.commit()
            print(f"order was succesfully added for Omen")
        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


add_author()


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


delete_author()


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


update_author()
