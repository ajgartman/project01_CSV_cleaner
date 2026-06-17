# CSV Data Cleaner. Project 01.
# For my own knowledge.
# Data analysis and manipulation library built on top of Pandas. Two primary data structures
# Series and DataFrame. Makes working with structural data intuitive as spreadsheet!
# 1. Importing modules
import pandas as pd
import os
from datetime import datetime as dt
import matplotlib.pyplot as plt
from fontTools.t1Lib import writeOther

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
df = reading

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
        return float(height[:(len(height)-2)])
    elif "'" in height:
        feet_and_inches = height.replace('"',"").split("'")
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
        modified_string = weight.replace("lbs","")
        return int(modified_string)*lbs_kg_ratio
    elif "kg" in weight:
        modified_string = weight.replace("kg","")
        return int(modified_string)
    else:
        return None

df["Weight"] = df["Weight"].apply(weight_formatting)
# Using in-built function to change values to numbers


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

def years_check(date):

    wrong_format = 0

    if "," in date:
        formatting = date.split(",")
        join_year = int(formatting[1])
        current_year = date_output.year

        if current_year - join_year > 10:
            return "Veteran"
        else:
            return "Less than 10 years"
    else:
        wrong_format += 1
        return "Format not correct!"

# Creating new column and applying function
df["10 Year Mark"] = df["Joined"].apply(years_check)

# Task 4. Converting 'Value', 'Wage' and "Release Clause' into numerical form.
def conversion(value):
    # Two cases.
    currency = value.replace("€","")
    if "M" in currency:
        number = currency.replace("M","")
        return float(number)*1000000
    elif "K" in currency:
        number = currency.replace("K","")
        return float(number)*1000
    else:
        return float(currency)

df[["Value","Wage","Release Clause"]] = df[["Value","Wage","Release Clause"]].map(conversion)

# Task 5. Stripping the star symbol and changing to numerical
columns = ["W/F","SM","IR"]

df[columns] = df[columns].map(lambda x: int(x.strip("★").strip()))

ax1 = df.plot.scatter(x="Wage",y="Value")

# Annotation of the graph - computationally heavy
# for idx,row in df.iterrows():
#     ax1.annotate(row["ID"],(row['Wage'], row['Value']))

plt.xlabel("Wage of the Player")
plt.ylabel("Current Value of the Player")
plt.grid(True)
plt.show()

# Duplicate check (Extra)
print("----- Duplicate Check -----")
duplicates = df.duplicated()
print("Checking if there are any duplicates...: ")
print(duplicates[duplicates == True])

# Filling missing values (Extra)
df["Loan Date End"] = df["Loan Date End"].fillna("Not on Loan")
print(df[["Loan Date End","Hits"]].dtypes)

# Modifying Hits column

def hits_formatting(value):

    if pd.isna(value):
        return 0
    elif "K" in value:
        value = value.replace("K","")
        return float(value)*1000
    else:
        return float(value)

df["Hits"] = df["Hits"].apply(hits_formatting)

# Rerunning INFO
print(df.info())

# Summary
print("""
Post clearing summary:
1. Converted designated columns to their numerical forms.
2. Removed unnecessary characters and newlines
3. Checked duplicate rows
4. Filled NULL columns with corresponding fallback values
""")

# Saving modified CSV - Output it later.
# Creating directory to save the file.
dir_name = "output_csv"
try:
    os.mkdir(dir_name)
    print(f"Directory '{dir_name}' created successfully.")
except FileExistsError:
    print(f"Directory '{dir_name}' already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create '{dir_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")


os_path = os.path.join(dir_name,'processed_data.csv')
df.to_csv(os_path,index=False)