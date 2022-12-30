# We have to import both numpy and pandas
import numpy as np
import pandas as pd
import csv

# A Series is a one-dimensional type of data to be stored
s = pd.Series([4,6,8,10], index=["A", "B", "C", "D"])

# print(s)

# Series can be instantiated by dictionaries as well
dict_series = pd.Series({1: 1.0, 2: 2.0, 3: 3.0, 4: 4.0})
# print(dict_series)

# If not giving an index, the index will be integer numbers
no_index_series = pd.Series([1,2,3,4,5])
print(no_index_series)

# If the series only receives a numerical input: it will be repeated along the index
# If also not giving an index, the index will just be 0 and end there
numerical_series = pd.Series(3)
print(numerical_series)

# This was just to mess around with Series
# and get a feel for them
"""
with open ("test_csv.csv", "r") as file:
    reader = tuple(csv.reader(file))
    names_list: list = []
    grades_list: list = []
    for line in reader:
        try:
            names_list.append(line[0])
            grades_list.append(line[1])\

        except IndexError:
            continue

test_series = pd.Series(grades_list, index=names_list)

print(test_series)
"""


