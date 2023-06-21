"""
Ground Station GUI (Tkinter Version)

This code constructs and runs the Ground Station GUI intended for a laptop.

The GUI displays data received over serial onto the display and allows users
to interact with its interface.

27 October 2022
"""

import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib
matplotlib.use("TkAgg")
from PIL import ImageTk, Image
from Parsing import Parse
from DataDisplays import Displays
from MapDisplay import Map
from AltDisplay import AltGraph
import serial
import json
import csv


class GroundStationGUI(Parse):

    def __init__(self):
        super().__init__()

        self.app = Tk()
        self.app.title("CRT Ground Station")
        self.w = self.app.winfo_screenwidth()
        self.h = self.app.winfo_screenheight()
        self.images = ["acc.jpg", "gyr.jpg", "mag.jpg", "acc.jpg"]
        self.f = open('data.csv', 'w')

        # CRT header [ENSURE FONT IS DOWNLOADED]
        self.f0 = Frame(master = self.app, width = self.w, height = self.h*0.05, bg = "#142C2E")
        self.f0.pack(fill = tk.BOTH, side = tk.TOP, expand = False)
        self.title = Label(master = self.f0, text = "CRT Ground Station", bg = "#142C2E", fg = "white", font = ('OCR A Extended', 14))
        self.title.pack(fill = tk.BOTH, side = tk.TOP, expand = True)

        # layout panels
        self.f1 = Frame(master = self.app, width = self.w, height = self.h*0.67, bg = "black")
        self.f1.pack(fill = tk.BOTH, side = tk.TOP, expand = True)
        self.f2 = Frame(master = self.app, width = self.w, height = self.h*0.33, bg = "black")
        self.f2.pack(fill = tk.BOTH, side = tk.BOTTOM, expand = True)

        # feature panels
        self.mapF = self.panel(self.f1, tk.LEFT, "GPS")
        self.msg_alt = self.panel(self.f1, tk.RIGHT, "")
        self.altF = self.panel(self.msg_alt, tk.TOP, "Altimeter")
        self.msgF = self.panel(self.msg_alt, tk.BOTTOM, "Messages")
        # sensor panels
        self.accF = self.panel(self.f2, tk.LEFT, "Acceleration")
        self.gyrF = self.panel(self.f2, tk.LEFT, "Gyroscope")
        self.magF = self.panel(self.f2, tk.LEFT, "Magnetometer")
        self.therF = self.panel(self.f2, tk.LEFT, "Thermometer")

        # set images
        self.img1 = ImageTk.PhotoImage(Image.open("acc.jpg"))
        self.a = Label(self.accF, image = self.img1, borderwidth = 0)
        self.a.pack()
        self.img2 = ImageTk.PhotoImage(Image.open("gyro.jpg"))
        self.g = Label(self.gyrF, image = self.img2, borderwidth = 0)
        self.g.pack()
        self.img3 = ImageTk.PhotoImage(Image.open("mag.jpg"))
        self.m = Label(self.magF, image = self.img3, borderwidth = 0)
        self.m.pack()
        self.img4 = ImageTk.PhotoImage(Image.open("ther.jpg"))
        self.t = Label(self.therF, image = self.img4, borderwidth = 0)
        self.t.pack()


        self.disp = Displays(self.accF, self.gyrF, self.magF, self.therF, self.msgF, self.altF, self.sensorreadings)
        self.mapgraph = Map(self.gps, self.mapF)
        self.altgraph = AltGraph(self.alt, self.altF)

        self.ser = serial.Serial(port = "COM8", baudrate = 9600)
        self.app.after(1000, lambda: self.update())

        #self.app.mainloop()

    def panel(self, f, s, header):
        """
        Creates a Frame object using a given master Frame f to overlay on, a given alignment side s, and a text to display header.
        """
        p = Frame(master = f, bg = "black", highlightbackground="#52C6D0", highlightthickness=2)
        p.pack(fill = tk.BOTH, side = s, expand = True)
        p_title = Label(master = p, text = header, bg = "black", fg = "white", font = ('Helvetica', 14))
        p_title.pack(fill = tk.BOTH, expand = False)
        return p

    def createButton(self, m, t, c):
        """
        Creates a button with a master Frame m, a display text t, and a command to execute upon click c.
        """
        b = Button(master = m, text = t, command = c)
        b.pack(side = tk.TOP)

    def update(self):
        """
        Reads from serial and updates attributes in response to the new data, then calls on update methods for
        each object on the GUI that needs to change with the new data.
        """
        try:
            self.serUpdate()
        except:
            pass

        self.a.config(image = self.img1)
        self.a.pack()
        self.g.config(image = self.img2)
        self.g.pack()
        self.m.config(image = self.img3)
        self.m.pack()
        self.t.config(image = self.img4)
        self.t.pack()


        # only calling on the update method for the DataDisplays and AltGraph object due to the Ground Station
        # only receiving altimeter data at competition.
        self.disp.dispUpdate(self.sensorreadings)
        self.altgraph.altUpdate(self.alt)
        #self.mapgraph.updateMap(self.gps)

        self.app.after(1000, lambda: self.update())


if __name__ == "__main__":
    gsg = GroundStationGUI()
    gsg.app.mainloop()
    gsg.f.close()
