# This program displays your name and address when
# a button is clicked.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # The main window widget
        self.main_window = tkinter.Tk()

        # Show info button
        self.my_button = tkinter.Button(self.main_window,
                                        text='Show Info',
                                        command=self.show_info)

        # Quit button
        self.quit_button = tkinter.Button(self.main_window,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Pack the buttons
        self.my_button.pack()
        self.quit_button.pack()

        # The tkinter main loop
        tkinter.mainloop()

    # The show info method
    def show_info(self):
        lines = ['Steven Marcus', '274 Baily Drive', 'Waynesville, NC 27999']
        tkinter.messagebox.showinfo('Text', '\n'.join(lines))
        

# MyGUI class instance
my_gui = MyGUI()
