# Notes: 
# 1. Use the following username and password to access the admin rights 
#    username: admin
#    password: password
# 2. Ensure you open the whole folder for this task in VS Code; otherwise, the 
#    program will look in your root directory for the text files.

import os
from datetime import datetime

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split('\n')
    task_data = [t for t in task_data if t != ""]
    
    for t_str in task_data:
        curr_t = {}
        
        task_components = t_str.split(';')
        
        if len(task_components) != 6:
            print(f"Skipping line: {t_str}. Incorrect format.")
            continue
        
        try:
            curr_t['username'] = task_components[0]
            curr_t['title'] = task_components[1]
            curr_t['description'] = task_components[2]
            curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
            curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
            curr_t['completed'] = True if task_components[5] == "Yes" else False

            task_list.append(curr_t)
        except ValueError as e:
            print(f"Skipping line: {t_str}. Error: {str(e)}")
            continue

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    if not user or ';' not in user:
        continue
    
    user_info = user.split(';')
    if len(user_info) != 2:
        continue
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


# Function to register a new user
def reg_user():
    """Registers a new user by taking username and password as input."""
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    with open("user.txt", "r") as file:
        user_data = file.readlines()

    for user in user_data:
        # Split the user data by semicolon to get username and password
        user_info = user.strip().split(";")

        # Check if the user already exists
        if user_info[0].strip() == username:
            print("Username already exists. Please try again with a different username.")
            return

    # If the user does not exist, add them to the user.txt file
    with open("user.txt", "a") as file:
        file.write(f"{username};{password}\n")

    print("User registered successfully.")


# Function to add a new task
def add_task():
    """Adds a new task by taking task details as input."""
    username = input("Enter username: ")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    assigned_date = datetime.now().strftime(DATETIME_STRING_FORMAT)
    completed = False

    with open("tasks.txt", "a") as file:
        file.write(f"{username};{title};{description};{due_date};{assigned_date};{completed}\n")

    print("Task added successfully.")


def view_all():
    if curr_user == 'admin':
        """Displays all tasks."""
        print("| Title | Description | Due Date | Status |")
        print("|---|---|---|---|")
        for task in task_list:
            if task['completed']:
                status = "Completed"
                color = "green"
            else:
                status = "Not Started"
                color = "red"
            print(f"| {task['title']} | {task['description']} | {task['due_date'].strftime(DATETIME_STRING_FORMAT)} | {status} |".format(color=color))
    else:
        my_tasks = [task for task in task_list if task['username'] == curr_user]

        if not my_tasks:
            print("No tasks assigned to you.")
        else:
            print("| Title | Description | Due Date | Status |")
            print("|---|---|---|---|")
            for task in my_tasks:
                if task['completed']:
                    status = "Completed"
                    color = "green"
                else:
                    status = "Not Started"
                    color = "red"
                print(f"| {task['title']} | {task['description']} | {task['due_date'].strftime(DATETIME_STRING_FORMAT)} | {status} |".format(color=color))

def view_mine():
    """Displays tasks assigned to the currently logged-in user."""
    my_tasks = [task for task in task_list if task['username'] == curr_user]

    if not my_tasks:
        print("No tasks assigned to you.")
    else:
        print("--- Tasks Assigned to You ---")
        for idx, task in enumerate(my_tasks, 1):
            print(f"Task {idx}:")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Assigned Date: {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Completed: {'Yes' if task['completed'] else 'No'}")
            print()

# Function to mark a task as completed
def mark_task():
    """Marks a task as completed."""
    task_index = int(input("Enter the index of the task you want to mark as completed: ")) - 1

    if task_index < 0 or task_index >= len(task_list):
        print("Invalid task index.")
    elif task_list[task_index]['username'] != curr_user:
        print("You can only mark your own tasks as completed.")
    else:
        task_list[task_index]['completed'] = True
        print("Task marked as completed.")


# Function to display the menu options
def display_menu():
    """Displays the menu options."""
    print("\n---- MENU ----")
    print("1. Register User")
    print("2. Add Task")
    print("3. View All Tasks")
    print("4. View My Tasks")
    print("5. Mark Task as Completed")
    print("6. Generate and Display Reports")
    print("7. Exit")

# Function to generate reports from tasks.txt and user.txt
def generate_reports():
    if curr_user != 'admin':
        print("You do not have permission to generate reports.")
        return
    
    # Create tasks.txt if it doesn't exist
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w") as default_file:
            pass

    # Create user.txt if it doesn't exist
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")

    # Read and display the contents of tasks.txt
    print("--- Tasks Report ---")
    with open("tasks.txt", "r") as task_file:
        task_data = task_file.read()
        print(task_data)

    # Read and display the contents of user.txt
    print("\n--- Users Report ---")
    with open("user.txt", "r") as user_file:
        user_data = user_file.read()
        print(user_data)

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        reg_user()
    elif choice == '2':
        add_task()
    elif choice == '3':
        view_all()
    elif choice == '4':
        view_mine()
    elif choice == '5':
        mark_task()
    elif choice == '6':
        generate_reports()  # Call the function to generate reports
    elif choice == '7':
        break  # Exit the program
    else:
        print("Invalid choice. Please try again.")

# Save the updated task list to the tasks.txt file
with open("tasks.txt", 'w') as task_file:
    for task in task_list:
        t_str = f"{task['username']};{task['title']};{task['description']};{task['due_date'].strftime(DATETIME_STRING_FORMAT)};{task['assigned_date'].strftime(DATETIME_STRING_FORMAT)};{'Yes' if task['completed'] else 'No'}"
        task_file.write(t_str + "\n")

# Get the total number of tasks
total_tasks = len(task_list)

# Write the total number of tasks to task_overview.txt file
with open("task_overview.txt", 'w') as task_overview_file:
    task_overview_file.write(f"Total tasks: {total_tasks}")

print("Program terminated.")
