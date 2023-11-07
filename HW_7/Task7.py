# 7. Number to English Words
# Description: Convert a non-negative integer
# to its English words representation.
# Example
# Input: 12345
# Example
# Output: "Twelve Thousand Three Hundred Forty Five"

def number_to_words(number):
    if type(number) == str or type(number) == float:
        raise TypeError("Invalid type!")

    ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    hundred = ' Hundred '

    thousand = ' Thousand '

    million = ' Million '

    billion = ' Billion '

    minus = 'Minus '

    if number < 0:
        return minus + number_to_words(number * -1)

    while number >= 0:
        if number < 10:
            return ones[number]
        elif number < 20:
            return teens[number - 10]
        elif number < 100:
            return tens[int(number / 10)] + (" " + number_to_words(number % 10) if (number % 10 != 0) else "")
        elif number < 1000:
            return number_to_words(int(number / 100)) + hundred + (number_to_words(number % 100) if (number % 100 != 0) else "")
        elif number < 1000000:
            return number_to_words(int(number / 1000)) + thousand + (number_to_words(number % 1000) if (number % 1000 != 0) else "")
        elif number < 1000000000:
            return number_to_words(int(number / 1000000)) + million + (number_to_words(number % 1000000) if (number % 1000000 != 0) else "")
        elif number < 1000000000000:
            return number_to_words(int(number / 1000000000)) + billion + (number_to_words(number % 1000000000) if (number % 1000000000 != 0) else "")
        return 'The limit is just below One Trillion(negative and positive)'


if __name__ == '__main__':
    num = input("Please enter an integer number: ")
    print(number_to_words(int(num)))
