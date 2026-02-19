import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# Load Dataset
# ==============================
df = pd.read_csv("train.csv")

print("\n==============================")
print("Dataset Loaded Successfully!")
print("==============================\n")

# ==============================
# Basic Info
# ==============================
print("First 5 Rows:\n", df.head())
print("\nDataset Shape (Rows, Columns):", df.shape)

print("\nDataset Info:")
print(df.info())

print("\nMissing Values Count:\n", df.isnull().sum())

print("\nStatistical Summary:\n", df.describe())

# ==============================
# Data Cleaning
# ==============================
print("\n==============================")
print("Data Cleaning Started")
print("==============================\n")

# Fill missing Age with median
df["Age"].fillna(df["Age"].median(), inplace=True)

# Fill missing Embarked with mode
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

# Drop Cabin column (too many missing values)
if "Cabin" in df.columns:
    df.drop("Cabin", axis=1, inplace=True)

print("\nMissing Values After Cleaning:\n", df.isnull().sum())

# ==============================
# Exploratory Data Analysis (EDA)
# ==============================

sns.set(style="whitegrid")

# 1. Survival Count
plt.figure(figsize=(6, 4))
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()

# 2. Gender vs Survival
plt.figure(figsize=(6, 4))
sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("Gender vs Survival")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# 3. Passenger Class vs Survival
plt.figure(figsize=(6, 4))
sns.countplot(x="Pclass", hue="Survived", data=df)
plt.title("Passenger Class vs Survival")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.show()

# 4. Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Age"], bins=30, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# 5. Age vs Survival
plt.figure(figsize=(8, 5))
sns.boxplot(x="Survived", y="Age", data=df)
plt.title("Age vs Survival")
plt.xlabel("Survived")
plt.ylabel("Age")
plt.show()

# 6. Fare Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Fare"], bins=30, kde=True)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.show()

# 7. Correlation Heatmap
plt.figure(figsize=(10, 6))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

print("\n==============================")
print("EDA Completed Successfully!")
print("==============================\n")