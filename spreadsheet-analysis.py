import csv

# with open('sales.csv', 'r') as csv_file:
    # spreadsheet = csv.DictReader(csv_file)

    # for row in spreadsheet:
        # print(row['year'], row['month'], row['sales'], row['expenditure'])

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    all_sales = []
    all_expenditure = []
    for row in spreadsheet:
        all_sales.append(int(row['sales']))
        all_expenditure.append(int(row['expenditure']))
    # print(all_sales)

total_sales = sum(all_sales)
total_expenditure = sum(all_expenditure)
total_profit = total_sales - total_expenditure
print("The total sales for 2018 is £" + str(total_sales) + ".")
print("The total expenditure for 2018 is £" + str(total_expenditure) + ".")
print("The profit for 2018 is £" + str(total_profit) + ".")


# all_profits = set(all_sales) - set(all_expenditures)
# all_profits = list(all_profits)
