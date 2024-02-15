# Import matplotlib package for graphing
# Import distributions from scipy.stats
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import binom

# Let X~Bernoulli(0.35)

# Define possible values of X
x = [0, 1]

# Graph the probability distribution of X

# Get bar heights from Bernoulli distribution
plt.bar(x, height=bernoulli.pmf(k=x, p=0.35), width=0.75)
plt.ylabel('Probability', fontsize=12)
plt.xlabel("X", fontsize=12)
plt.xticks(ticks=x)  # add ticks for values of x
plt.show()

# Let X~Bernoulli(0.35)

# Calculate P(X=0) using pmf()
bernoulli.pmf(k=0, p=0.35)

# Let X~Bernoulli(0.35)

# Calculate P(X=1) using pmf()
bernoulli.pmf(k=1, p=0.35)

# Let X~Bernoulli(0.35)

# Calculate the cumulative probability, P(X<=1) using cdf()
## Note P(X<=1) = P(X=0)+P(X=1) which is all possible values for X
bernoulli.cdf(k=1, p=0.35)

# Let X~Binomial(15,0.35)

# Define the possible values of X, specify range(0, n+1) to get whole numbers 0 to n.
x = range(0, 15 + 1)

# Graph the probability distribution of X
# Get bar heights from binomial(15, 0.35) distribution
plt.bar(x, height=binom.pmf(k=x, n=15, p=0.35), width=0.75)
plt.ylabel('Probability', fontsize=12)
plt.xlabel("X", fontsize=12)
plt.xticks(ticks=x)  # add ticks for values of x
plt.show()

# Let X~Binomial(15,0.35)

# The bar for X=13 is not visible on the graph, but P(X=13) is not zero
binom.pmf(k=13, n=15, p=0.35)

# Let X~Binomial(15,0.35)

# Calculate the cumulative proportion up to X=5, P(X<=5)
binom.cdf(k=5, n=15, p=0.35)
