import os


class Tracker:
    def __init__(self):
        self.__path = 'calories_and_weight_data'

    def print_all_tracked_calories(self):
        try:
            if os.path.getsize(self.__path) == 0:
                return "The tracker has no data."
        except OSError:
            return "The file does NOT exist!"

        with open(self.__path, "r") as file:
            return file.read()

    def print_last_tracked_calories(self):
        try:
            if os.path.getsize(self.__path) == 0:
                return "The tracker has no data."
        except OSError:
            return "The file does NOT exist!"

        with open(self.__path, "r") as file:
            return file.readlines()[-1]

    def add_to_tracker(self, date, calories, weight):
        with open(self.__path, "a") as file:
            file.write('\n')
            file.write(f"On {date}: User has burned approximately {calories:.2f} "
                       f"and has lost approximately {weight:.2f} kg")

