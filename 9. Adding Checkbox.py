# Adding checkbutton
from tkinter import *
# standard setting
root = Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("My GUI")

selected_option = StringVar()


def print_opt():
    print(selected_option.get())


check = Checkbutton(root, text='Example', variable=selected_option, command=print_opt, onvalue='ON', offvalue='OFF')
check.pack()
root.mainloop()
