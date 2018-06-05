'''
def add(a,b):
    return a+b

oneAddition = once(add)

oneAddition(2,2) # 4
oneAddition(2,2) # None
oneAddition(12,200) # None
'''


def once(func):
    once.counter = 0
    def inner(*args):
        if once.counter > 0:
            return None
        else:
            once.counter += 1
            return func(*args)
    return inner







def add(a,b):
    return a+b

oneAddition = once(add)

print(oneAddition(2,2)) # 4
print(oneAddition(2,2)) # None
print(oneAddition(12,200)) # None