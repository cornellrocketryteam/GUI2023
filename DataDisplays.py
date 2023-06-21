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

class Displays():

    def __init__(self, acc, gyr, mag, ther, msg, alti, sensorreadings):
        # initialize master frames
        self.acc = acc
        self.gyr = gyr
        self.magn = mag
        self.ther = ther
        self.msg = msg
        self.alti = alti
        self.readings = sensorreadings

        self.accel = self.readings[2]
        self.gyro = self.readings[3]
        self.mag = self.readings[4]

        self.formatData()

        # initalize data labels
        self.altLabel = self.label(self.alti, str(self.readings[1]))
        self.accelLabel = self.label(self.acc, str(self.accel))
        self.gyroLabel = self.label(self.gyr, str(self.gyro))
        self.magLabel = self.label(self.magn, str(self.mag))
        self.tempLabel = self.label(self.ther, str(self.readings[5]))
        self.messageLabel = self.label(self.msg, str(self.readings[6]))

        #reference: self.readings = [self.gps, self.alt, self.accel, self.gyro, self.mag, self.mag, self.temp, self.message]

    def label(self, f, t):
        """
        Creates a Label object using a given master Frame f and given text to display t.
        """
        l = Label(master = f, text = t, bg = "black", fg = "white", font = ('OCR A Extended', 24))
        l.pack(fill = tk.BOTH, side = tk.BOTTOM, expand = True)
        return l

    def labelUpdate(self, l, t):
        """
        Updates a given Label l to display the given text t.
        """
        l.config(text = str(t))
        l.pack(fill = tk.BOTH, side = tk.BOTTOM, expand = True)

    def formatData(self):
        """
        Formats sensor readings that come with x, y, and z components into a more readable format.
        """
        try:
            self.accel = self.readings[2]
            self.gyro = self.readings[3]
            self.mag = self.readings[4]

            self.accel = "x: " + str(self.accel[0]) + "\ny: " + str(self.accel[1]) + "\nz: " + str(self.accel[2])
            self.gyro = "x: " + str(self.gyro[0]) + "\ny: " + str(self.gyro[1]) + "\nz: " + str(self.gyro[2])
            self.mag = "x: " + str(self.mag[0]) + "\ny: " + str(self.mag[1]) + "\nz: " + str(self.mag[2])
        except:
            pass

    def dispUpdate(self, sensorreadings):
        """
        Updates the values displayed in each Label of the GUI.
        """
        self.readings = sensorreadings
        try:
            self.formatData()

            self.labelUpdate(self.altLabel, self.readings[1])
            self.labelUpdate(self.accelLabel, self.accel)
            self.labelUpdate(self.gyroLabel, self.gyro)
            self.labelUpdate(self.magLabel, self.mag)
            self.labelUpdate(self.tempLabel, self.readings[5])
            self.labelUpdate(self.messageLabel, self.readings[6])
        except:
            pass
