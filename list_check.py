'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''


def list_check(new_list):
    return all([isinstance(x, list) for x in new_list])


print(list_check([1, True, [],[1],[2,3]]))
print(list_check([[],[1],[2,3]]))