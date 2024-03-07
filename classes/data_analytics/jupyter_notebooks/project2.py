import pandas as pd
import sqlite3
import os

fileName1 = '20090919071137.csv' 
path = './Geolife_Trajectories_1.3/Data/120/Trajectory/' 
FileIdentification1 = os.path.join(path, fileName1)

# Read the CSV file into a DataFrame
Points_User120_File1 = pd.read_csv(FileIdentification1)
Points_User120_File1 = Points_User120_File1.drop(columns=['Order', 'Unused'])

conn = sqlite3.connect('geolife.db')

conn.execute("""
CREATE TABLE IF NOT EXISTS User120_Trajectory (
    Latitude REAL,
    Longitude REAL,
    Unused INTEGER,
    Altitude INTEGER,
    Days TEXT,
    Date TEXT,
    Time TEXT
)
""")

cur = conn.cursor()

Points_User120_File1.to_sql('User120_Trajectory', conn, if_exists='append', index=False)

conn.close()