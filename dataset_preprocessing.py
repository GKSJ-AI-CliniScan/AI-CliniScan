# Dataset Exploration and Data Preprocessing

import pandas as pd
import numpy as np

# Load your dataset
df = pd.read_csv("your_dataset.csv")   # change filename

# --- Dataset Exploration ---

print("Head of the dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# --- Data Preprocessing ---

# Remove duplicates
df = df.drop_duplicates()
print("\nDuplicates removed.")

# Handle missing values
df = df.fillna(method='ffill')  # you may change strategy
print("\nMissing values handled.")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print("\nColumn names cleaned.")

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)
print("\nCleaned dataset saved as cleaned_dataset.csv")
