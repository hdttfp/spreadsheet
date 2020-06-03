import csv
import matplotlib.pyplot as plt

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

average_sales = total_sales / len(list_months)
average_expenditure = total_expenditure / len(list_months)
average_profit = total_profit / len(list_months)

max_sales = max(list_sales)
min_sales = min(list_sales)
max_expenditure = max(list_expenditure)
min_expenditure = min(list_expenditure)
max_profit = max(list_profit)
min_profit = min(list_profit)
for month in range(0, 11):
    if list_sales[month] == max_sales:
        max_sales_month = month
    if list_sales[month] == min_sales:
        min_sales_month = month
    if list_expenditure[month] == max_expenditure:
        max_expenditure_month = month
    if list_expenditure[month] == min_expenditure:
        min_expenditure_month = month
    if list_profit[month] == max_profit:
        max_profit_month = month
    if list_profit[month] == min_profit:
        min_profit_month = month

with open('summary.csv', 'w+') as csv_file:
    field_names = ['data', 'total', 'average', 'maximum', 'max month', 'minimum', 'min month']
    summary = csv.DictWriter(csv_file, fieldnames=field_names)
    summary.writeheader()
    summary.writerow({'data': 'sales', 'total': total_sales, 'average': average_sales,
                      'maximum': max_sales, 'max month': list_months[max_sales_month],
                      'minimum': min_sales, 'min month': list_months[min_sales_month]})
    summary.writerow({'data': 'expenditure', 'total': total_expenditure, 'average': average_expenditure,
                      'maximum': max_expenditure, 'max month': list_months[max_expenditure_month],
                      'minimum': min_expenditure, 'min month': list_months[min_expenditure_month]})
    summary.writerow({'data': 'profit', 'total': total_profit, 'average': average_profit,
                      'maximum': max_profit, 'max month': list_months[max_profit_month],
                      'minimum': min_profit, 'min month': list_months[min_profit_month]})

list_month_change = [0]
for month in range(0, 11):
    monthly_change = int(((list_profit[month + 1] - list_profit[month]) / list_profit[month]) * 100)
    list_month_change.append(monthly_change)
max_change = max(list_month_change)

for month in range(0, 11):
    if list_month_change[month] == max_change:
        max_change_month = month

print("The greatest monthly change was {}% from {} to {}.".format(max_change, list_months[max_change_month - 1], list_months[max_change_month]))

plt.plot(list_months, list_sales)
plt.title('Data from the CSV File: Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
