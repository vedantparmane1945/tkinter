# Adding text
from tkinter import *

# standard setting
root = Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("My GUI")

text = Text(root, height=8)
text.pack()
text.insert("1.0", "Please enter the comment...")# 1.0 means 1st line 0th character (rule)

root.mainloop()