# Introduction
This project aims to classify news articles as fake or real using machine learning techniques. The primary focus is on text processing, feature extraction, and model evaluation. The model achieves an accuracy of 93.37%, providing a reliable tool for detecting fake news.

# Dataset
The dataset used in this project consists of news articles with the following columns:

title: The title of the news article

text: The main content of the news article

label: The label indicating whether the news is fake or real

# Model
Algorithm: PassiveAggressiveClassifier
Feature Extraction: TfidfVectorizer with stop words removal and max_df adjustment
Libraries Used: Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn

# Evaluation
The model was evaluated using the following metrics:
Accuracy: 93.37%

Confusion Matrix

Classification Report

# Results
The model effectively distinguishes between fake and real news articles.
Feature importance analysis provides insights into key indicators of fake news.

# Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to improve the project.
