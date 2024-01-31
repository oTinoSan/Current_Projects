# Load the necessary packages
import matplotlib.pyplot as plt
import seaborn as sns

# Load the attention dataset
att = sns.load_dataset("attention")

# Make plot
ax = sns.violinplot(x="score", data=att)

# Save the image
# plt.savefig("Attentionviolinplot.png")

# Show the image
plt.show()

# Make a side-by-side violin plot
ax = sns.violinplot(x="solutions", y="score", data=att)

plt.show()

# Add another variable to the plot
ax = sns.violinplot(x="solutions", y="score",
                    hue="attention", data=att, palette="muted")
ax.legend(loc="lower right")
plt.show()