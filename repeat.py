'''
repeat('*', 3) # '***'
repeat('abc', 2) # 'abcabc'
repeat('abc', 0) # ''
'''


def repeat(string, number):
    return string * number

print(repeat('*', 3)) # '***'
print(repeat('abc', 2)) # 'abcabc'
print(repeat('abc', 0)) # ''