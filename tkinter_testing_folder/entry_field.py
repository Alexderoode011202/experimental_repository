from tkinter import *
from typing import * 
root = Tk()

def name_plz(message: str) -> Tuple[Label, Entry, Label, Entry, Button]:
    """Creates a label, entry, button set which is meant for user input"""
    info = Label(root, text=message)
    input = Entry(root, width= 2)
    extra_info = Label(root, text= "And your last name plz")
    input_2 = Entry(root, width = 50, fg= "white")
    send = Button(root, text= "Submit", fg="#ff0000")
    return (info, input, extra_info, input_2, send)

a, b, c, d, e = name_plz("What is your name?")

widget: Widget
for num, widget in enumerate((a,b,c, d ,e)):
    widget.grid(column=0, row=num)

root.mainloop()
