# PyBank dataset
# Import os and csv modules to import the csv data files
import os
import csv

# Path for csv file
budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')

# Set variables for use in dataset analysis
total_months = []
total_net_amount = 0
change = []
previous_pnl = 0

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

        # Net total amount of "Profit/Losses" over the entire period
        profit_losses = int(row[1])
        total_net_amount += profit_losses

        # Changes in "Profit/Losses" over the entire period
        change_profit_loss = profit_losses - previous_pnl   
        change.append(change_profit_loss)
        previous_pnl = profit_losses

# Calculate total number of months
month_count = len(total_months)

# Calculate average change from overall profit/losses
average_change = sum(change[1:]) / (month_count - 1)
average_change = round(average_change, 2)

# Utilize max and min functions to find the values over the entire period
greatest_max = change.index(max(change))
greatest_min = change.index(min(change))

# Retrieve matching date to max/min values
max_date = total_months[greatest_max]
greatest_increase = change[greatest_max]
min_date = total_months[greatest_min]
greatest_decrease = change[greatest_min]

# Create the output txt file into the analysis folder
output_folder = os.path.join('.', 'analysis')
output_txtfile = os.path.join(output_folder, 'budget_analysis.txt')

with open(output_txtfile, 'w') as file:
  file.write("Financial Anaysis\n")
  file.write("----------------------------\n")
  file.write("Total Months: " + str(month_count) + "\n") 
  file.write("Total: $" + str(total_net_amount) + "\n")
  file.write("Average Change: $" + str(average_change) + "\n")
  file.write("Greatest Increase in Profits: " + str(max_date) + " ($" + str(greatest_increase) + ")" + "\n")
  file.write("Greatest Decrease in Profits: " + str(min_date) + " $(" + str(greatest_decrease) + ")" + "\n")

# Print analysis title and analysis values in terminal
print("Financial Anaysis")
print("----------------------------")
print("Total Months: ", month_count) 
print(f"Total: ${total_net_amount}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {min_date} (${greatest_decrease})")