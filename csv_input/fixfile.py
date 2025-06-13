import pandas as pd
filepath = 'csv_input/hfileD.csv'
# Load the CSV file
df = pd.read_csv(filepath)
df['source_name'] = 'D'  

df.to_csv(filepath, index=False)