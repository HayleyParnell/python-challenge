import os
import csv

# Specify the path to your CSV file
csvpath = os.path.join('Resources', 'election_data.csv') 

# Initialize variables to store the analysis results
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Open the CSV file for reading
with open(csvpath, mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

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

