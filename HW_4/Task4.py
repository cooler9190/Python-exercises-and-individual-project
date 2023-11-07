# 4. Lambda function inside a function
# Write a function that takes a number n and return a lambda function that multiplies its input by n
# Input: 3
# Output: A function that multiplies its input by 3

def multNumber(n):
    return lambda x: n * n

number = int(input("Enter a number: "))

newNumber = multNumber(number)

print(newNumber(number))