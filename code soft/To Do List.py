import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("📝 My To-Do List")
root.geometry("650x450")
root.config(bg="#f0f4f7")

heading_font = ("Helvetica", 18, "bold")
task_font = ("Helvetica", 12)

tasks = []

def add_task():
    task_text = task_entry.get().strip()
    if task_text == "":
        messagebox.showwarning("Input Error", "Please enter a task!")
        return
    tasks.append({"task": task_text, "done": False})
    task_entry.delete(0, tk.END)
    refresh_tasks()

def mark_done(index):
    tasks[index]["done"] = not tasks[index]["done"]
    refresh_tasks()

def delete_task(index):
    del tasks[index]
    refresh_tasks()

def refresh_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()

    for i, task in enumerate(tasks):
        frame = tk.Frame(task_frame, bg="#ffffff", bd=2, relief="groove")
        frame.pack(fill="x", pady=4, padx=5)

        color = "#a3f7bf" if task["done"] else "#fff"
        frame.config(bg=color)

        lbl = tk.Label(frame, text=task["task"], font=task_font, bg=color)
        lbl.pack(side="left", padx=10, pady=5)

        done_btn = tk.Button(frame, text="✔", command=lambda i=i: mark_done(i), bg="#4CAF50", fg="white", width=3)
        done_btn.pack(side="right", padx=5)

        del_btn = tk.Button(frame, text="🗑", command=lambda i=i: delete_task(i), bg="#e74c3c", fg="white", width=3)
        del_btn.pack(side="right", padx=5)

left_frame = tk.Frame(root, bg="#dceefb", width=220)
left_frame.pack(side="left", fill="y")

title_lbl = tk.Label(left_frame, text="My Tasks", bg="#dceefb", fg="#1e3d59", font=heading_font)
title_lbl.pack(pady=20)

task_entry = tk.Entry(left_frame, width=25, font=task_font)
task_entry.pack(pady=10, padx=10)

add_btn = tk.Button(left_frame, text="Add Task", command=add_task, bg="#1e90ff", fg="white", font=("Arial", 11, "bold"))
add_btn.pack(pady=5)

right_frame = tk.Frame(root, bg="#f0f4f7")
right_frame.pack(side="right", fill="both", expand=True)

task_frame = tk.Frame(right_frame, bg="#f0f4f7")
task_frame.pack(fill="both", expand=True, pady=10)

root.mainloop()

