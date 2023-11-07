from Calculator import Calculator
from Tracker import Tracker


class MainMenu:
    @staticmethod
    def print_menu():
        print("Welcome to The Calorie Tracker and Calculator!\n"
              "1. Calculator\n"
              "2. Tracker\n"
              "3. Exit")

    @staticmethod
    def print_tracker_menu():
        print("Welcome to The Calorie Tracker!\n"
              "1. Show last tracked session\n"
              "2. Show all tracked sessions")

    @staticmethod
    def start_app():
        while True:
            MainMenu.print_menu()
            choice = input("Enter desired operation: ")

            if choice == '1':
                calc = Calculator()
                print(calc.burned_calories_calculation())
            elif choice == '2':
                while True:
                    track = Tracker()
                    MainMenu.print_tracker_menu()
                    operation = input("Enter desired operation: ")

                    if operation == '1':
                        track.print_last_tracked_calories()
                    elif operation == '2':
                        track.print_all_tracked_calories()
                    else:
                        break
            else:
                print("Thank you for using the app and have a productive day! Stay healthy!")
                break

