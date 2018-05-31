# This code mimics the behaviour of the for loop
# It does this by using the built-in functions iter() and next(),
# which is what the implementation of the for loop does
# behind the scenes!

iterable = "Brett"

iterator = iter(iterable)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
