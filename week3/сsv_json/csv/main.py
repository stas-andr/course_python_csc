import csv
from datetime import datetime

str_with_2015 = []
with open("Crimes.csv", 'r') as input:
    reader = csv.DictReader(input)
    for row in reader:
        date = datetime.strptime(row['Date'], '%m/%d/%Y %H:%M:%S %p')
        year = date.year
        if year == 2015:
            str_with_2015.append(row)

max(count(row['Primary type']))

