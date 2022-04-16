"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
"""

import unittest


def square_sum(numbers):
  numbers=[i**2 for i in numbers]
  return sum(numbers)


class TestSquareSum(unittest.TestCase):
  def test_squares_one(self):
    self.assertEqual(square_sum([1, 2, 2]), 9)

  def test_larger_sums(self):
    self.assertEqual(square_sum([10, 100, 1000, 200, 587]), 1394669)


if __name__ == '__main__':
  unittest.main()