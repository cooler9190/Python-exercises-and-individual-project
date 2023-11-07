# 2. Prime Checker
# Description: Write a function that checks
# if a given number is prime or not.
# Example
# Input: 7
# Example
# Output: True

import math


def is_prime(number):
    if type(number) == str:
        raise TypeError("Invalid type!")

    if number < 0 or type(number) == float:
        return False

    fac = math.factorial(number - 1)

    if number - 1 == fac % number:
        return True
    else:
        return False


if __name__ == '__main__':
    numb = input("Enter a number: ")

    print(is_prime(int(numb)))
