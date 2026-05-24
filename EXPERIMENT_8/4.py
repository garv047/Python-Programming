# 4-task manager
import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

root = tk.Tk()
root.title("Task Manager")
root.geometry("300x300")

tk.Label(root, text="Task Manager", font=("Arial", 14)).pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Add Task", command=add_task).pack()

listbox = tk.Listbox(root)
listbox.pack(pady=10, fill="both", expand=True)

tk.Button(root, text="Delete Task", command=delete_task).pack()

root.mainloop()
