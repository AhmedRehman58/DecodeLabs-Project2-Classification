DecodeLabs AI Internship — Project 2
Ahmed Rehman | Batch 2026

Data Classification Using AI
C.O.R.E — Classification & Output Recognition Engine
A supervised machine learning model that classifies Iris flowers into 3 species using the K-Nearest Neighbors algorithm.

Features

Iris dataset loading and exploration
80/20 Train-Test Split
Feature Scaling using StandardScaler
KNN Classification Algorithm (n_neighbors=5)
Confusion Matrix evaluation
F1 Score and Accuracy reporting
100% Accuracy achieved


Tech Stack

Language: Python 3
Libraries: scikit-learn


How to Run
Install library:
bashpip install scikit-learn
Run the project:
bashpython "classifier p2.py"

Results
MetricScoreAccuracy100%F1 Score100%

Confusion Matrix
[[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]

Classification Report
              precision    recall  f1-score   support
      setosa       1.00      1.00      1.00        10
  versicolor       1.00      1.00      1.00         9
   virginica       1.00      1.00      1.00        11
    accuracy                           1.00        30

Dataset

Name: Iris Benchmark Dataset
Samples: 150
Classes: 3 (Setosa, Versicolor, Virginica)
Features: 4 (Sepal Length, Sepal Width, Petal Length, Petal Width)


About

Platform: DecodeLabs AI Internship
Batch: 2026
Engineer: Ahmed Rehman
