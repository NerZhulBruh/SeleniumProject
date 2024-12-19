import os
import csv
input_file = 'hermitage_exhibitions.csv'
output_file = 'hermitage_exhibitions_cleaned.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
        open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)

    for row in reader:
        if not all(field.strip() == '' for field in row):
            writer.writerow(row)
