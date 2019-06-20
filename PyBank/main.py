# Py Me Up Charlie
# Python Homework
#

import os
import csv

# Set path for file
budgetdata_csv = os.path.join("c:/", "DataVisual","UCFLM20190409DATA", "Homework","03-Python", 
 "Instructions", "PyBank", "Resources", "budget_data.csv")

# Lists to store data
month = []
profit_loss = []
profit = []
loss = []

#Open and read csv
with open(budgetdata_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        # Add months
        month.append(row[0])

        # Add profit and loss
        profit_loss.append(row[1])

#print(month)


#print(month_count)
month_count = len(month)
print('-------------------------')
print("Total Months: " + str(month_count))
#print('-------------------------')
new_profit_loss = list(map(int, profit_loss))
#print(new_profit_loss)

#print('-------------------------')
total_profit_loss = sum(new_profit_loss)
print("Total:  $" + str(total_profit_loss))

Average = (total_profit_loss / month_count)
print("Average Change:  $" + str(Average))

Maxprof = max(new_profit_loss)
#print(Maxprof)

Minprof = min(new_profit_loss)
#print(Minprof)

minpos = new_profit_loss.index(min(new_profit_loss))
#print(minpos)

maxpos = new_profit_loss.index(max(new_profit_loss))
#print(maxpos)


#print(month[minpos])
#print(month[maxpos])

print("Greatest Increase in profits: " + month[maxpos] + " " + str(Maxprof))
print("Greatest Decrease in Profits: " + month[minpos] + " " + str(Minprof))

