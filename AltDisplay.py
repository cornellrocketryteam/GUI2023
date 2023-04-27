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

# rocket speed: 800ft/sec

class AltGraph(Parse):

    def __init__(self):
        super().__init__()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.xs = []
        self.ys = []
        self.t = 0
        self.ani = ""

        # Format plot
        plt.title('Altitude vs Time')
        plt.ylabel('Alitude (ft)')
        self.ax.set_ylim([0, 12000])

        self.ani = animation.FuncAnimation(self.fig, partial(animate, alt=self), interval=200, cache_frame_data=False)
        plt.show(block=False)
        plt.ion()

    def altUpdate(self):
        self.ani = animation.FuncAnimation(self.fig, partial(animate, alt=self), interval=200, cache_frame_data=False, blit=True)
        plt.show(block=False)
        plt.ion()


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
