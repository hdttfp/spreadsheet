import csv

#  = ['year', 'month', 'sales', 'expenditure']

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    all_sales = []
    for row in spreadsheet:
        # print(row['year'], row['month'], row['sales'], row['expenditure'])
        all_sales.append(int(row['sales']))
    print(all_sales)