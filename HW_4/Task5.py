# 5. Palindrome Checker using Lambda
# Write a lambda function that checks weather a given string is a palindrome
# Input: "madam"
# Output: True

def isPalindrome(word):
    palindrome = lambda newSentance: word[::-1]

    if word == palindrome(word):
        return True
    else:
        return False

string = input("Enter a word: ")

print(isPalindrome(string))