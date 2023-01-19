## Task Manager 1
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

* **What is the goal of this project?**  This program was made using Python Programming and the built-in datetime library. It facilitates tasks management in one place, making possible for the user to log in and see and/or add tasks, as well as register new users. A special statistics is available to the administrator.

#### Functions:
* Log in function: user has to type in their credentials, which are then validated to allow the user to log into the program (read from 'user.txt').
* Registering a user: the current user can register a new user by entering a unique username and a new password.
* View all tasks: display all tasks currently on the Task Manager (read from 'tasks.txt')
* View my tasks: shows all tasks for the user currently logged in.
* Statistics: **ADMIN ONLY ->** Displays the total number of users and tasks.

#### Installation and Usage
This program requires Python 3.11, as previously described. The whole file 'task_manager_1' must be downloaded, including all files. 'tasks.txt' and 'user.txt', are necessary in order to execute this program, as they are used to store tasks and users details, respectively.
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
