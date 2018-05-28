# users = [
#     {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
#     {"username": "katie", "tweets": ["I love my cat"]},
#     {"username": "jeff", "tweets": []},
#     {"username": "bob123", "tweets": []},
#     {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
#     {"username": "guitar_gal", "tweets": []}
# ]
# # extract inactive users using filter:
#
# inactive_users = list(filter(lambda x: not x["tweets"], users))
# print(inactive_users)
#
# # extract usernames of inactive users w/ map and filter:
#
# inactive_users = list(map(lambda u: u["username"], filter(lambda x: not x["tweets"], users)))
# print(inactive_users)
#
# # extract inactive users using list comprehension:
#
# inactive_users = [x for x in users if not x["tweets"]]
# print(inactive_users)
#
# # extract usernames of inactive users w/ list comprehension
#
# inactive_users = [u["username"] for u in users if not u["tweets"]]
# print(inactive_users)


def remove_negatives(nums):
    return list(filter(lambda n: n >= 0,nums))


print(remove_negatives([1, 2, -3, 4, -5, -6, 7, 8]))


























