'''
reverse_vowels("Hello!") # "Holle!"
reverse_vowels("Tomatoes") # "Temotaos"
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''


def reverse_vowels(word):
    vowels = "aeiou"
    listing = []
    indexing = []
    for i in range(len(word)):
        if word[i].lower() in vowels:
            listing.append(word[i])
            indexing.append(i)

    output = list(zip(listing, sorted(indexing, reverse=True)))

    for i in range(len(word)):
        if word[i].lower() not in vowels:
            output.append((word[i], i))
    output = sorted(output, key=lambda x: x[1])
    return "".join(["".join(x[0]) for x in output])



reverse_vowels("Hello!") # "Holle!"
reverse_vowels("Tomatoes") # "Temotaos"
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"