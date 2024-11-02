import tkinter as tk
from tkinter import messagebox
import json
from tkinter import simpledialog

# Define the file to store tasks
TASK_FILE = "tasks.json"

# Load existing tasks from the JSON file, if available
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Initialize tasks
tasks = load_tasks()

# Function to add a new task
def add_task():
    title = title_entry.get()
    description = description_entry.get()
    priority = priority_var.get()
    due_date = due_date_entry.get()

    if not title:
        messagebox.showwarning("Input Error", "Please enter a task title.")
        return

    task = {
        "title": title,
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    update_task_list()
    clear_entries()

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        task_listbox.insert(tk.END, f"{task['title']} - {status}")

def clear_entries():
    title_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)
    priority_var.set("Medium")

# Function to mark a task as completed
def mark_task_completed():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["completed"] = True
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Function to delete a task
def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks.pop(selected_index)
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to update a task
def update_task():
    try:
        selected_index = task_listbox.curselection()[0]
        current_task = tasks[selected_index]
        
        # Prompt for new details
        new_title = simpledialog.askstring("Update Task", "New title:", initialvalue=current_task["title"])
        new_description = simpledialog.askstring("Update Task", "New description:", initialvalue=current_task["description"])
        new_priority = simpledialog.askstring("Update Task", "New priority (High, Medium, Low):", initialvalue=current_task["priority"])
        new_due_date = simpledialog.askstring("Update Task", "New due date (YYYY-MM-DD):", initialvalue=current_task["due_date"])

        if new_title:
            current_task["title"] = new_title
        if new_description:
            current_task["description"] = new_description
        if new_priority:
            current_task["priority"] = new_priority
        if new_due_date:
            current_task["due_date"] = new_due_date

        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to update.")

# GUI setup
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Task Title
tk.Label(root, text="Title:", bg="#f0f0f0", fg="#333333").pack(pady=5)
title_entry = tk.Entry(root, width=50, font=("Arial", 12), bg="#ffffff", fg="#000000")
title_entry.pack(pady=5)

# Task Description
tk.Label(root, text="Description:", bg="#f0f0f0", fg="#333333").pack(pady=5)
description_entry = tk.Entry(root, width=50, font=("Arial", 12), bg="#ffffff", fg="#000000")
description_entry.pack(pady=5)

# Task Priority
tk.Label(root, text="Priority:", bg="#f0f0f0", fg="#333333").pack(pady=5)
priority_var = tk.StringVar(value="Medium")
priority_menu = tk.OptionMenu(root, priority_var, "High", "Medium", "Low")
priority_menu.config(bg="#ffffff", fg="#000000")
priority_menu.pack(pady=5)

# Task Due Date
tk.Label(root, text="Due Date (YYYY-MM-DD):", bg="#f0f0f0", fg="#333333").pack(pady=5)
due_date_entry = tk.Entry(root, width=50, font=("Arial", 12), bg="#ffffff", fg="#000000")
due_date_entry.pack(pady=5)

# Task Listbox
task_listbox = tk.Listbox(root, width=70, height=10, font=("Arial", 12), bg="#ffffff", fg="#000000")
task_listbox.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, bg="#4CAF50", fg="#ffffff")
add_button.pack(side=tk.LEFT, padx=5)

update_button = tk.Button(button_frame, text="Update Task", command=update_task, bg="#2196F3", fg="#ffffff")
update_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="#F44336", fg="#ffffff")
delete_button.pack(side=tk.LEFT, padx=5)

complete_button = tk.Button(button_frame, text="Mark Completed", command=mark_task_completed, bg="#FFC107", fg="#000000")
complete_button.pack(side=tk.LEFT, padx=5)

# Initial task list display
update_task_list()

# Start the GUI main loop
root.mainloop()
