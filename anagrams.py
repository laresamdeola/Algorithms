"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an
array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""


def anagrams(word, words):
    sorts = []
    anagrams = []
    sorted_word = ''.join(sorted(word))
    for index, value in enumerate(words):
        words_sorted = sorted(value)
        sorts.append(''.join(words_sorted))
        for i in range(len(sorts)):
            if sorts[i] == sorted_word and i == index:
                anagrams.append(value)
    return anagrams