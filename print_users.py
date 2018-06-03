import csv


def print_users():
    with open("users.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for user in csv_reader:
            print(user[0], user[1])

#
# def print_users():
#     with open("users.csv") as csvfile:
#         csv_reader = csv.DictReader(csvfile)
#         for row in csv_reader:
#             print("{} {}".format(row['First Name'], row['Last Name']))


print_users()
