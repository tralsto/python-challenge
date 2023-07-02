# election_data.csv data set

# Import os and csv modules to import the csv data files
import os
import csv

# Open and read csv file
election_csv = os.path.join ('Resources', 'election_data.csv')

with open(election_csv) as csv_file:
    csv_reader  = csv.reader(csv_file, delimiter=",")

    print(csv_reader)

    # Read header row of csv file
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Then read through every row after the header row
    for row in csv_reader:
        print(row)

