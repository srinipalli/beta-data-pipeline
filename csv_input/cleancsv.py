import pandas as pd
C = input("Enter your csv file relative path: ")
df = pd.read_csv(C)
df.to_csv(f'csv_input/cleaned.csv', index=False, quoting=1)
