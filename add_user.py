import csv


def add_user(first, last):
    with open("users.csv", "a", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([first, last])


add_user("Devon", "McGregor")
add_user("Ryan", "McGregor")
add_user("Kitty", "McGregor")

