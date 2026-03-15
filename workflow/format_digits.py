import pandas as pd

df = pd.read_csv("data/digits-data.csv")

feature_cols = [col for col in df.columns if col.startswith("pixel_")]
label_col = "digit"

print("First five rows:")
print(df.head(), end="\n\n")

print("Shape:")
print(df.shape, end="\n\n")

print("Number of feature columns:")
print(len(feature_cols), end="\n\n")

print("Label column:")
print(label_col, end="\n\n")

print("Digit counts:")
print(df[label_col].value_counts().sort_index(), end="\n\n")

print("Feature summary (first five columns):")
print(df[feature_cols[:5]].describe(), end="\n\n")


