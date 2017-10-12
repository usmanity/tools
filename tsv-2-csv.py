import csv
import sys

tabbed_file = sys.argv[1]
csv_file = sys.argv[2]

with open(tabbed_file, 'rb') as input_file:
    file_read = csv.reader(input_file, delimiter='\t')
    contents = [line for line in file_read]

with open(csv_file, 'wb') as output_file:
    file_write = csv.writer(output_file, quotechar='', quoting=csv.QUOTE_NONE)
    file_write.writerows(contents)

'''
Note, I learned about this from this stackoverflow answer: https://stackoverflow.com/a/5591258/318822
'''
