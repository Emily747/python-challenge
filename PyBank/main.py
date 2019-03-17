#Emily Hudson
#Homerwork 3 Python Challenge
#DVA Cohort 3

#import csv file
import os
import csv
import numpy as np

#set path for file
homework3 = os.path.join('..','Pybank', 'PyBankData.csv')
#open and read csv
with open(homework3, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print a list out of the dates

    date = []
    net = []
    change =[]
    total = 0
    avg_change = 0
    length =len(date)
    
    #for each row in csvreader, add each thing in the 1st position (because we start at 0) to the list called "date"
    for row in csvreader:
        date.append(row[0])
        net.append(row[1])
        
    #removing headers from lists
    date.pop(0)
    net.pop(0)
    
    #make sure amounts are numbers to Python
    net = list(map(int, net))

    for number in net:
        total += number

    change = np.diff(net)
    avgchange = sum(change)/len(change)

    date.pop(0)
    net.pop(0)

    idxa = np.nanargmax(change)
    idxi = np.nanargmin(change)
    import sys
    sys.stdout = open('Financial Analysis.txt', 'w')
    print("Financial Analysis")
    print("----------------------------------------")
    print(f"Total Months: {len(date)+1}")
    print(f"Net Total Profit and Loss: ${total}")
    print(f"Average Change: ${avgchange}")
    print(f"Greatest Increase in Profits: {date[idxa]} ${change.max()}")
    print(f"Greatest Decrease in Profits: {date[idxi]} ${change.min()}")

    sys.stdout.close()

    
