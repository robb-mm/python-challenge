import os, csv

TotalVotes = 0; WinnerWon = 0
candidates = {}

csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)
    for row in csvreader:
        TotalVotes += 1

        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

    print("Election Results")
    print("-----------------------------------------")
    print(f"Total Votes: {TotalVotes}")
    print("-----------------------------------------")

    for name in candidates:
        PercentWon = round(candidates[name] / TotalVotes * 100, 3)
        TotalWon = candidates[name]
        print(f"{name}: {PercentWon}% ({TotalWon})")

        if (WinnerWon < TotalWon):
            WinnerWon = TotalWon
            WinnerName = name

    print("")
    print("-----------------------------------------")
    print(f"Winner: {WinnerName}")
    print("-----------------------------------------")

# Specify the file to write to
output_file = os.path.join('analysis', 'PyPoll.out')

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
