"""

You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single
integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)

"""
import unittest


def find_outlier(integers):
    even_numbers = []
    odd_numbers = []
    outlier = 0
    if len(integers) >= 3:
        for num in integers:
            if num % 2 > 0 and integers.count(num) == 1:
                odd_numbers.append(num)
            elif num % 2 == 0 and integers.count(num) == 1:
                even_numbers.append(num)
        if len(even_numbers) == 1:
            outlier = even_numbers[0]
        elif len(odd_numbers) == 1:
            outlier = odd_numbers[0]
    return outlier


class TestOutliers(unittest.TestCase):
  def test_odd_numbers(self):
    self.assertEqual(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)

  def test_even_numbers(self):
    self.assertEqual(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)


if __name__ == '__main__':
  unittest.main()