"""
#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing
letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will
always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'
"""


def find_missing_letter(chars):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    end = [i for i in range(len(alphabets)) if alphabets[i] == chars[-1]]
    start = [j for j in range(len(alphabets)) if alphabets[j] == chars[0]]
    yard = []
    caps_end = [o for o in range(len(caps)) if caps[o] == chars[-1]]
    caps_start = [p for p in range(len(caps)) if caps[p] == chars[0]]
    missing_letter = []

    if chars[0].islower():
        if chars[-1] in alphabets:
            for k in range(start[0], end[0] + 1):
                yard.append(alphabets[k])
            if yard != chars:
                for l in yard:
                    if l not in chars:
                        missing_letter.append(l)
    elif chars[0].isupper():
        if chars[-1] in caps:
            for m in range(caps_start[0], caps_end[0] + 1):
                yard.append(caps[m])
            if yard != chars:
                for n in yard:
                    if n not in chars:
                        missing_letter.append(n)
    return missing_letter[0]
