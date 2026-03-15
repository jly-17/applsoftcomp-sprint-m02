import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE


#load data
df = pd.read_csv("data/digits-data.csv")

#separate features & labels
feature_cols = [col for col in df.columns if col.startswith("pixel_")]
X = df[feature_cols]
y = df["digit"]

#t-SNE for 2d reduction 
tsne = TSNE(n_components=2, random_state=42, init="pca", learning_rate="auto")
X_embedded = tsne.fit_transform(X)

#scatterplot
plt.figure(figsize=(9,7))
scatter = plt.scatter(X_embedded[:, 0], X_embedded[:,1], c=y, s=10, alpha=0.75)


#labels/title 
plt.xlabel("t_SNE Dimension 1")
plt.ylabel("T-SNE Dimension 2") 
plt.title("Handwritten Digits t-SNE Projection")

#color legend
legend = plt.legend(*scatter.legend_elements(), title="Digit", loc="best")
plt.gca().add_artist(legend)

#save fig 
plt.tight_layout()
plt.savefig("figs/fig-digits.png", dpi=300)
plt.close()


