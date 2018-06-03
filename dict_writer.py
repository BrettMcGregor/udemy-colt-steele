from csv import writer, DictWriter

with open("cats.csv", "w", newline="") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({"Name": "Garfield",
                         "Breed": "Orange Tabby",
                         "Age": 10})