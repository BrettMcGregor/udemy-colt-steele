'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''


def titleize(long_string):
    caps = []
    for word in long_string.split(" "):
        caps.append(word.replace(word[0], word[0].upper()))
    return " ".join(caps)

print(titleize('oNLy cAPITALIZe fIRSt'))