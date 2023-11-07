# 1. StringReverser
# Description: Write a function that takes a string as input
# and returns its reverse.
# Example
# Input: "hello"
# Example
# Output: "olleh"

def reverse_string(string):
    if not isinstance(string, str):
        raise TypeError

    return string[::-1]


if __name__ == '__main__':

    word = input("Enter a string: ")

    print(reverse_string(word))


