# 📊 Telecom Customer Churn Prediction

## 📘 Project Overview
The **Telecom Customer Churn Prediction** project focuses on analyzing and predicting customer churn — i.e., whether a customer is likely to leave the telecom service.

The dataset contains information on **7,043 customers** from a telecommunications company.  
Each record represents one customer and includes details about their **demographics, location, tenure, subscription services, and churn status** (joined, stayed, or churned).

---

## 🎯 Aim
To **predict whether a customer will churn or not** using machine learning techniques.

---

---

## 🧠 Libraries Used

The following essential libraries were utilized for data manipulation, visualization, model building, and evaluation:

* **`numpy`**: Fundamental package for scientific computing and array operations.
* **`pandas`**: For data manipulation and analysis.
* **`seaborn`** & **`matplotlib.pyplot`**: For Exploratory Data Analysis (EDA) and visualization.
* **`sklearn.model_selection.train_test_split`**: To split the dataset into training and testing sets.
* **`sklearn.tree.DecisionTreeClassifier`**, **`plot_tree`**, **`export_text`**: For model training and visualization of the resulting decision tree.
* **`sklearn.metrics.ConfusionMatrixDisplay`** & **`accuracy_score`**: For model performance evaluation.
* **`sklearn.preprocessing.LabelEncoder`**: To convert categorical features into a numerical format.

---

## 🛠️ Project Workflow

The project followed a systematic approach to model development:

1.  **Data Import and Initial Assessment**: Loading the dataset and examining its structure.
2.  **Exploratory Data Analysis (EDA)**: Identifying patterns, checking for missing values, and visualizing key feature distributions.
3.  **Data Preprocessing**: Handling categorical variables (using **LabelEncoder**) and preparing features for the model.
4.  **Data Splitting**: Dividing the cleaned data into training and testing sets.
5.  **Model Training**: Fitting the **Decision Tree Classifier** to the training data.
6.  **Model Evaluation**: Assessing performance using metrics like **accuracy score** and displaying the **confusion matrix**.
7.  **Feature Importance and Optimization**: Analyzing feature contributions and considering potential model tuning.

---

## ⚙️ Model and Algorithm

### **Algorithm Used: Decision Tree Classifier** 🌳

* The machine learning model chosen for this prediction task is the **Decision Tree Classifier** from `scikit-learn`.
* The model is trained based on the **entropy** criterion, which measures the impurity or randomness of the data to guide the optimal splitting of nodes in the tree. This helps in building a tree that provides the most information gain at each split, leading to better classification of churn and non-churn customers.

 
