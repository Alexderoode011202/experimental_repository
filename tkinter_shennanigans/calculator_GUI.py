from tkinter_shennanigans.calculator_class import Calculator
from tkinter import *
from functools import partial
from typing import List, Dict
root = Tk()
calc = Calculator()

number_list: List[Button] = {}
for num in range(0,10):

    number_list.append(Button(root, text= str(num), width=10, height=10, command= partial(calc.add_number, str(num))))

for num, button in enumerate(number_list):
    button.grid(column=num, row=1)

root.mainloop()
