ITEM = ""
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def linear_search(list, target):
    half = len(list) // 2
    first_half = list[:half]
    second_half = list[half:]

    for i in range(0, len(first_half)):
        if first_half[i] == target:
            return i
    for j in range(0, len(second_half)):
        if second_half[j] == target:
            return j
    return None


def verify(index):
    if index is not None:
        print(f"{ITEM} has been found at index: {index}")
    else:
        print(f"{ITEM} has not been found")


# To verify that the linear search is consistent, this time to return the false path
result = linear_search(items, 100)
verify(result)
      
##To verify that the linear search is consistent, this time to return the true path

result = linear_search(items, 2)
verify(result)
