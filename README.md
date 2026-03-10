
# Student Performance Prediction using Logistic Regression

## Project Title

Machine Learning Model for Predicting Student Academic Performance Using Logistic Regression

## Project Developers

* Peterson Mwero
* Denis Kimutai
* Alex Purrenkei

Email: [petersonmwero@gmail.com]

---

## Project Overview

This project develops a 
machine learning model to predict whether a student will 
Pass or Fail based on academic and demographic factors such as hours studied,
attendance, previous scores, tutoring sessions, and other relevant indicators.

The model uses Logistic Regression
, a supervised learning algorithm commonly used for binary classification problems.

The dataset was cleaned, preprocessed, and split into 70% training data
and 30% testing data before training the model.

---

## Model Performance

The trained model achieved the following results on the test dataset:

* Accuracy: 89.33%
* Precision: 0.91 (Class 0), 0.83 (Class 1)
* **Recall: 0.95 (Class 0), 0.74 (Class 1)
* **F1 Score: 0.93 (Class 0), 0.78 (Class 1)
* **ROC AUC Score: 0.9569

These results show that the model performs well in predicting
student academic performance and can help identify students who may require early academic intervention.


## Project Structure
student-performance-ml/
│
├── dataset/
│   ├── X_train.csv
│   ├── X_test.csv
│   ├── y_train.csv
│   └── y_test.csv
│
├── models/
│   └── logistic_regression_model.pkl
│
├── clean_data.py
├── reduce_dataset.py
├── explore_data.py
├── feature_engineering.py
├── split_data.py
├── train_model.py
├── evaluate_model.py
├── requirements.txt
└── README.md
```
```
How to Run the Project
Running the Project
1. Clone the repository
git clone https://github.com/codewithdeniskimutai123/Logistic-Regression_MODEL.git

2. Navigate to the project folder
cd Logistic-Regression_MODEL/student-performance-ml

3. Install required dependencies
pip install -r requirements.txt

Run Scripts in the Following Order
Step 1 – Reduce the dataset
python reduce_dataset.py

Step 2 – Clean the dataset
python clean_data.py

Step 3 – Explore the dataset
python explore_data.py

Step 4 – Perform feature engineering
python feature_engineering.py

Step 5 – Split the dataset into training and testing sets
python split_data.py
This will create:

X_train.csv

X_test.csv

y_train.csv

y_test.csv


Step 6: Train the machine learning model
python train_model.py

This will create:

models/logistic_regression_model.pkl

Step 7 – Evaluate the model
python evaluate_model.py

Model Evaluation Output
Test Accuracy: 0.8933

Classification Report:
              precision    recall  f1-score   support

           0       0.91      0.95      0.93       222
           1       0.83      0.74      0.78        78

    accuracy                           0.89       300
   macro avg       0.87      0.84      0.86       300
weighted avg       0.89      0.89      0.89       300

Confusion Matrix:
#[[210  12]
#[ 20  58]]

ROC AUC Score: 0.9569

Repository

GitHub Repository:
https://github.com/codewithdeniskimutai123/Logistic-Regression_MODEL
```