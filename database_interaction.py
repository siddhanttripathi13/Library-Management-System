import pyodbc

class Book:
    
    def __init__(self):
        self.connection = pyodbc.connect(
            'DRIVER={SQL Server Native Client 11.0};SERVER=REACTION-PC;DATABASE=Library_Management_System;Trusted_Connection=yes;'
        )
        self.cursor = self.connection.cursor()

    def add_book(self, title, author, publisher, publication_year, quantity):
        sql = "INSERT INTO books (title, author, publisher, publication_year, quantity) VALUES (?, ?, ?, ?, ?)"
        values = (title, author, publisher, publication_year, quantity)
        self.cursor.execute(sql, values)
        self.connection.commit()
        print("Book added successfully.")

    def remove_book(self, book_id):
        sql = "DELETE FROM books WHERE book_id = ?"
        self.cursor.execute(sql, (book_id,))
        self.connection.commit()
        print("Book removed successfully.")

    def available_books(self):
        sql = "SELECT * FROM books WHERE quantity > 0"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"Book ID: {row.book_id}, Title: {row.title}, Quantity: {row.quantity}")

    def borrow_book(self, user_id, book_id, borrow_date, return_date):
        # Check book availability
        sql_check_availability = "SELECT quantity FROM books WHERE book_id = ?"
        self.cursor.execute(sql_check_availability, (book_id,))
        quantity = self.cursor.fetchone().quantity

        if quantity > 0:
            # Reduce book quantity in books table
            sql_update_quantity = "UPDATE books SET quantity = quantity - 1 WHERE book_id = ?"
            self.cursor.execute(sql_update_quantity, (book_id,))
            self.connection.commit()

            # Add record to borrow table
            sql_insert_borrow = "INSERT INTO borrow (user_id, book_id, borrow_date, return_date) VALUES (?, ?, ?, ?)"
            values = (user_id, book_id, borrow_date, return_date)
            self.cursor.execute(sql_insert_borrow, values)
            self.connection.commit()
            print("Book borrowed successfully.")
        else:
            print("Book is not available for borrowing.")

    def __del__(self):
        self.cursor.close()
        self.connection.close()


class User:
    def __init__(self):
        self.connection = pyodbc.connect(
            'DRIVER={SQL Server Native Client 11.0};SERVER=REACTION-PC;DATABASE=Library_Management_System;Trusted_Connection=yes;'
        )
        self.cursor = self.connection.cursor()

    def add_user(self, first_name, last_name, email, phone_number):
        sql = "INSERT INTO users (first_name, last_name, email, phone_number) VALUES (?, ?, ?, ?)"
        values = (first_name, last_name, email, phone_number)
        self.cursor.execute(sql, values)
        self.connection.commit()
        print("User added successfully.")

    def remove_user(self, user_id):
        sql = "DELETE FROM users WHERE user_id = ?"
        self.cursor.execute(sql, (user_id,))
        self.connection.commit()
        print("User removed successfully.")

    def all_users(self):
        sql = "SELECT * FROM users"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"User ID: {row.user_id}, Name: {row.first_name} {row.last_name}")

    def user_borrows(self, user_id):
        sql = "SELECT b.title, b.borrow_date, b.return_date FROM borrow b INNER JOIN users u ON b.user_id = u.user_id WHERE u.user_id = ?"
        self.cursor.execute(sql, (user_id,))
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"Title: {row.title}, Borrow Date: {row.borrow_date}, Return Date: {row.return_date}")

    def __del__(self):
        self.cursor.close()
        self.connection.close()


class Borrow:
    def __init__(self):
        self.connection = pyodbc.connect(
            'DRIVER={SQL Server Native Client 11.0};SERVER=REACTION-PC;DATABASE=Library_Management_System;Trusted_Connection=yes'
        )
        self.cursor = self.connection.cursor()

    def all_borrows(self):
        sql = "SELECT u.first_name, u.last_name, b.title, b.borrow_date, b.return_date FROM borrow b INNER JOIN users u ON b.user_id = u.user_id INNER JOIN books bk ON b.book_id = bk.book_id"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"User: {row.first_name} {row.last_name}, Title: {row.title}, Borrow Date: {row.borrow_date}, Return Date: {row.return_date}")

    def return_book(self, user_id, book_id):
        sql_update_quantity = "UPDATE books SET quantity = quantity + 1 WHERE book_id = ?"
        self.cursor.execute(sql_update_quantity, (book_id,))
        self.connection.commit()

        sql_update_borrow = "UPDATE borrow SET return_date = GETDATE() WHERE user_id = ? AND book_id = ? AND return_date IS NULL"
        self.cursor.execute(sql_update_borrow, (user_id, book_id))
        self.connection.commit()
        print("Book returned successfully.")

    def __del__(self):
        self.cursor.close()
        self.connection.close()