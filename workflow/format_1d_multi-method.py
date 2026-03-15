import pandas as pd

df = pd.read_csv("data/1d-multi-method-data.csv")

print("First five rows:")
print(df.head(), end="\n\n")

print("Shape:")
print(df.shape, end="\n\n")

print("Column names:")
print(df.columns.tolist(), end="\n\n")

print("Data Types")
print(df.dtypes, end="\n\n")

print("Missing Values:")
print(df.isna().sum(), end="\n\n")


print("Counts per method:")
print(df["method"].value_counts(), end="\n\n")

print("Grouped summary:")
print(df.groupby("method")["AUCROC"].describe(), end="\n\n")
