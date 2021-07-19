# This program lets a user select any or all of
# the services Joe's Automotive performs and when
# the user clicks a button, the total charges will
# be displayed.

import tkinter

class AutomotiveGUI:
    def __init__(self):
        # The main window
        self.main_window = tkinter.Tk()

        # The 3 frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Top frame
        self.top_label = tkinter.Label(self.top_frame,
                                       text='Select all ' + \
                                       'services you require.')
        # Pack the top frame
        self.top_label.pack()

        # Checkbuttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        # Set IntVar to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        # Checkbuttons for the mid frame
        self.cb1 = tkinter.Checkbutton(self.mid_frame, \
                                       text='Oil Change', \
                                       variable=self.cb_var1, \
                                       command=self.oil_change)
        self.cb2 = tkinter.Checkbutton(self.mid_frame, \
                                       text='Lube Job', \
                                       variable=self.cb_var2, \
                                       command=self.lube_job)
        self.cb3 = tkinter.Checkbutton(self.mid_frame, \
                                       text='Radiator flush', \
                                       variable=self.cb_var3, \
                                       command=self.radiator_flush)
        self.cb4 = tkinter.Checkbutton(self.mid_frame, \
                                       text='Transmission flush', \
                                       variable=self.cb_var4, \
                                       command=self.transmission_flush)
        self.cb5 = tkinter.Checkbutton(self.mid_frame, \
                                       text='Inspection', \
                                       variable=self.cb_var5, \
                                       command=self.inspection)
        self.cb6 = tkinter.Checkbutton(self.mid_frame, \
                                       text='Muffler replacement', \
                                       variable=self.cb_var6, \
                                       command=self.muffler)
        self.cb7 = tkinter.Checkbutton(self.mid_frame, \
                                       text='Tire rotation', \
                                       variable=self.cb_var7, \
                                       command=self.tire_rotation)

        # Pack the checkbuttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        # Label widgets for bottom frame
        self.bottom_label = tkinter.Label(self.bottom_frame,
                                          text='Total:')
        self.total = tkinter.StringVar()
        self.total.set('0.00')
        self.total_label = tkinter.Label(self.bottom_frame, \
                                         textvariable=self.total)
        # Pack the bottom frame
        self.bottom_label.pack(side='left')
        self.total_label.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # The mainloop
        tkinter.mainloop()

    def oil_change(self):
        total = float(self.total.get())
        if self.cb_var1.get():
            total += 30
        else:
            total -= 30
        total = format(total, '.2f')
        self.total.set(total)
    def lube_job(self):
        total = float(self.total.get())
        if self.cb_var2.get():
            total += 20
        else:
            total -= 20
        total =  format(total, '.2f')
        self.total.set(total)
    def radiator_flush(self):
        total = float(self.total.get())
        if self.cb_var3.get():
            total += 40
        else:
            total -= 40
        total = format(total, '.2f')
        self.total.set(total)
    def transmission_flush(self):
        total = float(self.total.get())
        if self.cb_var4.get():
            total += 100
        else:
            total -= 100
        total = format(total, '.2f')
        self.total.set(total)
    def inspection(self):
        total = float(self.total.get())
        if self.cb_var5.get():
            total += 35
        else:
            total -= 35
        total = format(total, '.2f')
        self.total.set(total)
    def muffler(self):
        total = float(self.total.get())
        if self.cb_var6.get():
            total += 200
        else:
            total -= 200
        total = format(total, '.2f')
        self.total.set(total)
    def tire_rotation(self):
        total = float(self.total.get())
        if self.cb_var7.get():
            total += 20
        else:
            total -= 20
        total = format(total, '.2f')
        self.total.set(total)

# AutomativeGUI object
auto_gui = AutomotiveGUI()
        
