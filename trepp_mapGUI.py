from tkinter import *
from PIL import Image, ImageTk


# Main function to start trepp mapping
def start_mapping():
    return get_dealname(), start_date(), end_date()


# Validate
def run_validation():
    pass


# Current month beginning and end date
def default_dates():
    pass


def get_dealname():
    return ent1.get()


def start_date():
    return ent2.get()


def end_date():
    return ent3.get()


def quit_window():
    root.destroy()


root = Tk()
root.geometry("650x140")
root.resizable(False, False)
root.title("Trepp-Spear Note Mapping")
root.columnconfigure(0, weight=1)
img = Image.open("C:\\Users\\Siddhesh\\PycharmProjects\\tkinter\\blackrock_logo.png").resize((90, 65))
photo = ImageTk.PhotoImage(img)
label = Label(root, image=photo)
label.grid()

input_frame = Frame(root)
input_frame.grid(padx=10, pady=10)

deal_label = Label(input_frame, text='Deal Name: ')
deal_label.grid(row=0, column=0, padx=(0, 10))

start_date_label = Label(input_frame, text='Start Date: ')
start_date_label.grid(row=0, column=2, padx=(0, 10))

end_date_label = Label(input_frame, text='End Date: ')
end_date_label.grid(row=0, column=10, padx=(0, 10))

checkbox_label = Checkbutton(input_frame, text='Current Month', command=default_dates, onvalue='ON', offvalue='OFF')
checkbox_label.grid(row=0, column=16, padx=(0, 10))

ent1 = Entry(input_frame, width=18, textvariable=StringVar())
ent1.grid(row=0, column=1, padx=(0, 10))
ent1.focus()
ent2 = Entry(input_frame, width=12, textvariable=StringVar())
ent2.grid(row=0, column=4, padx=(0, 10))
ent3 = Entry(input_frame, width=12, textvariable=StringVar())
ent3.grid(row=0, column=14, padx=(0, 10))

button_frame = Frame(root)
button_frame.grid(sticky="EW")
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
bt1 = Button(button_frame, text="Get Trepp Mapping", command=start_mapping)
bt1.grid(row=0, column=0, sticky="EW")
bt2 = Button(button_frame, text="Validate data", command=run_validation)
bt2.grid(row=0, column=1, sticky="EW")
bt3 = Button(button_frame, text="Quit", command=root.destroy)
bt3.grid(row=0, column=2, sticky="EW")

root.mainloop()
