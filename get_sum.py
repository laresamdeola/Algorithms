"""
Given two integers a and b, which can be positive or negative,
find the sum of all the integers between and including them and return it.
If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
"""
import unittest


def get_sum(a, b):
    ranges = [i for i in range(a, b+1)]
    the_reversed = [j for j in range(b, a+1)]
    total_sums = 0
    if a < b:
        total_sums = sum(ranges)
    elif a > b:
        total_sums = sum(the_reversed)
    else:
        total_sums = a
    return total_sums


class TestSums(unittest.TestCase):
    def test_one(self):
        self.assertEqual(get_sum(1, 0), 1)

    def test_two(self):
        self.assertEqual(get_sum(1, 2), 3)

    def test_three(self):
        self.assertEqual(get_sum(-1, 0), -1)


if __name__ == '__main__':
    unittest.main()
