#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

#You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote


#connect operating systems
import os

#connect election data
import csv

# Specify the path to your CSV file
csvpath = os.path.join('Resources', 'election_data.csv') 

# Set variables and dictionary
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Open the CSV file for reading
with open(csvpath, mode='r', newline='') as file:
    csv_reader = csv.reader(file)

    #skip header
    next(csv_reader)  

    for row in csv_reader:
        # Extract the candidate's name
        candidate_name = row[2]

        # Count the total number of votes cast
        total_votes += 1

        # Update the candidate's vote count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Specify the path for the output text file
output_path = os.path.join('Analysis', 'PyPoll_output.txt') 

# Write the analysis results to a text file
with open(output_path, mode='w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    # Calculate and write the percentage and total votes for each candidate
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        # Determine the winner based on popular vote
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes

    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

# Print the analysis results to the terminal
with open(output_path, mode='r') as output_file:
    print(output_file.read())

