import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password should be at least 4 characters long.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="Enter password length:", font=("Arial", 17)).pack(pady=10)
length_entry = tk.Entry(root, font=("Arial", 18), justify='center')
length_entry.pack()

tk.Button(root, text="Generate Password", font=("Arial", 18), command=generate_password).pack(pady=10)


result_var = tk.StringVar()
result_label = tk.Entry(root, textvariable=result_var, font=("Arial", 12), width=30, justify='center')
result_label.pack(pady=5)

root.mainloop()
