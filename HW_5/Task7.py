# 7.Nested Generator for Flattening Lists
# Description: Create a generator that takes a nested list and flattens it.
# Example Input: [[1, 2], [3, 4]]
# Example Output: 1, 2, 3, 4

inputLists = input("Enter lists: ")

listOfLists = []

for val in inputLists.split('], ['):
    val = val.replace('[', '').replace(']', '')
    listOfLists.append(list(val.split(', ')))


def flatten_list(list_of_lists):
    for subList in list_of_lists:
        for element in subList:
            yield element


print(*list(flatten_list(listOfLists)), sep=', ')
