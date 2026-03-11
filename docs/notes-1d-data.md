# Notes for 1d-data:

## Dataset understanding:
The file, data/1d-data.csv, contains 20 observations in a two-column format (value, group), and it appears to be tidy. The two groups are cases and control, and each contain 10 observations, while each row is a single observational measure within its respective group.

## Planned visualization & Why:
I plan to use a jitterplot with a boxplot overlay to compare the cases and control groups. I am choosing this because the dataset has a small number of observations per group, so it should be straightforward to convey individual points. A boxplot overlay will enable comparison of central tendency and spread while preserving the underlying data.

## Data preparation needs
Due to my conclusion that the dataset is tidy formatted, I primarily need to worry about ensuring group/label consistency by manually inspecting the CSV file. 

## AI usage
I used ChatGPT to help me check my inspections of the dataset/structure, troubleshoot and interpret command-line outputs as I built my workflow, and think through an appropriate visualization strategy that would be least likely to misrepresent data. 
