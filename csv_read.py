import csv

with open("fighters.csv") as file:
    csv_reader = csv.reader(file)   # Open using csv.reader
    fighters = [[s.upper() for s in row] for row in csv_reader]
    for row in csv_reader:
        print(row)  # Each row is a list...
    print(fighters)

print()


with open("fighters.csv") as file:
    csv_dict = csv.DictReader(file)  # Open using csv.DictReader
    for item in csv_dict:
        print(item["Name"])  # Each row is an ordered dict object


with open("screaming_fighters.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    for row in fighters:
        csv_writer.writerow(row)

