import csv


def update_users(old_first_name, old_last_name, new_first_name, new_last_name):
    with open("users.csv", "r", newline="") as file:
        csv_reader = list(csv.reader(file))  # convert reader object to list to use list methods
    counter = 0
    for user in csv_reader[1:]:
        if user == [old_first_name, old_last_name]:
            user[0], user[1] = new_first_name, new_last_name
            counter += 1

    with open("users.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        for row in csv_reader:
            csv_writer.writerow(row)

    return "Users updated: {}.".format(counter)


print(update_users("Brett", "McGregor", "Dad", "McGregor"))
