from tkinter import *
# standard setting
root = Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("My GUI")

label = Label(root, text='Hello World!', padx=20, pady=20)
label.config(font=("Segoe UI", 20)) # applying font
label.pack()

root.mainloop()