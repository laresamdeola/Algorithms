"""
Write a function named first_non_repeating_letter that takes a string input, and returns the first
character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the
letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character,
but the function should return the correct case for the initial letter. For example,
the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or
None for example
"""

def first_non_repeating_letter(string):
    original = [i for i in string]
    upper = string.upper()
    unique = [value for index, value in enumerate(upper) if upper.count(value) == 1]
    one = []
    for j in range(0, len(unique)):
        if unique[j] in original:
            one.append(unique[j])
        elif unique[j].lower() in original:
            one.append(unique[j].lower())
    if len(one) >= 1:
        return one[0]
    elif len(one) < 1:
        return ''