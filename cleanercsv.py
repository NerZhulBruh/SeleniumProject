import os
import csv

# Define input and output file names
input_file = 'hermitage_exhibitions.csv'
output_file = 'hermitage_exhibitions_cleaned.csv'

# Open the input file in read mode and output file in write mode
with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
        open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)

    # Iterate through each row in the input file
    for row in reader:
        # Check if the row is not empty
        if not all(field.strip() == '' for field in row):
            # Write the non-empty row to the output file
            writer.writerow(row)