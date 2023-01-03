import pandas as pd
import numpy as np
import matplotlib as mpl

original_df = pd.read_csv("C:/Users/Alexd/OneDrive/Documenten/GitHub/experimental_repository/datasets/test_csv.csv")

# print(original_df)
# original_df = original_df.set_index("name")
print(original_df)


##############

data_to_add: dict = {"name": ["Data Engineer"],
                     "grade": [12.5],
                     "passed": [True]}
df_to_add = pd.DataFrame(data_to_add)
print(df_to_add)

# testing the creation of dataframes by wiring lists together into a dictionary
# This dictionary then gets poured into the pd.DataFrame() method
values_to_add: list = ["Werewire", 7.2, False]
keys: list = list(original_df.columns)
final_dict: dict = {}
for value in values_to_add:
    final_dict.update({keys[values_to_add.index(value)]: [value]})

another_df = pd.DataFrame(final_dict)

original_df = pd.concat([original_df, another_df])

print("\n--------------------\n")
print(original_df)

# Conclusion: It is a bit tedious but definetely works

plot = original_df["grade"].plot(kind="hist")

mpl_plot = mpl

print(final_dict)

print(plot)






