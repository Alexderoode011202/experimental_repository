from tkinter import *
# Here we make the main object for tkinter
root = Tk()

#Create a label 
label_1 = Label(root, text="Hello world!")
label_2 = Label(root, text="I have no clue what I am doing")
button = Button(root, text= "Click me?")
# Now we force it onto the screen
label_1.pack()
label_2.pack()
button.pack()
# And here we run the main loop
root.mainloop()