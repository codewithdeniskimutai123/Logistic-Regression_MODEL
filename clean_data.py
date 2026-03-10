# STEP 3: DATA CLEANING

import pandas as pd

# Load the reduced dataset
df = pd.read_csv("dataset/reduced_student_performance.csv")

print("Original dataset shape:", df.shape)


# 1. Check missing values

print("\nMissing values before cleaning:")
print(df.isnull().sum())


# 2. Fill missing values for categorical columns

categorical_columns = df.select_dtypes(include=['object']).columns

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])


# 3. Verify missing values removed

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# 4. Remove duplicates if any

df = df.drop_duplicates()
print("\nNumber of duplicate rows removed (if any):", df.duplicated().sum())


# 5. Save cleaned dataset

df.to_csv("dataset/cleaned_student_performance.csv", index=False)
print("\nCleaned dataset saved successfully as 'cleaned_student_performance.csv'.")
print("Final dataset shape:", df.shape)