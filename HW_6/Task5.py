# 5. Задача: Реализирайте клас TemperatureConverter
# със статични методи за конвертиране между градуси Целзий и Фаренхайт.
# Вход: конвертиране на 32 градуса Целзий до Фаренхайт
# Изход: 89.6 градуса Фаренхайт

class TemperatureConverter:
    @staticmethod
    def converter(degree, val):
        if degree == "C":
            return f"{(val - 32) * 5 / 9} degrees Celsius"
        elif degree == "F":
            return f"{(val * 9 / 5) + 32} degrees Fahrenheit"
        else:
            return "Degree not supported"


degrees = float(input("Enter degrees value: "))

temp = input("Convert degrees to C or F: ")

print(TemperatureConverter.converter(temp, degrees))
