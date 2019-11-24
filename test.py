'''
Basic GUI Structure
'''
from tkinter import *

root = Tk()
root.title("Trepp-Spear Mapping")
root.columnconfigure(0, weight=1)

def deal_date(*args):
    deal_val = deal.get()
    date_val = date.get()
    return deal_val, date_val

deal = StringVar()
date = StringVar()

input_frame = Frame(root)
input_frame.grid(padx=10, pady=10)

deal_label = Label(input_frame, text='Deal Name: ')
deal_label.grid(row=0, column=0, padx=(0, 10))

deal_label = Label(input_frame, text='Date: ')
deal_label.grid(row=0, column=2, padx=(0, 10))

ent1 = Entry(input_frame, width=25,textvariable=deal)
ent1.grid(row=0, column=1, padx=(0, 10))
ent1.focus()
ent2 = Entry(input_frame, width=15,textvariable=date)
ent2.grid(row=0, column=4, padx=(0, 10))

button_frame = Frame(root)
button_frame.grid(sticky = "EW")
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
bt1 = Button(button_frame, text = "Load Deal", command=deal_date)
bt1.grid(row=0, column=0, sticky = "EW")
bt2 = Button(button_frame, text = "Get Trepp Mapping")
bt2.grid(row=0, column=1, sticky = "EW")
bt3 = Button(button_frame, text = "Exit")
bt3.grid(row=0, column=2, sticky = "EW")

root.mainloop()
