# CSV Data Cleaner. Project 01.
# For my own knowledge.
# Data analysis and manipulation library built on top of Numpy. Two primary data structures
# Series and DataFrame. Makes working with structural data intuitive as spreadsheet!

# 1. Importing data
import pandas as pd

CSV_FILE = "fifa21_raw_data_v2.csv"

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
    pass

df["Height"] = df["Height"].apply(height_formatting)
print(df["Height"])

def weight_formatting(str_input):
    # Same as with height, more than one case identified...
    pass

df["Weight"] = df["Weight"].apply(weight_formatting)
print(df["Weight"])
