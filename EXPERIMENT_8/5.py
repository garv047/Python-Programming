# 5-login and signup
import tkinter as tk

def signup():
    u = e1.get()
    p = e2.get()

    if u and p:
        with open("users.txt", "a") as f:
            f.write(u + "," + p + "\n")
        result.config(text="Signup Successful")
    else:
        result.config(text="Fill all fields")

def login():
    u = e1.get()
    p = e2.get()

    try:
        with open("users.txt", "r") as f:
            users = f.readlines()

        for user in users:
            username, password = user.strip().split(",")
            if u == username and p == password:
                result.config(text="Login Successful")
                return

        result.config(text="Invalid Login")
    except:
        result.config(text="No users found")

root = tk.Tk()
root.title("Login System")
root.geometry("300x220")

tk.Label(root, text="Login / Signup", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Username").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Password").pack()
e2 = tk.Entry(root, show="*")
e2.pack()

tk.Button(root, text="Login", command=login).pack(pady=5)
tk.Button(root, text="Signup", command=signup).pack()

result = tk.Label(root, text="")
result.pack(pady=5)

root.mainloop()
