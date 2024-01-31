# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Loads the unemployment dataset
unemployment = pd.read_csv('unemployment.csv').dropna()

# Set title
plt.title('U.S. unemployment rate', fontsize=20)

# Set x and y axis labels
plt.xlabel('Year')
plt.ylabel('% of total labor force')

# Make plot
plt.plot(unemployment["Year"], unemployment["Value"])

# Show the image
plt.show()