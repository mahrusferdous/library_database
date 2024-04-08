from connect_db import connect_db


def add_order():
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            # set order information into variables
            omen_id = 8
            order_date = "2024-04-05"

            # query to insert into Orders table
            query = "INSERT INTO Orders (date, customer_id) VALUES (%s, %s)"
            # execute query
            cursor.execute(query, (order_date, omen_id))
            #              query, tuple with the above order information
            conn.commit()
            print(f"order was succesfully added for Omen")
        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()


add_order()


def delete_order():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            # set order information to be deleted
            customer_id = 2
            # order_id to be deleted
            order_id = 4

            # sql query to delete
            query = "DELETE FROM Orders WHERE order_id = %s AND customer_id = %s"
            cursor.execute(query, (order_id, customer_id))
            conn.commit()
            print("Your order was successfully deleted!")

        except Exception as e:
            print(f"and error occurred: {e}")

        finally:
            cursor.close()
            conn.close()


delete_order()
