In this repository, you will find all capstone projects I've done for the Software Engineering Skills Bootcamp at HyperionDev, supported by the Department for Education.

---
## Contents

| Project Name | Description |
|--------------|-------------|
| Finance Calculator | Calculates bond payments or investments financial return based on user's input. |
| Task Manager 1 | Program to facilitate tasks assignment and management. |
| Task Manager 2 | Upgraded task manager with additional functions to edit tasks and to generate reports to improve user's productivity. |
| Inventory Manager | Nike shoes' inventory manager that allows the user to view, add and track items in stock. |
| Bookstore Manager | Program for a library clerk to manage the inventory, making possible to visualize and make alterations on items currently on stock. |

---
## Requirements

- Python 3.11 - [read more](https://www.python.org/downloads/release/python-3110/)
---

## Projects
### Finance Calculator

* **What is the goal of this project?**  This program was done using Python Programming and the built-in math library. This solution helps the user to calculate bond payments and to predict investments returns. It allows the user to choose which calculator they would like to access (e.g. investment calculator or bond calculator) and calculates the outcome for the chosen option, based on details provided by the user.

#### Functions:
* Investment calculator: if the user choose this option, it will prompt the user with questions for specific details to calculate their revenue (e.g. simple or compound interest, interest_rate, amount invested, timespan).
* Bond calculator: if the user choose this option, it will prompt the user with questions for specific details to calculate the monthly amount to be paid (e.g. property value, interest rate, timespan).

#### Installation and Usage
This program requires Python 3.11, as previously described. The finance calculator can be accessed through [here](finance_calculator/), and once downloaded, the script can be executed on the terminal by typing `python3 finance_calculators.py` as shown below:

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/finance_calc_terminal.png" width=75% height=75%>
</p>
Obs.: you should navigate to the folder where financial_calculator.py is located in using the 'cd' command.

Then, the user should choose an option by typing the referred key word on terminal (e.g. 'bond' or 'investment') and press Enter. Then, after providing the details required by the system, the result will be displayed.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/d76a143ef1f576c5645362531c707288066fadab/images/finance_calculator_example.png" width=75% height=75%>
</p>


### Task Manager 1

* **What is the goal of this project?**  This program was made using Python Programming and the built-in datetime library. It facilitates tasks management in one place, making possible for the user to log in and see and/or add tasks, as well as register new users. A special statistics is available to the administrator.

#### Functions:
* Log in function: user has to type in their credentials, which are then validated to allow the user to log into the program (read from 'user.txt').
* Registering a user: the current user can register a new user by entering a unique username and a new password.
* View all tasks: display all tasks currently on the Task Manager (read from 'tasks.txt')
* View my tasks: shows all tasks for the user currently logged in.
* Statistics: **ADMIN ONLY ->** Displays the total number of users and tasks.

#### Installation and Usage
This program requires Python 3.11, as previously described. The Task Manager 1 can be accessed through [here](task_manager_1/). The whole file 'task_manager_1' must be downloaded, including all files. 'tasks.txt' and 'user.txt', are necessary in order to execute this program, as they are used to store tasks and users details, respectively.
Once the contents are downloaded, the script can be executed on the terminal by typing `python3 task_manager.py` as shown below. The user will have to log in. The default log in details are 'admin' and 'adm1n', for username and passwords, respectively.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_1_terminal.png" width=50% height=50%>
</p>
Obs.: you should navigate to the folder where financial_calculator.py is located in using the 'cd' command.

The user will then be prompt with a menu offering several tools for tasks management. The first tool this program offers is to register new users. The user will have to enter a new username and password, followed by a password confirmation. Then, this new user will be saved on 'user.txt' for future reference, and the initial menu will be prompted again.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_1_add_new_user.png" width=50% height=50%>
</p>

The next feature is to add new tasks. The user will be asked to enter a username of which this task is assigned for, followed by task title, description and due date, as demonstrated below. Once all details are provided, the new task is saved into 'tasks.txt' for future reference, and the menu is prompted again.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_1_adding_new_task.png" width=75% height=75%>
</p>

Furthermore, the user can also see, in a user-friendly format, all tasks currently saved on Task Manager, or only tasks assigned to them, using 'va' and 'vm' menu options, as shown below.

View all:
<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_1_va.png" width=75% height=75%>
</p>

View my tasks:
<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_1_vm.png" width=75% height=75%>
</p>

Finally, the administrator have an option to see the statistics of the program, which shows the number of users and tasks currently registered.

View my tasks:
<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_1_st.png" width=50% height=50%>
</p>

### Task Manager 2

* **What is the goal of this project?**  This project was done using Python Programming and the built-in datetime library. This is an improved version of the previously described Task Manager project. It preserves the same features, however some tweaks are made, such as validating if a new user is unique, offering the option to select and edit tasks previusly registered and create detailed reports considering all users and tasks, and for each individual.

#### Functions:
* Log in function: user has to type in their credentials, which are then validated to allow the user to log into the program (read from 'user.txt').
* Registering a user: the current user can register a new user by entering a unique username and a new password.
* View all tasks: display all tasks currently on the Task Manager (read from 'tasks.txt')
* View my tasks: shows all tasks for the user currently logged in and asks if the user would like to select a task to be edited.
* Editing a task: a task can be reassigned and/or marked as complete. Additionally, the due data can also be changed.
* Statistics and reports: **ADMIN ONLY ->** Display all statistics for users and tasks. The administrator can also generate reports regarding tasks and users, containing information such as how many tasks a referred user has completed, uncompleted or overdue.


#### Installation and Usage
This program requires Python 3.11, as previously described. The Task Manager 2 can be accessed through [here](task_manager_2/). The whole file 'task_manager_2' must be downloaded, including all files. 'tasks.txt' and 'user.txt', are necessary in order to execute this program, as they are used to store tasks and users details, respectively.
Once the contents are downloaded, the script can be executed on the terminal by typing `python3 task_manager2.py` as shown below. The user will have to log in. The default log in details are 'admin' and 'adm1n', for username and passwords, respectively.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_2_terminal.png" width=50% height=50%>
</p>
Obs.: you should navigate to the folder where financial_calculator.py is located in using the 'cd' command.

For registering a user, adding a task and view all tasks functions, please refer to 'Task Manager 1' documentation, as these options are preserved.

###### New functions added to Task Manager 2:

Now, when a user asks to see all their tasks, they will be prompted with a sub menu asking if they would like to select one of those tasks to be edited.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_1_initial.png" width=50% height=50%>
</p>

Now when the user selects the option to see all their tasks, they are also prompts with an option to select a task.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_2_vm.png" width=75% height=75%>
</p>

After selecting a task (a mock test was added to demonstrate this function), the user is now prompted with the following options:

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_2_edit_menu.png" width=50% height=50%>
</p>

If the user chooses to mark a task as complete, the referred task is automatically updated to display "Yes" as completion details.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_2_mark_complete.png" width=75% height=75%>
</p>

Whereas, if the user chooses to edit a task, the program will prompt the user with a new set of choices. Then, the user can choose to alter the task's due date, or to whom the task is assigned for.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_2_edit_menu_2.png" width=50% height=50%>
</p>

The administrator now has the option to generate detailed reports regarding the data currently registered within the program.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_2_generate_reports.png" width=50% height=50%>
</p>

When the administrator selects this option, two .txt files are automatically generated to display detailed information about the users and tasks, respectivelly, shown below:

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_2_users_report.png" width=50% height=50%>
</p>

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_2_tasks_report.png" width=50% height=50%>
</p>

Finally, the administrator can have these details displayed on the terminal by selecting the statistics option on the menu.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_2_st.png" width=50% height=50%>
</p>


### Inventory Manager

* **What is the goal of this project?**  This project was done using Python Programming and focused on applying Object-Oriented Programming principles. It provides a comprehensive and organized view and management tool for a shoe warehouse.

#### Functions:
* See all products: displays a list of all products currently available in a user-friendly format.
* Enter a new product: the user can add a new product to the inventory containing all pertinent details.
* Restock a product: the user can update the quantity in stock for a particular item.
* Search product/ see product value/ see item on sale: the user can see the referred information for a specific item.

#### Installation and Usage
This program requires Python 3.11, as previously described, and was developed applying all concepts inherent to Object-Oriented Programming principles. The Inventory Manager can be accessed through [here](inventory_manager/). The whole file 'inventory_manager' must be downloaded, including 'inventory.txt', which holds all information about the products in stock.
Once the contents are downloaded, the script can be executed on the terminal by typing `python3 inventory_manager.py` as shown below. The user will be prompted with a menu, as shown below.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/inventory_manager_terminal.png" width=50% height=50%>
</p>
Obs.: you should navigate to the folder where financial_calculator.py is located in using the 'cd' command.

If the user chooses the option to see all items currently on stock, a list of all products will be displayed in a user-friendly format.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/inventory_manager_see_all.png" width=25% height=25%>
</p>

The user can also add register a new product to the program. After providing all the required deitals (e.g. product name, id, price and quantity), the product will automatically be added to 'inventory.txt' for future reference.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/inventory_manager_add_new.png" width=50% height=50%>
</p>

If the user decides to restock an item, the program will automatically find the product with the lowest quantity on stock, and ask the user if they would like to restock the referred item. After providing how many items they would like to restock, a feedback is shown to the user, as it is possible to see below.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/inventory_manager_restock.png" width=75% height=75%>
</p>

The user can also search an item using the item's id. Then, the program will automatically fetch all the details for the referred product and display them in a user-friendly manner.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/inventory_manager_search.png" width=50% height=50%>
</p>

It is possible to check the total item for every item currently in stock. The total value is calculated based on item's price and quantity. The final result is displayed to the user as a table.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/inventory_manager_total.png" width=50% height=50%>
</p>

Finally, the user can also fetch witch item is currently on sale. The program will automatically find the item with the highest availability on stock, and return this product's details to the user.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/inventory_manager_sale.png" width=50% height=50%>
</p>


### Bookstore Manager

* **What is the goal of this project?**  This project was done using Python Programming and sqlite3 library. It supplies the user with a complete tool to manage products in a bookstore.

#### Functions:
* See all books: retrieve all items within the books database and display to user.
* Enter or delete a book: alters the current database to add or remove a record.
* Update a book: update a detail for a book within the database.
* Search a book: searches the database using a primary key and returns the record to the user.

#### Installation and Usage
This program requires Python 3.11, as previously described, and was developed using the sqlite3 built-in library. The Bookstore Manager can be accessed through [here](bookstore_manager/). Only 'bookstore_manager.py' is necessary to execute this program, as the database will be generated automatically if none is found.
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
