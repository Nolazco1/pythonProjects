# This program draws a house using
# tkinter canvas

import tkinter

class houseGUI:
    def __init__(self):
        # The main window
        self.main_window = tkinter.Tk()

        # Canvas widget
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # House base
        self.canvas.create_rectangle(50, 50, 130, 100)

        # House roof
        self.canvas.create_line(50, 50,  130, 50, 90, 15, 50, 50)

        # Roof window
        self.canvas.create_oval(110, 45, 70, 30)

        # Door
        self.canvas.create_rectangle(75, 100, 100, 80)

        # Pack the canvas
        self.canvas.pack()

        # The mainloop
        tkinter.mainloop()

# houseGUI object
my_house = houseGUI()
