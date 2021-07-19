# This program calculates a car's gas mileage

import tkinter

class MPGCalcGUI:
    def __init__(self):
        # The main widget
        self.main_window = tkinter.Tk()

        # The frames
        self.top_frame = tkinter.Frame()
        self.upper_mid_frame = tkinter.Frame()
        self.lower_mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Top Frame
        self.prompt_label = tkinter.Label(self.top_frame, \
                                          text='Number of gallons of car:')
        self.gallons_entry = tkinter.Entry(self.top_frame, width=10)
        # Pack top frame
        self.prompt_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        # Upper mid frame
        self.prompt2_label = tkinter.Label(self.upper_mid_frame, \
                                           text='Miles the car can drive on ' + \
                                           'a full tank:')
        self.miles_entry = tkinter.Entry(self.upper_mid_frame, width=10)
        # Pack the Upper mid frame
        self.prompt2_label.pack(side='left')
        self.miles_entry.pack(side='left')

        # Lower mid frame
        self.descr_label = tkinter.Label(self.lower_mid_frame,
                                         text='MPG:')
        self.value = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.lower_mid_frame, \
                                       textvariable=self.value)
        # Pack the lower mid frame
        self.descr_label.pack(side='left')
        self.mpg_label.pack(side='left')

        # The bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, \
                                          text='Calculate', \
                                          command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text='Quit', \
                                          command=self.main_window.destroy)
        # Pack bottom frame
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack all the frames
        self.top_frame.pack()
        self.upper_mid_frame.pack()
        self.lower_mid_frame.pack()
        self.bottom_frame.pack()

        # The mainloop
        tkinter.mainloop()

    # The calculate method
    def calculate(self):
        gallons = float(self.gallons_entry.get())
        miles = float(self.miles_entry.get())
        mpg = format(miles / gallons, ',.1f').rstrip('0').rstrip('.')
        self.value.set(mpg)

# MPGCalcGUI object
mpg_calc = MPGCalcGUI()
