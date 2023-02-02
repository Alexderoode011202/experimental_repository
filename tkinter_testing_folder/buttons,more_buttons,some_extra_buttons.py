from tkinter import *

root = Tk()
def some_func():
    print("sup!")
    widget = Label(root, text="I did something!", fg= "red")
    widget.pack()
button = Button(root, text="I can't be clicked :(", state= DISABLED)
button_1 = Button(root, text="But I can be clicked! :D", command= some_func, fg= "blue", bg="#246B58")

button.pack()
button_1.pack()

root.mainloop()