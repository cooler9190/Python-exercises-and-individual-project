# 12. Generator for Multiplication Table
# Write a generator function that yields the multiplication table for a given number up to n.
# Input: 3, 5
# Output: 3, 6, 9, 12, 15

def multiplicationGenerator(base, n):
    for i in range(1, n + 1):
        i *= base
        yield i

input = [int(num) for num in input("Enter the base number and n-th number fo multiplication: ").split(", ")]

print(*list(multiplicationGenerator(input[0], input[1])), sep = ', ')
