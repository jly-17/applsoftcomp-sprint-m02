# Notes for 1d-multi-method-data
## Dataset understanding
The file data/1d-multi-method-data.csv contains 100 observations with two columns: “method” and “AUCROC”. Each row represents an AUC-ROC measurement which appears to be associated with a particular method. The dataset also appears to include repeated measurements for multiple methods, including “Proposed” and other methods.

## Planned visualization & Why
I plan to use a boxplot of AUC-ROC by method with overlaid jittered points. I will highlight “Proposed” using stronger visual emphasis. I am trying this approach because the dataset contains multiple values per method, and as such I want to preserve scores distribution rather than barcharting which would collapse methods data. A boxplot with jittered points would preserve central tendency, spread, and individual observations, while allowing “Proposed” to be highlighted clearly.

## Data preparation needs
Dataset presents in tidy format, with one row per measurement. As in previous phases, formatting work will likely focus on validating data types, checking for missing values, and confirming the number of observations per method.

## AI usage
I used ChatGPT to compare visualization options and refine code for visualizations. I selected the plotting direction based on my own reading of the dataset and the assignment requirement to highlight “Proposed”.
