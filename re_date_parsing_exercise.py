import re


def parse_date(string):
    result = {}
    regex_date = re.compile(r"\b([0123][1-9])[/|.|,]([01]?\d)[/|.|,](\d{4}\b$)")
    match = regex_date.search(string)
    result.update({"d": match.group(1)})
    result.update({"m": match.group(2)})
    result.update({"y": match.group(3)})
    if match:
        return result
    return None


print(parse_date("01/12/1999"))
print(parse_date("31,12,1999"))
print(parse_date("01.12.1999"))
