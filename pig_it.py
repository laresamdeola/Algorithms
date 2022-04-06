"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

import unittest


def pig_it(text):
    # split the string into separate words
    split_text = text.split(' ')
    # empty list, to be filled with the pigged strings
    pig = []
    # loop through the split strings and perform the algorithm
    for i in range(0, len(split_text)):
        if split_text[i].isalpha():
            pigged = split_text[i][1:] + ''.join(reversed(split_text[i][0])) + 'ay'
        else:
            pigged = split_text[i][1:] + ''.join(reversed(split_text[i][0]))
        pig.append(pigged)
    return ' '.join(pig)


text_1 = 'Pig latin is cool'
text_2 = 'Hello world !'
pig_it(text_1)


class TestPiggedStrings(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(pig_it(text_1), 'igPay atinlay siay oolcay')

    def test_punctuations(self):
        self.assertEqual(pig_it(text_2), 'elloHay orldway !')


if __name__ == '__main__':
    unittest.main()