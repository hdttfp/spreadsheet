import csv

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    for row in spreadsheet:
        print(row['year'], row['month'], row['sales'], row['expenditure'])

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    list_months = []
    list_sales = []
    list_expenditure = []
    list_profit = []
    for row in spreadsheet:
        list_months.append(row['month'])
        list_sales.append(int(row['sales']))
        list_expenditure.append(int(row['expenditure']))
        list_profit.append(int(row['sales']) - int(row['expenditure']))
    # print(list_sales)
    # print(list_expenditure)
    # print(list_profit)

total_sales = sum(list_sales)
total_expenditure = sum(list_expenditure)
total_profit = total_sales - total_expenditure
print("The total sales for 2018 is £" + str(total_sales) + ".")
print("The total expenditure for 2018 is £" + str(total_expenditure) + ".")
print("The profit for 2018 is £" + str(total_profit) + ".")

list_month_change = [0]
for month in range(0, 11):
    monthly_change = int(((list_profit[month + 1] - list_profit[month]) / list_profit[month]) * 100)
    list_month_change.append(monthly_change)
greatest_change = max(list_month_change)

for month in range(0, 11):
    if list_month_change[month] == greatest_change:
        greatest_month = month

print("The greatest monthly change was {}% from {} to {}.".format(greatest_change, list_months[greatest_month - 1], list_months[greatest_month]))
