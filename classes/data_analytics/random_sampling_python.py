# Import pandas package
import pandas as pd

# Load the dataset
# Dataset contains 403 paintings (rows) and 69 features (columns)
paintings = pd.read_csv('bob_ross.csv')

# View dataframe
# Dataframes with more than 60 rows only show the first 5 and last 5 rows
paintings

# Select a sample of 20 paintings, without replacement, from
# the paintings dataframe
sample20Paintings = paintings.sample(n=20, replace=False)

# View dataframe containing the sampled of paintings
# Dataframes with 60 or fewer rows show all rows
sample20Paintings