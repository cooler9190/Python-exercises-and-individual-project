# 7. Задача: Създайте класове Bird, Swimmer, и Penguin, където Penguin
# наследява и двата класа и комбинира техните свойства.
# Вход: създаване на пингвин и извикване на методите за плуване и летене
# Изход: "Swimming" и "Can't fly"

class Swimming:
    @staticmethod
    def swim():
        return "Swimming"


class Bird:
    #maybe make it instance method
    @staticmethod
    def fly():
        return "Flying"


class Penguin(Bird, Swimming):
    def __init__(self, name):
        self.name = name

    def fly(self):
        return "Can't fly"


pesho = Penguin("Pesho")

print("Pesho: ")

print(pesho.swim())

print(pesho.fly())
