import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#load data
df = pd.read_csv("data/1d-multi-method-data.csv")

#order methods by median AUCROC (highest-lowest)
order = (df.groupby("method")["AUCROC"]
.median()
.sort_values(ascending=False)
.index)

#build palette highlighting what was proposed
palette = {method: "lightgray" for method in order}

palette["Proposed"] = "tab:orange"

#create figure 
plt.figure(figsize=(11,6))


#boxplot for methods
sns.boxplot(data=df, x="method", y="AUCROC", order=order, palette=palette)

#jittered points for raw obs
sns.stripplot(data=df, x="method", y="AUCROC", order=order, color="black", size=3, alpha=0.45, jitter=True)

#labels/title 
plt.xlabel("Method")
plt.ylabel("AUC-ROC")
plt.title("AUC-ROC by Method (Proposed Highlighted)")
plt.xticks(rotation=45, ha="right")

#save fig
plt.tight_layout()
plt.savefig("figs/fig-1d-multi-method.png", dpi=300)
plt.close()
