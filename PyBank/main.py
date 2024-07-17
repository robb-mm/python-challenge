import os
import csv

TotalMonths = 0; NetProfit = 0; 
MinProfit = 0; MaxProfit = 0
PrevProfit = 0; ProfitChange = 0; AveChange = 0
ProfitChanges = []

csvpath = os.path.join('Resources', 'budget_data_temp.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)
    for row in csvreader:
        # print(row)

        TotalMonths += 1
        NetProfit += int(row[1])

        ProfitChange = int(row[1]) - PrevProfit
        ProfitChanges.append(ProfitChange)
        
        # save current row's Profit as PrevProfit
        PrevProfit = int(row[1])

        if (MaxProfit < ProfitChange):
            MaxProfit_Date = row[0]
            MaxProfit = ProfitChange
            # print(f"{TotalMonths}: {MaxProfit}")

        if (MinProfit > ProfitChange):
            MinProfit_Date = row[0]
            MinProfit = ProfitChange
        
    
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {TotalMonths}")
    print(f"Net Profit: ${NetProfit}")

    # print(f"ProfitChanges {ProfitChanges}")
    AveChange = sum(ProfitChanges) / len(ProfitChanges)
    # print(f"AveChange = {sum(ProfitChanges)} / {len(ProfitChanges)}")
    print(f"Average Change: {AveChange}")

    print(f"Greatest Increase in Profits: {MaxProfit_Date} (${MaxProfit})")
    print(f"Greatest Decrease in Profits: {MinProfit_Date} (${MinProfit})")

# Specify the file to write to
output_path = os.path.join('analysis', 'PyBank.out')

# with open(output_path, 'w') as csvfile:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=' \0')

#     # Write the first row (column headers)
#     csvwriter.writerow("Financial Analysis")
#     csvwriter.writerow("------------------")
#     # csvwriter.writerow()
with open(output_path, 'w') as text:
    text.write("Financial Analysis\n")
    text.write("------------------\n")
    text.write(f"Total Months: {TotalMonths}\n")
    text.write(f"Net Profit: ${NetProfit}\n")
    text.write(f"Greatest Increase in Profits: {MaxProfit_Date} (${MaxProfit})\n")
    text.write(f"Greatest Decrease in Profits: {MinProfit_Date} (${MinProfit})\n")

