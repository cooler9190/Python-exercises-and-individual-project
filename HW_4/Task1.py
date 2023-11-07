# 1. Simple Lambda Function
# Write a lambda function that takes two numbers and returns their sum.
# Input: 5, 3
# Output: 8

sum = lambda a, b: a + b

numbers = [int(numbers) for numbers in input("Enter two numbers: ").split(', ')]

print(sum(numbers[0], numbers[1]))