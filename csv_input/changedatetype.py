import pandas as pd

# Load your CSV file
df = pd.read_csv("csv_input/fileE.csv")

# Convert 'reported_date' and 'assigned_date' to MM/DD/YYYY format
df['datereported'] = pd.to_datetime(df['datereported']).dt.strftime('%m/%d/%Y')
df['assignee_date'] = pd.to_datetime(df['assignee_date']).dt.strftime('%m/%d/%Y')

# Save back to CSV (overwrite or save as new file)
df.to_csv("csv_input/fileE.csv", index=False)
