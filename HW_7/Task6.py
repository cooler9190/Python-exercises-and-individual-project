# 6. Parentheses Validator
# Description: Write a function
# that checks if a string
# containing just the characters
# '(', ')', '{', '}', '[', and ']' is valid.
# The brackets must close in the correct order.
# Example
# Input: "{{}[]}"
# Example
# Output: True

def validate_parentheses(string):
    if string == "":
        raise ValueError

    opening_brackets = []

    for char in string:
        if char in ['(', '{', '[']:
            opening_brackets.append(char)
        elif (opening_brackets and
              ((opening_brackets[-1] == '(' and char == ')') or
                (opening_brackets[-1] == '{' and char == '}') or
                (opening_brackets[-1] == '[' and char == ']'))):
            opening_brackets.pop()
        else:
            continue

    return not opening_brackets


if __name__ == '__main__':
    expression = input("Enter an expression: ")
    try:
        print(validate_parentheses(expression))
    except ValueError:
        print("Expression is empty")
