import re


def parse_bytes(string):
    regex_bytes = re.compile(r"\b[0,1]{8}\b")
    return regex_bytes.findall(string)

print(parse_bytes("11010101 101 323"))
print(parse_bytes("my data is: 11010101 11010101"))
print(parse_bytes("my data is"))
