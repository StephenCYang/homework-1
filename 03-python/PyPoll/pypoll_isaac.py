# PROBLEMS
# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process...
# ...You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv)...
# ...The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create...
# ...a Python script that analyzes the votes and calculates each of the following:

# (1) The total number of votes cast
     #(After the header row, iterate through each row and add it to a counter)
# (2) A complete list of candidates who received votes
     #(Possibly look for unique values in the 3rd row (index 2).
# (3) The total number of votes each candidate won.
# (4) The percentage of votes each candidate won.
     #(sum the votes for each candidate and then device by the total votes)
# (5) The winner of the election based on popular vote.
     #(maybe use "max" function and assign to a variable, then if >< statement to determine the winner)
# As an example, your analysis should look similar to the one below:
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#-----------------------------------------------------

import csv
#IMPORTING MODULES
import os

#GRAB CVS FILE (data to be analyzed)
csv_file = os.path.join("Resources" , "election_data.csv")
txt_file = os.path.join("Analysis" , "analysis.txt")

#DEFINE VARIABLES (based on the HW problems)
candidate_list = [] #storing the different candidates in here
candidate_votes = {} #A dictionary that will hold the candidates name along with ther corresponding number of votes.)
total_votes = 0 #counter
candidate_winner = ""
winner_votes = 0 #counter #ooo

#Open CSV and read
with open(csv_file) as data:
    csv_reader = csv.DictReader(data) #unlike PyBank, this reads my first row as a header (no need for "next" function)...
    #...read my csv as a dictionary, and will read like a dictionary.

    #Start iterating through rows to get the total number of votes, the candidates, and their individual votes.

    for row in csv_reader:
        total_votes += 1 #this increments and ads to the variable at each iteration
        candidate_name = row["Candidate"] #ooo Once done, see if i can add this variable to the top ist of variables

        #set up if statement so that if candidate_name isnt in the candidate list it get's added and so does their votes. Append?
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

#WRITE ANALYSIS TO TXT FILE.
#ATTENTION MARK & AHMED: This is not how I want to export my analysis. I can't get it another way. I get too many errors...
#... I would like to assign all of this to a variable, but my code is different.
with open(txt_file , "w") as txt_file:
    print("POLL ANALYSIS",file=txt_file)
    print("********************",file=txt_file)
    print(f"Total votes: {total_votes:,}",file=txt_file)
    print("********************",file=txt_file)
    print(f"List of candidates: {candidate_list}",file=txt_file)
    print("********************",file=txt_file)
    #print(candidate_votes)
    for candidate in candidate_votes:
        candidate_votes.get(candidate_name)
        percentage_of_votes = float(candidate_votes[candidate]) / float(total_votes) * 100
        print(f"{candidate}: {percentage_of_votes:.2f}% ({candidate_votes.get(candidate):,})",file=txt_file)
        if candidate_votes[candidate] > winner_votes:
            winner_votes = candidate_votes[candidate]
            candidate_winner = candidate
    print("********************",file=txt_file)
    percentage_of_votes = (winner_votes / total_votes) * 100
    print(f"The winner is {candidate_winner} and got {percentage_of_votes:.2f}% of the votes ({winner_votes:,})",file=txt_file)

#PRINT ANALYSIS TO TERMINAL
    print("POLL ANALYSIS")
    print("*" * 20)
    print(f"Total votes: {total_votes:,}")
    print("-" * 20)
    print(f"List of candidates: {candidate_list}")
    print("*" * 20)
    #print(candidate_votes)
    for candidate in candidate_votes:
        candidate_votes.get(candidate_name)
        percentage_of_votes = float(candidate_votes[candidate]) / float(total_votes) * 100
        print(f"{candidate}: {percentage_of_votes:.2f}% ({candidate_votes.get(candidate):,})")
        if candidate_votes[candidate] > winner_votes:
            winner_votes = candidate_votes[candidate]
            candidate_winner = candidate
    print("*" * 20)
    percentage_of_votes = (winner_votes / total_votes) * 100
    print(f"The winner is {candidate_winner} and got {percentage_of_votes:.2f}% of the votes ({winner_votes:,})")