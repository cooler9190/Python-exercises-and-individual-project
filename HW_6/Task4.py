# 4. Задача: Създайте клас Calculator, който предоставя статични методи за основни аритметични операции.
# Вход: събиране на 5 и 3
# Изход: 8


class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ZeroDivisionError
        return x / y


operation = input("Enter an arithmetic operation: ")

a = float(input("Enter a: "))
b = float(input("Enter b: "))

commandDict = {"add": Calculator.add(a, b),
               "subtract": Calculator.subtract(a, b),
               "multiply": Calculator.multiply(a, b),
               "divide": Calculator.divide(a, b)}

result = commandDict.get(operation)

if result is not None:
    print(result)
else:
    print("No such command")






