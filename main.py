ITEM = ""
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def linear_search(list,target):
  for i in range(0, len(list)):
    if list[i] == target:
      return i
  return None


def verify(index):
  if index is not None:
    print(f"{ITEM} has been found at index: {index}")
  else:
    print(f"{ITEM} has not been found")


#To verify that the linear search is consistent, this time to return the false path
    
result = linear_search(items, 100)
verify(result)

##To verify that the linear search is consistent, this time to return the true path

result = linear_search(items, 10)
verify(result)