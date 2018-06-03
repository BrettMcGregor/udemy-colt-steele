# searches for a user in users.csv
# returns index of user if found else a message

import csv


def find_user(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = list(csv.reader(file))  # convert reader object to list to use list methods
        if [first_name, last_name] in csv_reader:
            return csv_reader.index([first_name, last_name])
        return "{} {} not found.".format(first_name, last_name)


print(find_user("Brett", "McGregor"))
print(find_user("Colt", "Steele"))
print(find_user("Not", "Here"))
