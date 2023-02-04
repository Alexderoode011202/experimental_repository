from calculator_class import Calculator
from calculator_class import itersplit
from tkinter import *
from functools import partial
from typing import List, Dict

root = Tk()
calc = Calculator()

operators: List[str] = ['+', '-', '*', "/"]
operators_button_list: List[Button] = []
number_button_list: List[Button] = []


# Create the numbers
for num in range(1,10):
    number_button_list.append(Button(root, text= str(num), width=10, height=3, command= partial(calc.add_number, str(num))))
zero = Button(root, text= "0", height=3, width=10, command=partial(calc.add_number, '0'))
filler_1 = Label(root, height=3, width=10)
filler_2 = Label(root, height=3, width=10)
# some_list = [filler_1, zero, filler_2]
number_button_list.extend([filler_1, zero, filler_2])

# Grid the numbers
split_num_but_list: List[List[Widget]] = itersplit(iterable=number_button_list, n_chunks= 4)
for row_num, row in enumerate(split_num_but_list):
    for column, button in enumerate(row):
        print(f"row: {row_num}, column: {column}")
        button.grid(row=row_num, column=column)

# Create the operators
for op in operators:
    operators_button_list.append(Button(root, text=op, width = 10, height=3, command= partial(calc.add_operator, op)))



root.mainloop()
