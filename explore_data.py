# STEP 2: DATA EXPLORATION (EDA)

# Import required libraries
import pandas as pd

# Load the reduced dataset
df = pd.read_csv("dataset/reduced_student_performance.csv")


# 1. Display first 5 rows

print("\nFIRST 5 ROWS OF DATASET")
print(df.head())


print("\nDATASET SHAPE")
print(df.shape)


print("\nCOLUMN NAMES")
print(df.columns)


print("\nDATA TYPES")
print(df.dtypes)



print("\nDATASET INFO")
print(df.info())

print("\nMISSING VALUES PER COLUMN")
print(df.isnull().sum())


print("\nSTATISTICAL SUMMARY")
print(df.describe())

duplicates = df.duplicated().sum()

print("\nNUMBER OF DUPLICATE ROWS")
print(duplicates)

print("\nUNIQUE VALUES PER COLUMN")

for column in df.columns:
    print(column, ":", df[column].nunique())


print("\nTARGET VARIABLE SUMMARY (Exam Score)")
print(df["Exam_Score"].describe())

print("\nDATA EXPLORATION COMPLETED SUCCESSFULLY")