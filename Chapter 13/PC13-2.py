# This program translates Latin words to
# English. The windows displays 3 buttons, one
# for each latin word. When clicked the program
# displays the english translation.

import tkinter

class TranslatorGUI:
    def __init__(self):
        # The main window
        self.main_window = tkinter.Tk()

        # Main window frames
        self.top_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Top frame label
        self.top_label = tkinter.Label(self.top_frame,
                                       text='Choose a ' + \
                                       'Latin word to translate:')
        # Pack the label
        self.top_label.pack()

        # The 3 buttons for the 3 different latin words
        self.sinister_button = tkinter.Button(self.middle_frame, \
                                              text='sinister',
                                              command=self.translateword1)
        self.dexter_button = tkinter.Button(self.middle_frame, \
                                            text='dexter',
                                            command=self.translateword2)
        self.medium_button = tkinter.Button(self.middle_frame, \
                                            text='medium',
                                            command=self.translateword3)
        # Pack the buttons
        self.sinister_button.pack(side='left')
        self.dexter_button.pack(side='left')
        self.medium_button.pack(side='left')

        # Bottom frame labels
        self.bottom_left_label = tkinter.Label(self.bottom_frame, \
                                               text='English Translation:')
        self.translation = tkinter.StringVar()
        self.trans_label = tkinter.Label(self.bottom_frame, \
                                         textvariable=self.translation)
        self.bottom_left_label.pack(side='left')
        self.trans_label.pack(side='left')
        
        # Pack the frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # The mainloop
        tkinter.mainloop()

    # Define the translateword methods
    def translateword1(self):
        self.translation.set('left')
    def translateword2(self):
        self.translation.set('right')
    def translateword3(self):
        self.translation.set('center')

# Translator object
translator = TranslatorGUI()
                            
