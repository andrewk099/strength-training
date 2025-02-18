import tkinter as tk

class StrengthPlanCreator:

    def __init__(self, root):

        root.title("Custom Strength Plan")

        self.exercise01 = tk.StringVar()
        exercise1 = tk.Entry(root, font=16, width=26, textvariable=self.exercise01).grid(row=1, column=2, sticky="w")
        exercise1_label = tk.Label(root, text="Exercises", font=16).grid(row=1, column=1)

        self.exercise02 = tk.StringVar()
        exercise2 = tk.Entry(root, font=16, width=26, textvariable=self.exercise02).grid(row=2, column=2, sticky="w")

        self.exercise03 = tk.StringVar()
        exercise3 = tk.Entry(root, font=16, width=26, textvariable=self.exercise03).grid(row=3, column=2, sticky="w")

        self.exercise04 = tk.StringVar()
        exercise4 = tk.Entry(root, font=16, width=26, textvariable=self.exercise04).grid(row=4, column=2, sticky="w")

        self.exercise05 = tk.StringVar()
        exercise5 = tk.Entry(root, font=16, width=26, textvariable=self.exercise05).grid(row=5, column=2, sticky="w")

        self.exercise06 = tk.StringVar()
        exercise6 = tk.Entry(root, font=16, width=26, textvariable=self.exercise06).grid(row=6, column=2, sticky="w")

        self.exercise07 = tk.StringVar()
        exercise7 = tk.Entry(root, font=16, width=26, textvariable=self.exercise07).grid(row=7, column=2, sticky="w")

        self.sets_reps_01 = tk.StringVar()
        sets_reps_1 = tk.Entry(root, font=16, width=10, textvariable=self.sets_reps_01).grid(row=1, column=4, sticky="w")
        sets_reps_1_label = tk.Label(root, text="Sets X reps", font=16).grid(row=1, column=3, sticky="w")

        self.sets_reps_02 = tk.StringVar()
        sets_reps_2 = tk.Entry(root, font=16, width=10, textvariable=self.sets_reps_02).grid(row=2, column=4, sticky="w")

        self.sets_reps_03 = tk.StringVar()
        sets_reps_3 = tk.Entry(root, font=16, width=10, textvariable=self.sets_reps_03).grid(row=3, column=4, sticky="w")

        self.sets_reps_04 = tk.StringVar()
        sets_reps_4 = tk.Entry(root, font=16, width=10, textvariable=self.sets_reps_04).grid(row=4, column=4, sticky="w")

        self.sets_reps_05 = tk.StringVar()
        sets_reps_5 = tk.Entry(root, font=16, width=10, textvariable=self.sets_reps_05).grid(row=5, column=4, sticky="w")

        self.sets_reps_06 = tk.StringVar()
        sets_reps_6 = tk.Entry(root, font=16, width=10, textvariable=self.sets_reps_06).grid(row=6, column=4, sticky="w")

        self.sets_reps_07 = tk.StringVar()
        sets_reps_7 = tk.Entry(root, font=16, width=10, textvariable=self.sets_reps_07).grid(row=7, column=4, sticky="w")

        self.rep_max_01 = tk.DoubleVar()
        rep_max_1 = tk.Entry(root, font=16, width=4, textvariable=self.rep_max_01).grid(row=1, column=6)
        rep_max_1_label = tk.Label(root, text="Enter Rep Max", font=16).grid(row=1, column=5)

        self.rep_max_02 = tk.DoubleVar()
        rep_max_2 = tk.Entry(root, font=16, width=4, textvariable=self.rep_max_02).grid(row=2, column=6)

        self.rep_max_03 = tk.DoubleVar()
        rep_max_3 = tk.Entry(root, font=16, width=4, textvariable=self.rep_max_03).grid(row=3, column=6)

        self.rep_max_04 = tk.DoubleVar()
        rep_max_4 = tk.Entry(root, font=16, width=4, textvariable=self.rep_max_04).grid(row=4, column=6)

        self.rep_max_05 = tk.DoubleVar()
        rep_max_5 = tk.Entry(root, font=16, width=4, textvariable=self.rep_max_05).grid(row=5, column=6)

        self.rep_max_06 = tk.DoubleVar()
        rep_max_6 = tk.Entry(root, font=16, width=4, textvariable=self.rep_max_06).grid(row=6, column=6)

        self.rep_max_07 = tk.DoubleVar()
        rep_max_7 = tk.Entry(root, font=16, width=4, textvariable=self.rep_max_07).grid(row=7, column=6)

        save_button = tk.Button(root, text="Save Entry", command=self.save_entry_to_file)
        save_button.grid(row=8, column=1, sticky="w")

    def round_list_to_nearest_five(self, x):
        return list(map(lambda x : round(x / 5) * 5, x))

    def calculate_weights(self, weight):
        weight_list = [weight] * 8
        multipliers = [.85, .875, .9, .925, .95, .975, 1, 1.025]
        return self.round_list_to_nearest_five(list(map(lambda x, y : x * y, weight_list, multipliers)))

    def create_line(self, exercise, sets_reps, rep_max):
        line = []
        line.append(exercise + " ")
        line.append(sets_reps + " ")
        weights = self.calculate_weights(rep_max)
        for w in weights:
            line.append(str(w) + " ")
        line.append("\n")
        return line

    def save_entry_to_file(self):
        lines = (
                self.create_line(self.exercise01.get(), self.sets_reps_01.get(), self.rep_max_01.get()),
                self.create_line(self.exercise02.get(), self.sets_reps_02.get(), self.rep_max_02.get()),
                self.create_line(self.exercise03.get(), self.sets_reps_03.get(), self.rep_max_03.get()),
                self.create_line(self.exercise04.get(), self.sets_reps_04.get(), self.rep_max_04.get()),
                self.create_line(self.exercise05.get(), self.sets_reps_05.get(), self.rep_max_05.get()),
                self.create_line(self.exercise06.get(), self.sets_reps_06.get(), self.rep_max_06.get()),
                self.create_line(self.exercise07.get(), self.sets_reps_07.get(), self.rep_max_07.get())
        )
        with open("output.txt", "w") as file: 
            for line in lines:
                for x in line:
                    file.write((x))

        status_label = tk.Label(root, text="")
        status_label.grid(row=9, column=1, sticky="w")
        status_label.config(text="Entry saved to file!")
        
root = tk.Tk()
StrengthPlanCreator(root)
root.mainloop()