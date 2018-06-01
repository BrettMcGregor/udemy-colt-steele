# def week():
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     for day in days:
#         yield day
#
#
# days = week()
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# # print(next(days))
#
# print()
#
# for day in week():
#     print(day)



def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        if answer == "yes":
            answer = "no"
        else:
            answer = "yes"
        # answer = "no" if answer == "yes" else "yes"




gen = yes_or_no()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
