import matplotlib as mpl
import pandas as pd
import numpy as np
import datetime

# Turns of the copy warning
pd.set_option('mode.chained_assignment', None)

test_dataframe = pd.read_csv("../datasets/current.csv")

smaller_df = test_dataframe[["id", "label", "date", "confirmed", "recovered", "deaths"]]

print(smaller_df.head())

# smaller_df["date"] = pd.to_datetime(smaller_df["date"])
print(smaller_df.head())

print(smaller_df.dtypes)

smaller_df["date"] = smaller_df["date"].astype("str")

print(smaller_df.head())

print(smaller_df.dtypes)

smaller_df["death_toll%"] = np.round(smaller_df["deaths"]/smaller_df["confirmed"], 2)

print(smaller_df.loc[smaller_df["confirmed"] > 900000])

print(smaller_df.head(1))
print(type(smaller_df.head(1)))