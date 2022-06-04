"""
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""

def solution(string, ending):
  if ending == string[-(len(ending)):] or ending == '':
    return True
  else:
    return False


"""
Tests

test.assert_equals(solution('abcde', 'cde'), True)
test.assert_equals(solution('abcde', 'abc'), False)
test.assert_equals(solution('abcde', ''), True)
"""