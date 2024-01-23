# Import packages and functions
import pandas as pd
from sklearn.linear_model import LinearRegression

# Import flights and remove missing values
flights = pd.read_csv('arrival_delay_data.csv').dropna()

# Define X and y and convert to proper format
X = flights[['dep_delay', 'dep_time']].values.reshape(-1, 2)
y = flights[['arr_delay']].values.reshape(-1, 1)

# Initialize a linear regression model
multipleModel = LinearRegression()

# Fit the linear model
multipleModel = multipleModel.fit(X, y)

# Predict the arrival delay and save the slope coefficient
yHat = multipleModel.predict([[56, 1107]])
slope = multipleModel.coef_

print('Predicted arrival delay:', yHat)
print('Slope coefficients:', slope)