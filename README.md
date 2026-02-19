# PRODIGY_DS_02
# Task 02 - Exploratory Data Analysis (EDA) on Titanic Dataset

# 📌 Project Overview
This project focuses on performing **Data Cleaning** and **Exploratory Data Analysis (EDA)** on the famous **Titanic Dataset**.  
The aim is to explore relationships between different variables and identify patterns and trends affecting passenger survival.



# 📂 Dataset Used
Dataset: Titanic Dataset (Kaggle)  
Files used: `train.csv`

📌 Source Link:  
https://github.com/projediinfotech/Datascience-datasets/tree/main/Task/Module-2/202



# 🎯 Objectives
 🎀Load and understand the dataset
 🎀Handle missing values
 🎀Perform data cleaning
 🎀Explore statistical summary of data
 🎀Visualize patterns and relationships
 🎀Identify factors affecting survival rate


## 🛠️ Technologies Used
 Python
 Pandas
 NumPy
 Matplotlib
 Seaborn
 Scikit-learn
 SciPy
 Statsmodels


# 📌 Steps Performed
# ✅ 1. Data Loading
Loaded dataset using Pandas

# ✅ 2. Data Cleaning
 Checked missing values
 Filled missing values in columns like `Age`
 Dropped columns with too many missing values such as `Cabin`
 Removed duplicate values (if any)

# ✅ 3. Exploratory Data Analysis (EDA)
Survival Count Analysis
Gender vs Survival
Passenger Class vs Survival
Age Distribution
Correlation Heatmap


# 📊 Key Insights
 Majority of passengers did not survive.
 Females had a higher survival rate than males.
 Passengers in 1st class survived more compared to 2nd and 3rd class.
 Younger passengers had better survival chances.
 Ticket class and gender are strong indicators of survival.



## 📁 Project Structure
Task02_eda/ │ ├── dataset/ │   └── train.csv │ ├── eda_analysis.py ├── requirements.txt ├── README.md └── venv/   (not pushed to GitHub)




## ▶️ How to Run the Project

### ✅ Step 1: Create Virtual Environment
bash
python -m venv venv

✅ Step 2: Activate Virtual Environment


For Windows (PowerShell):

Bash

.\venv\Scripts\activate


✅ Step 3: Install Dependencies

Bash

pip install -r requirements.txt


✅ Step 4: Run Python File

Bash

python eda_analysis.py

📌 Output
The project generates visualizations such as:
Survival Count Bar Chart
Gender vs Survival
Passenger Class vs Survival
Age Distribution Histogram
Correlation Heatmap
👨‍💻 Author

Name: Ayesha Khanum N
Internship Program: Prodigy InfoTech
Task: Task-02 (Exploratory Data Analysis)

⭐ Conclusion

This project successfully demonstrates data cleaning and EDA techniques using Python.
It provides meaningful insights into survival patterns and relationships between important variables in the Titanic dataset.
