# Py Me Up Charlie
# Python Homework
# PyBank

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
print("Financial Analysis")
print("-------------------------")

print("Total Months: " + str(month_count))

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

print("Greatest Increase in profits: " + month[maxpos] + " " + "($" + str(Maxprof)+ ")")
print("Greatest Decrease in Profits: " + month[minpos] + " " + "($" + str(Minprof) + ")")

# save the output file path
output_file = os.path.join("c:/", "Users","clari", "BootcampHomework","python-challenge", 
 "PyBank", "PyBankoutput.txt")

 # open the file and write to csv
with open(output_file, "w") as f:
    #writer =csv.writer(datafile)
    f.write("Financial Analysis" + "\n")
    f.write("------------------" + "\n")
    f.write("Total Months: " + str(month_count) + "\n")
    f.write("Total:  $" + str(total_profit_loss) + "\n")
    f.write("Average Change:  $" + str(Average) + "\n")
    f.write("Greatest Increase in profits: " + month[maxpos] + " " + "($" + str(Maxprof)+ ")" + "\n")
    f.write("Greatest Decrease in Profits: " + month[minpos] + " " + "($" + str(Minprof) + ")" + "\n")
