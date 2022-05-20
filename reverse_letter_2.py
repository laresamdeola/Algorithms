"""
Task
Given a string str, reverse it omitting all non-alphabetic characters.

Example
For str = "krishan", the output should be "nahsirk".

For str = "ultr53o?n", the output should be "nortlu".

Input/Output
[input] string str
A string consists of lowercase latin letters, digits and symbols.

[output] a string
"""


def reverse_letter(string):
  string = string[::-1]
  pure = [string[j] for j in range(0, len(string)) if string[j].isalpha()]
  return (''.join(pure))

