# 11. Nested Function to calculate Exponential
# Write a function containing a nested function that calculates the exponential of a number using a given base
# Input: 2, 3
# Output 8

def power(base, exponent):
    def calculate():
        val = 1
        for i in range(exponent):
            val *= base
        return val
    print(calculate())

input = [int(numbers) for numbers in input("Enter the base and the exponent: ").split(", ")]

power(input[0], input[1])