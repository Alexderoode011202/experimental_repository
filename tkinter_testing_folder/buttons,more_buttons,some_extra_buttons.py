from tkinter import *

root = Tk()

button = Button(root, text="I can't be clicked :(", state= DISABLED)
button_1 = Button(root, text="But I can be clicked! :D")

button.pack()
button_1.pack()

root.mainloop()