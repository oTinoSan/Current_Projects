# Loads the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Loads the ExamScores dataset
scores = pd.read_csv('ExamScores.csv').dropna()

# Transforms the data
df = pd.melt(scores, value_name="Score", var_name="Exam")

# Plot
sns.boxplot(x="Exam", y="Score", data=df)

# Saves the image
# plt.savefig("Examsboxplots.png")

# Shows the image
plt.show()

# Plots without outliers
sns.boxplot(x="Exam", y="Score", data=df, whis=100)

plt.show()


########################################
# Boxplot 5 number summary and boxplot #
########################################

# Loads packages
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Reads the mtcars.csv file into a dataframe called mtcars
mtcars = pd.read_csv("mtcars.csv").dropna()

# Prints the first few lines of mtcars
print(mtcars.head())

# Show summary statistics for the variable wt
mtcars.wt.describe()

# Plots a box plot
sns.boxplot(data=mtcars.wt, width=0.35)

plt.show()