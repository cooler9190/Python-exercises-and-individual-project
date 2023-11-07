# 3.Nested Function for Calculating Factorial
# Write a function that contains a nested function to calculate the factorial of a number.
# Input: 5
# Output: 120

def factorial(number):
    fac = 1
    def calculate(n, num = fac):
        for i in range(1, n + 1):
            num *= i
        return num
    print(calculate(number))

x = int(input("Enter a number: "))

factorial(x)