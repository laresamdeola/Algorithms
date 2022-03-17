"""
Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation.
Lowercase characters can be numbers. If the method gets a number as input, it should return a string.

Examples
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"
"""


def to_underscore(string):
    string = str(string)
    string = [i for i in string]
    for j in range(1, len(string)):
        if string[j].isupper():
            string[j] = f"_{string[j]}"
            if j:
                string.append(string[j])
                string.pop()
    return (''.join(string).lower())



