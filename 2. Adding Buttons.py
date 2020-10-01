import tkinter as tk
from tkinter import ttk

def greet():
    print("Good Day !")

root = tk.Tk()
button1 = ttk.Button(root, text = "Greet", command = greet)
button1.pack(side='left')

button2 = ttk.Button(root, text = "Quit", command = root.destroy)
button2.pack(side='left')

root.mainloop()
