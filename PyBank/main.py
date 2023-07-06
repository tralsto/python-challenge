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
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

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
        change_profit_loss = profit_losses - change
        average_change.append(change_profit_loss)

        total_avg_change = sum(average_change)/len(average_change)
        total_avg_change = round(total_avg_change, 2)

        # The greatest increase in profits (date and amount) over the entire period
        if change_profit_loss > greatest_increase[1]:
            greatest_increase[0] = date
            greatest_increase[1] = change_profit_loss
    
        percent_inc = (greatest_increase[1] / total_net_amount) * 100
        percent_inc = round(percent_inc, 2)

        # The greatest decrease in profits (date and amount) over the entire period
        if change_profit_loss < greatest_decrease[1]:
            greatest_decrease[0] = date
            greatest_decrease[1] = change_profit_loss
        
        percent_dec = (greatest_decrease[1] / total_net_amount) * 100
        percent_dec = round(percent_dec, 2)

# Create the output txt file into the analysis folder
output_folder = os.path.join('.', 'analysis')
output_txtfile = os.path.join(output_folder, 'budget_analysis.txt')

with open(output_txtfile, 'w') as file:
  file.write("Financial Anaysis\n")
  file.write("----------------------------\n")
  file.write("Total Months: " + str(month_count) + "\n") 
  file.write("Total: $" + str(total_net_amount) + "\n")
  file.write("Average Change: $" + str(total_avg_change) + "\n")
  file.write("Greatest Increase in Profits: " + str(greatest_increase[0]) + str(percent_inc) + "\n")
  file.write("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + str(percent_dec) + "\n")


# Print analysis title and analysis values in terminal
print("Financial Anaysis")
print("----------------------------")
print("Total Months: ", month_count) 
print(f"Total: ${total_net_amount}")
print(f"Average Change: ${total_avg_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} ({percent_inc}%)")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} ({percent_dec}%)")