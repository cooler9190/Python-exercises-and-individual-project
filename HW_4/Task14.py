# 14. Nested Functions for String Manipulation
# Write a function containing nested functions to perform various string manipulations like uppercase, lowercase, and
# capitalization.
# Input: "hello", "uppercase"
# Output: "HELLO"


def manipulateStr(string, command):
    if command == "uppercase":
        def uppercase():
            return string.upper()
        print(uppercase())
    elif command == "lowercase":
        def lowercase():
            return string.lower()
        print(lowercase())
    elif command == "capitalization":
        def capitalization():
            return string.capitalize()
        print(capitalization())
    else:
        print("Incorrect input!")

input = [value for value in input("Enter a string and a command: ").split(', ')]


manipulateStr(input[0], input[1])
