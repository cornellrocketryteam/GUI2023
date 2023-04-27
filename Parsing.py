"""
Parsing

This code takes JSON objects as inputs and parses them into values for each sensor.
These sensor values are then used in their proper locations in the GUI.

12 January 2023
"""
import serial
import json
import csv
import time


class Parse():

    def __init__(self):
        self.jstr = ""
        self.gps = [0.0, 0.0]
        self.alt = 0.0
        self.accel = 0.0
        self.gyro = 0.0
        self.mag = 0.0
        self.temp = 0.0
        self.message = ""
        self.f = open('data.csv', 'a')

    def setValues(self):
        # make into dictionary
        self.jstr = json.loads(self.jstr)

        self.gps = [self.jstr["latitude"], self.jstr["longitude"]]
        self.alt = self.jstr["elevation"]
        self.accel = [self.jstr["accel_x"], self.jstr["accel_y"], self.jstr["accel_z"]]
        self.gyro = [self.jstr["gyro_x"], self.jstr["gyro_y"], self.jstr["gyro_z"]]
        self.mag = [self.jstr["mag_x"], self.jstr["mag_y"], self.jstr["mag_z"]]
        self.temp = self.jstr["temp"]
        self.message = self.jstr["messages"]

    # for testing purposes
    def printValues(self):
        print(self.jstr)

        """
        print(self.gps)
        print(self.alt)
        print(self.accel)
        print(self.gyro)
        print(self.mag)
        print(self.temp)
        print(self.message)
        """

    def serUpdate(self):
        #ser = serial.Serial(port = "COM3", baudrate = 9600)
        self.ser.reset_output_buffer()
        self.jstr = self.ser.readline().decode("utf-8")
        self.f.write(self.jstr)
        try:
            self.setValues()
        except:
            pass
        self.printValues()


#p = Parse()

"""
JSON format reference:

{
   "latitude": 0.0,
   "longitude":0.0,
   "elevation":0.0,
   "accel_x":0.0,
   "accel_y":0.0,
   "accel_z":0.0,
   "gyro_x":0.0,
   "gyro_y":0.0,
   "gyro_z":0.0,
   "mag_x":0.0,
   "mag_y":0.0,
   "mag_z":0.0,
   "temp":0.0,
   "messages":[
      "Sensor Error",
      "Transitioned State",
      "Reached Apogee"
   ]
}

"""
