from tkinter import *
from typing import List, Union
from functools import partial
root = Tk()
num_list: List[int] = []
class Calculator:
    def __init__(self):
        self.num_list: List[str] = []
        self.operator_list: List[str] = []
        self.current_index : int = 0

    def add_number(self, num: str) -> None:
        """ 
        adds a number for the calculator to process
        :param num: takes the number to process
        :returns: None
        """
        new_int: bool = False
        if type(num) != type("test"):
            num = str(num)

        # Check whether we have a new number indeed
        try: 
            current_num = self.operator_list[self.current_index]
        except IndexError:
            current_num = ""
            new_int = True

        #add to the current number
        current_num = current_num + num

        #Add it to the number list in one way or another
        if new_int:
            self.num_list[self.current_index] = current_num
        else:
            self.num_list.append(current_num)

        return None


    def remove_number(self) -> None:
        """ 
        removes a number from the current number if it has any numbers in it
        """
        current_num = self.num_list[self.current_index]

        if current_num == "":
            return None
        else:
            current_num = current_num[:-1]
        return None

    def add_operator(self, operator: str):
        """ 
        adds a parameter to the operator.
        :param operator: takes an operator in the form of a string, and accepts it in the calculator.
        :returns: None
        """

        if type(num) != type("test"):
            num = str(num)

        self.current_index += 1
        self.operator_list.append(operator)
        return None
    
    def calculate(self) -> Union[int, float]:
        """ 
        calculates using the given numbers and operators to perform its calculations
        :returns: result in the form of an integer or float
        """
        result: Union[float, int] = None
        leftover_op: str 
        self.operator_list.append(None)
        num_and_op: List[tuple[str, str]] = zip(self.num_list, self.operator_list)

        for num, op in num_and_op:
            # Very first part
            if result == None:
                result = int(num)
                leftover_op = op

            # Everything else
            else:
                if leftover_op == "-":
                    result = result- int(num)
                elif leftover_op == "+":
                    result = result + int(num)
                elif leftover_op == "*":
                    result = result * int(num)
                elif leftover_op == "/":
                    result = result/int(num)
                leftover_op = op

        return result
