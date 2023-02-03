"""
from tkinter import *

root = Tk()

mylabel= Label(root, text="You have a virus!:D")

# Shoving it onto the screen
mylabel.pack()

root.mainloop()
""" 

import tkinter as tk

def on_button_click():
    print("Button was clicked!")

root = tk.Tk()

button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack()

root.mainloop()