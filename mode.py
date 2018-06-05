'''
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''

# define mode below:


def mode(l):
    return sorted(list(zip(set(l),[l.count(num) for num in set(l)])), key=lambda x: x[1])[-1][0]


mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4