import csv

csvpath = '../Desktop/LearnPython/Assignment3/election_data.csv'
with open(csvpath,encoding='utf-8') as f:
  csvreader = csv.DictReader(f)

  # creating variables with empty lists
  Voters = []
  Votes = []
  candidate_votedfor =[]
  Unique =[]
  output =[]
  New_list=[]
  Percentage_vote=[]

  for row in csvreader:

# filling in empty lists
    candidate_votedfor.append(row['Candidate'])
    Voters.append(row['Voter ID'])

# Total number of votes cast
Total_votes= len(Voters)

# A complete list of candidates voted for.
Unique = set(candidate_votedfor)
New_list = list(Unique)


Votes = [0] * len(New_list)
# print (Votes)

# Loop through unique. count the number of votes each candidate received.
for i in range(len(New_list)):
    count=0
    for candidate in candidate_votedfor:
        if New_list[i] == candidate:
           count += 1

    Votes[i] += count

# candidate's votes/total votes * 100
Percentage_vote = [j / Total_votes * 100 for j in Votes]
Percentage_vote = [round(j) for j in Percentage_vote]

# finding the winner
winner_index = Votes.index(max(Votes))
winner = New_list[winner_index]

# define and print out analysis
Header ="Election Results "
Line0="    ----------------------------          "
Line1= f'Total Votes: : {Total_votes}'
Line6= f'Winner : {winner} '

print (Header)
print (Line0)
print (Line1)
print (Line0)
for i in range(len(Percentage_vote)) :
    Poll=(f'      {New_list[i]}: {Percentage_vote[i]}% ({Votes[i]})')
    print(Poll)
print (Line0)
print (Line6)

# Exporting results of analysis
output_path = r"C:/Users/portia/Documents/GitHub/python-challenge/PyPoll/Election_output.csv"
with open(output_path,"w") as outpt:

    csvwriter = csv.writer(outpt)

    csvwriter.writerow([Header])
    csvwriter.writerow([Line0])
    csvwriter.writerow([Line1])
    csvwriter.writerow([Line0])


for i in range(len(Percentage_vote)) :
    Poll=(f'       {New_list[i]}: {Percentage_vote[i]}% ({Votes[i]}) \n')
    csvwriter.writerow([Poll])
csvwriter.writerow([Line0])
csvwriter.writerow([Line6])
