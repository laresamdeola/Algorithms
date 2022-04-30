"""
If you can't sleep, just count sheep!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.


"""
"""
def count_sheep(n):
    sheep = []
    for i in range(1, n+1):
        sheep.append(f"{i} sheep...")
    return ''.join(sheep)
"""


Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""


def solution(s):
    break_camel = [i for i in s]
    for index, value in enumerate(break_camel):
        if value.isupper():
            break_camel[index] = f" {value}"
    return (''.join(break_camel))