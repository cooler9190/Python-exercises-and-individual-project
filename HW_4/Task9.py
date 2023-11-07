# 9. Generator to Yield Powers of Two
# Write a generator function that yields the powers of two up to n
# Input: 4
# Output: 1, 2, 4, 8

def powersOfTwoGenerator(n):
    val = 1
    for i in range(n):
        yield val
        val *= 2

n = input("Enter a number: ")

print(*list(powersOfTwoGenerator(int(n))), sep = ', ')