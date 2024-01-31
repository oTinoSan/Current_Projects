# Import packages and functions
import pandas as pd
from sklearn.linear_model import LinearRegression

# Import flights and remove missing values
flights = pd.read_csv('flight_delay_data.csv').dropna()

# Define X and y and convert to proper format
X = flights[['dep_delay']].values.reshape(-1, 1)
y = flights[['arr_delay']].values.reshape(-1, 1)

# Initialize a linear regression model
linearModel = LinearRegression()

# Fit the linear model
linearModel = linearModel.fit(X, y)

# Predict the arrival delay and assign the slope

yHat = linearModel.predict([[16]])
slope = linearModel.coef_

print('Predicted arrival delay:', yHat[0][0])
print('Slope coefficient:', slope[0][0])