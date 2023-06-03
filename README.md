# Library Management System

This is a Library Management System project implemented using Python and Microsoft SQL Server. The project provides a set of Python classes that interact with an SQL Server database to perform various operations related to managing books, users, and borrowing records in a library.

## Features

- Add books to the library with details such as title, author, publisher, publication year, and quantity.
- Remove books from the library using the book ID.
- View all available books in the library.
- Borrow books for users, reducing the quantity in the library and adding borrowing records.
- Add new users to the library system with details such as first name, last name, email, and phone number.
- Remove users from the library using the user ID.
- View all users registered in the library system.
- View the books borrowed by a specific user.
- View all books borrowed by all users.
- Return a book borrowed by a user, updating the return date and increasing the book's quantity in the library.

## Installation

1. Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/library-management-system.git
```

2. Set up the SQL Server database by executing the provided SQL scripts to create the necessary tables and establish the schema.

3. Install the required dependencies by running the following command:

```bash
pip install pyodbc
```

4. Update the database connection details in the Python code (`Book`, `User`, and `Borrow` classes) to match your SQL Server configuration.

## Usage

1. Import the required classes from the Python script into your own project:

```python
from book import Book
from user import User
from borrow import Borrow
```

2. Create instances of the classes and utilize their methods to perform library management operations.

```python
# Example usage of Book class
book = Book()

# Add a book
book.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Scribner", 1925, 5)

# Remove a book
book.remove_book("b1")

# View available books
book.available_books()

# Borrow a book
book.borrow_book("u1", "b2", "2023-06-01", "2023-07-01")

# Example usage of User class
user = User()

# Add a user
user.add_user("John", "Doe", "johndoe@example.com", "123-456-7890")

# Remove a user
user.remove_user("u1")

# View all users
user.all_users()

# View books borrowed by a user
user.user_borrows("u2")

# Example usage of Borrow class
borrow = Borrow()

# View all books borrowed by all users
borrow.all_borrows()

# Return a book
borrow.return_book("u2", "b2")
```

3. Run your Python script to execute the desired library management operations.

## Contributing

Contributions to the Library Management System project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to the developers and contributors of the pyodbc library for enabling connectivity between Python and SQL Server.