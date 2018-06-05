'''
rAvg = running_average();
rAvg(10) // 10.0;
rAvg(11) // 10.5;
rAvg(12) // 11;

rAvg2 = running_average()
rAvg2(1) // 1
rAvg2(3) // 2
'''


def running_average():
    running_average.total = 0
    running_average.counter = 0

    def nested_function(num):
        running_average.total += num
        running_average.counter += 1
        return running_average.total / running_average.counter

    return nested_function


rAvg = running_average()
print(rAvg(10)) # 10.0
print(rAvg(11)) # 10.5
print(rAvg(12)) # 11



































# def running_average():
#     running_average.accumulator = 0
#     running_average.size = 0
#
#     def inner(number):
#         running_average.accumulator += number
#         running_average.size += 1
#         return running_average.accumulator / running_average.size
#
#     return inner