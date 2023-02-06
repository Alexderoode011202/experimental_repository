from tkinter import *
from tkinter import Image as Img
from PIL import ImageTk, Image
from typing import List
# IMPOR IMAGE AFTER EVERYTHING ELSE

root = Tk()

paths: List[str] = [
    "C:/Users/Alexd/Downloads/metropolis.jpg",
    "C:/Users/Alexd/Downloads/ralsei's cake.png",
    "C:/Users/Alexd/Downloads/Berdley.png",
    "C:/Users/Alexd/Downloads/kromer.jpeg",
    "C:/Users/Alexd/Downloads/Deltarune-Ch-3.png"
]
images: List[Label] = []
for path in paths:
    images.append(Label(root, image=ImageTk.PhotoImage(Image.open(path))))

current: Label = images[0]


def switcher(direction: str) -> None:
    global current
    global images
    index: int = images.index(current)
    if direction == ">":
        if index == len(images) -1:
            current = images(0)
        else:
            current = images[index+1]
    elif direction == "<":
        if index == 0:
            current=images(len(images)-1)
        else:
            current = images(index-1)
    else:
        raise ValueError(f"Function does not support '{direction}'")

def remove()-> None:
    current.grid_forget()

def refresh() -> None:
    current.grid(row=0, column=0)
    
current.grid(row=0,column=0)
back: Button = Button(root, text="<<", command= lambda x="<": [current.grid_forget(), switcher(x), current.grid(row=0, column=0, columnspan=3)])
forth: Button = Button(root, text="forth", command= print("nah"))
exit: Button = Button(root, text=">>", command=root.quit)

back.grid(row=1, column=0)
exit.grid(row=1, column=0)
forth.grid(row=1, column=2)

root.mainloop()





