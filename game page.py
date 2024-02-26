import tkinter as tk

root = tk.Tk()
root.geometry("350x360")
root.title("Games")
root.configure(background="#F3CCF3")

game1 = tk.Button(root, text="   Word Quest   ", fg="#392467", bg = "#FFE5E5", font=('Arial', 13 ,"bold"))
game1.grid(row=0, column=0, padx=100, pady=80)

game2 = tk.Button(root, text="   Quiz Quest   ", fg="#392467", bg = "#FFE5E5", font=('Arial', 13 ,"bold"))
game2.grid(row=1, column=0)

root.mainloop()