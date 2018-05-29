# import keyword
#
#
# def contains_keyword(*args):
#     return any(keyword.iskeyword(arg) for arg in args)
#     # for arg in args:
#     #     return keyword.iskeyword(arg)
#
#
# print(contains_keyword("for", "if", "Brett"))


# from keyword import iskeyword


# def contains_keyword(*args):
#     for item in args:
#         if iskeyword(item):
#             return True
#     return False
#
#
# print(contains_keyword("for", "if", "Brett"))


# from keyword import iskeyword
# def contains_keyword(*args):
#     for item in args:
#         return iskeyword(item)
#
# print(contains_keyword("for", "if", "Brett"))

from keyword import iskeyword

def contains_keyword(*args):
    return type(any([arg for arg in args if iskeyword(arg)]))


print(contains_keyword("for", "if", "Brett"))