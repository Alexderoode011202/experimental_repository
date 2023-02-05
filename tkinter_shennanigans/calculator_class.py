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
        self.result: Union[int, float] = 0



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
        print(f"current: {self.current_num}")
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

        self.current_index += 1
        self.operator_list.append(operator)
        print(operator)
        self.num_list.append(self.current_num)
        self.current_num = ""
        print(f"current: {self.current_num}")
        return None
    
    def calculate(self) -> Union[int, float]:
        """ 
        calculates using the given numbers and operators to perform its calculations
        :returns: result in the form of an integer or float
        """
        # Add final number to the number list
        self.num_list.extend([self.current_num, 'end'])
        self.current_num = ""

        self.operator_list.append('end')

        # set up the entire calculation
        num_and_op: List[tuple[str, str]] = zip(self.num_list, self.operator_list)
        full_calculation: List[Union[int, str]] = []

        print(f"numbers: {self.num_list}")
        print(f"operators: {self.operator_list}")
        # create the full sum: e.g: 3+4+5
        for num, op in num_and_op:
            if num == "end" or op == None:
                full_calculation.extend([num, op])
            else:
                full_calculation.extend([int(num), op])
        
        print(full_calculation)
        for index in range(0,len(full_calculation) -1, 2):

            print(f"stuff: {full_calculation[index]}")
            num_one: int = full_calculation[index]
            try:
                operator: str = full_calculation[index+1]
            except IndexError:
                print(f"result: {num_one}")
                self.start_over()
                return num_one
            try:
                num_two: int = full_calculation[index+2]
            except IndexError:
                print(f"result: {num_one}")
                self.start_over()
                return num_one

            if not operator or not num_two:
                print(f"result: {num_one}")
                return num_one
            
            else:
                if operator == "+":
                    full_calculation[index+2] = num_one + num_two
                elif operator == "*":
                    full_calculation[index+2] = num_one * num_two
                elif operator == "/":
                    full_calculation[index+2] = num_one / num_two
                elif operator == "-":
                    full_calculation[index+2] = num_one-num_two
        
        return None

    def get_current_num(self) -> str:
        return self.current_num

    def get_result(self) -> str:
        return str(self.result)

    def start_over(self) -> None:
        "Sets all the arguments to their standard value"
        self.num_list: List[str] = []
        self.operator_list: List[str] = []
        self.current_index : int = 0
        self.current_num: str = ""
        self.result: Union[int, float] = 0

# Is meant to be used to the GUI
def itersplit(iterable: Iterable, n_chunks: int) -> List[List[any]]:
    if len(iterable)%n_chunks != 0:
        raise UnsplittableException
    seperated_list: list = []
    chunk_size: int = int(len(iterable)/n_chunks)

    for i in range(0, len(iterable), chunk_size):
        seperated_list.append(iterable[i:i+chunk_size])

    return seperated_list

# for i in range(0, len(data), 100):
#   chunk = data[i:i + 100]




