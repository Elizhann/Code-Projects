import tkinter #   import tkinter

#   define class for template
class TemplateGUI:
    def __init__(self, window):
        self.window = window
        window.title('Template Tkinter GUI')
        window.geometry("100x100")

        #   defines and packs top frame and widgets within
        self.top_frame = tkinter.Frame(window)
        self.label = tkinter.Label(self.top_frame, text = 'This is a sample GUI')
        self.label.pack()

        self.top_frame.pack(side = 'top')

        #defines middle frame and widgets within

        self.middle_frame = tkinter.Frame(window)
        self.entry = tkinter.Entry(self.middle_frame)
        self.entry.pack()

        self.middle_frame.pack()

        #   sample button type 1
        self.bottom_frame = tkinter.Frame(window)
        self.enter_button = tkinter.Button(self.bottom_frame, text = 'Enter', command = self.enter)
        self.enter_button.pack(side = 'left')

        #   sample button type 2
        self.exit_button = tkinter.Button(self.bottom_frame, text = 'Exit', command = window.quit)
        self.exit_button.pack(side = 'right')

        self.bottom_frame.pack(side = 'bottom')


    #   sample function to do something
    def enter(self):
        print('Doing something')


root = tkinter.Tk()
Test_template = TemplateGUI(root)
root.mainloop()
