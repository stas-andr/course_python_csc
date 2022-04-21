import csv
from datetime import datetime

primary_types_in_2015 = []
with open("Crimes.csv", 'r') as input:
    reader = csv.DictReader(input)
    for row in reader:
        date = datetime.strptime(row['Date'], '%m/%d/%Y %H:%M:%S %p')
        year = date.year
        if year == 2015:
            primary_types_in_2015.append(row['Primary Type'])

print(max(primary_types_in_2015, key=primary_types_in_2015.count))

