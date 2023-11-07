# 2. Задача: Реализирайте клас Person, който инкапсулира личните данни и
# предоставя методи за промяна само след валидация с парола.
# Вход: парола "secret", промяна на имейл
# Изход: новият имейл

class Person:
    def __init__(self, name, age, password, email='', telephone=0):
        self.name = name
        self.age = age
        self.__password = str(password)
        self.__email = email
        self.__telephoneNum = telephone

    def choose_command(self):
        password = input("Enter the password: ")
        while password != self.__password:
            password = input("Incorrect password, please try again: ")

        command = int(input("Choose a command option(1 to 3):\n "
                        "1. Change password \n"
                        "2. Change email \n"
                        "3. Change telephone number\n"))

        if command == 1:
            self.set_password()
        elif command == 2:
            self.set_email()
        elif command == 3:
            self.set_telephone()
        else:
            print("No such command available!")
            exit()

    @property
    def get_password(self):
        return self.__password

    @property
    def get_email(self):
        return self.__email

    @property
    def get_telephone(self):
        return self.__telephoneNum

    def set_password(self):
        new_password = input("Please enter the new password you wish to change: ")
        self.__password = new_password
        print("Password set to: ", self.get_password)

    def set_email(self):
        new_email = input("Please enter the new email you wish to change: ")
        self.__email = new_email
        print("Email set to: ", self.get_email)

    def set_telephone(self):
        new_number = int(input("Please enter the new telephone you wish to change: "))
        self.__telephoneNum = new_number
        print("Telephone number set to: ", self.get_telephone)


person1 = Person('Nick', 22, 1234)

person1.choose_command()
