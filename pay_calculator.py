#   this program adds a basic tkinter GUI to the function organized pay + overtime calculator

import tkinter #   import tkinter

#   define class for template
class PayCalculator:
    def __init__(self, window):
        #   define window and design information
        self.window = window
        window.title('Pay Calculator')
        window.geometry("200x200")


        #   top frame to give instructions
        self.top_frame = tkinter.Frame(window)
        self.instruction_label = tkinter.Label(text = 'Enter hours and rate to calculate pay')
        self.instruction_label.pack()
        self.top_frame.pack()

        #   frame containing rate entry
        self.rate_frame = tkinter.Frame(window)
        self.rate_label = tkinter.Label(self.rate_frame, text = 'Rate:')
        self.rate_label.pack(side = 'left')
        self.rate_entry = tkinter.Entry(self.rate_frame)
        self.rate_entry.pack(side = 'right')
        self.rate_frame.pack()

        #   frame containing hours entry
        self.hours_frame = tkinter.Frame(window)
        self.hours_label = tkinter.Label(self.hours_frame, text = 'Hours:')
        self.hours_label.pack(side = 'left')
        self.hours_entry = tkinter.Entry(self.hours_frame)
        self.hours_entry.pack(side = 'right')
        self.hours_frame.pack()

        #   middle frame with returned data
        self.middle_frame = tkinter.Frame(window)

        self.pay_label_text = tkinter.StringVar()
        self.overtime_label_text = tkinter.StringVar()
        self.total_label_text = tkinter.StringVar()

        self.pay_label = tkinter.Label(self.middle_frame, textvariable = self.pay_label_text)
        self.overtime_label = tkinter.Label(self.middle_frame, textvariable = self.overtime_label_text)
        self.total_label = tkinter.Label(self.middle_frame, textvariable = self.total_label_text)

        self.pay_label.pack()
        self.overtime_label.pack()
        self.total_label.pack()
        self.middle_frame.pack()

        #   bottom frame with calculation buttons
        self.bottom_frame = tkinter.Frame(window)
        self.enter_button = tkinter.Button(self.bottom_frame, text = 'Calculate', command = self.computepay)
        self.enter_button.pack(side = 'left')
        self.exit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = window.quit)
        self.exit_button.pack(side = 'right')
        self.bottom_frame.pack()

#   defines function to calculate pay
    def computepay(self):
        #   get rate information from entry window
        rate = self.rate_entry.get()
        rate = float(rate)

        #   get hours information from entry window
        hours = self.hours_entry.get()
        hours = float(hours)

        #   calculate base pay, overtime and total pay
        pay = (hours * rate)

        if hours > 40:
            overtime = (rate * 1.5) * (hours - 40)
        else:
            overtime = 0

        total = (hours * rate ) + overtime

        #   set information to fill blank labels
        self.pay_label_text.set('Base Pay: ' + '$' + str(pay))
        self.overtime_label_text.set('Overtime: ' + '$' + str(overtime))
        self.total_label_text.set('Total Pay: ' + '$' + str(total))

#   call tkinter, and class(object)
root = tkinter.Tk()
pay = PayCalculator(root)
root.mainloop()
