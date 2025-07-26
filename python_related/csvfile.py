import csv

with open('employ.csv',mode='r') as file:
    csvfile = csv.reader(file)

    for lines in csvfile:
        print(lines)