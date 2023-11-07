# 17. Function to Sort Variable Number of Lists
# Write a function that takes a variable number of lists and returns a single list containing all the elements, sorted.
# Input: [3, 1], [5, 2], [4, 0]
# Output: [0, 1, 2, 3, 4, 5]

input = input("Enter lists: ")

listOfLists = []

for val in input.split('], ['):
    val = val.replace('[', '').replace(']', '')
    listOfLists.append(list(val.split(', ')))

def unpackAndSort(list):
    newList = []
    for val in list:
        for num in val:
            newList.append(int(num))
    newList.sort()

    return newList

print(unpackAndSort(listOfLists))
