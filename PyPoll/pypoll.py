import os
import csv
# variables
candidate_names = []
votes_each_can = {}
percent_votes_each_can = {}
line_count = 0
total_votes = 0

csvpath = os.path.join('PyPoll/Resources/election_data.csv')
with open(csvpath) as csvfile:
    csv = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv)

    for row in csv:
        total_votes += 1
        current_candidate = row[2]
        if current_candidate not in candidate_names:
            candidate_names.append(current_candidate)
            votes_each_can[current_candidate] = 1
        else:
            votes_each_can[current_candidate] += 1
# output/outwrite file
with open("output.txt", "w") as report_file:
    report_file.write("Election Results\n")
    report_file.write("--------------------\n")
    report_file.write(f"Total Votes: {total_votes}\n")
    report_file.write("--------------------\n")
    for candidate, votes in votes_each_can.items():
        percent_votes = (votes/total_votes) * 100
        percent_votes_each_can[candidate] = percent_votes
        report_file.write(f"{candidate}: {percent_votes:.3f}%({votes})\n")
    report_file.write("--------------------\n")

    # Find Winner with override
    winner = max(votes_each_can, key=votes_each_can.get)
    report_file.write(f"Winner:{winner}\n")
    report_file.write("--------------------\n")
# Print the results:
    print("Election Results")
    print("--------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------")
    for candidate, votes in votes_each_can.items():
        percent_votes = (votes / total_votes) * 100
        percent_votes_each_can[candidate] = percent_votes
        print(f"{candidate}: {percent_votes:.3f}% ({votes})")
    print("--------------------")
    # Find Winner
    print(f"Winner: {winner}")
    print("--------------------")
     