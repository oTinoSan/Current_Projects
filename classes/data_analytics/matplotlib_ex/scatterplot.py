# Load the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

##################################
# Scatterplot w/ regression line #
##################################

# Create the data points
x = np.array([0, 5, 3, 4, 7, 8, 10])
y = np.array([5, 2, 5, 15, 27, 15, 31])

# Define the plot
sns.regplot(x=x, y=y, ci=None)

# Save the image
# plt.savefig("scatterplot.png")

# Show the image
plt.show()

###################################
# Scatterplot w/o regression line #
###################################

# Load the rock data set
df = pd.read_csv("rock.csv").dropna()

# Set title
plt.title('Area and perimeter of rock', fontsize=20)

# define plot
sns.regplot(x=df["Area"], y=df["Perimeter"], ci=None, fit_reg=False)

# show the image
plt.show()

##############
# Strip plot #
##############

# Load the titanic dataset
titanic = sns.load_dataset("titanic")

# Set title
plt.title('Fares paid by passengers of the Titanic by deck', fontsize=20)

# Define plot
sns.stripplot(x="deck", y="fare", jitter=False, data=titanic)

# Save the image
# plt.savefig("titanicstripplot.png")

# Show the image
plt.show()

###########################
# Strip plot w/ jittering #
###########################

# Add jittering
sns.stripplot(x="deck", y="fare", jitter=True, data=titanic)

# Save the image
# plt.savefig("titanicstripplot_jittering.png")

# Show the image
plt.show()

##############
# Swarm plot #
##############

# Set title
plt.title('Fares paid by passengers of the Titanic by deck', fontsize=20)

# Define plot
sns.swarmplot(x="deck", y="fare", hue = "sex", data=titanic);

# Save the image
# plt.savefig("titanicswarmplot.png")

# Show the image
plt.show()
