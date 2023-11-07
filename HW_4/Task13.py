# 13. Lambda Function to Apply Function to List
# Write a lambda function that takes another function and a list and applies the function to every element of the list.
# Input: lambda x: x*2, [1, 2, 3]
# Output: [2, 4, 6]

lambdaFunc = input("Enter lambda expression: ")

numList = [int(num) for num in input("Enter the list of numbers: ").split(', ')]

f = lambda x: eval(lambdaFunc)

for i in range(len(numList)):
    numList[i] = f(numList[i])

print(numList)
