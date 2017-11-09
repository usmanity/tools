import csv
import sys


if len(sys.argv) < 2:
    print("""
Usage:
    """)

dotted_file = sys.argv[1]
csv_file = sys.argv[2]
print('Tabbed file: ', dotted_file)
print('CSV output: ', csv_file)

contents = []
with open(dotted_file, 'rb') as input_file:
    print("Opening tabbed file...")
    file_read = csv.reader(input_file)
    for line in file_read:
        line[0] = line[0].replace('.', ' ')
        contents.append(line)

with open(csv_file, 'wb') as output_file:
   file_write = csv.writer(output_file, quotechar='', quoting=csv.QUOTE_NONE)
   file_write.writerows(contents)
