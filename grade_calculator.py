#   this is a program that adds a very basic GUI functionality to the basic grade caculator program
import tkinter

#   define class
class GradeCalculator:
#   GUI structure function
    def __init__(self, window):
        #   define main structure
        self.window = window
        window.title('Grade Calculator')
        window.geometry("300x100")

        #   define title frame
        self.title_frame = tkinter.Frame(window)
        self.title_label = tkinter.Label(self.title_frame, text = 'Enter a number between 0-1 to calculate letter grade')
        self.title_label.pack()
        self.title_frame.pack()

        #   define entry frame
        self.entry_frame = tkinter.Frame(window)
        self.grade_entry = tkinter.Entry(self.entry_frame)
        self.grade_entry.pack()
        self.entry_frame.pack()

        #   define results frame
        self.results_frame = tkinter.Frame(window)
        self.results_text = tkinter.StringVar()
        self.results_label = tkinter.Label(self.results_frame, textvariable = self.results_text)
        self.results_label.pack()
        self.results_frame.pack()

        #   define buttons frame
        self.buttons_frame = tkinter.Frame(window)
        self.calculate_button = tkinter.Button(self.buttons_frame, text = 'Calculate', command = self.computegrade)
        self.exit_button = tkinter.Button(self.buttons_frame, text = 'Exit', command = window.quit)
        self.exit_button.pack(side = 'right')
        self.calculate_button.pack(side = 'left')
        self.buttons_frame.pack()

    #   defines function to compute grade and return value to results_text label
    def computegrade(self):
        try:
            number_grade = self.grade_entry.get()
            number_grade = float(number_grade)
            if number_grade < 0 or number_grade > 1:
                self.results_text.set('Please enter a valid number')
            elif number_grade > .9:
                self.results_text.set('Grade: A')
            elif number_grade > .8:
                self.results_text.set('Grade: B')
            elif number_grade > .7:
                self.results_text.set('Grade: C')
            elif number_grade > .6:
                self.results_text.set('Grade: D')
            else:
                self.results_text.set('Grade: F')
        except ValueError:
                self.results_text.set('Please enter a valid number')

#   call tkinter, and class(object)
root = tkinter.Tk()
grade = GradeCalculator(root)
root.mainloop()
