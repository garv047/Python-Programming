# 2-basic calculator for performing basic arithmetic operations
import tkinter as tk

# Function to update expression
def press(num):
    entry.insert(tk.END, num)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")
root.geometry("250x300")

entry = tk.Entry(root, font=("Arial", 16), justify="right")
entry.pack(fill="both", ipadx=8, ipady=8, pady=10)

buttons = [
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','.','=','+')
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        if btn == "=":
            tk.Button(frame, text=btn, command=equal).pack(side="left", expand=True, fill="both")
        else:
            tk.Button(frame, text=btn, command=lambda b=btn: press(b)).pack(side="left", expand=True, fill="both")

tk.Button(root, text="Clear", command=clear).pack(fill="both")

root.mainloop()
