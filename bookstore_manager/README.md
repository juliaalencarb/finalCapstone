## Bookstore Manager
---
## Contents

| Section | Description |
|--------------|-------------|
| Requirements | A list of any software necessary to run this solution. |
| Functions | Brief elucidation of this program's properties. |
| Usage | A detailed explanation of the program's features and how to use them. |

---
## Requirements

- Python 3.11 - [read more](https://www.python.org/downloads/release/python-3110/)
---

* **What is the goal of this project?**  This project was done using Python Programming and sqlite3 library. It supplies the user with a complete tool to manage products in a bookstore.

#### Functions:
* See all books: retrieve all items within the books database and display to user.
* Enter or delete a book: alters the current database to add or remove a record.
* Update a book: update a detail for a book within the database.
* Search a book: searches the database using a primary key and returns the record to the user.

#### Installation and Usage
This program requires Python 3.11, as previously described, and was developed using the sqlite3 built-in library. Only 'bookstore_manager.py' is necessary to execute this program, as the database will be generated automatically if none is found.
Once the script is downloaded, the script can be executed on the terminal by typing `python3 bookstore_manager.py` as shown below. The user will then be prompted with a menu.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/bookstore_terminal.png" width=75% height=75%>
</p>
Obs.: you should navigate to the folder where financial_calculator.py is located in using the 'cd' command.

The user can then choose from the options listed as previously seen. If the user desires to add a new book to the database, they can do it by choosing option 1. After providing all the required details, as described below, the new item is saved to the database.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/bookstore_manager_enter_new.png" width=50% height=50%>
</p>

The user can also edit a record currently present within the database. In the following steps, it is demonstrated how to change the title, author and quantity of a record. The user will need to provide the id as a primary key to access the record they wish to alter.

- Changing a title:
<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/bookstore_manager_change_title.png" width=25% height=25%>
</p>

- Changing an author:
<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/bookstore_manager_change_author.png" width=25% height=25%>
</p>

- Changing an item's quantity:
<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/bookstore_manager_change_quantity.png" width=25% height=25%>
</p>

The user can also delete a record by choosing the delete option from the menu. Again, the user will need to provide the item's id as a primary key.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/bookstore_manager_delete.png" width=50% height=50%>
</p>

Finally, the user can see all records presently registered within the database by choosing 'See all books' from the menu.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/bookstore_manager_view_all.png" width=75% height=75%>
</p>
