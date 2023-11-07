from tkinter import messagebox
import datetime
from Tracker import Tracker


class Calculator:
    @staticmethod
    def calculate(weight, exercise, duration):
        try:
            weight = float(weight)
            duration = int(duration)
        except ValueError:
            return "Incorrect input! Please enter again!"

        if weight < 15 or weight > 160:
            return "Weight must be between 15 and 160 kg! Please enter again!"

        if duration <= 0:
            return "Duration cannot be 0 or less! Please enter again"

        met_values = {"Running": 8, "Bicycling": 7.5, "Weightlifting": 6}
        met_value = met_values.get(exercise)

        if met_value is None:
            return "Unrecognized exercise type! Please enter again!"

        calories_burned = (met_value * 3.5 * weight) / 200 * duration
        weight_loss = calories_burned * 0.00013
        result_text = f"Calories burned: {calories_burned:.2f}\nWeight loss: {weight_loss:.2f} kg"

        choice = messagebox.askyesno("Track Progress", "Would you like to track your progress?")
        if choice:
            curr_date = datetime.datetime.today()
            curr_date = curr_date.strftime("%Y/%m/%d %H:%M:%S")
            Tracker.add_to_tracker(Tracker(), curr_date, calories_burned, weight_loss)

        return result_text


