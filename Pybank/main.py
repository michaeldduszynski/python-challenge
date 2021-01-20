import os
import csv
    
# Variables
total_months = 0
net_total = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Link CSV
csvpath = os.path.join('budget_data.csv')

# Open & Read CSV File
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    row = next(csvreader)

    # Calculate Variables
    previous_row = int(row[1])
    total_months += 1
    net_total += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Calculate Each Row 
    for row in csvreader:
        total_months += 1
        net_total += int(row[1])

        budget_change = int(row[1]) - previous_row
        monthly_change.append(budget_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
    #Calculate Increase  
    if int(row[1]) > greatest_increase:
        greatest_increase = int(row[1])
        greatest_increase_month = row[0]
            
    # Calculate Decrease
     if int(row[1]) < greatest_decrease:
        greatest_decrease = int(row[1])
        greatest_decrease_month = row[0]  
        
    # Calculate Average
    average_change = sum(monthly_change)/ len(monthly_change)

    # Calculate Date
    greatest = max(monthly_change)
    lowest = min(monthly_change)

# Print
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${greatest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# Create txt file
output_file = os.path.join('budget_data.txt')

# Write txt file
with open(output_file, 'w',) as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${greatest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")