import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=5, pady=5)

        self.task_list = tk.Listbox(root, width=50)
        self.task_list.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.subtask_button = tk.Button(root, text="Add Subtask", command=self.add_subtask)
        self.subtask_button.grid(row=2, column=0, padx=5, pady=5)

        self.due_date_button = tk.Button(root, text="Set Due Date", command=self.set_due_date)
        self.due_date_button.grid(row=2, column=1, padx=5, pady=5)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.grid(row=2, column=2, padx=5, pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        self.update_task_list()

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append({"task": task_text, "subtasks": [], "due_date": None})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def add_subtask(self):
        try:
            selected_index = self.task_list.curselection()[0]
            task_text = simpledialog.askstring("Subtask", "Enter subtask:")
            if task_text:
                self.tasks[selected_index]["subtasks"].append(task_text)
                self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task.")

    def set_due_date(self):
        try:
            selected_index = self.task_list.curselection()[0]
            due_date = simpledialog.askstring("Due Date", "Enter due date (YYYY-MM-DD):")
            if due_date:
                try:
                    due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
                    self.tasks[selected_index]["due_date"] = due_date
                    self.update_task_list()
                except ValueError:
                    messagebox.showwarning("Warning", "Invalid date format. Please enter date in YYYY-MM-DD format.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task.")

    def mark_completed(self):
        try:
            selected_index = self.task_list.curselection()[0]
            self.task_list.itemconfig(selected_index, {'bg': 'green'})
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task.")

    def delete_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_index)
            del self.tasks[selected_index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task.")

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            task_text = task["task"]
            if task["due_date"]:
                task_text += " - Due: " + task["due_date"].strftime("%Y-%m-%d")
            self.task_list.insert(tk.END, task_text)
            for subtask in task["subtasks"]:
                self.task_list.insert(tk.END, "   - " + subtask)

def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()