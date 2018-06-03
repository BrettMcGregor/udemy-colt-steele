import csv

with open("csv_write.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Blue", 4])
    csv_writer.writerow(["Kitty", 1])

