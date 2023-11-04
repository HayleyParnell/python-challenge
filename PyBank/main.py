#Your task is to create a Python script that analyzes the records to calculate each of the following values:

#The total number of months included in the dataset

#the net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

#final script should both print the analysis to the terminal and export a text file with the results



#import and set file path associated with the file

import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')


#set variables
total_months = 0
months = []

total_profit_losses = 0
previous_profit_loss = 0
profit_loss_changes = []


#open and read the file
with open(csvpath,mode ="r", newline = "") as file:
    csv_reader = csv.reader(file)
    print(csv_reader)

    csv_header = next(csv_reader)
    
    
    #find the total number of months
    for row in csv_reader:
        #set variables for month and profit losses
        month = row[0]
        profit_loss = int(row[1])

        #find total profit/losses
        total_profit_losses += profit_loss

    #total profit/losses changes
        if total_months > 0 :
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)
            months.append(month)

        previous_profit_loss = profit_loss

        total_months += 1


#calculate average change in profit/losses
average_change = sum(profit_loss_changes) / len(profit_loss_changes)   

# Find the greatest increase and decrease in profits
greatest_increase = max(profit_loss_changes)
greatest_decrease = min(profit_loss_changes)
      
#find month of the greatest increase and decrease
increase_month = months[profit_loss_changes.index(greatest_increase)]
decrease_month = months[profit_loss_changes.index(greatest_decrease)]


# Specify the path for the output text file
output_path = os.path.join("Analysis", "PyBank_output.txt")

# Write the analysis results to a text file
with open(output_path, mode='w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_losses}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n")

