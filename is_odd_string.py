'''
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''


def is_odd_string(the_string):
    alphabet = "_abcdefghijklmnopqrstuvwxyz"
    result = 0
    for char in the_string:
        result += alphabet.index(char)
    return result % 2 != 0














is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
print(is_odd_string('veryfunny')) # False