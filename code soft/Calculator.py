import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("🧮 Modern Calculator")
root.geometry("320x420")
root.config(bg="#dfe6e9")
root.resizable(False, False)

display = tk.Entry(root, font=("Helvetica", 20, "bold"), border=0, relief="ridge", bg="#ecf0f1", justify="right")
display.pack(pady=30, padx=10, ipady=10, fill="x")

def on_click(symbol):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(symbol))

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        messagebox.showerror("Error", "Invalid Input!")

def create_button(parent, text, row, col, bg, fg="#2d3436", cmd=None):
    button = tk.Button(parent, text=text, font=("Helvetica", 14, "bold"),
                       bg=bg, fg=fg, width=5, height=2, relief="flat",
                       activebackground="#b2bec3", command=cmd)
    button.grid(row=row, column=col, padx=5, pady=5)
    return button

frame = tk.Frame(root, bg="#dfe6e9")
frame.pack()

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        create_button(frame, text, row, col, bg="#0984e3", fg="white", cmd=calculate)
    elif text in {"+", "-", "*", "/"}:
        create_button(frame, text, row, col, bg="#fdcb6e", fg="#2d3436", cmd=lambda t=text: on_click(t))
    else:
        create_button(frame, text, row, col, bg="#74b9ff", fg="white", cmd=lambda t=text: on_click(t))

clear_btn = tk.Button(root, text="C", font=("Helvetica", 14, "bold"), bg="#d63031", fg="white",
                      width=10, relief="flat", command=clear)
clear_btn.pack(pady=10)

root.mainloop()
