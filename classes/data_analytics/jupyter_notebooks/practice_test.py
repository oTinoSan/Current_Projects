import pandas as pd
import os

fileName2 = '20091011115337.csv'
path = './MysteriousData/121/Trajectory/'
FileIdentification2 = os.path.join(path, fileName2)
Data_2 = pd.read_csv(FileIdentification2)
Data_2

# Find duplicated rows
duplicated_rows = Data_2.duplicated()

# Count duplicated rows
num_duplicated_rows = duplicated_rows.sum()

print(f'There are {num_duplicated_rows} duplicated rows.')

