input_file = 'csv_input/employeetablewithoutchange.csv'
output_file = 'csv_input/employeetablewithoutquotes.csv'

with open(input_file, 'r', encoding='utf-8') as infile:
    content = infile.read()

# Remove all double quotes
content_no_quotes = content.replace('"', '')

with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write(content_no_quotes)
