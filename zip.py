# def interleave(string1, string2):
#     return "".join(x[0] + x[1] for x in zip(string1, string2))
#
#
# print(interleave("Brett","McGregor"))
# print(interleave("aaa","zzz"))


# def triple_and_filter(numbers):
#     return [num * 3 for num in numbers if num % 4 == 0]
#
# print(triple_and_filter([1,2,3,4]))
#

#
# def triple_and_filter(numbers):
#     return list(map(lambda y: y * 3, filter(lambda x: x % 4 == 0, numbers)))
#
#
# print(triple_and_filter([1, 2, 3, 4]))


# def extract_full_name(dicts_list):
#     return ["".join(x["first"] + " " + x["last"]) for x in dicts_list]
#
#
#
# print(extract_full_name([{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]))

