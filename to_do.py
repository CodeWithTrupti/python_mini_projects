import tkinter as t
from tkinter import messagebox
def add_task():
    task = entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        update_listbox()
        entry.delete(0, t.END)
    else:
        messagebox.show("Input Error")
def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            update_listbox()
        else:
            messagebox.show("Error")
    else:
        messagebox.show("Error", "Please select a task.")
def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        if 0 <= index < len(tasks):
            tasks.pop(index)
            update_listbox()
        else:
            messagebox.show("Error")
    else:
        messagebox.show("Error", "Please select a task.")
def update_listbox():
    listbox.delete(0, t.END)
    for task in tasks:
        status = "Done" if task["done"] else "Not Done"
        listbox.insert(t.END, f"{task["task"]} - {status}")
tasks = []
root = t.Tk()
root.title("To-Do List")
entry = t.Entry(root, width=40)
entry.pack(pady=10)
add_button = t.Button(root, text="Add your Task", command=add_task)
add_button.pack(pady=5)
listbox = t.Listbox(root, width=50, height=10)
listbox.pack(pady=10)
mark_done_button = t.Button(root, text="Mark your task as Done", command=mark_done)
mark_done_button.pack(pady=5)
delete_button = t.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)
root.mainloop()

