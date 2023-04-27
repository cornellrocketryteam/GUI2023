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
from DataDisplays import Displays
from MapDisplay import Map
from AltDisplay import AltGraph
import serial
import json
import csv


class GroundStationGUI():

    def __init__(self):
        self.app = Tk()
        self.app.title("CRT Ground Station")
        self.w = self.app.winfo_screenwidth()
        self.h = self.app.winfo_screenheight()
        self.images = ["acc.jpg", "gyr.jpg", "mag.jpg", "acc.jpg"]

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
        self.map = self.panel(self.f1, tk.LEFT, "GPS")
        self.msg_alt = self.panel(self.f1, tk.RIGHT, "")
        self.alt = self.panel(self.msg_alt, tk.TOP, "Altimeter")
        self.msg = self.panel(self.msg_alt, tk.BOTTOM, "Messages")
        # sensor panels
        self.acc = self.panel(self.f2, tk.LEFT, "Acceleration")
        self.gyr = self.panel(self.f2, tk.LEFT, "Gyroscope")
        self.mag = self.panel(self.f2, tk.LEFT, "Magnetometer")
        self.ther = self.panel(self.f2, tk.LEFT, "Thermometer")

        # set images
        self.img1 = ImageTk.PhotoImage(Image.open("acc.jpg"))
        self.a = Label(self.acc, image = self.img1, borderwidth = 0)
        self.a.pack()
        self.img2 = ImageTk.PhotoImage(Image.open("gyro.jpg"))
        self.g = Label(self.gyr, image = self.img2, borderwidth = 0)
        self.g.pack()
        self.img3 = ImageTk.PhotoImage(Image.open("mag.jpg"))
        self.m = Label(self.mag, image = self.img3, borderwidth = 0)
        self.m.pack()
        self.img4 = ImageTk.PhotoImage(Image.open("ther.jpg"))
        self.t = Label(self.ther, image = self.img4, borderwidth = 0)
        self.t.pack()

        #dsb = Scrollbar(self.data, orient = "vertical", bg = "white", command = self.data.yview)
        #msb = Scrollbar(self.msg, orient = "vertical", bg = "white", command = self.msg.yview)

        self.disp = Displays(self.acc, self.gyr, self.mag, self.ther, self.msg, self.alt)
        self.mapgraph = Map()
        self.altgraph = AltGraph()

        #self.embedAltGraph()
        #self.embedMapGraph()

        self.f = open('data.csv', 'w')
        self.ser = serial.Serial(port = "COM3", baudrate = 9600)
        self.app.after(1000, lambda: self.update())

        #self.app.mainloop()

    def panel(self, f, s, header):
        p = Frame(master = f, bg = "black", highlightbackground="#52C6D0", highlightthickness=2)
        p.pack(fill = tk.BOTH, side = s, expand = True)
        p_title = Label(master = p, text = header, bg = "black", fg = "white", font = ('Helvetica', 14))
        p_title.pack(fill = tk.BOTH, expand = False)
        return p

    def createButton(self, m, t, c):
        b = Button(master = m, text = t, command = c)
        b.pack(side = tk.TOP)

    def embedAltGraph(self):
        canvas = FigureCanvasTkAgg(self.altgraph.fig, master = self.alt)
        canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        canvas.draw()

    def embedMapGraph(self):
        canvas = FigureCanvasTkAgg(self.mapgraph.fig, master = self.map)
        canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        canvas.draw()

    def update(self):
        self.ser.reset_output_buffer()
        try:
            self.disp.jstr = self.ser.readline().decode("utf-8")
            self.altgraph.jstr = self.disp.jstr
            self.mapgraph.jstr = self.disp.jstr
            self.f.write(self.disp.jstr)

            try:
                self.disp.setValues()
                self.mapgraph.setValues()
                self.altgraph.setValues()
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

            #self.altgraph.altUpdate()
            self.altgraph.ani.resume()
            self.disp.printValues()
            self.disp.dispUpdate()
            self.mapgraph.updateMap()

        except:
            pass

        self.app.after(1000, lambda: self.update())


if __name__ == "__main__":
    print('almost sure')
    gsg = GroundStationGUI()
    gsg.app.mainloop()
