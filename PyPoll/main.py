# Py Me Up Charlie
# Python Homework
# PyPoll

import os
import csv

# Set path for file
electiondata_csv = os.path.join("election_data.csv")

# PyPoll\election_data.csv

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

#can_list = []
#for x in Candidate(row[2]):
#    if x == 'Li':
#        can_list.append(x)

# can_count = len(can_list)



