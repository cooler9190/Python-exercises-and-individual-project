# 4. Anagram Checker
# Description: Write a function that
# checks if two given words are anagrams
# of each other.
# Example
# Input: "listen", "silent"
# Example
# Output: True

def are_anagrams(string1, string2):

    string1 = string1.upper()
    string2 = string2.upper()

    if string1 == '' or string2 == '':
        raise ValueError
    elif len(string1) == len(string2) and sorted(string1) == sorted(string2):
        return True
    else:
        return False


if __name__ == '__main__':
    a = input("Enter first word: ")
    b = input("Enter second word: ")

    try:
        print(are_anagrams(a, b))
    except ValueError:
        print("Empty strings cannot be anagrams!")

