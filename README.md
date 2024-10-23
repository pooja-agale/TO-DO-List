# TO-DO-List

Task Manager App (To-Do List)
This project is a simple Task Manager application built using Python and the Tkinter library. It allows users to add tasks, subtasks, set due dates, mark tasks as completed, and delete tasks from the list. The graphical user interface (GUI) is simple and user-friendly, making it easy for users to manage their to-do lists.

Features:
Add Tasks: Users can add new tasks to the list using an input field and a button.
Subtasks: Each task can have multiple subtasks, which can be added via a pop-up dialog.
Due Dates: Users can assign a due date to each task in the YYYY-MM-DD format.
Mark as Completed: Tasks can be marked as completed, and they will appear with a green background.
Delete Tasks: Users can delete any task along with its subtasks.
Task Display: The task list shows the main task along with its subtasks, and due dates (if set) are displayed alongside the tasks.
Technologies Used:
Python: The application is written in Python, a versatile programming language.
Tkinter: Tkinter is a built-in Python library used for creating graphical user interfaces (GUIs). It is used here to create the windows, buttons, input fields, and task list display.
Datetime: The Python datetime module is used for handling and validating the due dates entered by the user.
How the App Works:
Adding a Task: The user types a task into the input field and clicks the "Add Task" button to add it to the task list.
Adding Subtasks: By selecting a task and clicking the "Add Subtask" button, users can enter subtasks associated with the main task.
Setting Due Date: Selecting a task and clicking the "Set Due Date" button prompts the user to input a due date in the format YYYY-MM-DD. If the format is correct, the date is displayed next to the task.
Marking as Completed: Once a task is completed, the user can select the task and click "Mark as Completed" to visually change the background of the task to green.
Deleting Tasks: The user can remove any task from the list by selecting it and clicking the "Delete Task" button.
Project Structure:
Entry Field: For adding new tasks.
Listbox: Displays tasks and subtasks in a structured format.
Buttons: Provide controls for adding tasks, subtasks, setting due dates, marking tasks as completed, and deleting tasks.
Setup Instructions:
Ensure that Python is installed on your machine.
Run the script (task_manager.py) to launch the Task Manager GUI.
Use the input fields and buttons to manage your tasks.
