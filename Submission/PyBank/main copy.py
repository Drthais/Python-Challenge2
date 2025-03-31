# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
max_increase = 0
max_decrease = 0
max_increase_month = ""
max_decrease_month = ""
total_net_change = 0
previous_profit = 0
current_profit = 0


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    previous_profit = int(first_row[1])
    current_change = previous_profit



    # Track the total and net change
    total_net += current_change
   
    
    


    # Process each row of data
    for row in reader:
        current_change = int(row[1]) - previous_profit
        previous_profit = int(row[1])

        # Track the total
        total_net += int(row[1])
        total_months += 1
        


        # Track the net change
        total_net_change += current_change 

        # Calculate the greatest increase in profits (month and amount)
        if current_change > max_increase:
            max_increase = current_change
            max_increase_month = row[0]


        # Calculate the greatest decrease in losses (month and amount)
        if current_change < max_decrease:
            max_decrease = current_change
            max_decrease_month = row[0]



# Calculate the average net change across the months
avg_change = total_net_change / (total_months - 1)



# Generate the output summary
output = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${avg_change:.2f}
Greatest Increase in Profits: {max_increase_month} (${max_increase})
Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})"""


# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
