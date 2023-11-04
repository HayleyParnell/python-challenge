#Your task is to create a Python script that analyzes the records to calculate each of the following values:

#The total number of months included in the dataset

#the net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

#final script should both print the analysis to the terminal and export a text file with the results

import os
import csv

# Specify the path to your CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize variables to store the analysis results
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

# Open the CSV file for reading
with open(csvpath, mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        # Extract the month and profit/loss values
        month = row[0]
        profit_loss = int(row[1])

        # Calculate the total profit/losses
        total_profit_losses += profit_loss

        # Calculate the changes in profit/losses
        if total_months > 0:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)
            months.append(month)

        previous_profit_loss = profit_loss

        total_months += 1

# Calculate the average change in profit/losses
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(profit_loss_changes)
greatest_decrease = min(profit_loss_changes)

# Get the corresponding month for the greatest increase and decrease
increase_month = months[profit_loss_changes.index(greatest_increase)]
decrease_month = months[profit_loss_changes.index(greatest_decrease)]

# Print the analysis results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

# Specify the path for the output text file
output_path = os.path.join('Analysis','PyBank_output.txt')

# Write the analysis results to a text file
with open(output_path, mode='w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_losses}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n")


