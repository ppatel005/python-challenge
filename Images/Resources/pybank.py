import os
import csv
cvspath = os.path.join('budget_data.csv')

with open(budget_data_csv, newline='') as csvfile:
    cvs = cvs.reader(cvsfile, delimiter=',')
    cvs_header = next(cvsreader)
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
        

total_month = 0
total_volume = 0
greatestIncrease = 0
greatestDecrease = 0
greatestMonth = []
worstMonth = []
change = []
monthtomonthchange = []


