'''
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
'''

def three_odd_numbers(num_list):
    return any(sum(num_list[i: i + 3]) % 2 != 0 for i in range(len(num_list)-2))



    # for i in range(len(num_list)-2):
    #     print(num_list[i: i + 3])
    #     print(sum(num_list[i: i + 3]) % 2 != 0)





print(three_odd_numbers([1,2,3,4,5])) # True
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0])) # True
print(three_odd_numbers([5,2,1])) # False
print(three_odd_numbers([1,2,3,3,2])) # False
