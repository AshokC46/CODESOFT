import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description):
        self.description = description
        self.is_completed = False
        

    def __str__(self):
        return f"{self.description} - {'Done' if self.is_completed else 'Not Done'}"

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        self.task_listbox = tk.Listbox(root, width=70, height=20, bg="lightblue", fg="black")
        self.task_listbox.pack(pady=10)

        self.task_entry = tk.Entry(root, width=50, bg="lightpink", fg="black")
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="steelblue", fg="black",)
        self.add_button.pack(pady=5)
        self.add_button.bind("<Enter>", self.on_enter)
        self.add_button.bind("<Leave>", self.on_leave)

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task, bg="steelblue", fg="black")
        self.complete_button.pack(pady=5)
        

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="steelblue", fg="black")
        self.delete_button.pack(pady=5)

    def on_enter(self, event):
        event.widget.config(bg="hotpink", fg="black")

    def on_leave(self, event):
        event.widget.config(bg="steelblue", fg="black")

    def add_task(self):
        task_description = self.task_entry.get().strip()  
        print(f"Attempting to add task: '{task_description}'")  
        if task_description:
            self.tasks.append(Task(task_description))
            self.task_entry.delete(0, tk.END)  
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must enter a task description.")
        print(f"Current tasks: {self.tasks}")  

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index].is_completed = True
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")
        print(f"Task {selected_index} marked as completed")  

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")
        print(f"Task {selected_index} deleted")  

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, str(task))
        print("Task list updated")  

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
