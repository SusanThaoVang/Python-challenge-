# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
budgetcsv=os.path.join("Resources", "budget_data.csv")  # Input file path
budgetcsv=os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
total_profits = []
total_changes = []
# Add more variables to track other necessary financial data

# Open and read the csv

with open(budgetcsv, newline='') as budgetcsv:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budgetcsv, delimiter=',')
    # Read the header row first 
    csv_header = next(csvreader)
    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    

    # Track the total and net change
with open(in_file) as revenue_data:
    reader = csv.DictReader(revenue_data)
    header = next(reader)
    # first_row = next(reader)
    # total_months += 1
    # total_Profit_Losses = total_Profit_Losses + int(first_row["Profit/Losses"])
    # previous_revenue = int(first_row["Profit/Losses"])

# Track the total
    for row in csvreader:
        months.append(row[0])
        profits.append(int(float(row[1])))

        # Track the net change
    for x in range(1, len(profits)):
        changes.append((int(profits[x]) - int(profits[x-1])))

        # Calculate the greatest increase in profits (month and amount)
        max_date = months[changes.index(max(changes)) + 1]

        # Calculate the greatest decrease in losses (month and amount)
        min_date = months[changes.index(min(changes)) + 1]


# Calculate the average net change across the months
   for row in reader:
        # int(row["Profit/Losses"])
   
        total_months += 1
        total_Profit_Losses = total_Profit_Losses + int(row["Profit/Losses"])

        revenue_change = int(row["Profit/Losses"]) - previous_revenue
        previous_revenue = int(row["Profit/Losses"])
        revenue_change_list += [revenue_change]
        month_of_change += [row["Date"]]

        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"] 
            greatest_decrease[1] = revenue_change   

revenue_avg = sum(revenue_change_list)/ len(revenue_change_list)

# Generate the output summary
output = os.path.join("Analysis", "Analysis.txt")

# Print the output
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {len(months)}")
print(f"Total Profits: ${sum(profits)}")
print(f"Average change:  ${round(changemonths, 2)}")
print(f"The greatest increase is {max_date} (${max(changes)})")
print(f"The greatest decrease is {min_date} (${min(changes)})")

# Write the results to a text file
#with open(file_to_output, "w") as txt_file:
    #txt_file.write(output)
with open(output, "w") as file:
    writer = csv.writer(file)
    file.write("Financial Analysis\n")
    file.write("------------------------\n")
    file.write(f"Total Months: {len(months)}\n")
    file.write(f"Total Profits: ${sum(profits)}\n")
    file.write(f"Average change:  ${round(changemonths, 2)}\n")
    file.write(f"The greatest increase is {max_date} (${max(changes)})\n")
    file.write(f"The greatest decrease is {min_date} (${min(changes)})\n")