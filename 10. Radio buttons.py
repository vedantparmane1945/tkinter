# Radio buttons
from tkinter import *
# standard setting
root = Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("My GUI")

storage_var = StringVar()
opt_one = Radiobutton(root, text='Option 1', variable=storage_var, value='first')
opt_one.pack()
opt_two = Radiobutton(root, text='Option 2', variable=storage_var, value='second')
opt_two.pack()
opt_three = Radiobutton(root, text='Option 3', variable=storage_var, value='third')
opt_three.pack()
root.mainloop()