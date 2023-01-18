## Task Manager 2
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

* **What is the goal of this project?**  This project was done using Python Programming and the built-in datetime library. This is an improved version of the previously described Task Manager project. It preserves the same features, however some tweaks are made, such as validating if a new user is unique, offering the option to select and edit tasks previusly registered and create detailed reports considering all users and tasks, and for each individual.

#### Functions:
* Log in function: user has to type in their credentials, which are then validated to allow the user to log into the program (read from 'user.txt').
* Registering a user: the current user can register a new user by entering a unique username and a new password.
* View all tasks: display all tasks currently on the Task Manager (read from 'tasks.txt')
* View my tasks: shows all tasks for the user currently logged in and asks if the user would like to select a task to be edited.
* Editing a task: a task can be reassigned and/or marked as complete. Additionally, the due data can also be changed.
* Statistics and reports: **ADMIN ONLY ->** Display all statistics for users and tasks. The administrator can also generate reports regarding tasks and users, containing information such as how many tasks a referred user has completed, uncompleted or overdue.


#### Usage
This program requires Python 3.11, as previously described. The whole file 'task_manager_2' must be downloaded, including all files. 'tasks.txt' and 'user.txt', are necessary in order to execute this program, as they are used to store tasks and users details, respectively.
Once the contents are downloaded and the script is executed, the user will have to log in. The default log in details are 'admin' and 'adm1n', for username and passwords, respectively.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/task_manager_1_initial.png" width=50% height=50%>
</p>

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
