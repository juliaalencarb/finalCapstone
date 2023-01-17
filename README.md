# HyperionDev Capstone Projects

In this repository, you will find all capstone projects I've done for the Software Engineering Skills Bootcamp at HyperionDev, supported by the Department for Education.

---
## Contents

- Project: Finance Calculator
  - Description: Calculates bond payments or investments financial return based on user's input.
- Project: Task Manager 1
  - Description: Program to facilitate tasks assignment and management.
- Project: Task Manager 2
  - Description: Upgraded task manager with additional functions to edit tasks and to generate reports to improve user's productivity.
- Project: Inventory Manager
  - Description: Nike shoes' inventory manager that view, add and track items in stock.
- Project: Bookstore Manager
  - Description: Program for a library clerk to manage the inventory, making possible to visualize and make alterations on items currently on stock.
---

---
## Requirements

- Python 3.11 - [read more](https://www.python.org/downloads/release/python-3110/)
---

## Projects
### Finance Calculator

The finance calculator can be accessed through [here](finance_calculator/).
* **What is the goal of this project?**  This program was done using Python Programming. It allows the user to choose which calculator they would like to access (e.g. investment calculator or bond calculator) and calculates the outcome for the chosen option.

#### Functions:
* Investment calculator: if the user choose this option, it will prompt the user with questions for specific details to calculate their revenue (e.g. simple or compound interest, interest_rate, amount invested, timespan).
* Bond calculator: if the user choose this option, it will prompt the user with questions for specific details to calculate the monthly amount to be paid (e.g. property value, interest rate, timespan).


### Task Manager 1

The Task Manager 1 can be accessed through [here](task_manager_1/). 'tasks.txt' and 'user.txt' are also necessary for storing tasks and users details, respectively.
* **What is the goal of this project?**  This program was made using Python Programming and built-in methods. It facilitates tasks management in one place, making possible for the user to log in and see and/or add tasks, as well as register new users. A special statistics is available to the administrator.

#### Functions:
* Log in function: user has to type in their credentials, which are then validated to allow the user to log into the program (read from 'user.txt').
* Registering a user: the current user can register a new user by entering a unique username and a new password.
* View all tasks: display all tasks currently on the Task Manager (read from 'tasks.txt')
* View my tasks: shows all tasks for the user currently logged in.
* Statistics: **ADMIN ONLY ->** Displays the total number of users and tasks.


### Task Manager 2

Improved Task Manager. It can be accessed through [here](task_manager_2/). 'tasks.txt' and 'user.txt' are also necessary for storing tasks and users details, respectively.
* **What is the goal of this project?**  This project was done using Python Programming and built-in methods. It facilitates tasks management in one place, making possible for the user to log in and see and/or add tasks, register new users. Administrator's special features include: statistics and generate reports.

#### Functions:
* Log in function: user has to type in their credentials, which are then validated to allow the user to log into the program (read from 'user.txt').
* Registering a user: the current user can register a new user by entering a unique username and a new password.
* View all tasks: display all tasks currently on the Task Manager (read from 'tasks.txt')
* View my tasks: shows all tasks for the user currently logged in and asks if the user would like to select a task to be edited.
* Editing a task: a task can be reassigned and/or marked as complete. Additionally, the due data can also be changed.
* Statistics and reports: **ADMIN ONLY ->** Display all statistics for users and tasks. The administrator can also generate reports regarding tasks and users, containing information such as how many tasks a referred user has completed, uncompleted or overdue.


### Inventory Manager

The Inventory Manager can be accessed through [here](inventory_manager/). 'inventory.txt' is also necessary for storing inventory details.
* **What is the goal of this project?**  This project was done using Python Programming and focused on applying Object-Oriented Programming principles. It provides a comprehensive and organized view and management tool for a shoe warehouse.

#### Functions:
* See all products: displays a list of all products currently available in a user-friendly format.
* Enter a new product: the user can add a new product to the inventory containing all pertinent details.
* Restock a product: the user can update the quantity in stock for a particular item.
* Search product/ see product value/ see item on sale: the user can see the referred information for a specific item.


### Bookstore Manager

The Inventory Manager can be accessed through [here](bookstore_manager/).
* **What is the goal of this project?**  This project was done using Python Programming and sqlite3 library. It supplies the user with a complete tool to manage products in a bookstore.

#### Functions:
* See all books: retrieve all items within the books database and display to user.
* Enter or delete a book: alters the current database to add or remove a record.
* Update a book: update a detail for a book within the database.
* Search a book: searches the database using a primary key and returns the record to the user.
