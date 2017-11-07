import csv
import sys

if len(sys.argv) < 2:
    print("""
Usage:
    python tsv-2-csv.py <tabbed-file> <output-csv-file>
        
Currently, both files are required.

Credit: I learned about this from this stackoverflow answer: https://stackoverflow.com/a/5591258/318822
    """)

tabbed_file = sys.argv[1]
csv_file = sys.argv[2]
print('Tabbed file: ', tabbed_file)
print('CSV output: ', csv_file)

with open(tabbed_file, 'rb') as input_file:
    print("Opening tabbed file...")
    file_read = csv.reader(input_file, delimiter='\t')
    contents = [line for line in file_read]
    print(contents)

with open(csv_file, 'wb') as output_file:
    file_write = csv.writer(output_file, quotechar='', quoting=csv.QUOTE_NONE)
    file_write.writerows(contents)
