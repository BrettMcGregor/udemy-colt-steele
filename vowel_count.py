'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''


def vowel_count(new_string):
    vowel_dict = {}
    vowels = 'aeiou'
    for letter in new_string:
        if letter.lower() in vowels:
            vowel_dict.update({letter.lower(): new_string.lower().count(letter.lower())})
    return vowel_dict


print(vowel_count('awesome')) # {'a': 1, 'e': 2, 'o': 1}
print(vowel_count('Elie')) # {'e': 2, 'i': 1}
