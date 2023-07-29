import os
import csv
total_months = 0
total_monthslist = []
total_profitlist = []
total_profit = 0 
profit_changes = []
profit_months = []
greatest_Increase_Amount = 0
greatest_Increase_Month = ''
greatest_Decrease_Amount = 0
greatest_Decrease_Month = ''
total_average = 0
previous_profit = 0
profit_change = 0 
last_row = 0
monthtomonthchange = []
csvpath = os.path.join('PyBank/Resources/budget_data.csv')
with open(csvpath) as csvfile:
    csv = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv)
    for row in csv:
        total_monthslist.append(row[0])
        # total_months = len(total_monthslist)
        total_profitlist.append(int(row[1]))
        # total_profit = sum(total_profitlist)
        # calculate the difference between month to month 
        if len(total_monthslist) > 1:
            profit_change = int(row[1]) - previous_profit
            profit_changes.append(profit_change)
            profit_months.append(row[0])
        previous_profit = int(row[1])
    greatest_Increase_Amount = max(profit_changes)
    idx = profit_changes.index(greatest_Increase_Amount)
    greatest_Increase_Month = profit_months[idx]
    greatest_Decrease_Amount = min(profit_changes)
    idx = profit_changes.index(greatest_Decrease_Amount)
    greatest_Decrease_Month = profit_months[idx]
    total_months = len(total_monthslist)
    total_profit = sum(total_profitlist)
    count = len(profit_changes)
    amount = sum(profit_changes)
    total_average = round(amount/count,2)
    output = []
    output.append("Financial Analysis")
    output.append("--------------------")
    output.append(f"Total Months: {total_months}")
    output.append(f"Total Profit: ${total_profit}")
    output.append(f"Total Average: ${total_average}")
    output.append(f"Greatest Increase in Profits: {greatest_Increase_Month} (${greatest_Increase_Amount})")
    output.append(f"Greatest Decrease in Profits: {greatest_Decrease_Month} (${greatest_Decrease_Amount})")
    #print(monthtomonthchange)
    for line in output:
        print(line)
    outpath = os.path.join('PyBank/Analysis/output.txt')
    with open(outpath,"w") as outfile:
        for line in output:
            outfile.write(line+"\n")

    
    



