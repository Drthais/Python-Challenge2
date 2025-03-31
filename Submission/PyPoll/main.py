# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates_poll = {}


# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1


        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates_poll:
            candidates_poll[candidate_name] = 1
        else:
            candidates_poll[candidate_name] += 1


        # Add a vote to the candidate's count

winners_votes = max(candidates_poll.values())
total_votes = sum(candidates_poll.values())
for candidate_name, votes in candidates_poll.items():
    if votes == winners_votes:
        winner_name = candidate_name
        break
    
    
    
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print('Election Results')
    txt_file.write('Election Results\n')    
    print('-------------------------')  
    txt_file.write('-------------------------\n')   
    print(f'Total Votes: {total_votes}')    
    txt_file.write(f'Total Votes: {total_votes}\n')     
    print('-------------------------')
    txt_file.write('-------------------------\n')

    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_name, votes in candidates_poll.items():
        

        # Get the vote count and calculate the percentage
        vote_percentage = (votes/total_votes) * 100

        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage
        print(f'{candidate_name}: {vote_percentage:.3f}% ({votes})')
        txt_file.write(f'{candidate_name}: {vote_percentage:.3f}% ({votes})\n')


    # Generate and print the winning candidate summary
    print('-------------------------')  
    txt_file.write('-------------------------\n')   
    print(f'Winner: {winner_name}')    
    txt_file.write(f'Winner: {winner_name}\n')   
    print('-------------------------')
    txt_file.write('-------------------------\n')


    # Save the winning candidate summary to the text file
