def is_all_strings(iterable):
    return all([isinstance(x, str) for x in iterable])


print(is_all_strings(["a", "b", "c"]))
