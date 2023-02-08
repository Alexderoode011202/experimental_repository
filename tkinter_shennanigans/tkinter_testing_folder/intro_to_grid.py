from tkinter import * 

# Create the root again
root = Tk()

my_label = Label(root, text= "My name is:[ (&151079#@ ]")
my_label_2 = Label(root, text= "I don't like talking about myself")
my_label_3 = Label(root, text= "aa")

my_label.grid(row= 0, column= 0)
my_label_2.grid(row= 1, column = 2)
my_label_3.grid(row =2, column = 1)
root.mainloop()

# Here I just started messing around more with the code just for the sake of it
another_root = Tk()

my_label_4 = Label(another_root, text= "My name is:[ (&151079#@ ]")
my_label_5 = Label(another_root, text= "I don't like talking about myself")
my_label_6 = Label(another_root, text= "aa")

my_label_4.grid(row=0, column = 0)
my_label_5.grid(row=1, column = 0)
my_label_6.grid(row=2, column=0)
another_root.mainloop()

