import csv

INPUT_FILE = "csv_input/HRMtriage3.csv"      # Replace with your filename
OUTPUT_FILE = "csv_input/HRMtriage3.csv"       # Output after cleanup

def clean_csv(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        rows = []

        for row in reader:
            cleaned_row = [cell.strip() for cell in row]  # strip all fields
            rows.append(cleaned_row)

    with open(output_file, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
        writer.writerows(rows)

    print(f"✅ Cleaned and quoted file saved as: {output_file}")

if __name__ == "__main__":
    clean_csv(INPUT_FILE, OUTPUT_FILE)
