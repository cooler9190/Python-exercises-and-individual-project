# 3. Date Validator
# Description: Write a function that validates
# a date string in the format "DD/MM/YYYY".
# Example
# Input: "29/02/2020"
# Example
# Output: True(2020 was a leap year)

from datetime import date


def date_validator(date_str):
    if date_str[2] != '/' or date_str[5] != '/':
        #raise ValueError("Unrecognised format!")
        return False

    try:
        date(int(date_str[6:]), int(date_str[3:5]), int(date_str[:2]))
    except ValueError:
        return False

    return True


if __name__ == '__main__':
    new_date = input("Enter a date in format 'DD/MM/YYYY': ")

    print(date_validator(new_date))
