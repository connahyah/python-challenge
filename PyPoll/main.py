## PyPoll
#* In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
#(Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
#* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
#The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
#Your task is to create a Python script that analyzes the votes and calculates each of the following:

import csv

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
file_to_load = "election_data.csv"
file_to_output = "election_analysis.txt"
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)
    for row in reader:

        # Run the loader animation
        print(". ", end=""),


#  * The total number of votes cast
total_votes = 0

# * A complete list of candidates who received votes
candidate_options = []
candidate_votes = {}

# * The percentage of votes each candidate won

# * The total number of votes each candidate won

# * The winner of the election based on popular vote.
winning_candidate = ""
winning_count = 0


        # Add to the total vote count
        total_votes = total_votes + 1
 
        # Extract the candidate name from each row
        candidate_name = row["Candidate"]

        # If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:
        # Retrieve vote count and percentage
            votes = candidate_votes.get(candidate)
            vote_percentage = float(votes) / float(total_votes) * 100
        # Determine winning vote count and candidate
            if (votes > winning_count):
                winning_count = votes
                winning_candidate = candidate

        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")
   txt_file.write(election_results)

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
