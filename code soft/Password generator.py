import tkinter as tk
from tkinter import messagebox
import random
import string

root = tk.Tk()
root.title("🔐 Modern Password Generator")
root.geometry("420x400")
root.config(bg="#cfd9df")  
root.resizable(False, False)

title_font = ("Helvetica", 18, "bold")
label_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

password_var = tk.StringVar()
length_var = tk.IntVar(value=12)
include_upper = tk.BooleanVar(value=True)
include_lower = tk.BooleanVar(value=True)
include_digits = tk.BooleanVar(value=True)
include_symbols = tk.BooleanVar(value=True)

def generate_password():
    length = length_var.get()
    chars = ""
    if include_upper.get():
        chars += string.ascii_uppercase
    if include_lower.get():
        chars += string.ascii_lowercase
    if include_digits.get():
        chars += string.digits
    if include_symbols.get():
        chars += string.punctuation

    if not chars:
        messagebox.showwarning("Warning", "Select at least one character type!")
        return

    password = "".join(random.choice(chars) for _ in range(length))
    password_var.set(password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

frame = tk.Frame(root, bg="#ffffff", bd=3, relief="ridge", highlightbackground="#74b9ff", highlightthickness=2)
frame.place(x=30, y=40, width=360, height=320)

title = tk.Label(frame, text="Password Generator", font=title_font, bg="#ffffff", fg="#2d3436")
title.pack(pady=10)

display = tk.Entry(frame, textvariable=password_var, font=("Consolas", 14, "bold"), width=25,
                   relief="flat", justify="center", bg="#f1f2f6", fg="#2f3542")
display.pack(pady=10)

copy_btn = tk.Button(frame, text="📋 Copy", font=("Helvetica", 10, "bold"),
                     bg="#74b9ff", fg="white", relief="flat", command=copy_password)
copy_btn.pack(pady=5)

len_frame = tk.Frame(frame, bg="#ffffff")
len_frame.pack(pady=10)
len_lbl = tk.Label(len_frame, text="Password Length:", bg="#ffffff", font=label_font)
len_lbl.pack(side="left")
slider = tk.Scale(len_frame, from_=4, to=24, orient="horizontal", variable=length_var,
                  bg="#ffffff", troughcolor="#74b9ff", fg="#2d3436", highlightthickness=0)
slider.pack(side="left", padx=10)

check_frame = tk.Frame(frame, bg="#ffffff")
check_frame.pack(pady=10)
tk.Checkbutton(check_frame, text="Uppercase", variable=include_upper, bg="#ffffff", font=label_font).grid(row=0, column=0)
tk.Checkbutton(check_frame, text="Lowercase", variable=include_lower, bg="#ffffff", font=label_font).grid(row=0, column=1)
tk.Checkbutton(check_frame, text="Digits", variable=include_digits, bg="#ffffff", font=label_font).grid(row=1, column=0)
tk.Checkbutton(check_frame, text="Symbols", variable=include_symbols, bg="#ffffff", font=label_font).grid(row=1, column=1)

generate_btn = tk.Button(frame, text="✨ Generate Password", font=button_font,
                         bg="#0984e3", fg="white", relief="flat", command=generate_password)
generate_btn.pack(pady=15)

root.mainloop()
