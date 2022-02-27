"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example,
the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least
once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers
and punctuation.
"""


def is_pangram(s):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    pangram = None
    if s.isalpha() is True:
        for i in range(len(alphabets)):
            if s in alphabets[i]:
                pangram = True
            else:
                pangram = False
    elif s.isalpha() is False:
        for i in range(len(alphabets)):
            if alphabets[i] in s:
                pangram = True
            else:
                pangram = False
    print(pangram)


