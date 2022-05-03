
"""
In this Kata we are passing a number (n) into a function.

Your code will determine if the number passed is even (or not).

The function needs to return either a true or false.

Numbers may be positive or negative, integers or floats.

Floats with decimal part non equal to zero are considered UNeven for this kata.

def is_even(n): 
    if n % 2 == 0:
        return True
    else:
        return False
"""

"""


Issue
Looks like some hoodlum plumber and his brother has been running around and damaging your stages again.

The pipes connecting your level's stages together need to be fixed before you receive any more complaints.

Pipes list is correct when each pipe after the first index is greater (+1) than the previous one, and that there is no duplicates.

Task
Given the a list of numbers, return a fixed list so that the values increment by 1 for each index from the minimum value up to the maximum value (both included).

Example
Input: 1,3,5,6,7,8 Output: 1,2,3,4,5,6,7,8

def pipe_fix(nums):
    return [i for i in range(nums[0], (nums[-1] + 1))]
"""

"""
All Star Code Challenge #18

Create a function that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

("Hello", "o")  ==>  1
("Hello", "l")  ==>  2
("", "z")       ==>  0
Notes:

The first argument can be an empty string
The second string argument will always be of length 1


def str_count(strng, letter):
    occurs = [i for i in range(0, len(strng)) if strng[i] == letter]
    if len(occurs) < 1:
        return 0
    else:
        return len(occurs)

"""
"""
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.

def sum_mix(arr):
    return sum([int(arr[i]) for i in range(0, len(arr))])
"""

"""
Create a combat function that takes the player's current health and the amount of damage recieved, and returns the player's new health. Health can't be less than 0.

def sum_mix(arr):
    return sum([int(arr[i]) for i in range(0, len(arr))])
"""

"""
Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

def problem(a):
    value = "Error"
    if type(a) == int or type(a) == float:
        value = (a*50)+6
    return value

In this kata you will create a function that takes in a list and returns a list with the reverse order.

Examples (Input -> Output)
* [1, 2, 3, 4]  -> [4, 3, 2, 1]
* [9, 2, 0, 7]  -> [7, 0, 2, 9]

def reverse_list(l):
    l.reverse()
    return l
"""