# 15. Generator for Geometric Progression
# Write a generator function that yields a geometric progression with a given start, ratio, and length.
# Input: 2, 3, 4
# Output: 2, 6, 18, 54

def geometricProg(start, ratio, length):
    for i in range(1, length + 1):
        yield start
        start *= ratio

inputData = [int(num) for num in input("Enter the start, ratio and length of the geometric progression: ").split(', ')]

print(*list(geometricProg(inputData[0], inputData[1], inputData[2])), sep=', ')
