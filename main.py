#import csv file
import os
import csv

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
    delta = 0
    length =len(date)
    
    #for each row in csvreader, add each thing in the 1st position (because we start at 0) to the list called "date"
    for row in csvreader:
        date.append(row[0])
        net.append(row[1])
        
    #print(date)
    date.pop(0)
    net.pop(0)
    
    net = list(map(int, net))

    for number in net:
        total += number
          
    for i in range(length - 1):
            delta = i - (i + 1)
            change.append(abs(delta))

    print (delta)
    #print(date)
    #print(net)
    print(f"Total Months: {len(date)}")
    print(f"Net Profit and Loss: {total}")
    