########################################################################################
# Create a 2-dimensional array containing the arrays [11, 15, 3, 19], [16, 10, 17, 6], # # [1, 14, 13, 7]. ######################################################################
########################################################################################

# Load the necessary package
import numpy as np

# Create an array
myArray = np.array([[11, 15, 3, 19], [16, 10, 17, 6], [1, 14, 13, 7]])

# Print the array
print(myArray)

#########################################
# Insert 'f' into the last row of myArr #
#########################################

# Load necessary package
import numpy as np

# Create array
myArr = [['r', 'y', 'v', 'w'], ['x', 's', 'm', 'k']]

# Insert character into the last row of array
myArr = np.insert(myArr, 2, 'f', axis=0)

# Print the array
print(myArr)

###########################
# Delete row 1 of exArray #
###########################

# Load necessary package
import numpy as np

# Create array
exArray = [[1, 9], [5, 4], [3, 6], [0, 7]]

# Delete row 1 of array
exArray = np.delete(exArray, 1, axis=0)

# Print the array
print(exArray)

#######################################
# Flatten myArray in row-major order. #
#######################################

# Load necessary package
import numpy as np

# Create array
myArray = [[4, 5, 9], [3, 8, 1]]

# Flatten array
myArray = np.ravel(myArray)

# Print the array
print(myArray)

#########################################################
# Return the standard deviation of elements in myArray. #
#########################################################

# Load necessary package
import numpy as np

# Create array
myArray = [[34, 17, 12, 24, 32], [47, 15, 38, 35, 49], [20, 48, 46, 37, 18]]

# Find standard deviation of array elements
myArray = np.std(myArray)

# Print the array
print(myArray)


#################
# Array example #
#################

# Loads necessary packages
import pandas as pd

# Loads the taxi.csv dataset
taxicabsNY = pd.read_csv('taxi.csv').dropna()

# Subset a column of the taxicabsNY dataframe by specifying the column name
tip = taxicabsNY[['tip']]

# Prints the column
print(tip)

# Using the iloc() method, display the first 11 columns and the first 10 rows of the taxisNY dataframe.

# Subset taxisNY using the iloc method
df = taxisNY.iloc[:10, :11]

# Prints the column
print(df)


# Using the loc() method, display all rows after and including row 8, and the fare column of the cabsNY dataframe.

# Subset cabsNY by specifying columns and rows using the loc method
df = cabsNY.loc[8:, ['fare']]

# Prints the column
print(df)

# Display all rows of the taxisNY dataframe where the total column is == 13.
# Subset taxisNY using comparison operators
df = taxisNY[taxisNY['total'] == 13]

# Prints the column
print(df)


# Display all rows of the taxicabsNY dataframe where pickup_borough is at Manhattan and dropoff_zone is either at Greenwich Village South or Saint Albans.

# Subset taxicabsNY using comparison and logical operators
df = taxicabsNY[(taxicabsNY['pickup_borough'] == 'Manhattan') & ((taxicabsNY['dropoff_zone'] == 'Greenwich Village South') | (taxicabsNY['dropoff_zone'] == 'Saint Albans'))]

# Prints the column
print(df)


