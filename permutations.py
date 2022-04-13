"""
In this kata you have to create all permutations of a non empty input string and remove duplicates, if present.
This means, you have to shuffle all letters from the input in all possible orders.

Examples:

* With input 'a'
* Your function should return: ['a']
* With input 'ab'
* Your function should return ['ab', 'ba']
* With input 'aabb'
* Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.
"""

import unittest
from itertools import permutations as permutation


def permutations(string):
    perm = permutation(string)
    perm = sorted(set(perm))
    perm = [''.join(i) for i in perm]
    return perm


class TestPermutations(unittest.TestCase):
    def test_one_character(self):
        self.assertEqual(permutations('a'), ['a'])

    def test_two_characters(self):
        self.assertEqual(permutations('ab'), ['ab', 'ba'])

    def test_four_characters(self):
        self.assertEqual(permutations('aabb'), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])


if __name__ == '__main__':
    unittest.main()