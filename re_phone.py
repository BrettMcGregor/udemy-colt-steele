import re


def extract_phone(string):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    match = phone_regex.search(string)
    if match:
        return match.group()


def extract_all_phone_numbers(string):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    return phone_regex.findall(string)


def is_valid_phone(string):
    phone_regex = re.compile(r"^\d{3} \d{3}-\d{4}^")
    match = phone_regex.search(string)
    if match:
        return True
    return False


print(extract_phone("my number is 432 567-4432"))
print(extract_phone("my number is 4332 567-4432"))


print(extract_all_phone_numbers("my number is 432 567-4432 or call me at 443 882-1133"))


print(is_valid_phone("432 567-4432"))
