import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Jashanpreet's Task Manager")
root.geometry("500x500")

tasks = []

# Functions
def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
    else:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)


def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
        tasks.pop(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task first!")


def mark_completed():
    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)

        if not task.startswith("✓ "):
            task_listbox.delete(selected)
            task_listbox.insert(selected, "✓ " + task)

    except IndexError:
        messagebox.showwarning("Warning", "Please select a task first!")


def clear_tasks():
    answer = messagebox.askyesno(
        "Confirm",
        "Do you want to clear all tasks?"
    )

    if answer:
        task_listbox.delete(0, tk.END)
        tasks.clear()


# Heading
title_label = tk.Label(
    root,
    text="✨ Jashanpreet's Task Manager ✨",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

# Task Entry
task_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12)
)
task_entry.pack(pady=10)

# Add Button
add_button = tk.Button(
    root,
    text="Add Task",
    width=15,
    command=add_task
)
add_button.pack(pady=5)

# Task List
task_listbox = tk.Listbox(
    root,
    width=50,
    height=12,
    font=("Arial", 11)
)
task_listbox.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack()

complete_button = tk.Button(
    button_frame,
    text="Mark Completed",
    command=mark_completed
)
complete_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    command=delete_task
)
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(
    button_frame,
    text="Clear All",
    command=clear_tasks
)
clear_button.grid(row=0, column=2, padx=5)

# Run Application
root.mainloop()
