import mysql.connector
import csv

# MySQL connection config
config = {
    'user': 'root',
    'password': 'Root1234',
    'host': 'localhost',  # or your MySQL host
    'database': 'ticket'
}

# Connect to the MySQL database
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

# Query to fetch all data from a specific table
table_name = 'employee'  # change if needed
query = f"SELECT * FROM {table_name};"
cursor.execute(query)

# Fetch column names
columns = [desc[0] for desc in cursor.description]

# Fetch all rows
rows = cursor.fetchall()

# Write to CSV file
csv_filename = f"csv_input/{table_name}.csv"
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(columns)  # Write header
    writer.writerows(rows)    # Write data

print(f"Data exported to {csv_filename} successfully.")

# Clean up
cursor.close()
connection.close()
