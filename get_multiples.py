'''
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''


def get_multiples(num=1, count=10):
    x = 0
    while count > 0:
        yield x + num
        x += num
        count -= 1


evens = get_multiples(2, 3)
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))