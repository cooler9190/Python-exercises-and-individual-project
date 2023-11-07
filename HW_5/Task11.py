# 11.Writing a Password Strength Checker Function
# Description: Write a function to check the strength of a password
# based on criteria like length, use of special characters, etc.
# Example Input: “P@ssw0rd123”
# Example Output: “Strong”

from enum import Enum


class Strength(Enum):
    Weak = 0
    Good = 1
    Strong = 2
    Very_strong = 3


def password_strength(password):
    strength = 0

    if len(password) < 1 or len(password) > 12:
        print("Password cannot be 0 or longer than 12!")
        exit()

    if len(password) >= 5:
        strength += 1

    special_char_count = 0
    for char in password:
        if not (char.isalpha() or char.isdigit()):
            special_char_count += 1

    if special_char_count <= 3:
        strength += 1
    elif special_char_count > 3:
        strength += 2

    print(Strength(strength).name)


newPassword = input("Enter your password: ")

password_strength(newPassword)
