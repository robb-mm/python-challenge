import os, csv

TotalVotes = 0; WinnerWon = 0
candidates = {}

# specify the csv file to analyse
csvpath = os.path.join('Resources', 'election_data.csv')

# open the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    # read the header row
    next(csvreader)
    
    # read the csv rows
    for row in csvreader:
        # increment this, it's one vote per row
        TotalVotes += 1

        # track the candidate's vote count, using a dictionary {name:vote count}
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

    # Display the results
    print("Election Results")
    print("-----------------------------------------")
    print(f"Total Votes: {TotalVotes}")
    print("-----------------------------------------")

    # iterate over the candidates dictionary
    for name in candidates:
        
        # divide candidate's votes by total votes, then multiply by 100
        PercentWon = round(candidates[name] / TotalVotes * 100, 3)
        TotalWon = candidates[name]
        
        # Display the candidate's name, percentage of votes won, total number of votes won
        print(f"{name}: {PercentWon}% ({TotalWon})")

        # track the winner, WinnerWon as marker variable
        if (WinnerWon < TotalWon):
            WinnerWon = TotalWon
            WinnerName = name

    # Display the results
    print("")
    print("-----------------------------------------")
    print(f"Winner: {WinnerName}")
    print("-----------------------------------------")

# Specify the file to write to
output_file = os.path.join('analysis', 'PyPoll.out')

# Write the results to file
with open(output_file, 'w') as text:
    text.write("Election Results\n")
    text.write("-----------------------------------------\n")
    text.write(f"Total Votes: {TotalVotes}\n")
    text.write("-----------------------------------------\n")

    for name in candidates:
        PercentWon = round(candidates[name] / TotalVotes * 100, 3)
        TotalWon = candidates[name]
        text.write(f"{name}: {PercentWon}% ({TotalWon})\n")

    text.write("\n-----------------------------------------\n")
    text.write(f"Winner: {WinnerName}\n")
    text.write("-----------------------------------------\n")
