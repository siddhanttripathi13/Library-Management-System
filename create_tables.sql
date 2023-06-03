-- Books Table--
CREATE TABLE books (
  id INT IDENTITY(1,1) NOT NULL,
  book_id AS 'b' + CAST(id AS VARCHAR(10)) PERSISTED,
  title VARCHAR(255),
  author VARCHAR(255),
  publisher VARCHAR(255),
  publication_year INT,
  quantity INT,
  CONSTRAINT books_pk PRIMARY KEY (book_id)
);

--Users Table--
CREATE TABLE users (
  id INT IDENTITY(1,1) NOT NULL,
  user_id AS 'u' + CAST(id AS VARCHAR(10)) PERSISTED,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  email VARCHAR(255),
  phone_number INT,
  CONSTRAINT users_pk PRIMARY KEY (user_id)
)

--Borrow Table--
CREATE TABLE borrow (
    id INT IDENTITY(1,1) NOT NULL,
    borrow_id AS 'b' + CAST(id as VARCHAR(10)) PERSISTED,
    user_id VARCHAR(11),
    book_id VARCHAR(11),
    borrw_date DATE,
    return_date DATE
    CONSTRAINT borrow_users FOREIGN KEY (user_id) REFERENCES users(user_id),
    CONSTRAINT borrow_books FOREIGN KEY (book_id) REFERENCES books(book_id),
    CONSTRAINT borrow_pk PRIMARY KEY (borrow_id)
)

SELECT * from books