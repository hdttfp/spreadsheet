import csv

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    for row in spreadsheet:
        print(row['year'], row['month'], row['sales'], row['expenditure'])

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    all_sales = []
    for row in spreadsheet:
        all_sales.append(int(row['sales']))
    print('Sales by month: {}.'.format(all_sales))


with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    all_expenditures = []
    for row in spreadsheet:
        all_expenditures.append(int(row['expenditure']))
    print('Expenditures by month: {}.'.format(all_expenditures))

all_profits = set(all_sales) - set(all_expenditures)
all_profits = list(all_profits)
print('Profit by month: {}'.format(all_profits))

total_sales = sum(all_sales)
print('Total sales: {}'.format(total_sales))

total_expenditure = sum(all_expenditures)
print('Total expenditure: {}'.format(total_expenditure))

total_profit = total_sales - total_expenditure
print('Total profit: {}'.format(total_profit))

