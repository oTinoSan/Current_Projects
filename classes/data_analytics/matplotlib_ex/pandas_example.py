# imports the pandas library
import pandas as pd

# loads a file containing comma-separated values and assigns
#     the data frame to variable DataFrame
data_frame1 = pd.read_csv('file.csv')

# loads text file where the values are separated by a space with no column labels
data_frame2= pd.read_csv('file.txt', sep = ' ', header = None)

# loads an excel file
data_frame3 = pd.read_excel('file.xlsx', sheetname='Sheet1')