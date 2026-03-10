# STEP 4: FEATURE ENGINEERING

import pandas as pd


df = pd.read_csv("dataset/cleaned_student_performance.csv")

print("Original cleaned dataset shape:", df.shape)


# 1. Convert Exam_Score into Pass/Fail

df['Pass'] = df['Exam_Score'].apply(lambda x: 1 if x >= 70 else 0)


# 2. Select relevant features

features_to_keep = [
    'Hours_Studied',
    'Attendance',
    'Sleep_Hours',
    'Previous_Scores',
    'Tutoring_Sessions',
    'Physical_Activity',
    'Gender',
    'School_Type',
    'Parental_Education_Level'
]

df = df[features_to_keep + ['Pass']]

print("Dataset shape after selecting features:", df.shape)


# 3. Encode categorical variables

categorical_cols = ['Gender', 'School_Type', 'Parental_Education_Level']
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

print("Dataset shape after encoding categorical variables:", df.shape)

# 4. Save the feature-engineered dataset

df.to_csv("dataset/feature_engineered_student_performance.csv", index=False)

print("\nFeature-engineered dataset saved successfully as 'feature_engineered_student_performance.csv'.")