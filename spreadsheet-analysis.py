import csv

field_names = ['year', 'month', 'sales', 'expenditure']

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file, field_names)

print(spreadsheet)
