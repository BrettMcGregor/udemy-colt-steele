'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''


def sum_pairs(new_list, total):
    for i in range(len(new_list) - 1):
        if new_list[i] + new_list[i + 1] == total:
            return new_list[i: i + 2]
        return []


print(sum_pairs([4,2,10,5,1], 6))
print(sum_pairs([11,20,4,2,1,5], 100))
