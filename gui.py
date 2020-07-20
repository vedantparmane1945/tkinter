from tkinter import *


class gui:
    def __init__(self, master):
        self.master = master

        self.input_frame = Frame(master)
        self.input_frame.grid(padx=10, pady=10)
        self.name_label = Label(self.input_frame, text='Name: ')
        self.name_label.grid(row=0, column=0, padx=(0, 10))

        self.ent1 = Entry(self.input_frame, width=18, textvariable=StringVar())
        self.ent1.grid(row=0, column=1, padx=(0, 10))
        self.ent1.focus()

        self.button_frame = Frame(master)
        self.button_frame.grid(sticky="EW")
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.bt1 = Button(self.button_frame, text="Submit", command=self.get_name)
        self.bt1.grid(row=0, column=0, sticky="EW")
        self.bt2 = Button(self.button_frame, text="Done", command=master.destroy)
        self.bt2.grid(row=0, column=1, sticky="EW")

    def get_name(self):
        name = self.ent1.get()
        self.master.destroy()

root = Tk()
gui(root)
root.mainloop()
