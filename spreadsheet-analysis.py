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

max_sales = max(list_sales)
min_sales = min(list_sales)
for month in range(0, 11):
    if list_sales[month] == max_sales:
        max_sales_month = month
    if list_sales[month] == min_sales:
        min_sales_month = month
print("{} had the greatest sales of £{}.".format(list_months[max_sales_month], max_sales))
print("{} had the lowest sales of £{}.".format(list_months[min_sales_month], min_sales))


list_month_change = [0]
for month in range(0, 11):
    monthly_change = int(((list_profit[month + 1] - list_profit[month]) / list_profit[month]) * 100)
    list_month_change.append(monthly_change)
max_change = max(list_month_change)

for month in range(0, 11):
    if list_month_change[month] == max_change:
        max_change_month = month

print("The greatest monthly change was {}% from {} to {}.".format(max_change, list_months[max_change_month - 1], list_months[max_change_month]))
