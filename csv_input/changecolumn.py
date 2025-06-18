import csv

input_file = 'csv_input/employeetablewithoutquotes.csv'
output_file = 'csv_input/employeetable.csv'

with open(input_file, mode='r', newline='',) as infile, \
     open(output_file, mode='w', newline='') as outfile:

    reader = csv.DictReader(infile,delimiter=';')
    fieldnamesz = reader.fieldnames
    print(fieldnamesz)
    writer = csv.DictWriter(outfile, fieldnames=fieldnamesz,delimiter=';')
    writer.writeheader()

    for row in reader:
        if row['category'].lower() == 'core services and backend services':
            row['category'] = 'Frontend'
        elif row['category'].lower() == 'backend development and ux':
            row['category'] = 'Backend'
        elif row['category'].lower() == 'data and system management':
            row['category'] = 'Data'
        else:
            row['category'] = 'Infrastructure'
        writer.writerow(row)
