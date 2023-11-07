# 8. Lambda Function to sort a List Tuples
# Write a lambda function that takes a list of tuples and sorts them by second element
# Input: [(1,2), (3,1), (5,0)]
# Output: [(5,0), (3,1), (1,2)]

input = input("Enter tuples: ")

tupleList = []

for tup in input.split('), ('):
    tup = tup.replace('(', '').replace(')', '')
    tupleList.append(tuple(tup.split(', ')))

tupleList.sort(key = lambda x: x[1])

print(tupleList)
