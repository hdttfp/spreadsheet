import csv

#  = ['year', 'month', 'sales', 'expenditure']

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(dict(row))
