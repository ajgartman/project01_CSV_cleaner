import pandas as pd

# Testing file - Pandas practice

# Exercise 1 - Series

temp = [22.1, 19.5, 24.0, 21.3, 18.7, 25.4, 23.8]
index = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

temp_series = pd.Series(temp, index=index)

# print(temp_series[temp_series>22.0])

# Printing the mean, minimum, maximum temperature
# Need to add mean(),max(),min()... etc

# Adding 2 degrees to every value in series
# Applying lambda function to the series :)
#print(temp_series.apply(lambda x: x+2))

# ---------- ---------- ----------
# Exercise 2. Creating and inspecting dataframes.
# Creating df from list of dicts.

students = [{"name": "Alice", "course": "CS", "grade": 74, "year": 1},
            {"name": "Bob", "course": "CS", "grade": 85, "year": 2},
            {"name": "Carol", "course": "EEE", "grade": 42, "year": 1},
            {"name": "Dan", "course": "EEE", "grade": 90, "year": 3},
            {"name": "Eve", "course": "CS", "grade": 63, "year": 2},
            {"name": "Frank", "course": "Math", "grade": 55, "year": 1}]

df = pd.DataFrame(students)
# print(df.shape)
# print(df.columns)
# print(df.head(3))
# print(df.describe())
df = df.astype({"grade": "int32","year":"int32"}).dtypes

# Exercise 3
# print(df.iloc[0:2,0:2])
# print(df[(df["grade"] > 70) & (df["course"] == "CS")])
# print(df[df["name"].isin(["Alice","Bob"])])

# Exercise 4
# df["grade_percent"] = df["grade"] / 100
#
#
# def get_band(grade_input):
#     if grade_input >= 70:
#         return "Distinction"
#     elif 60 > grade_input > 70:
#         return "Pass"
#     else:
#         return "Fail"
#
# # Applying functions to the dataframes.
# df["band"] = df["grade"].apply(lambda x: "Pass" if x >= 60 else "Fail")
#
# df["summary"] = df.apply(lambda row: f"{row['name']} scored {row['grade']} - {row["band"]}", axis=1)
#
# df = df.drop('grade_percent', axis=1)
#
# print(df)
