"""
The goal of this exercise is to convert a string to a new string where each character in the new string
is "(" if that character appears only once in the original string, or ")" if that character appears more
than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("

"""


def duplicate_encode(word):
    encode, duplicate, full_word = "", "", ""
    words = []
    word_lower = word.lower()
    if word_lower.isascii() is True:
        for i in word_lower:
            if word_lower.count(i) == 1:
                encode = word_lower.replace(f"{word_lower}", "(")
            elif word_lower.count(i) > 1:
                encode = word_lower.replace(f"{word_lower}", ")")
            words.append(encode)
            full_word = duplicate.join(words)
        print(full_word)
