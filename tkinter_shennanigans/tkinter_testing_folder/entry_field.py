from tkinter import *
from typing import * 
root = Tk()

def get_name() -> Label:
    if name_field.get() == "name":
        return None
    confirmed: Label = Label(root, text=f"Hello {name_field.get()}")
    confirmed.pack()
    name_field.delete(0, "end")
    name_field.insert(0, "name")
    return None
    

info: Label = Label(root, text="Please insert your name")
name_field = Entry(root, width= 20, fg="grey", state="normal")
# name_field.insert(index=0, string="name")
confirmation: Button = Button(root, text="press to confirm", command=get_name)

info.pack()
name_field.pack()
confirmation.pack()

root.mainloop()