# PyBank dataset

# Import os and csv modules to import the csv data files
import os
import csv

# Path for csv file
budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')

# Set variables for use in dataset analysis
total_months = []
total_net_amount = 0
total_change = 0
change = 0
average_change = []
greatest_increase = []
greatest_decrease = []

# Open csv file containing the financial data
with open(budget_csv) as csv_file:
    csv_reader  = csv.reader(csv_file, delimiter=",")
    
    # Skip header so it does not get analyzed
    header = next(csv_reader)

    # Then read through every row after the header row
    for row in csv_reader:

        # Analyze the total number of months in the dataset
        date = (row[0])
        total_months.append(date)

        month_count = len(total_months)

        # Net total amount of "Profit/Losses" over the entire period
        profit_losses = int(row[1])
        total_net_amount += profit_losses

        # Changes in "Profit/Losses" over the entire period, and then the average of those changes
        change_pro_los = profit_losses - change
        average_change.append(change_pro_los)

        total_avg_change = sum(average_change)/len(average_change)
        total_avg_change = round(total_avg_change, 2)

        # The greatest increase in profits (date and amount) over the entire period
        # The greatest decrease in profits (date and amount) over the entire period

# Create the output txt file
output_txtfile = "budget_analysis.txt"

with open(output_txtfile, 'w') as file:

# Print analysis title and analysis values
print("Financial Anaysis")
print("----------------------------")
print("Total Months: ", month_count) 
print(f"Total: ${total_net_amount}")
print(f"Average Change: ${total_avg_change}")
print(f"Greatest Increase in Profits: {}%")
print(f"Greatest Decrease in Profits: {}%")