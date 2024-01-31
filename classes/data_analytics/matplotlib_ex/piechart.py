# Load the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load the titanic dataset
df = sns.load_dataset("titanic")

# Count the number of passengers for each class
a = df[df.pclass == 1]["pclass"].count()
b = df[df.pclass == 2]["pclass"].count()
c = df[df.pclass == 3]["pclass"].count()

# Data to plot
labels = 'First', 'Second', 'Third'
sizes = [a, b, c]

########################
# Percentage Pie Chart #
########################

# Define lot
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Set title
plt.title('Titanic passengers by class', fontsize=20)

# Set legend
patches, texts = plt.pie(sizes)
plt.legend(patches, labels, loc="lower right")

# Set axes to be equal to produce a perfectly circular chart
plt.axis('equal')

# Save the image
# plt.savefig("piechart.png")

# Show the image
plt.show()

###################
# Count Pie Chart #
###################

# Make a pie chart with counts instead of percentages
tot = sum(sizes)
def autopct(x): return "%d" % round(x*tot/100, 2)

# Make the pie chart
plt.pie(sizes, labels=labels, autopct=autopct)

# Set title
plt.title('Titanic passengers by class', fontsize=20)

# Set legend
patches, texts = plt.pie(sizes)
plt.legend(patches, labels, loc="lower right")

# Set axes to be equal to produce a perfectly circular chart
plt.axis('equal')

# Save the image
# plt.savefig("piechart_count.png")

plt.show()

####################
# Exploded Piechart#
####################

# Calculate the number in each class
a = df[df.survived == 1]["survived"].count()
b = df[df.survived == 0]["survived"].count()

# Create a tuple of the categories
explodeTuple = (0.1, 0.0)

# Define data to plot
labels = 'Survived', 'Did not survive'
sizes = [a, b]

# Define plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explodeTuple)

# Set title
plt.title('Survivors of the Titanic', fontsize=20)

# Set axes to be equal to produce a perfectly circular chart
plt.axis('equal')

# Save the image
# plt.savefig("explodedpiechart.png")

# Show the image
plt.show()