import pandas as pd

# loading dataset in initial format and validating consistency

df = pd.read_csv("data/1d-data.csv")

print("first five rows:")
print(df.head(), end="\n\n")

print("shape")
print(df.shape, end="\n\n")

print("column names")
print(df.columns.tolist(), end="\n\n")

print("data types:")
print(df.dtypes, end="\n\n")

print("unique groups:")
print(df["group"].unique(), end="\n\n")

print("missing values:")
print(df.isna().sum(), end="\n\n")
