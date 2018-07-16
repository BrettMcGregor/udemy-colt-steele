import re


def is_valid_time(string):
    time_regex = re.compile(r"^\d\d?:\d{2}$")
    match = time_regex.search(string)
    if match:
        return True
    return False


print(is_valid_time("10:45"))
print(is_valid_time("10.45"))
print(is_valid_time("1999"))
print(is_valid_time("130:45"))
print(is_valid_time("1:45"))
