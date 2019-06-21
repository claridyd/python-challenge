# Py Me Up Charlie
# Python Homework
# PyPoll

import os
import csv

# Set path for file
electiondata_csv = os.path.join("c:/", "DataVisual","UCFLM20190409DATA", "Homework","03-Python", 
 "Instructions", "PyPoll", "Resources", "election_data.csv")

#List to store data
VoterId = []
County = []
Candidate = []

 #Open and read csv
with open(electiondata_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        # Add VoterId
        VoterId.append(row[0])

        # Add County
        County.append(row[1])

        # Add Candidate
        Candidate.append(row[2])
# Get total votes
votecount = len(VoterId)

print("Total Votes: " + str(votecount))   

# Get unique candidate names
c_list = list(set(Candidate))
#print(c_list)
for word in c_list:
    print(word)

# Variable to hold candidate count
c_total = []

# Calcuate percentage
# c_percent = ((c_total / votecount)*100)

#for c_total in c_list:
#    VoterId.append(row[0])   
#print(c_total)







