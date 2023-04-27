"""
Test Altimeter Display

Uses live altimeter data to track the LV and shows its path on the display.
"""

import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.figure import Figure
from functools import partial
import numpy as np
import time
from Parsing import Parse

import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


# rocket speed: 800ft/sec

class AltGraph(Parse):

    def __init__(self, altP):
        super().__init__()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.xs = []
        self.ys = []
        self.t = 0
        self.altF = altP

        self.canvas = FigureCanvasTkAgg(self.fig, master = self.altF)
        self.canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        self.canvas.draw()

        self.updatePlot()

    # make graph not show up a billion times
    def updatePlot(self):
        plt.cla()

        # Add data points
        self.xs.append(float(self.t))
        self.ys.append(float(self.alt))
        self.xs = self.xs[-20:]
        self.ys = self.ys[-20:]
        plt.plot(self.xs, self.ys)

        # Format plot
        plt.title('Altitude vs Time')
        plt.ylabel('Alitude (ft)')
        plt.xlabel(' ')
        #self.ax.set_ylim([0, 12000])

        #plt.show(block = False)
        self.t += 1

        self.canvas.draw_idle()

#alt = AltGraph()
