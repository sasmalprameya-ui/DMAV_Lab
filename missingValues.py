import pandas as pd
import numpy as np
import matplotlib as plt

# Sample dataset
data = {
    "Name": ["Amit", "Rahul", "Priya", "Neha"],
    "Age": [22, None, 21, None],
    "Marks": [85, 90, None, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Check missing values
print("\nMissing values in dataset:")
print(df.isnull())

# Count missing values in each column
print("\nTotal missing values in each column:")
print(df.isnull().sum())

# Rows that contain missing values
print("\nRows with missing values:")
print(df[df.isnull().any(axis=1)])