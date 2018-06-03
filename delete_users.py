import csv


def delete_users(first_name, last_name):
    with open("users.csv", "r") as file_in:
        csv_reader = list(csv.reader(file_in))  # cast to list to access list methods

        counter = 0

        for user in csv_reader:
            if user == [first_name, last_name]:
                csv_reader.remove(user)
                counter += 1

        with open("users.csv", "w", newline="") as file_out:
            csv_writer = csv.writer(file_out)
            for user in csv_reader:
                csv_writer.writerow(user)

    return "Users deleted: {}.".format(counter)


print(delete_users("Grace", "Hopper"))
