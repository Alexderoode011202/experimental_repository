# We have to import both numpy and pandas
import numpy as np
import pandas as pd
import csv
pd.set_option('mode.chained_assignment', None)
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
            grades_list.append(line[1])

        except IndexError:
            continue

test_series = pd.Series(grades_list, index=names_list)

print(test_series)
"""



test_df = pd.read_csv("/datasets/current.csv", encoding="utf-8")
"""
nl_thing: list = []
for line in test_df["id"]:
    if "nl" in line:
        nl_thing.append(line)
        print(line)


print(test_df.columns)
smaller_df = test_df[["id", "label", "confirmed", "deaths", "recovered"]]


# df[df['A'].str.contains("hello")]
smaller_df = smaller_df[smaller_df["id"].str.contains("nl.")]
print(smaller_df)
print("\n-------------------------------------------------------------------\n")

print(smaller_df.query("deaths > 1300"))
"""


#############
"""
garbage_df = pd.read_csv("test_csv.csv")

print(garbage_df)

garbage_df = garbage_df.set_index("passed")

print(garbage_df.loc["True"])
print(len(garbage_df.loc["True"]))

print(len(garbage_df))

print(garbage_df.dtypes)
"""

##############
""" 

print(pd.__version__)

another_df = test_df.copy()
print(another_df.head())

print(another_df.loc[another_df["label"].isna()])
"""
print(test_df.columns)
test_df = test_df[["id", "label", "confirmed" , "deaths"]]

print(test_df.head())

nl_subset = test_df.loc[test_df["id"].str.contains("nl.")]
# nl_subset["confirmed"] = nl_subset["confirmed"].astype("float")
# nl_subset["confirmed"] = nl_subset["confirmed"].astype("int")
print(nl_subset)

nl_subset["death rate%"] = np.round(nl_subset["deaths"]/nl_subset["confirmed"], decimals=3)


print(nl_subset.columns)

print(nl_subset)

nl_subset.set_index(nl_subset["label"])

print(nl_subset)
