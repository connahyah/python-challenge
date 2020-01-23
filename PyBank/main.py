# PyBank
# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

import csv
file_to_load = "budget_data.csv"
file_to_output = "budget_analysis.txt"
reader = csv.DictReader(revenue_data)

# Your task is to create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
total_months = 0
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])

# The net total amount of "Profit/Losses" over the entire period
total_revenue = 0
prev_revenue = 0

# The average of the changes in "Profit/Losses" over the entire period
month_of_change = []
revenue_change_list = []
        revenue_change = int(row["Revenue"]) - prev_revenue
        prev_revenue = int(row["Revenue"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# The greatest increase in profits (date and amount) over the entire period
greatest_increase = ["", 0]
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

# The greatest decrease in losses (date and amount) over the entire period
greatest_decrease = ["", 9999999999999999999]
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
