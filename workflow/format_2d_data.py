import pandas as pd

df = pd.read_csv("data/2d-data.csv")

print("First five rows:")
print(df.head(), end="\n\n")

print("Shape:")
print(df.shape, end="\n\n")

print("Column names:")
print(df.columns.tolist(), end="\n\n")

print("Data types:")
print(df.dtypes, end="\n\n")

print("Missing values:")
print(df.isna().sum(), end="\n\n")

print("Summary statistics:")
print(df.describe(), end="\n\n")
