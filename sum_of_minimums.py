def sum_of_minimums(numbers):
  mins = []
  for i in numbers:
    mins.append(min(i))
  print(sum(mins))