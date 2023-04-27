"""
Test Map Display

Use live GPS data to draw a path onto a map image.
"""

import tkinter as tk
from tkinter import *
import csv
import numpy as np
import pandas as pd
import matplotlib
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from Parsing import Parse

class Map(Parse):

    def __init__(self):
        super().__init__()
        self.lat_min = 42.6740
        self.lat_max = 42.7320
        self.long_min = -77.2310
        self.long_max = -77.1521
        self.bounds = (self.long_min, self.long_max, self.lat_min, self.lat_max)
        self.map_img = plt.imread('map.png')

        # test launch coords
        #self.lat = 42.702980
        #self.long = -77.191559

        # setup plot
        self.fig, self.ax = plt.subplots(figsize = (6,5))
        self.ax.set_title('Test Launch Map')
        self.ax.set_xlim(self.bounds[0],self.bounds[1])
        self.ax.set_ylim(self.bounds[2],self.bounds[3])

        self.ax.imshow(self.map_img, zorder=0, extent = self.bounds, aspect= 'equal')
        #im = plt.imread('map.png')
        #implot = plt.imshow(im, extent=self.bounds)
        plt.show(block=False)

    def updateMap(self):
        self.ax.scatter(self.gps[1], self.gps[0], zorder=1, alpha= 0.2, c='b', s=10)
        self.ax.imshow(self.map_img, zorder=0, extent = self.bounds, aspect= 'equal')
        plt.show(block=False)
