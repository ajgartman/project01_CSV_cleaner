# CSV Data Cleaner. Project 01.
# For my own knowledge.
# Data analysis and manipulation library built on top of Pandas. Two primary data structures
# Series and DataFrame. Makes working with structural data intuitive as spreadsheet!
# 1. Importing modules
import pandas as pd
import os
from datetime import datetime as dt
import matplotlib.pyplot as plt

CSV_FILE = "fifa21_raw_data.csv"

# Inspecting the data
reading = pd.read_csv(CSV_FILE,dtype=object)
# Getting the details
print("----------")
print("CSV description")
print(reading.describe())
print("----------")
print("CSV information")
print(reading.info())

# Creating DataFrame object
df = pd.DataFrame(reading)

# Sequence
#1.
# Creating a series of columns and corresponding amount of NULL values
print("----------")
print("Creating Series of Columns and corresponding NULL values.")
missing = df.isnull().sum()

# Checking how many missing values are there.
# Trying to get the picture of the dataset.
print("----------")
print("Checking how many missing values are there...")
print(missing[missing>0])

print("----------")
print("Checking shape")
print(df.shape)

# Task 1. Converting the height and weight columns to numerical forms
print(df[["Height","Weight"]].dtypes)
# Checking... Both columns are 'objects'. Will have to apply functions.
# Creating function for Height column
def height_formatting(height):
    # We are having two cases - Feet/Inches and cm's
    # Problem we need to solve is: how can we identify two separate cases.

    if "cm" in height:
        return height[:(len(height)-2)]
    elif "'" in height:
        feet_and_inches = height.strip('"').split("'")
        feet = feet_and_inches[0]
        inches = feet_and_inches[1]
        feet_cm = int(feet)*30.48
        inches_cm = int(inches)*2.54
        total = feet_cm + inches_cm
        return total
    else:
        return None

df["Height"] = df["Height"].apply(height_formatting)

def weight_formatting(weight):
    # Two cases: "lbs" and "kg's"
    if "lbs" in weight:
        lbs_kg_ratio = 0.4535
        modified_string = weight.strip("lbs")
        return int(modified_string)*lbs_kg_ratio
    elif "kg" in weight:
        modified_string = weight.strip("kg")
        return int(modified_string)
    else:
        return None

df["Weight"] = df["Weight"].apply(weight_formatting)
# Using in-built function to change values to numbers
df[["Weight","Height"]] = df[["Weight","Height"]].apply(pd.to_numeric)

# After the modification...
print("----- After formatting -----")
print(df[["Height","Weight"]].dtypes)

# Task 2. Removing unnecessary newline characters
# Looping through object columns and applying str.replace method...

for column in df.select_dtypes(include="object"):
    df[column] = df[column].str.replace("\n","")

# Task 3. Checking if a player spent more than 10 years at the club.

# Hypothetical date
time = "01/01/21"
date_format = "%d/%m/%y"
date_output = dt.strptime(time,date_format)

def age_check(date):
    formatting = date.split(",")
    join_year = int(formatting[1])
    current_year = date_output.year

    if current_year - join_year > 10:
        return "Veteran"
    else:
        return "Less than 10 years"

# Creating new column and applying function
df["10 Year Mark"] = df["Joined"].apply(age_check)

# Task 4. Converting 'Value', 'Wage' and "Release Clause' into numerical form.
def conversion(value):
    # Two cases.
    currency = value.strip("€")
    if "M" in currency:
        number = currency.strip("M")
        return float(number)*1000000
    elif "K" in currency:
        number = currency.strip("K")
        return float(number)*1000
    else:
        return None

df[["Value","Wage","Release Clause"]] = df[["Value","Wage","Release Clause"]].map(conversion)

# Task 5. Stripping the star symbol and changing to numerical

columns = ["W/F","SM","IR"]

df[columns] = df[columns].map(lambda x: int(x.strip("★").strip()))
df[columns] = df[columns].apply(pd.to_numeric)

ax1 = df.plot.scatter(x="Wage",y="Value")

for idx,row in df.iterrows():
    ax1.annotate(row["ID"],(row['Wage'], row['Value']))

plt.xlabel("Wage of the Player")
plt.ylabel("Current Value of the Player")
plt.grid(True)
plt.show()


# Saving modified CSV - Output it later.
os_path = os.path.join('output_csv','processed_data.csv')
df.to_csv(os_path,index=False)