# 16. Function to Compute Power of Variable Arguments
# Write a function that takes a variable number of arguments and returns the result of raising the first argument to the
# power of the rest in order.
# Input: 2, 3, 2
# Output: 64 (i.e., 2^3^2 = 64)

def power(*args):
    result = args[0]

    for exponent in args[1:]:
        result = result ** exponent
    return result

inputData = [int(num) for num in input("Enter a base and powers to raise the base to: ").split(', ')]

print(power(*inputData))
