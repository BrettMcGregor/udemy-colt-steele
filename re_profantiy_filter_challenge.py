import re


def censor(string):
    re_profanity = re.compile(r"[F|f]rack[a-z]*\b")
    # match = re_profanity.findall(string)
    return re_profanity.sub("CENSORED", string)
    # return match

print(censor("Frack you"))
print(censor("I hope you fracking die"))
print(censor("you fracking Frack"))
