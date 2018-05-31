
def is_palindrome(word):
    return "".join(word.split(" ")).lower() == "".join(word.split(" ")).lower()[::-1]


print(is_palindrome('amanaplana canalpanama')) # True)

word = 'aManaplana canalpanama'
print(is_palindrome('testing')) # False)
print(is_palindrome('tacocat')) # True)
print(is_palindrome('hannah')) # True
print(is_palindrome('Robe rt')) # False