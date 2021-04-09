import os
import csv
csvpath = os.path.join('...','Resources','election_data.csv')
csvreader = csv.reader(csvfile,delimiter=',')
print(csvreader)