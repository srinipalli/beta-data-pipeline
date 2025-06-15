import pandas as pd
import csv
filepath = 'csv_input/hdfile.csv'
# Load your CSV file
df = pd.read_csv(filepath)

# Convert 'reported_date' and 'assigned_date' to MM/DD/YYYY format
df['reported_date'] = pd.to_datetime(df['reported_date'], format='%Y-%m-%d').dt.strftime('%d-%m-%Y')
df['assigned_date'] = pd.to_datetime(df['assigned_date'], format='%Y-%m-%d').dt.strftime('%d-%m-%Y')

# Save back to CSV (overwrite or save as new file)
df.to_csv(filepath, index=False, quoting=csv.QUOTE_ALL)

