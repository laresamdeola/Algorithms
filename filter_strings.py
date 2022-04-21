"""
In this kata you will create a function that takes a list of non-negative integers
and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""
import unittest


def filter_list(l):
    filtered = [i for i in l if type(i) == int]
    print(filtered)


class TestFilterStrings(unittest.Testcase):
    def test_one(self):
        self.assertEqual(filter_list([1,2,'a','b']), [1,2])
    
    def test_two(self):
        self.assertEqual(filter_list([1,2,'aasf','1','123',123]), [1,2,123])
      
    def test_three(self):
      self.assertEqual(filter_list([1,4,5,'a','b']), [1,4,5])