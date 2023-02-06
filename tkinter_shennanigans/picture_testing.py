from tkinter import *
from PIL import Image, ImageTk
from typing import List

root = Tk()
root.iconbitmap("tkinter_shennanigans/scout (1).ico")

paths: List[str]= ["tkinter_shennanigans/Berdley.png",
    "tkinter_shennanigans/kromer.jpeg",
    "tkinter_shennanigans/Deltarune-Ch-3.png",
    "tkinter_shennanigans/ralsei's cake.png",
    "tkinter_shennanigans/Pootis Mann.jpg"
    ]

images: List[PhotoImage] = []
for path in paths:
    images.append(ImageTk.PhotoImage(Image.open(path)))

current: PhotoImage = images[0]


def switch(operator: str) -> None:
    global current
    global images
    index = images.index(current)
    
    if operator == "<":
        if index == images[0]:
            current = images[len(images)-1]
        else:
            current = images[index-1]
    elif operator == ">":
        if current == images[len(images)-1]:
            current = images[0]
        else:
            current= images[index+1]
    else:  raise ValueError(f"Operator: {operator} does not get supported")

shower: Label = Label(root, image=current)

back: Button = Button(root, width=7, height=3,text= '<<', command= lambda x= "<": [switch(x,), shower.configure(image=current)])
forth: Button = Button(root, width=7, height=3, text=">>", command = lambda x=">": [switch(x,), shower.configure(image=current), print(current)])
exit: Button = Button(root,width=7, height=3, text="Quit", command=root.quit)
shower.grid(column= 0, columnspan=3)
back.grid(row=1, column=0)
exit.grid(row=1, column=1)
forth.grid(row=1, column=2)

root.mainloop()