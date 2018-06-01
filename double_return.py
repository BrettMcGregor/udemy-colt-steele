'''
@double_return
def add(x, y):
    return x + y

add(1, 2) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]
'''


def double_return(fn):
    def wrapper(*args, **kwargs):
        return [fn(*args, **kwargs), fn(*args, **kwargs)]
    return wrapper


@double_return
def add(x, y):
    return x + y

@double_return
def greet(name):
    return "Hi, I'm " + name


print(greet("Colt")) # ["Hi, I'm Colt", "Hi, I'm Colt"]


print(add(1,2))
