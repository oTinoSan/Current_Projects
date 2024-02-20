# Loads the necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

####################
# Vertical Barchart#
####################

# Loads the titanic dataset
titanic = sns.load_dataset("titanic")

# Sets the style of the bar charts
sns.set_theme(style="whitegrid", color_codes=True)

# Title
plt.title('Titanic passengers by class', fontsize=20)

# Plots a vertical bar chart
sns.countplot(x="class", color="b", data=titanic)

# Saves the image
#plt.savefig("verticalbarchart.png")

# Shows the image
plt.show()

######################
# Horizontal Barchart#
######################

# Sets the style of the bar charts
sns.set_theme(style="whitegrid", color_codes=True)

# Title
plt.title('Titanic passengers by class', fontsize=20)

# Plots a horizontal bar chart
sns.countplot(y="class", color="b", data=titanic)

# Saves the image
#plt.savefig("horizontalbarchart.png")

plt.show()

###################
# Grouped Barchart#
###################

# Set the style of the bar charts
sns.set_theme(style="whitegrid", color_codes=True)

# Set title
plt.title('Titanic survivors and deaths by class', fontsize=20)

# Generate a vertical bar chart
sns.countplot(x="class", hue="survived", palette="dark:b", data=titanic)

# Save the image
# plt.savefig("groupedbarchart.png")

# Shows the image
plt.show()

####################
# Stacked Barchart#
####################

# Load data frame
crashes = sns.load_dataset("car_crashes")
df = crashes.loc[range(5)]

# Intialize the figure
f, ax = plt.subplots()

# Plot total crashes
sns.set_color_codes("pastel")
sns.barplot(x="total", y="abbrev", data=df, label="Total", color="b")

# Plot crashes related to speeding
sns.set_color_codes("muted")
sns.barplot(x="speeding", y="abbrev", data=df, label="Speeding-related", color="b")

# Set Title
plt.title('Speeding-related automobile collisions', fontsize=20)

# Set legend
ax.legend(ncol=1, loc="lower right")
ax.set(xlim=(0, 28), ylabel="State", xlabel="Automobile collisions (per billion miles)")

# saves the image
#plt.savefig("stacked.png")

# Shows the image
plt.show()