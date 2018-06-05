'''
find_greater_numbers([1,2,3]) # 3
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''


def find_greater_numbers(l):
    count = 0
    for i in range(len(l)-1, 0, -1):
        # print(l[i::-1])
        for j in l[i-1::-1]:
            # print(l[i], j)
            if l[i] > j:
                count += 1


    print("count = ",count)









find_greater_numbers([1,2,3]) # 3
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0

