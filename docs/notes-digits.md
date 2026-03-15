


# Notes for digits-data

## Dataset understanding
The file data/digits-data.csv contains 1797 observations w/ 65 columns. 64 columns - pixel_0 through pixel_63 - represent the intensity values of an 8x8 handwritten digit image while the final column (digit) provides the class label from 0 to 9.

## Planned visualization
T-SNE seems appropriate for this phase of the project, so I plan to reduce the 64 pixel dimensions to 2 dimensions using t-SNE and then create a scatter plot colored by digit class. This seems like a good plan because the original dataset has 64 numeric image features per sample, therefore it likely cannot be visualized directly in 2D without dimensionality reduction. A t-SNE projection may reveal local clustering structure among digit classes, and coloring the points by the provided digit labels may make similarities and separations between classes easier to interpret.
## Data preparation needs
The dataset appears tidy, with one row per sample and a separate label column. As in the previous phases, formatting work will likely focus on validating the feature columns, confirming the label column, and separating predictors from class labels before dimensionality reduction.

## AI usage
I used ChatGPT to help inspect the dataset structure and think through an appropriate dimensionality-reduction-based visualization strategy. I selected the final approach based on my own understanding of the assignment and the dataset.

