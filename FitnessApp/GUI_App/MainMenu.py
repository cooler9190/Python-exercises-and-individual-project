from Calculator import Calculator
from Tracker import Tracker
import tkinter as tk
from tkinter import messagebox

LARGE_FONT = ("Verdana", 16)
SMALL_FONT = ("Verdana", 12)


class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.attributes("-fullscreen", True)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPageGUI, CalculatorGUI, TrackerGUI):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPageGUI)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPageGUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        label = tk.Label(self, text="Calorie calculator and Tracker", font=LARGE_FONT, bg="black", fg="white")
        label.pack(pady=20)

        button1 = tk.Button(self, text="Calculator",
                            command=lambda: controller.show_frame(CalculatorGUI))

        button1.pack(pady=10)

        button2 = tk.Button(self, text="Tracker",
                            command=lambda: controller.show_frame(TrackerGUI))

        button2.pack(pady=10)

        button3 = tk.Button(self, text="Exit", bg="red", fg="black",
                            command=lambda: StartPageGUI.close_app())
        button3.pack(pady=10)

    @staticmethod
    def close_app():
        message = tk.messagebox.showinfo("Exit Message",
                                         "Thank you for using the app and have a productive day! Stay healthy!")

        if message:
            GUI().quit()


class CalculatorGUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        label = tk.Label(self, text="Calculator", font=LARGE_FONT, bg="black", fg="white")
        label.pack(pady=20)

        weight_label = tk.Label(self, text="Enter your weight (in kg):", font=SMALL_FONT, bg="black", fg="white")
        weight_label.pack()

        weight_entry = tk.Entry(self, font=SMALL_FONT)
        weight_entry.pack()

        exercise_label = tk.Label(self, text="Enter the type of exercise", font=SMALL_FONT, bg="black", fg="white")
        exercise_label.pack()

        exercise_var = tk.StringVar()
        exercise_entry = tk.Entry(self, textvariable=exercise_var, font=SMALL_FONT)
        exercise_entry.pack()

        time_label = tk.Label(self, text="Enter duration of exercise (in minutes):", font=SMALL_FONT, bg="black", fg="white")
        time_label.pack()

        time_entry = tk.Entry(self, font=SMALL_FONT)
        time_entry.pack()

        result_label = tk.Label(self, text='', font=SMALL_FONT, bg="black", fg="white")
        result_label.pack(pady=10)

        calculate_button = tk.Button(self, text="Calculate", font=SMALL_FONT,
                                     command=lambda: result_label.config(text=Calculator.calculate(
                                         weight_entry.get(), exercise_var.get(), time_entry.get())))
        calculate_button.pack(pady=10)

        return_button = tk.Button(self, text="Return", font=SMALL_FONT,
                                  command=lambda: controller.show_frame(StartPageGUI))
        return_button.pack(pady=10)


class TrackerGUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        label = tk.Label(self, text="Tracker", font=LARGE_FONT, bg="black", fg="white")
        label.pack(pady=20)

        button1 = tk.Button(self, text="Show last tracked session", font=SMALL_FONT,
                            command=lambda: result_label.config(text=Tracker().print_last_tracked_calories()))

        button1.pack(pady=10)

        button2 = tk.Button(self, text="Show all tracked sessions", font=SMALL_FONT,
                            command=lambda: result_label.config(text=Tracker().print_all_tracked_calories()))

        button2.pack(pady=10)

        result_label = tk.Label(self, text='', font=SMALL_FONT, bg="black", fg="white")
        result_label.pack()

        button3 = tk.Button(self, text="Return", font=SMALL_FONT,
                            command=lambda: controller.show_frame(StartPageGUI))

        button3.pack(pady=10)
