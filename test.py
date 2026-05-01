import pandas as pd
import numpy as np

# Testing series objects.
# There are two: Series and DataFrames
# Using


# data = [1,3,5,6,8,"hehe"]
#
# series = pd.Series(data)
#
# print(series)

# s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
#
# print(s.index)

# Series can be instantiated from dictionaries too!

# dictionary = {"a":0.0,"b":1.0,"c":2.0}
# s = pd.Series(dictionary,name="Test")

# NaN - not a number! Standard missing data marker used in Pandas!
# If data is scalar value, value will be repeated to match the length of the index!

# s["a"] = 1.69
# print(s["a"])
# print(s)

# Creating DataFrame...

dates = pd.date_range("20260110",periods=6)

df = pd.DataFrame(np.random.randn(6, 4), columns=list("ABCD"))
# By printing dtypes we get to see type of each column!
print(df.dtypes)