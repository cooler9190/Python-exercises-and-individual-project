# 2. Generator to Yield Fibonacci Sequence
# Write a generator function that yields the Fibonacci sequence up to n numbers.
# Input: 5
# Output: 0, 1, 1, 2, 3


def fibSequence(n):
    x, y = 0, 1
    for _ in range(n):
        yield x
        x, y = y, x + y


num = input("Enter a number: ")
print(*list(fibSequence(int(num))), sep=', ')

