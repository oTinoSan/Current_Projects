# Import the necessary modules
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Read in nbaallelo_slr.csv
nba = pd.read_csv('nbaallelo_slr.csv').dropna()

# Create a new column in the data frame that is the difference between pts and opp_pts
nba['y'] = nba['pts'] - nba['opp_pts']

# Store relevant columns as variables
X = nba[['elo_i']]
y = nba['y']

# Initialize the linear regression model
SLRModel = LinearRegression()

# Fit the model on X and y. Note: X must be a DataFrame, not a Series, hence the double brackets
SLRModel.fit(X, y)

# Print the intercept
intercept = SLRModel.intercept_
print('The intercept of the linear regression line is ', end="")
print(f'{intercept:.3f}. ')

# Print the slope
slope = SLRModel.coef_
print('The slope of the linear regression line is ', end="")
print(f'{slope[0]:.3f}. ')

# Compute the proportion of variation explained by the linear regression using the LinearRegression object's score method
score = SLRModel.score(X, y)
print('The proportion of variation explained by the linear regression model is ', end="")
print(f'{score:.3f}. ')
