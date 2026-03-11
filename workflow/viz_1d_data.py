import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

#load dataset
df = pd.read_csv("data/1d-data.csv")

#create fig
plt.figure(figsize=(8,6))

#group sum
sns.boxplot(data=df, x="group", y="value")

#raw obs using jitter 
sns.stripplot(data=df, x="group", y="value", jitter=True, alpha=0.7)

#labels/title
plt.xlabel("group")
plt.ylabel("value")
plt.title("1d DATA: Cases v Control")

plt.tight_layout()
plt.savefig("figs/fig-1d-data.png", dpi=300)
plt.close()
