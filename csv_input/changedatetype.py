import pandas as pd
filepath = 'csv_input/hfilea.csv'
# Load your CSV file
df = pd.read_csv(filepath)

# Convert 'reported_date' and 'assigned_date' to MM/DD/YYYY format
df['reported_date'] = pd.to_datetime(df['reported_date'], dayfirst=True).dt.strftime('%Y-%m-%d')
df['assigned_date'] = pd.to_datetime(df['assigned_date'], dayfirst=True).dt.strftime('%Y-%m-%d')

# Save back to CSV (overwrite or save as new file)
df.to_csv(filepath, index=False)

