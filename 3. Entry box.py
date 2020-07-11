import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Trepp-Spear Mapping")
input_frame1 = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame1.pack(fill="both")
ttk.Label(input_frame1, text='Deal Name: ').pack(side='left', padx=(0, 10))

ent = ttk.Entry(input_frame1, width=15, textvariable=tk.StringVar())
ent.pack(side='left')
ent.focus()
input_frame2 = ttk.Frame(input_frame1, padding=(20, 10))
input_frame2.pack(fill="both")
ttk.Button(input_frame2, text="Load Deal").pack(side='left')
ttk.Button(input_frame2, text="Get Trepp Name").pack(side='left')
ttk.Button(input_frame2, text="Quit", command=root.destroy).pack(side='left')

root.mainloop()
