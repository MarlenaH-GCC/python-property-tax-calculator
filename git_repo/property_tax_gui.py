import tkinter
import tkinter.messagebox

class Property_TaxGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text='Enter numeric actual value of property:')
        self.value_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side='left', padx=5, pady=5)
        self.value_entry.pack(side='left', padx=5, pady=5)

        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate', command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left', padx=5, pady=5)
        self.quit_button.pack(side='left', padx=10, pady=10)

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()
        
    def calculate(self):
        value = float(self.value_entry.get())
        assessment_value = value * 0.6
        property_tax = assessment_value * 0.0075
        tkinter.messagebox.showinfo('Result', f'Assessment Value: ${assessment_value:.2f}\nProperty Tax: ${property_tax:.2f}')

if __name__ == '__main__':
    calc_tax = Property_TaxGUI()