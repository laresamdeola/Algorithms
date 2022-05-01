=begin
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

Examples
makeNegative(1);  # return -1
makeNegative(-5); # return -5
makeNegative(0);  # return 0
Notes
The number can be negative already, in which case no change is required.
Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
=end


def make_negative(num)
  if num > 0
      num = num * -1
  elsif num < 0
      num = num
  elsif num == 0
      num = 0
  end
  return num
end




=begin
Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

For example:

a = 1
b = 4
--> [1, 2, 3, 4]
=end

def between(a, b)
  betweens = Array(a..b)
  return betweens
  
end



=begin
Your function takes two arguments:

current father's age (years)
current age of his son (years)
Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).
=end


def twice_as_old(dad, son)
  twice = son+son
  as_old = dad-twice
  if as_old < 0
    as_old = as_old * -1
  end
  return as_old
end