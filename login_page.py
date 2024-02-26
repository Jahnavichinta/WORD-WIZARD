import tkinter as tk
import sqlite3
from tkinter import messagebox

root = tk.Tk()
root.geometry("350x360")
root.title("masthIshQ")
root.configure(background="peru")

Tops = tk.Frame(root, bg="peru", pady=2, width=300, height=70, relief="ridge")
Tops.grid(row=0, column=0, pady=(10, 0))

Mid = tk.Frame(root, bg="peru", pady=2, width=300, height=150, relief="ridge")
Mid.grid(row=1, column=0)

Down = tk.Frame(root, bg="peru", pady=2, width=300, height=80, relief="ridge")
Down.grid(row=2, column=0, pady=(0, 10))

lblTitle = tk.Label(Tops, font=("arial", 15, "bold"), text="                 masthIshQ             ", bd=15, bg="peru", fg="cornsilk")
lblTitle.grid(row=0, column=0)

name_label = tk.Label(Mid, font=("arial", 15, "bold"), text="Name", bd=15, bg="peru", fg="cornsilk")
name_label.grid(row=0, column=0, padx=(10, 0))

entry_name = tk.Entry(Mid)
entry_name.grid(row=0, column=1)

age_label = tk.Label(Mid, font=("arial", 15, "bold"), text="Age", bd=15, bg="peru", fg="cornsilk")
age_label.grid(row=1, column=0, padx=(10, 0))

entry_age = tk.Entry(Mid)
entry_age.grid(row=1, column=1)

def checker():
    name = entry_name.get()
    age = entry_age.get()
    
    if not name or not age:
        messagebox.showwarning("Incomplete Details", "Please fill all details")
    else:
        submit()
        messagebox.showinfo("Success", "Successfully submitted")

def submit():
    name_val = entry_name.get()
    age_val = entry_age.get()
    
    conn = sqlite3.connect("xyz1.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS userdata (
                      name TEXT NOT NULL,
                      age INTEGER NOT NULL
                    )''')
    cursor.execute("INSERT INTO userdata (name, age) VALUES (?, ?)", (name_val, age_val))
    conn.commit()
    conn.close()

submit_button = tk.Button(Down, text="Submit", font=("Arial", 10, "bold"), width=6, bg="bisque", command=checker)
submit_button.grid(row=0, column=0, pady=10)

root.mainloop()