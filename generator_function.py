def week():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        yield day


days = week()
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
# print(next(days))

print()

for day in week():
    print(day)
