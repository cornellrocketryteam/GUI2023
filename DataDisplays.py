"""
DataDisplays

This code creates the content for the Data Panel and Message Panel in the
GroundStationGUI.

12 January 2023
"""

import tkinter as tk
from tkinter import *
from Parsing import Parse
import time

class Displays(Parse):

    def __init__(self, acc, gyr, mag, ther, msg, alti):
        super().__init__()
        # initialize master frames
        self.acc = acc
        self.gyr = gyr
        self.magn = mag
        self.ther = ther
        self.msg = msg
        self.alti = alti

        self.formatData()

        # initalize data labels
        self.accelLabel = self.label(self.acc, str(self.accel))
        self.gyroLabel = self.label(self.gyr, str(self.gyro))
        self.magLabel = self.label(self.magn, str(self.mag))
        self.tempLabel = self.label(self.ther, str(self.temp))
        self.messageLabel = self.label(self.msg, str(self.message))
        self.altLabel = self.label(self.alti, str(self.alt))


    def label(self, f, t):
        l = Label(master = f, text = t, bg = "black", fg = "white", font = ('OCR A Extended', 24))
        l.pack(fill = tk.BOTH, side = tk.BOTTOM, expand = True)
        return l

    def labelUpdate(self, l, t):
        l.config(text = str(t))
        l.pack(fill = tk.BOTH, side = tk.BOTTOM, expand = True)

    def formatData(self):
        try:
            self.accel = "x: " + str(self.accel[0]) + "\ny: " + str(self.accel[1]) + "\nz: " + str(self.accel[2])
            self.gyro = "x: " + str(self.gyro[0]) + "\ny: " + str(self.gyro[1]) + "\nz: " + str(self.gyro[2])
            self.mag = "x: " + str(self.mag[0]) + "\ny: " + str(self.mag[1]) + "\nz: " + str(self.mag[2])
        except:
            pass

    def dispUpdate(self):
        try:
            self.formatData()

            self.labelUpdate(self.accelLabel, self.accel)
            self.labelUpdate(self.gyroLabel, self.gyro)
            self.labelUpdate(self.magLabel, self.mag)
            self.labelUpdate(self.tempLabel, self.temp)
            self.labelUpdate(self.messageLabel, self.message)
            self.labelUpdate(self.altLabel, self.alt)
        except:
            pass
