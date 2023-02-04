from tkinter import *
from typing import List, Union, Iterable, Tuple
from functools import partial

class UnsplittableException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg = "This iterable is not evenly diviseable!"

root = Tk()
num_list: List[int] = []
class Calculator:
    def __init__(self):
        self.num_list: List[str] = []
        self.operator_list: List[str] = []
        self.current_index : int = 0
        self.current_num: str = ""


    def add_number(self, num: str) -> None:
        """ 
        adds a number for the calculator to process
        :param num: takes the number to process
        :returns: None
        """
        new_int: bool = False
        
        if type(num) != type("test"):
            num = str(num)

        if self.current_num == "" and num == "0":
            return None
        else:
            self.current_num = self.current_num + num

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

        if type(operator) != type("test"):
            num = str(num)

        self.current_index += 1
        self.operator_list.append(operator)
        self.num_list.append(self.current_num)
        self.current_num = ""
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


# Is meant to be used to the GUI
def itersplit(iterable: Iterable, n_chunks: int) -> List[List[any]]:
    if len(iterable)%n_chunks != 0:
        raise UnsplittableException
    seperated_list: list = []
    chunk_size: int = int(len(iterable)/n_chunks)
    print(f"CHUNK_SIZE: {chunk_size}")

    for i in range(0, len(iterable), chunk_size):
        seperated_list.append(iterable[i:i+chunk_size])

    return seperated_list


# for i in range(0, len(data), 100):
#   chunk = data[i:i + 100]




