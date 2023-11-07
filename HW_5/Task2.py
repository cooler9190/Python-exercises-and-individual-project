# 2.Animal Hierarchy
# Task: Create a class Animal with basic properties like name and sound.
# Extend it with subclasses for specific animals like Dog, Cat, and implement their specific behaviors.
# Example Input: dog = Dog(); dog.sound()
# Example Output: “Woof!”

class Animal:
    def __init__(self, name, sound="Sound"):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.sound)


class Dog(Animal):
    def __init__(self, name, sound="Woof!"):
        super().__init__(name, sound)


class Cat(Animal):
    def __init__(self, name, sound="Meow!"):
        super().__init__(name, sound)


animalType = input("Enter the animal type: ")

if animalType == "Dog":
    animal = Dog('Sharo')
elif animalType == "Cat":
    animal = Cat('Maca')
else:
    print("Animal type not supported!")
    exit()

command = input("Enter the command: ")

if command == "sound":
    animal.make_sound()
else:
    print("Command not supported!")
    exit()
