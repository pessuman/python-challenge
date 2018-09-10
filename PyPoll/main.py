import csv

csvpath = './Users/Desktop/LearnPython/Assignment3/election_data.csv'
with open(csvpath,encoding='utf-8') as f:
  reader = csv.DictReader(f)
  
