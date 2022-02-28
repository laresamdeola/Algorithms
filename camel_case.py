"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"""


def to_camel_case(text):
    name_title = text.title()
    if text != "":
        first_letter = text[0].lower()
        camel_case = name_title.replace(f"{name_title[0]}", f"{first_letter}", 1)
        upper_camel_case = name_title.replace(f"{first_letter}", f"{name_title[0]}", 0)
        dummy_string = ""
        camel = ""
        if text[0].isupper():
            if "_" in upper_camel_case:
                split_string = upper_camel_case.split("_")
                camel = dummy_string.join(split_string)
            elif "-" in upper_camel_case:
                split_string = upper_camel_case.split("-")
                camel = dummy_string.join(split_string)
        elif text[0].islower():
            if "_" in name_title:
                split_string = camel_case.split("_")
                camel = dummy_string.join(split_string)
            elif "-" in name_title:
                split_string = camel_case.split("-")
                camel = dummy_string.join(split_string)
        print(camel)
    else:
        print('')
