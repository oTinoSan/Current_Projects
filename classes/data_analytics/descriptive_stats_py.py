# Import pandas and matplotlib packages
import pandas as pd
import matplotlib.pyplot as plt  # used to create a histogram

# Load the dataset
nhanes = pd.read_csv('nhanes.csv')

# View dataset (first/last 5 rows and the first/last 10 columns)
nhanes

# Calculate a selection of descriptive statistics for all numeric
# features with describe()

## 45 numeric features in the dataset so not all can be shown
nhanes.describe()

# Calculate the mean for a subset of numeric features in the dataframe

## Specifying axis=0 returns the mean of each feature (column),
## if axis=1, the mean of each instance (row) would be returned.
nhanes[['Age', 'AgeMonths']].mean(axis=0, skipna=True)

# Visualize Pulse feature with a histogram
plt.hist(x=nhanes['Pulse'])
plt.show()

# Calculate a selection of descriptive statistics for a single feature
# with describe()
nhanes['Pulse'].describe()

# Calculate the Pulse features' variance
nhanes['Pulse'].var()

# Calculate the Pulse features' skewness
nhanes['Pulse'].skew()


