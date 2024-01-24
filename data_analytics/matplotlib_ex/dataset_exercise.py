# loads the pandas library
import pandas as pd
import seaborn as sns

# loads the titanic dataset 
titanic = sns.load_dataset("titanic")

## loads the titanic dataset 
#titanic = pd.read_csv('titanic.csv')

# find the number of rows and columns
print(titanic.shape,'\n')

# find the column names
print(titanic.columns, '\n')

# find the data types of the columns
print(titanic.dtypes, '\n')

# find median for all numeric variables
print(titanic.median(numeric_only=True), '\n')

# find the minimum for all numeric variables
print(titanic.min(numeric_only=True), '\n')

# find the mean for all numeric variables
print(titanic.mean(numeric_only=True), '\n')

# print the dataframe for columns sex and survived
print(titanic[["sex","survived"]], '\n')

# print the first 5 rows of columns sex and survived
print(titanic[["sex","survived"]].head(), '\n')

# prints dataframe of the first 5 rows
print(titanic[0:5])

# prints all rows where the column age has a value of 22
print(titanic[titanic.age == 22])

# prints all rows where column fare has a value less than 10.0.
print(titanic[titanic.fare < 10.0])

# returns dataframe containing first 6 rows and 
#     the columns pclass and age of the titanic
print(titanic.loc[0:5,["pclass","age"]])

# returns DataFrame containing the first 6 rows and 
#     the first 6 columns of the titanic
print(titanic.iloc[0:5,0:5])






