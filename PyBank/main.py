import csv
csvpath = './Desktop/LearnPython/Assignment3/budget_data.csv'
with open(csvpath) as F:
  csvreader = csv.DictReader(F)
  Dates = []
  Profit_Loss = []
  Difference=[]
  previous_amount=0
  total=0
  # read the csvfile
  for row in csvreader:
    #  put data into the empty variables above

      Dates.append(row['Date'])
      total += int(row['Profit/Losses'])
      Profit_Loss.append(row['Profit/Losses'])

     # loop through Profit_Loss
for i in Profit_Loss:

    Difference.append(int(i)- previous_amount)
    previous_amount=int(i)

# pop the very first value since there is no difference recorded
Difference.pop(0)

#find the location of the max and min changes
max_change= Difference.index(max(Difference))
min_change= Difference.index(min(Difference))

Date_Greatest_Increase= Dates[max_change + 1]
Date_Greatest_Decrease= Dates[min_change + 1]


total_change=sum(Difference)

# finding the average
Average=0
Average=total_change/(len(Dates)-1)

# print out final output using f'strings
Header="Financial Analysis"
Line1="----------------------------"
Line2= f'Total Months : {len(Dates)}'
Line3= f'Total : ${total}'
Line4= f'Average  Change : ${Average} '
Line5=f'Greatest Increase in Profits : {Date_Greatest_Increase}  ( ${max(Difference)})'
Line6=f'Greatest Decrease in Profits : {Date_Greatest_Decrease}  (${min(Difference)})'

print (Header)
print (Line1)
print (Line2)
print (Line3)
print (Line4)
print (Line5)
print (Line6)

# exporting results from the analysis
output_path = r"C:/Users/portia/Documents/GitHub/python-challenge/PyBank/Budget_output2.csv"
with open(output_path,"w") as output:

    csvwriter = csv.writer(output)

    csvwriter.writerow([Header])
    csvwriter.writerow([Line1])
    csvwriter.writerow([Line2])
    csvwriter.writerow([Line3])
    csvwriter.writerow([Line4])
    csvwriter.writerow([Line5])
    csvwriter.writerow([Line6])
