"""
Write a function that returns a string in which firstname is swapped with last name.

name_shuffler('john McClane'); => "McClane john"
"""

def name_shuffler(str_):
  full_name = str_.split(' ')
  return f"{full_name[1]} {full_name[0]}"
  