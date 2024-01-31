# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Loads the fibonacci dataset
fibonacci = pd.read_csv('naive_fib.csv').dropna()

# Set title
plt.title('Naïve Fibonacci implementation', fontsize=20)

# Set x and y axis labels
plt.xlabel('n')
plt.ylabel('Seconds (s)')

# Make plot
plt.plot(fibonacci["fib_value"], fibonacci["time"])

# Set y-axis to logarithmic scale
plt.yscale('log')

# Show the image
plt.show()