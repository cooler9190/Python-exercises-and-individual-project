# 1. Задача: Създайте клас BankAccount, който да инкапсулира баланса
# и позволява депозиране и теглене след проверка на PIN код.
# Вход: PIN 1234, депозит 100, теглене 50
# Изход: баланс 50

class BankAccount:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.__balance = balance

    @property
    def get_balance(self):
        return self.__balance

    def deposit(self):
        pin = int(input("Enter your pin code: "))
        if pin != self.pin:
            print("WRONG PIN CODE!")
        else:
            value = int(input("Enter deposit value: "))
            self.__balance += value
            print(self.__balance)

    def withdrawal(self):
        pin = int(input("Enter your pin code: "))
        if pin != self.pin:
            print("WRONG PIN CODE!")
        else:
            value = int(input("Enter deposit value: "))
            while value > self.__balance:
                value = int(input("You can't withdraw more than what you already have, please try again: "))

            self.__balance -= value
            print(self.__balance)


account1 = BankAccount(1234)
print(account1.get_balance())

account2 = BankAccount(5678, 50)
print(account2.get_balance())

account1.deposit()

account2.withdrawal()

