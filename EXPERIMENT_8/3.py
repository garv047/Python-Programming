# 3-student registration for a course
import tkinter as tk
import csv

def register():
    name = e1.get()
    email = e2.get()
    course = e3.get()

    if name and email and course:
        with open("students.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, email, course])

        result.config(text="Saved!")
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
    else:
        result.config(text="Fill all fields")

root = tk.Tk()
root.title("Student Registration")
root.geometry("300x250")

tk.Label(root, text="Student Registration", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Name").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Email").pack()
e2 = tk.Entry(root)
e2.pack()

tk.Label(root, text="Course").pack()
e3 = tk.Entry(root)
e3.pack()

tk.Button(root, text="Register", command=register).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()
