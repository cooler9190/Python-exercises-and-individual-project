from datetime import date
from Tracker import Tracker


class Calculator:
    def __init__(self):
        self.__weight = 0
        self.__time = 0
        self.__exercises = {"Running": 8,
                            "Bicycling": 7.5,
                            "Weightlifting": 6}

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, val):
        if not isinstance(val, float):
            raise TypeError
        elif val < 35 or val > 160:
            raise ValueError("Weight cannot be less than 15 or more than 160 kg")

        self.__weight = val

    @property
    def time(self):
        return self.__weight

    @time.setter
    def time(self, val):
        if not isinstance(val, int):
            raise TypeError

        self.__time = val

    def burned_calories_calculation(self):
        total_calories_burned, total_weight_lost = 0, 0
        self.weight = float(input("Enter your weight(in kg): "))

        while True:
            exercise = input("Enter the type of exercise: ")
            met_value = self.__exercises.get(exercise)

            if met_value is None:
                print("Unrecognized exercise type! Please enter again")
                continue

            self.time = int(input("Enter the duration of the exercise(in minutes): "))

            calories_burned = (met_value * 3.5 * self.__weight) / 200 * self.__time
            weight_loss = calories_burned * 0.00013

            total_calories_burned += calories_burned
            total_weight_lost += weight_loss

            flag = input("Is this everything?(Y/N): ")
            flag.upper()

            while flag != 'Y' and flag != 'N':
                flag = input("The input is unrecognised, please enter again: ")

            if flag == 'Y':
                choice = input('Would you like to track your progress?(Y/N):')
                choice.upper()
                if choice == 'Y':
                    curr_date = date.today()
                    Tracker.add_to_tracker(Tracker(), curr_date, total_calories_burned, total_weight_lost)
                    return (f"Total calories burned are approximately {total_calories_burned} "
                            f"and total wight loss is approximately {total_weight_lost} kg")

            else:
                continue



