import pandas as pd

# Load your CSV file
df = pd.read_csv("csv_input/fileD.csv")

# Convert 'reported_date' and 'assigned_date' to MM/DD/YYYY format
df['reported_date'] = pd.to_datetime(df['reported_date']).dt.strftime('%m/%d/%Y')
df['assigned_date'] = pd.to_datetime(df['assigned_date']).dt.strftime('%m/%d/%Y')

# Save back to CSV (overwrite or save as new file)
df.to_csv("csv_input/fileD.csv", index=False)
