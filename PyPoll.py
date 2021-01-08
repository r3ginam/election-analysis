# Add dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# initialize total votes variable (accumulator) to 0
total_votes = 0
#Declare a new list
candidate_options = []
#Declare a new dictionary
candidate_votes = {}
#winning candidate and winning count tracker
winning_candidate = " "
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
     # Read the header row
    headers = next(file_reader)
    #Print each row in the CSV file
    for row in file_reader:
        #add to the total vote count
        total_votes += 1
        #print candidate name from each row
        candidate_name = row[2]
        #Add to candidate list without repeating names
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1
# Save the results to our text file
with open(file_to_save, "w") as txt_file:
#Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #save the final vote count to the text file.
    txt_file.write(election_results)
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate percentage of votes
        vote_percentage = float(votes) /float(total_votes) * 100
        # Print the candidate name and percentage of votes
        print(f'{candidate_name}: recieved {vote_percentage: .2f}% of the vote.')
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        #Determine winning vote count and candidate
        #Determine if the cotes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true, then winning count = votes, etc.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set winning candidate = candidate name
            winning_candidate = candidate_name
    #Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidates results to the text file.
    txt_file.write(winning_candidate_summary)
    
    # 1. The total number of votes cast
    # 2. A complete list of candidates who received votes
    # 3. The percentage of votes each candidate won
    # 4. The total number of votes each candidate won
    # 5. The winner of the election based on popular vote