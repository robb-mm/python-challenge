import os
import csv

TotalMonths = 0; NetProfit = 0; 
MinProfit = 0; MaxProfit = 0
PrevProfit = 0; ProfitChange = 0; AveChange = 0
ProfitChanges = []

# specify the csv file to analyse
csvpath = os.path.join('Resources', 'budget_data.csv')

# open the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    # read the header row
    next(csvreader)
    
    # read the csv rows
    for row in csvreader:
        
        # increment this, it's one month per row
        TotalMonths += 1
        
        # update this, it's one profit/loss per row
        NetProfit += int(row[1])

        # current row's profit/loss minus previous row's profit/loss
        ProfitChange = int(row[1]) - PrevProfit
        
        # put ProfitChange in a list
        ProfitChanges.append(ProfitChange)
        
        # save current row's Profit as PrevProfit
        PrevProfit = int(row[1])

        # set current row's ProfitChange as MaxProfit, if condition true
        if (MaxProfit < ProfitChange):
            MaxProfit_Date = row[0]
            MaxProfit = ProfitChange

        # set current row's ProfitChange as MinProfit, if condition true
        if (MinProfit > ProfitChange):
            MinProfit_Date = row[0]
            MinProfit = ProfitChange
        

    # get the average Profit Change for all months
    AveChange = round(sum(ProfitChanges) / len(ProfitChanges), 2)
    
    # Display the results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {TotalMonths}")
    print(f"Net Profit: ${NetProfit}")
    print(f"Average Change: ${AveChange}")
    print(f"Greatest Increase in Profits: {MaxProfit_Date} (${MaxProfit})")
    print(f"Greatest Decrease in Profits: {MinProfit_Date} (${MinProfit})")

# Specify the file to write to
output_path = os.path.join('analysis', 'PyBank.out')

# Write the results to file
with open(output_path, 'w') as text:
    text.write("Financial Analysis\n")
    text.write("------------------\n")
    text.write(f"Total Months: {TotalMonths}\n")
    text.write(f"Net Profit: ${NetProfit}\n")
    text.write(f"Average Change: ${AveChange}\n")
    text.write(f"Greatest Increase in Profits: {MaxProfit_Date} (${MaxProfit})\n")
    text.write(f"Greatest Decrease in Profits: {MinProfit_Date} (${MinProfit})\n")

