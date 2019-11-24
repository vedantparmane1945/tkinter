from tkinter import *
from PIL import Image, ImageTk

# standard setting
root = Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("My GUI")

img = Image.open("C:\\Users\\Siddhesh\\PycharmProjects\\Python_Project\\google.png").resize((80, 60))
photo = ImageTk.PhotoImage(img)
label = Label(root, text='This is google logo', image=photo, compound='left') # text will only work with compound, else remove both text and compound
label.pack()

root.mainloop()