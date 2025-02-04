import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate():
    try:
        length = int(entry_length.get())
        if length < 1:
            raise ValueError("Password length must be at least 1")
        
        generated_password = generate_password(length)
        entry_password.delete(0, tk.END)  
        entry_password.insert(0, generated_password) 
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

root = tk.Tk()
root.title("Password Generator")

label_length = tk.Label(root, text="Enter password length:")
label_length.pack(pady=20)

entry_length = tk.Entry(root)
entry_length.pack(pady=20)

button_generate = tk.Button(root, text="Generate Password", command= generate)
button_generate.pack(pady=20)

label_password = tk.Label(root, text="Generated Password:")
label_password.pack(pady=20)

entry_password = tk.Entry(root, width=50)
entry_password.pack(pady=20)

root.mainloop()


