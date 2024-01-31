import numpy as np
import pandas as pd
import scipy.stats as st

########
# Mean #
########

# Creates an array
arr1 = np.array([4, 8, 2, 10, 5])

# Prints the mean 
print(np.mean(arr1))

#######################
# Mean of a dataframe #
#######################

scores = pd.read_csv('ExamScores.csv')

# Prints the first few lines of data
print(scores.head())

# Prints the mean for each exam
print(scores.mean())

# Prints the mean for Exam1 only
print(scores[['Exam1']].mean())

# Prints the means for Exam1 and Exam2
print(scores[['Exam1', 'Exam2']].mean())

##########
# Median #
##########

# Creates an array
arr1 = np.array([4, 8, 2, 10, 5])

# Prints the median
print(np.median(arr1))

#########################
# Median of a dataframe #
#########################

# Loads the ExamScores dataset
scores = pd.read_csv('ExamScores.csv')

# Prints the median for each exam
print(scores.median())

# Prints the median for Exam1 only
print(scores[['Exam1']].median())

########
# Mode #
########

# Creates an array
arr1 = np.array([[4, 8, 2], [2, 5, 10], [2, 1, 10]])
print(arr1)

# Prints the mode
print(st.mode(arr1, keepdims=True))

#######################
# Mode of a dataframe #
#######################

# Loads the ExamScores dataset
scores = pd.read_csv('ExamScores.csv')

# Prints the mode(s) for each exam
print(scores.mode())

# Prints the mode(s) for Exam1 only
print(scores[['Exam1']].mode())

#################################
# Standard Deviation & Variance #
#################################

arr1 = np.array([10, 2, 5, 7, 3, 5])

# Population standard deviation for the array
print(np.std(arr1))

# Population variance of the array
print(np.var(arr1))

# Sample standard deviation for the array
print(np.std(arr1, ddof=1))

# Sample variance of the array
print(np.var(arr1, ddof=1))

##############################################
# Standard Deviation & Variance of dataframe #
##############################################

# Loads the ExamScores dataset
scores = pd.read_csv('ExamScores.csv')

# Sample standard deviation for each exam
print(scores.std())

# Sample standard deviation for Exam1 only
print(scores[['Exam1']].std()) 

# Sample variance for each exam
print(scores.var())

# Sample variance for Exam1 only
print(scores[['Exam1']].var())

# Population variance for each exam
print(scores.var(ddof=0))

# Sample variance for Exam1 only
print(scores[['Exam1']].var(ddof=0))

###########################
# Mean Absolute Deviation #
###########################


# Loads the ExamScores dataset
scores = pd.read_csv('ExamScores.csv')

# Prints the mean absolute deviation of all scores
print(scores.mad())

# Prints the mean absolute deviation of Exam 1
print(scores['Exam1'].mad())

#######################
# Min, Max, and Range #
#######################

import pandas as pd
scores = pd.read_csv('ExamScores.csv')

# Prints the minimum score for each exam
print(scores.min())

# Prints the minimum score for Exam1 only
print(scores[['Exam1']].min())

# Prints the maximum score for each exam
print(scores.max())

# Prints the maximum score for Exam1 only
print(scores[['Exam1']].max())

# Calculating the range by subtracting the minimum from the maximum
score_range = scores.max() - scores.min()
print(score_range)

# Defining a function that can be used repeatedly
def range_of_scores(x):
  return x.max() - x.min()
print(range_of_scores(scores))
print(range_of_scores(scores[['Exam1']]))
print(range_of_scores(scores[['Exam2']]))
print(range_of_scores(scores[['Exam4']]))

#############################
# Percentiles and Quartiles #
#############################

import pandas as pd
scores = pd.read_csv('ExamScores.csv')

# Prints the summary for each exam
print(scores.describe())

# Prints the summary for Exam1 only
print(scores[['Exam1']].describe())