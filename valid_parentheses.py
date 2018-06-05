'''
valid_parentheses("()") # True
valid_parentheses(")(()))") # False
valid_parentheses("(") # False
valid_parentheses("(())((()())())") # True
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''
#
#
# def valid_parentheses(paren_string):
#     result = 0
#     for p in list(paren_string):
#         if result < 0:
#             return False
#         elif p == "(":
#             result += 1
#         elif p == ")":
#             result -= 1
#     return result == 0
#
#
# print(valid_parentheses("()"))  # True
# print(valid_parentheses(")(()))"))  # False
# print(valid_parentheses("("))  # False
# print(valid_parentheses("(())((()())())"))  # True
# print(valid_parentheses('))(('))  # False
# print(valid_parentheses('())('))  # False
# print(valid_parentheses('()()()()())()('))  # False


def valid_parentheses(string):

    check = string

    while "()" in check:
        check = "".join(check.split("()"))

    return len(check) == 0

print(valid_parentheses("()"))  # True
print(valid_parentheses(")(()))"))  # False
print(valid_parentheses("("))  # False
print(valid_parentheses("(())((()())())"))  # True
print(valid_parentheses('))(('))  # False
print(valid_parentheses('())('))  # False
print(valid_parentheses('()()()()())(s)('))  # False