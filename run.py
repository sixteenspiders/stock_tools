import argparse
import csv

help_text = 'Example: python3 run.py filename.csv'
parser = argparse.ArgumentParser(description = help_text)
parser.add_argument("file", help="Filename of the CSV file")
args = parser.parse_args()
if args.file:
    pass
else:
    print('No filename')
    exit(2)
fin_name = args.file
fout_name = 'OP_' + args.file
fin_handle = open(fin_name, encoding = 'utf-8')
csv_reader = csv.reader(fin_handle)
fin_list = list(csv_reader)

fout_handle = open(fout_name, mode = 'w', newline='')
csv_writer = csv.writer(fout_handle, delimiter = ',')
csv_writer.writerow(['Symbol', 'Volatility'])

for x in range(1, len(fin_list)):
    csv_writer.writerow([fin_list[x][1], 100*float(fin_list[x][6])])

fin_handle.close()
fout_handle.close()

print('Input File:\t' + fin_name + '\nOutput File:\t' + fout_name)
