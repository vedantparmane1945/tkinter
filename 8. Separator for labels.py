# separating 2 label
from tkinter import ttk
from tkinter import *
# standard setting
root = Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("My GUI")

label1 = Label(root, text='Hello World!', padx=20, pady=20)
label1.config(font=("Segoe UI", 20)) # applying font
label1.pack()

ttk.Separator(root, orient="horizontal").pack(fill='x') # small separator is visible on output

label2 = Label(root, text='Hello Universe!', padx=20, pady=20)
label2.config(font=("Segoe UI", 20)) # applying font
label2.pack()

root.mainloop()