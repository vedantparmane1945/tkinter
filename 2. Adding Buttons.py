import tkinter as tk
from tkinter import ttk

def greet():
    print("Good Day !")

root = tk.Tk()
ttk.Button(root, text = "Greet", command = greet).pack(side='left')
ttk.Button(root, text = "Quit", command = root.destroy).pack(side='left')

root.mainloop()