import pandas as pd

# Mapping of filenames to the name of their description field
files_description_column_map = {
    "csv_input/hfilea.csv": "description",
    "csv_input/hfileb.csv": "description",
    "csv_input/hfilec.csv": "bug_desc",
    "csv_input/hfiled.csv": "description",
    "csv_input/hfilee.csv": "description",
}

# Clean function to remove quotes and commas
def clean_text(text):
    return str(text).replace(',', '')

# Process each file
for file, desc_column in files_description_column_map.items():
    try:
        df = pd.read_csv(file)
        if desc_column in df.columns:
            df[desc_column] = df[desc_column].apply(clean_text)
            df.to_csv(file, index=False)
            print(f"[✓] Cleaned '{desc_column}' in {file}")
        else:
            print(f"[!] Column '{desc_column}' not found in {file}")
    except Exception as e:
        print(f"[X] Failed to process {file}: {e}")