"""
Test Altimeter Display

Uses live altimeter data to track the LV and shows its path on the display.
"""

import tkinter as tk
from tkinter import *
import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from functools import partial
import numpy as np
import time
from Parsing import Parse

# rocket speed: 800ft/sec

class AltGraph():

    def __init__(self, alt, altF):
        super().__init__()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.xs = []
        self.ys = []
        self.t = 0
        #self.ani = ""
        self.alt = alt
        self.altF = altF

        # Format plot
        plt.title('Altitude vs Time')
        plt.ylabel('Alitude (ft)')
        self.ax.set_ylim([0, 12000])

        # self.ani = animation.FuncAnimation(self.fig, partial(animate, alt=self), interval=200, cache_frame_data=False)
        # plt.show(block=False)
        # plt.ion()

        self.canvas = FigureCanvasTkAgg(self.fig, master = self.altF)
        self.canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        self.canvas.draw()

    def altUpdate(self, alt):
        self.alt = alt
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

        # self.ani = animation.FuncAnimation(self.fig, partial(animate, alt=self), interval=200, cache_frame_data=False, blit=True)
        # plt.show(block=False)
        # plt.ion()
        # self.canvas.draw()


def animate(frame, alt: AltGraph=None):

    # Add x and y to lists
    try:
        # print(alt.alt)
        alt.ys.append(float(alt.alt))
        alt.xs.append(float(alt.t))
    except:
        pass

    alt.t += 1

    # Limit x and y lists to 20 items
    alt.xs = alt.xs[-20:]
    alt.ys = alt.ys[-20:]

    # Draw x and y lists
    alt.ax.clear()
    alt.ax.plot(alt.xs, alt.ys)
    alt.ani.pause()


#alt = AltGraph()
