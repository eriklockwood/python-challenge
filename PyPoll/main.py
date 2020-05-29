import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, 'r') as election_data:
    candidates = dict()
    tot_votes = 0
    csvreader = csv.reader(election_data)
    next(csvreader)
    for row in csvreader:
        vote = row[2]
        tot_votes += 1
        if vote in candidates:
            candidates[vote] += 1
        else:
            candidates[vote] = 1

    print()
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {tot_votes}')
    print('-------------------------')
    for key, value in candidates.items():
        percent = value/tot_votes
        print(f'{key}: {percent:2.3%} ({value} votes for)')
    print('-------------------------')
    print(f'Winner: {max(candidates, key=lambda key: candidates[key])}')
    print('-------------------------')
    print()

    with open("Output.txt", "w") as text_file:
        print('Election Results', file=text_file)
        print('-------------------------', file=text_file)
        print(f'Total Votes: {tot_votes}', file=text_file)
        print('-------------------------', file=text_file)
        for key, value in candidates.items():
            percent = value/tot_votes
            print(f'{key}: {percent:2.3%} ({value} votes for)', file=text_file)
        print('-------------------------', file=text_file)
        print(f'Winner: {max(candidates, key=lambda key: candidates[key])}', file=text_file)