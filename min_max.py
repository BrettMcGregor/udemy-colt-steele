# def extremes(iterable):
#     return min(iterable), max(iterable)
#
#
# print(extremes([1,2,3,5,4,5]))
# print(extremes("alcatrza"))
#
#
# def max_magnitude(num_list):
#     return max(abs(n) for n in num_list)
#
#
# print(max_magnitude([1,2,3,54,4,5]))
#
#
# def sum_even_values(args):
#     return sum(x for x in args if x % 2 == 0)
#
#
# print(sum_even_values([1,2,3,4,5,6,88]))
#



def sum_floats(*args):
    return sum(num for num in args if isinstance(num, float))

print(sum_floats(1.5, 2.4, 'awesome', [], 1)) # 3.9)
print(sum_floats(1,2,3,4,5)) # 0)
