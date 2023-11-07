# 6. Generator for Prime Numbers
# Write a generator function that yields prime numbers up to n
# Input: 10
# Output: 2, 3, 5, 7

import math
def generatePrimeNumbers(n):
    for i in range(2, n + 1):
        fac = math.factorial(i - 1)
        if i - 1 == fac % i:
            yield i


num = input("Enter a number: ")
print(*list(generatePrimeNumbers(int(num))), sep = ', ')
