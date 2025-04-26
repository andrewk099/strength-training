import tkinter as tk

class StrengthPlanCreator:

    def __init__(self, root):

        root.title("Custom Strength Plan Creator")
        root.geometry("1600x900")

        self.save_button = tk.Button(root, text="Save Entry", command=self.save_entry_to_file).grid(row=0, column=0, sticky="w")

        self.control = tk.IntVar(root, 0)
        self.weight_option1 = tk.Radiobutton(root, font=16, text="Fast Progression", variable=self.control, value=1).grid(row=0, column=1)
        self.weight_option2 = tk.Radiobutton(root, font=16, text="Slow Progression", variable=self.control, value=2).grid(row=0, column=2)

        self.str_exercise_entries = []
        self.exercise_entries = []
        max_range = 8

        self.frame = tk.Frame(root)
        self.label = tk.Label(root, text="Day 1", font=16).grid(row=1, column=0)

        for i in range(max_range):
            tk_str = tk.StringVar()
            entry = tk.Entry(root, textvariable=tk_str, font=16, width=26)
            self.str_exercise_entries.append(tk_str)
            self.exercise_entries.append(entry)
            entry.grid(row=i + 1, column=1, sticky="w")
        
        self.str_exercise_entries2 = []
        self.exercise_entries2 = []

        self.frame = tk.Frame(root)
        self.label = tk.Label(root, text="Day 2", font=16).grid(row=1, column=6)

        for i in range(max_range):
            tk_str = tk.StringVar()
            entry = tk.Entry(root, textvariable=tk_str, font=16, width=26)
            self.str_exercise_entries2.append(tk_str)
            self.exercise_entries2.append(entry)
            entry.grid(row=i + 1, column=7, sticky="w")

        self.str_exercise_entries3 = []
        self.exercise_entries3 = []

        self.frame = tk.Frame(root)
        self.label = tk.Label(root, text="Day 3", font=16).grid(row=9, column=0)

        for i in range(max_range):
            tk_str = tk.StringVar()
            entry = tk.Entry(root, textvariable=tk_str, font=16, width=26)
            self.str_exercise_entries3.append(tk_str)
            self.exercise_entries3.append(entry)
            entry.grid(row=i + 9, column=1, sticky="w")

        self.str_exercise_entries4 = []
        self.exercise_entries4 = []

        self.frame = tk.Frame(root)
        self.label = tk.Label(root, text="Day 4", font=16).grid(row=9, column=6)

        for i in range(max_range):
            tk_str = tk.StringVar()
            entry = tk.Entry(root, textvariable=tk_str, font=16, width=26)
            self.str_exercise_entries4.append(tk_str)
            self.exercise_entries4.append(entry)
            entry.grid(row=i + 9, column=7, sticky="w")
        
        self.str_sets_reps_entries = []
        self.sets_reps_entries = []

        self.frame = tk.Frame(root)
        self.label = tk.Label(root, text="Sets X Reps", font=16).grid(row=1, column=2)

        for i in range(max_range):
            tk_str = tk.StringVar()
            entry = tk.Entry(root, textvariable=tk_str, font=16, width=10)
            self.str_sets_reps_entries.append(tk_str)
            self.sets_reps_entries.append(entry)
            entry.grid(row=i + 1, column=3, sticky="w")

        self.str_sets_reps_entries2 = []
        self.sets_reps_entries2 = []

        self.frame = tk.Frame(root)
        self.label = tk.Label(root, text="Sets X Reps 2", font=16).grid(row=1, column=8)

        for i in range(max_range):
            tk_str = tk.StringVar()
            entry = tk.Entry(root, textvariable=tk_str, font=16, width=10)
            self.str_sets_reps_entries2.append(tk_str)
            self.sets_reps_entries2.append(entry)
            entry.grid(row=i + 1, column=9, sticky="w")

        self.str_sets_reps_entries3 = []
        self.sets_reps_entries3 = []

        self.frame = tk.Frame(root)
        self.label = tk.Label(root, text="Sets X Reps 3", font=16).grid(row=9, column=2)

        for i in range(max_range):
            tk_str = tk.StringVar()
            entry = tk.Entry(root, textvariable=tk_str, font=16, width=10)
            self.str_sets_reps_entries3.append(tk_str)
            self.sets_reps_entries3.append(entry)
            entry.grid(row=i + 9, column=3, sticky="w")

        self.str_sets_reps_entries4 = []
        self.sets_reps_entries4 = []

        self.frame = tk.Frame(root)
        self.label = tk.Label(root, text="Sets X Reps 4", font=16).grid(row=9, column=8)

        for i in range(max_range):
            tk_str = tk.StringVar()
            entry = tk.Entry(root, textvariable=tk_str, font=16, width=10)
            self.str_sets_reps_entries4.append(tk_str)
            self.sets_reps_entries4.append(entry)
            entry.grid(row=i + 9, column=9, sticky="w")

        self.float_rep_max_entries = []
        self.rep_max_entries = []

        self.frame = tk.Frame(root)
        self.label = tk.Label(root, text="Rep Max", font=16).grid(row=1, column=4)

        for i in range(max_range):
            tk_str = tk.DoubleVar()
            entry = tk.Entry(root, textvariable=tk_str, font=16, width=4)
            self.float_rep_max_entries.append(tk_str)
            self.rep_max_entries.append(entry)
            entry.grid(row=i + 1, column=5, sticky="w")

        self.float_rep_max_entries2 = []
        self.rep_max_entries2 = []

        self.frame = tk.Frame(root)
        self.label = tk.Label(root, text="Rep Max", font=16).grid(row=1, column=10)

        for i in range(max_range):
            tk_str = tk.DoubleVar()
            entry = tk.Entry(root, textvariable=tk_str, font=16, width=4)
            self.float_rep_max_entries2.append(tk_str)
            self.rep_max_entries2.append(entry)
            entry.grid(row=i + 1, column=11, sticky="w")

        self.float_rep_max_entries3 = []
        self.rep_max_entries3 = []

        self.frame = tk.Frame(root)
        self.label = tk.Label(root, text="Rep Max", font=16).grid(row=9, column=4)

        for i in range(max_range):
            tk_str = tk.DoubleVar()
            entry = tk.Entry(root, textvariable=tk_str, font=16, width=4)
            self.float_rep_max_entries3.append(tk_str)
            self.rep_max_entries3.append(entry)
            entry.grid(row=i + 9, column=5, sticky="w")

        self.float_rep_max_entries4 = []
        self.rep_max_entries4 = []

        self.frame = tk.Frame(root)
        self.label = tk.Label(root, text="Rep Max", font=16).grid(row=9, column=10)

        for i in range(max_range):
            tk_str = tk.DoubleVar()
            entry = tk.Entry(root, textvariable=tk_str, font=16, width=4)
            self.float_rep_max_entries4.append(tk_str)
            self.rep_max_entries4.append(entry)
            entry.grid(row=i + 9, column=11, sticky="w")
        
            
    def round_list_to_nearest_five(self, x):
        return list(map(lambda x : round(x / 5) * 5, x))

    def calculate_weights(self, weight):
        weight_list = [weight] * 8
        multipliers = []
        if self.control.get() == 1:
            multipliers = [.875, .9, .925, .95, .975, 1, 1.025, 1.05]
        elif self.control.get() == 2:
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
        lines = [
                ["Day 1", "\n"],
                self.create_line(self.exercise_entries[0].get(), self.sets_reps_entries[0].get(), self.float_rep_max_entries[0].get()),
                self.create_line(self.exercise_entries[1].get(), self.sets_reps_entries[1].get(), self.float_rep_max_entries[1].get()),
                self.create_line(self.exercise_entries[2].get(), self.sets_reps_entries[2].get(), self.float_rep_max_entries[2].get()),
                self.create_line(self.exercise_entries[3].get(), self.sets_reps_entries[3].get(), self.float_rep_max_entries[3].get()),
                self.create_line(self.exercise_entries[4].get(), self.sets_reps_entries[4].get(), self.float_rep_max_entries[4].get()),
                self.create_line(self.exercise_entries[5].get(), self.sets_reps_entries[5].get(), self.float_rep_max_entries[5].get()),
                self.create_line(self.exercise_entries[6].get(), self.sets_reps_entries[6].get(), self.float_rep_max_entries[6].get()),
                self.create_line(self.exercise_entries[7].get(), self.sets_reps_entries[7].get(), self.float_rep_max_entries[7].get()),
                ["Day 2", "\n"],
                self.create_line(self.exercise_entries2[0].get(), self.sets_reps_entries2[0].get(), self.float_rep_max_entries2[0].get()),
                self.create_line(self.exercise_entries2[1].get(), self.sets_reps_entries2[1].get(), self.float_rep_max_entries2[1].get()),
                self.create_line(self.exercise_entries2[2].get(), self.sets_reps_entries2[2].get(), self.float_rep_max_entries2[2].get()),
                self.create_line(self.exercise_entries2[3].get(), self.sets_reps_entries2[3].get(), self.float_rep_max_entries2[3].get()),
                self.create_line(self.exercise_entries2[4].get(), self.sets_reps_entries2[4].get(), self.float_rep_max_entries2[4].get()),
                self.create_line(self.exercise_entries2[5].get(), self.sets_reps_entries2[5].get(), self.float_rep_max_entries2[5].get()),
                self.create_line(self.exercise_entries2[6].get(), self.sets_reps_entries2[6].get(), self.float_rep_max_entries2[6].get()),
                self.create_line(self.exercise_entries2[7].get(), self.sets_reps_entries2[7].get(), self.float_rep_max_entries2[7].get()),
                ["Day 3", "\n"],
                self.create_line(self.exercise_entries3[0].get(), self.sets_reps_entries3[0].get(), self.float_rep_max_entries3[0].get()),
                self.create_line(self.exercise_entries3[1].get(), self.sets_reps_entries3[1].get(), self.float_rep_max_entries3[1].get()),
                self.create_line(self.exercise_entries3[2].get(), self.sets_reps_entries3[2].get(), self.float_rep_max_entries3[2].get()),
                self.create_line(self.exercise_entries3[3].get(), self.sets_reps_entries3[3].get(), self.float_rep_max_entries3[3].get()),
                self.create_line(self.exercise_entries3[4].get(), self.sets_reps_entries3[4].get(), self.float_rep_max_entries3[4].get()),
                self.create_line(self.exercise_entries3[5].get(), self.sets_reps_entries3[5].get(), self.float_rep_max_entries3[5].get()),
                self.create_line(self.exercise_entries3[6].get(), self.sets_reps_entries3[6].get(), self.float_rep_max_entries3[6].get()),
                self.create_line(self.exercise_entries3[7].get(), self.sets_reps_entries3[7].get(), self.float_rep_max_entries3[7].get()),
                ["Day 4", "\n"],
                self.create_line(self.exercise_entries4[0].get(), self.sets_reps_entries4[0].get(), self.float_rep_max_entries4[0].get()),
                self.create_line(self.exercise_entries4[1].get(), self.sets_reps_entries4[1].get(), self.float_rep_max_entries4[1].get()),
                self.create_line(self.exercise_entries4[2].get(), self.sets_reps_entries4[2].get(), self.float_rep_max_entries4[2].get()),
                self.create_line(self.exercise_entries4[3].get(), self.sets_reps_entries4[3].get(), self.float_rep_max_entries4[3].get()),
                self.create_line(self.exercise_entries4[4].get(), self.sets_reps_entries4[4].get(), self.float_rep_max_entries4[4].get()),
                self.create_line(self.exercise_entries4[5].get(), self.sets_reps_entries4[5].get(), self.float_rep_max_entries4[5].get()),
                self.create_line(self.exercise_entries4[6].get(), self.sets_reps_entries4[6].get(), self.float_rep_max_entries4[6].get()),
                self.create_line(self.exercise_entries4[7].get(), self.sets_reps_entries4[7].get(), self.float_rep_max_entries4[7].get())
        ]

        with open("output.txt", "w") as file:
            for line in lines:
                if ' ' in line:
                    line.remove(' ')
                elif 0 in line:
                    line.remove(0)
                else:
                    for x in line:
                        file.write(x)

root = tk.Tk()
StrengthPlanCreator(root)
root.mainloop()