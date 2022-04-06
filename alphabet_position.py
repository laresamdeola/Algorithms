"""
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
"""


def alphabet_position(text):
    text = text.lower()
    text_dict = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j', '11': 'k','12': 'l','13': 'm','14': 'n','15': 'o',
    '16': 'p','17': 'q','18': 'r','19': 's','20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'}
  
    position = []
  
    for i in range(len(text)):
        for keys, values in text_dict.items():
            if text[i] == values:
                position.append(keys)
            else:
                continue
    print(' '.join(position))


alphabet_position("The sunset sets at twelve o' clock.")