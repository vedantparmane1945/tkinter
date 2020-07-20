from tkinter import *
from tkinter import ttk
import datetime
from tkcalendar import DateEntry
now = datetime.datetime.now()

root = Tk()

cal = DateEntry(root, width=30, bg="darkblue", fg="white", year=now.year)
cal.delete(0, "end")
cal.grid()

root.mainloop()
