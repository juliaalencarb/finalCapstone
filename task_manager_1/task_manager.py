#=====importing libraries===========
from datetime import datetime

# Declaring variable that will hold the user's username.
user_username = ""
# Creating an empty dictionary to store a list (empty) of usernames and passwords from the file.
user_pw = {}
usernames = []
passwords = []

#====Login Section====
# Section that will allow a user to login.
# Reading usernames and password from the user.txt file.
with open("../HyperionDev_II/user.txt", "r") as file:
    user_data = file.readlines()
    for data in user_data:
        split_user_data = data.split(",") # Splitting data every ",".
        # Adding usernames and passwords to previously created lists.
        usernames.append(split_user_data[0])
        stripped_pw = split_user_data[1].strip(" \n") # Stripping spaces and new lines.
        passwords.append(stripped_pw)

# Populating previously created dictionary with lists of usernames and passwords.
user_pw["username"] = usernames
user_pw.update({'password': passwords})


# Using a while loop to validate username and password. Here I'm using the helper variable 'is_logged_in'.
is_logged_in = False

while not is_logged_in:
    user_username = input("Please enter your username: ")
    # If the username is correct, ask for password, if not displays appropriate message.
    if user_username in user_pw['username']:
        username_index = user_pw['username'].index(user_username)
        user_password = input("Please enter your password: ")

        # Log in if username and passwords are correct, if not displays appropriate message.
        if user_password == user_pw['password'][username_index]:
            print("You're logged in.")
            is_logged_in = True
        else:
            print("Incorrect password. Try again.")
    else:
        print("Incorrect username. Try again.")

while True:
    # Presenting the menu to the user and making sure that the user input is converted to lower case.
    # Displays additional option for 'admin'.
    if user_username == "admin":
        menu = input('''Select one of the following Options below:
        r -     Registering a user
        a -     Adding a task
        va -    View all tasks
        vm -    View my task
        st -    Statistics
        e -     Exit
        : ''').lower()
    else:
        menu = input('''Select one of the following Options below:
    r -     Registering a user
    a -     Adding a task
    va -    View all tasks
    vm -    View my task
    e -     Exit
    : ''').lower()

    # Adds a new user to the user.txt file, only if user is 'admin'.
    if menu == 'r':
        if user_username == "admin":
            # Request input of a new username.
            new_username = input("Please enter your new username: ")
            # Request input of a new password.
            new_password = input("Please enter new password: ")
            # Request input of password confirmation.
            new_password_confirmation = input("Please repeat new password: ")
            # Check if the new password and confirmed password are the same, then add them to the user.txt file.
            # Otherwise, displays a relevant message.
            if new_password == new_password_confirmation:
                with open('../HyperionDev_II/user.txt', "a") as f:
                    f.write(f"\n{new_username}, {new_password}")
            else:
                print("You entered a different password. Try again.")
        else:
            print("Only the Administrator is able to register new users.")

    # Allows user to add a new task to task.txt file.
    elif menu == 'a':
        # Asks the username of the person whom the task is assigned to, title, description and due date of the task.
        new_task_username = input("Please enter the username this task is designed to: ")
        new_task_title = input("Please enter the title of the new task: ")
        new_task_description = input("Please enter a task description: ")
        new_task_date = input("Enter the due date for this task (DD/MM/YYYY): ")
        formatted_date = datetime.strptime(new_task_date, "%d/%m/%Y") # Formatting input date to the requested format.
        final_formatted_date = formatted_date.strftime('%d %b %Y')
        # Getting the current date using datetime.
        current_date = datetime.now()
        formatted_current_date = current_date.strftime("%d %b %Y") # Formatting to requested format.
        # Adding new task to 'tasks.txt'.
        with open("../HyperionDev_II/tasks.txt", "a") as f:
            f.write(f"\n{new_task_username}, {new_task_title}, {new_task_description}, {formatted_current_date}, {final_formatted_date}, No")

    # Reading tasks from task.txt file and printing formatted task as required.
    elif menu == 'va':
        with open("../HyperionDev_II/tasks.txt", "r") as f:
            data = f.readlines()

            for task in data:
                split_task = task.split(",") # Split line by ",".
                print(f"""
Task:           {split_task[1]}
Assigned to:     {split_task[0]}
Date Assigned:  {split_task[3]}
Due Date:       {split_task[4]}
Task Complete?  {split_task[5]}
Task Description:
 {split_task[2]}\n""")

    # Reading tasks from task.txt file and printing formatted task as requested (specific for user).
    elif menu == 'vm':
        with open("../HyperionDev_II/tasks.txt", "r") as f:
            data = f.readlines()

            for task in data:
                split_task = task.split(",") # Split line by ",".
                if split_task[0] == user_username: # Selecting only tasks for this specific user.
                    print(f"""
Task:           {split_task[1]}
Assigned to:     {split_task[0]}
Date Assigned:  {split_task[3]}
Due Date:       {split_task[4]}
Task Complete?  {split_task[5]}
Task Description:
 {split_task[2]}\n""")

    # Displays tasks and users counts (specific for 'admin').
    elif menu == "st":
        with open("../HyperionDev_II/user.txt", "r") as f:
            users = f.readlines()
            total_users_num = len(users) # Getting total users number.

        with open("../HyperionDev_II/tasks.txt", "r") as f:
            tasks = f.readlines()
            total_task_num = len(tasks) # Getting total tasks number.

        print(f"""
Total Number of Tasks: {total_task_num}
Total Number of Users: {total_users_num}""")

    # Exits the program.
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # Displays appropriate message if user selects wrong option.
    else:
        print("You have made a wrong choice, Please Try again")
