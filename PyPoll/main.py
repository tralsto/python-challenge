# PyPoll dataset

# Import os and csv modules to import the csv data files
import os
import csv

# Path for csv file
election_csv = os.path.join ('.', 'Resources', 'election_data.csv')

# Variables for use in analysis of dataset
total_votes = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0

# Open and read csv file containing election data
with open(election_csv) as csv_file:
    csv_reader  = csv.reader(csv_file, delimiter=",")

    # Skip header so it does not get analyzed
    header = next(csv_reader)

    # Then read through every row after the header row
    for row in csv_reader:

        # The total number of votes cast
        total_votes += 1

        # A complete list of candidates who received votes
        candidate_name = row[2]
        
        # Count the votes for each candidate
        if candidate_name == "Charles Casper Stockham":
            stockham_votes += 1
        elif candidate_name == "Diana DeGette":
            degette_votes += 1
        elif candidate_name == "Raymon Anthony Doane":
            doane_votes += 1

# Calculate the percent of vote per candidate
stockham_percentage = (stockham_votes / total_votes) * 100
stockham_percentage = round(stockham_percentage, 3)

degette_percentage = (degette_votes / total_votes) * 100
degette_percentage = round(degette_percentage, 3)

doane_percentage = (doane_votes / total_votes) * 100
doane_percentage = round(doane_percentage, 3)

# The winner of the election based on popular vote
if stockham_votes > degette_votes and stockham_votes > doane_votes:
    winner = "Charles Casper Stockham"
elif degette_votes > stockham_votes and degette_votes > doane_votes:
    winner = "Diana DeGette"
elif doane_votes > stockham_votes and doane_votes > degette_votes:
    winner = "Raymon Anthony Doane"

print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"Charles Casper Stockham: {stockham_percentage}% ({stockham_votes})")
print(f"Diana DeGette: {degette_percentage}% ({degette_votes})")
print(f"Raymon Anthony Doane: {doane_percentage}% ({doane_votes})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")