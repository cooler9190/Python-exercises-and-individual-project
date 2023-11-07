# 7. Nested Functions of Arithmetic Operators
# Write a function, containing nested functions for addition, subtraction, multiplication and division.
# The outer function should take two numbers and an operator as input and return the result.
# Input: 10, 5, "add"
# Output: 15

def calculate(x, y, operator):
    if operator == "add":
        def addition():
            return x + y
        print(addition())
    elif operator == "subtract":
        def subtraction():
            return x - y
        print(subtraction())
    elif operator == "multiply":
        def multiplication():
            return x * y
        print(multiplication())
    elif operator == "divide":
        def division():
            if y != 0:
                return x / y
            else:
                return "Cannot divide by zero!"
        print(division())
    else:
        print("Incorrect input!")

input = [value for value in input("Enter two numbers and an operator: ").split(', ')]


calculate(float(input[0]), float(input[1]), input[2])
