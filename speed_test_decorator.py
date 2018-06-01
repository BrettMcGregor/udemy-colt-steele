from time import time


def speed_test(fn):  # decorator function which records time to execute the function
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}...")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(10000000))    # compare runtime when using generator expression


@speed_test
def sum_nums_list():
    return sum([x for x in range(10000000)])    # compare runtime when using list comprehension


sum_nums_gen()
print()
sum_nums_list()
