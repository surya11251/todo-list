import tkinter as tk
from tkinter import messagebox

# Sample tasks, each task is a dictionary with a name and a completed status
tasks = []

# Function to add a task
def add_task():
    task_name = task_entry.get()
    if task_name and task_name != "add item...":  # Ensures placeholder text isn't added
        tasks.append({"name": task_name, "completed": False})
        task_entry.delete(0, tk.END)
        display_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to mark a task as completed
def mark_completed(task_index):
    tasks[task_index]["completed"] = not tasks[task_index]["completed"]
    display_tasks()

# Function to remove a task
def remove_task(task_index):
    tasks.pop(task_index)
    display_tasks()

# Function to edit a task
def edit_task(task_index):
    new_task_name = task_entry.get()
    if new_task_name and new_task_name != "add item...":  # Ensures placeholder text isn't added
        tasks[task_index]["name"] = new_task_name
        task_entry.delete(0, tk.END)
        display_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to display tasks with buttons
def display_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()  # Clear the task frame

    for index, task in enumerate(tasks):
        # Strike-through effect if task is completed
        task_style = {"bg": "#D3D3D3", "width": 30, "anchor": "w", "padx": 10}
        if task["completed"]:
            task_label = tk.Label(task_frame, text=f"{task['name']} (Done)", **task_style, fg="green", font=("Arial", 10, "bold"))
        else:
            task_label = tk.Label(task_frame, text=task["name"], **task_style)

        task_label.grid(row=index, column=0, pady=5, sticky="w")

        # Mark as Completed Button
        mark_button = tk.Button(task_frame, text="Complete", command=lambda i=index: mark_completed(i))
        mark_button.grid(row=index, column=1, padx=5)

        # Edit Button
        edit_button = tk.Button(task_frame, text="Edit", command=lambda i=index: edit_task(i))
        edit_button.grid(row=index, column=2, padx=5)

        # Delete Button
        delete_button = tk.Button(task_frame, text="Delete", command=lambda i=index: remove_task(i))
        delete_button.grid(row=index, column=3, padx=5)

# Main window setup
window = tk.Tk()
window.title("TODO LIST")
window.geometry("400x400")

# Title
title_label = tk.Label(window, text="Surya’s TODO LIST", font=("Arial", 24, "bold"))
title_label.pack(pady=10)

# Entry field
task_entry = tk.Entry(window, width=35)
task_entry.insert(0, "add item...")  # Placeholder text
task_entry.pack(pady=10)

# Add button
add_button = tk.Button(window, text="ADD", command=add_task, width=10)
add_button.pack()

# Task list frame
task_frame = tk.Frame(window)
task_frame.pack(pady=20)

# Initial call to display tasks (empty on start)
display_tasks()

# Run the application
window.mainloop()