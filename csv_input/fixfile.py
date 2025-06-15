import pandas as pd
import csv
filepath = 'csv_input/hefile.csv'
# Load the CSV file
df = pd.read_csv(filepath)

df.to_csv(filepath, index=False,quoting=csv.QUOTE_ALL)