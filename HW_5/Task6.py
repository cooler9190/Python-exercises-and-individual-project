# 6. Implement a Custom Range Generator
# Description: Create a generator function that mimics the built-in range function.
# It should accept start, stop, and step arguments.
# Example Input: custom_range(2, 10, 2)
# Example Output: 2, 4, 6, 8

def custom_range(start, stop, step=1):
    if step == 0:
        raise Exception(ValueError)
    while start != stop:
        yield start
        start += step


print(*list(custom_range(2, 10)), sep=", ")

print(*list(custom_range(2, 10, 2)), sep=", ")

