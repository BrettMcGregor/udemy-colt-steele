'''
EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
];

sum_up_diagonals(list1); # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
];

sum_up_diagonals(list2); # 30

list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
];

sum_up_diagonals(list3); # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
];

sum_up_diagonals(list4); # 68
'''


def sum_up_diagonals(array):
    result = 0
    for i in range(len(array[0])):
        result += array[i][i]
        result += array[-i][-i-1]
    print(result)


list4 = [
    [ 1, 2, 3, 4 ],
    [ 5, 6, 7, 8 ],
    [ 9, 10, 11, 12 ],
    [ 13, 14, 15, 16 ]
]

sum_up_diagonals(list4) # 68

list2 = [
    [ 4, 1, 0 ],
    [ -1, -1, 0],
    [ 0, 0, 9]
]

sum_up_diagonals(list2) # 11

































