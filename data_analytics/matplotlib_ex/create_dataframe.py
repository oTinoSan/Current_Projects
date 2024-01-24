import pandas as pd

# Creates a data frame
df = pd.DataFrame({                  
                   'Student': {0: "Michael", 1: "Arushi", 2: "Roberta", 3: "Michael", 4: "Arushi", 5: "Roberta"},
                   'Score': {0: 90, 1: 98, 2: 92, 3: 90, 4: 98, 5: 92}, 
                   'Date': {0: "2018-01-03", 1: "2018-01-03", 2: "2018-01-03", 3: "2018-01-13", 
                            4: "2018-01-13", 5: "2018-01-13"}}, 
                  columns=['Date','Student','Score'])
print("Original data frame:\n", df)

# Group by student and date, and find the mean score
print("\n Pivot() output: \n", pd.pivot(df, index = "Date", columns = "Student", values= "Score"), '\n')

# Creates a data frame
df = pd.DataFrame({'Student': {0: "Michael", 1: "Arushi", 2: "Roberta"},
                       'SAT': {0: 1480, 1: 1520, 2: 1460}, 
                       'ACT': {0: 34, 1: 32, 2: 32}}, 
                        columns=['Student','SAT','ACT'])

# Melt the data frame by columns Student, Test, and Scores
print(pd.melt(df, id_vars = "Student", var_name = "Test", value_vars = ["SAT", "ACT"], value_name = "Scores"))
