# Task Management System

The Task Management System is a application developed as a capstone project for HyperionDev. It allows users to manage tasks, register new users, add tasks, view tasks, mark tasks as completed, and generate reports.

## Features

- User Registration: Users can register by providing a username and password.
- Add Task: Users can add a new task by providing task details such as title, description, due date, and assignee.
- View All Tasks: Users can view all tasks in the system. Admin users can view tasks assigned to all users, while regular users can only view their own tasks.
- Mark Task as Completed: Users can mark their assigned tasks as completed.
- Generate Reports: Admin users can generate reports containing information about tasks and registered users.

# Prerequisites

- Python (version X.X.X)
- [Optional] Visual Studio Code

# Getting Started

1. Clone the repository: `git clone [repository URL]`
2. Open the project folder in Visual Studio Code or any other text editor.
3. Ensure that the whole project folder is opened to allow proper file access.
4. Open the terminal and navigate to the project folder.
5. Run the program: `python task_management.py`
6. Follow the on-screen instructions to use the Task Management System.

## Usage

The Task Management System supports the following menu options:

1. Register User: Allows a user to register by providing a unique username and password.
2. Add Task: Lets a user add a new task by providing task details.
3. View All Tasks: Displays all tasks in the system. Admin users can view tasks assigned to all users, while regular users can only view their own tasks.
4. View My Tasks: Shows tasks assigned to the currently logged-in user.
5. Mark Task as Completed: Allows a user to mark their assigned tasks as completed.
6. Generate and Display Reports: Generates reports containing information about tasks and registered users. This option is available only to admin users.
7. Exit: Terminates the program.

## User Login 

To access the admin rights and perform tasks that require admin privileges, use the following credentials:

- Username: admin
- Password: password

Please note that for security reasons, it is recommended to change the default admin password after the initial login.

## File Management

The Task Management System uses two text files to store data:

- `tasks.txt`: Stores task-related information.
- `user.txt`: Stores registered user information.

Ensure that both files are located in the project folder. If they don't exist, the program will create them automatically.

## Contributing

Contributions to the Task Management System project are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request describing your changes.