import pandas as pd
import matplotlib.pyplot as plt

#load validated 2d-dataset
df = pd.read_csv("data/2d-data.csv")

#create fig
plt.figure(figsize=(8,6))

#scatterplot w/transparency to reduce overplotting
plt.scatter(df["x"], df ["y"], s=8, alpha=0.25)

#labels/titles
plt.xlabel("x")
plt.ylabel("y")
plt.title("2D Data: Scatter Plot of X & Y")

#save fig
plt.tight_layout()
plt.savefig("figs/fig-2d_data.png", dpi=300)
plt.close()




