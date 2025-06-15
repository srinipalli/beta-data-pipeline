import csv

INPUT_FILE = "csv_input/HRMtriage2.csv"
OUTPUT_FILE = "csv_input/HRMtriage3.csv"
EXPECTED_COLUMNS = 11

def fix_multiline_csv(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    header = lines[0].strip().split(",")
    fixed_rows = [header]

    buffer = ""
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue  # skip blank lines

        buffer += line + " "

        # Try to parse current buffer
        try:
            row = next(csv.reader([buffer]))
            if len(row) == EXPECTED_COLUMNS:
                fixed_rows.append(row)
                buffer = ""  # reset buffer
        except Exception as e:
            # parsing failed, continue adding lines
            continue

    # Write the cleaned CSV
    with open(output_file, "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out, quoting=csv.QUOTE_ALL)
        for row in fixed_rows:
            writer.writerow(row)

    print(f"✅ Cleaned file saved as: {output_file}")

if __name__ == "__main__":
    fix_multiline_csv(INPUT_FILE, OUTPUT_FILE)
