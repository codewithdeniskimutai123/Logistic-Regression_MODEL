# STEP 6: TRAIN LOGISTIC REGRESSION MODEL
import os
os.makedirs("models", exist_ok=True)
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib


X_train = pd.read_csv("dataset/X_train.csv")
X_test = pd.read_csv("dataset/X_test.csv")
y_train = pd.read_csv("dataset/y_train.csv").values.ravel()
y_test = pd.read_csv("dataset/y_test.csv").values.ravel()


model = LogisticRegression(max_iter=1000, random_state=42)


model.fit(X_train, y_train)


y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Test Accuracy: {accuracy:.4f}")
print("\nClassification Report:\n", report)


joblib.dump(model, "models/logistic_regression_model.pkl")
print("\nTrained Logistic Regression model saved as 'logistic_regression_model.pkl'")