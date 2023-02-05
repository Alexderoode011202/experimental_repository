from calculator_class import Calculator
from calculator_class import itersplit
from tkinter import *
from functools import partial
from typing import List, Dict, Union

root = Tk()
calc = Calculator()

operators: List[str] = ['+', '-', '*', "/"]
operators_button_list: List[Button] = []
number_button_list: List[Button] = []

# Create and grid the screen
screen = Entry(root, width=10)
screen.grid(column=0, row=0)

# Create the numbers
number_button_list.append(Button(root, text = "1", width=10, height=3, command= lambda: [calc.add_number("1"), screen.delete(0, "end"), screen.insert(0,calc.get_current_num())]))
number_button_list.append(Button(root, text = "2", width=10, height=3, command= lambda: [calc.add_number("2"), screen.delete(0, "end"), screen.insert(0,calc.get_current_num())]))
number_button_list.append(Button(root, text = "3", width=10, height=3, command= lambda: [calc.add_number("3"), screen.delete(0, "end"), screen.insert(0,calc.get_current_num())]))
number_button_list.append(Button(root, text = "4", width=10, height=3, command= lambda: [calc.add_number("4"), screen.delete(0, "end"), screen.insert(0,calc.get_current_num())]))
number_button_list.append(Button(root, text = "5", width=10, height=3, command= lambda: [calc.add_number("5"), screen.delete(0, "end"), screen.insert(0,calc.get_current_num())]))
number_button_list.append(Button(root, text = "6", width=10, height=3, command= lambda: [calc.add_number("6"), screen.delete(0, "end"), screen.insert(0,calc.get_current_num())]))
number_button_list.append(Button(root, text = "7", width=10, height=3, command= lambda: [calc.add_number("7"), screen.delete(0, "end"), screen.insert(0,calc.get_current_num())]))
number_button_list.append(Button(root, text = "8", width=10, height=3, command= lambda: [calc.add_number("8"), screen.delete(0, "end"), screen.insert(0,calc.get_current_num())]))
number_button_list.append(Button(root, text = "9", width=10, height=3, command= lambda: [calc.add_number("9"), screen.delete(0, "end"), screen.insert(0,calc.get_current_num())]))

zero = Button(root, text= "0", height=3, width=10, command=lambda: [calc.add_number("0"), screen.delete(0, "end"), screen.insert(0,calc.get_current_num())])
filler_1 = Button(root, height=3, width=10, text = "-del", command= lambda: [calc.remove_number(), screen.delete(0, "end"), screen.insert(0, calc.get_current_num())])

def calculate_results() -> None:
    answer: Union[float, int] = calc.calculate()
    screen.delete(0, "end")
    screen.insert(0, f"{answer}")

filler_2 = Button(root, height=3, width=10, text="=", command=calculate_results)
    
# some_list = [filler_1, zero, filler_2]
number_button_list.extend([filler_1, zero, filler_2])

# Grid the numbers + diverse
print(f"list length: {len(number_button_list)}")
split_num_but_list: List[List[Widget]] = itersplit(iterable=number_button_list, n_chunks= 4)
for row_num, row in enumerate(split_num_but_list):
    for column, button in enumerate(row):
        # print(f"row: {row_num}, column: {column}")
        button.grid(row=row_num+1, column=column)

def oper_caller(operator: str):
    calc.add_operator(operator= operator)
    screen.delete(0, "end")
    
# Create the operators
print("operator creation")
for num, op in enumerate(operators):
    print(op)
    operators_button_list.append(Button(root, text=op, width = 10, height=3, command= partial(oper_caller, op)))

# Grid the operators
for num ,op in enumerate(operators_button_list):
    op.grid(column=3, row =num+1)

root.mainloop()
