# STEP 5: SPLIT DATA INTO TRAIN AND TEST SETS

import pandas as pd
from sklearn.model_selection import train_test_split

# Load the feature-engineered dataset
df = pd.read_csv("dataset/feature_engineered_student_performance.csv")

print("Feature-engineered dataset shape:", df.shape)


# 1. Separate features and target

X = df.drop('Pass', axis=1)
y = df['Pass']

print("Features shape:", X.shape)
print("Target shape:", y.shape)


# 2. Split into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print("\nTraining features shape:", X_train.shape)
print("Training target shape:", y_train.shape)
print("Testing features shape:", X_test.shape)
print("Testing target shape:", y_test.shape)


# 3. Optionally, save splits for later use

X_train.to_csv("dataset/X_train.csv", index=False)
X_test.to_csv("dataset/X_test.csv", index=False)
y_train.to_csv("dataset/y_train.csv", index=False)
y_test.to_csv("dataset/y_test.csv", index=False)

print("\nTrain/Test split completed and saved successfully.")