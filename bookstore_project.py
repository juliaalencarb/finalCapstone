# Importing sqlite3 library.
import sqlite3


# Declaring logo to be printed when the program is initiated.
logo = '''================================================================================================
___  ____ ____ _  _ ____ ___ ____ ____ ____    _  _ ____ _  _ ____ ____ ____ _  _ ____ _  _ ___ 
|__] |  | |  | |_/  [__   |  |  | |__/ |___    |\/| |__| |\ | |__| | __ |___ |\/| |___ |\ |  |  
|__] |__| |__| | \_ ___]  |  |__| |  \ |___    |  | |  | | \| |  | |__] |___ |  | |___ | \|  |  
================================================================================================'''

# Declaring books requested on task 48.
current_books = [
    (3001, "A Tale of Two Cities", "Charles Dickens", 30),
    (3002, "Harry Potter and the Philosopher's Stone", "J. K. Rowling", 40),
    (3003, "The Lion, the Witch and the Wardrobe", "D. S. Lewis", 25),
    (3004, "The Lord of the Rings", "J. R. R. Tolkien", 37),
    (3005, "Alice in Wonderland", "Lewis Carroll", 12),
]


# In this block I will be declaring all functions necessary for my program to run.
# Each function contains its own description (documentation).
def add_book():
    """Adds a new book and its details to the table books on bookstore_database. Returns a feedback message to user."""
    new_id = int(input("Enter book id: "))
    new_title = input("Enter book title: ").title()
    new_author = input("Enter book author: ").title()
    new_book_qty = int(input("Enter book quantity: "))
    cursor.execute("INSERT INTO books VALUES(?, ?, ?, ?)", (new_id, new_title, new_author, new_book_qty))
    bookstore_db.commit()
    return f"Book '{new_title}' (id {new_id}) was added to the database.\n"


def delete_book(record_id):
    """Receives a book id and deletes the record associated with this key on the table books on bookstore_database.
    Returns a feedback message to user."""
    cursor.execute("DELETE FROM books WHERE id = (?)", (record_id,))
    bookstore_db.commit()
    return f"The entry for id {record_id} was deleted from the database.\n"


def update_book(record_id):
    """Receives a book id of which book the user would like to update.
    Prompts a menu to the user, and updates the information chosen by the user.
     Returns a feedback message to the user."""
    sub_menu = int(input("""What would you like to change?
    1. Title
    2. Author
    3. Quantity
    0. Back to menu
    : """))

    if sub_menu == 1:
        new_title = input("Enter new title: ").title()
        cursor.execute("UPDATE books SET title = (?) WHERE id = (?)", (new_title, record_id))
        bookstore_db.commit()
        return f"Title was changed for id {record_id}.\nNew title: '{new_title}.\n"
    elif sub_menu == 2:
        new_author = input("Enter new author: ").title()
        cursor.execute("UPDATE books SET author = (?) WHERE id = (?)", (new_author, record_id))
        bookstore_db.commit()
        return f"Author was changed for id {record_id}\nNew author: {new_author}.\n"
    elif sub_menu == 3:
        new_qty = int(input("Enter new quantity: "))
        cursor.execute("UPDATE books SET qty = (?) WHERE id = (?)", (new_qty, record_id))
        bookstore_db.commit()
        return f"Quantity was changed for id {record_id} to {new_qty}.\n"
    elif sub_menu == 0:
        return ""
    else:
        print("Invalid option. Try again.")


def search_book(record_id):
    """Receives a book id and returns the record associated with this id from table books on bookstore_database."""
    res = cursor.execute("SELECT * FROM books WHERE id = (?)", (record_id,))
    output = res.fetchone()
    return output


def see_all_books():
    """Returns all books currently on table books on bookstore_database."""
    res = cursor.execute("SELECT * FROM books")
    return res


# Initializing database connection and cursor.
bookstore_db = sqlite3.connect("bookstore_database")
cursor = bookstore_db.cursor()

# Piece of code used for testing purposes only.
# cursor.execute("DROP TABLE books")


# Trying to create 'books' table on bookstore_database as described below. Then, I'm trying to populate
# this table with the books list previously declared. All changes are committed.
# Creating an exception in case the table already exists to prevent the program to crash.
try:
    cursor.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)")
    bookstore_db.commit()

    cursor.executemany("INSERT INTO books VALUES(?, ?, ?, ?)", current_books)
    bookstore_db.commit()

except sqlite3.OperationalError as error:
    bookstore_db.rollback()


# Creating a helper variable to be able to start a while true loop.
is_on = True
print(f"{logo}\n")  # printing logo.

# Loop to keep prompting user with the menu. Selecting action based on user choice. If user decides
# to quit the application, set is_on to False and ends the loop.
# I've decided to add 'see all books' to the menu to be able to easily see the changes made to
# the database.
while is_on:
    menu = int(input("""    1. Enter book
    2. Update book
    3. Delete book
    4. Search books
    5. See all books
    0. Exit
    : """))

    if menu == 1:
        print(add_book())
        continue
    elif menu == 2:
        book_id = int(input("Enter book id: "))
        print(update_book(book_id))
        continue
    elif menu == 3:
        book_id = int(input("Enter book id: "))
        print(delete_book(book_id))
        continue
    elif menu == 4:
        book_id = int(input("Enter book id: "))
        print(f"{search_book(book_id)}\n")
        continue
    elif menu == 5:
        all_books = see_all_books()
        for row in all_books:
            print(row)
        print("")
        continue
    elif menu == 0:
        is_on = False

# Closing the database.
bookstore_db.close()
