# 10. Lambda Function to filter out Even Numbers
# Write a lambda function that filters even numbers from a given list
# Input: [1, 2, 3, 4, 5]
# Output: [2, 4]

numList = [int(numbers) for numbers in input("Enter  numbers: ").split(', ')]

#evenNumList = list(filter(lambda x: x % 2 == 0, numList))

even = lambda x: x % 2 == 0

evenNumList = []

for val in numList:
    if even(val):
        evenNumList.append(val)

print(evenNumList)