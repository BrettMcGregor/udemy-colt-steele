import pdb

first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)

# pdb import and use commonly on one line of code. e.g.
# this is because it is usually there temporarily while
# the developer debugs the program


def add_numbers(*args):
    import pdb; pdb.set_trace()
    return sum(args)


# Common pdb commands:
# l (list)
# n (step to next line)
# p (print)
# c (continue - runs remainder of program and ends debugging)
