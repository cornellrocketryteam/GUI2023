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
        self.accel = [0.0, 0.0, 0.0]
        self.gyro = [0.0, 0.0, 0.0]
        self.mag = [0.0, 0.0, 0.0]
        self.temp = 0.0
        self.message = ""
        self.sensorreadings = [self.gps, self.alt, self.accel, self.gyro, self.mag, self.temp, self.message]

    def setValues(self):
        """
        Takes the current JSON string and parses it into each of its sensor components, then assigns these sensor values
        to their corresponding attribute.
        """
        # make into dictionary
        self.jstr = json.loads(self.jstr)

        # self.gps = [self.jstr["latitude"], self.jstr["longitude"]]
        self.alt = self.jstr["altitude_rel"] #self.jstr["elevation"]
        # self.accel = [self.jstr["accel_x"], self.jstr["accel_y"], self.jstr["accel_z"]]
        # self.gyro = [self.jstr["gyro_x"], self.jstr["gyro_y"], self.jstr["gyro_z"]]
        # self.mag = [self.jstr["mag_x"], self.jstr["mag_y"], self.jstr["mag_z"]]
        # self.temp = self.jstr["temp"]
        # self.message = self.jstr["messages"]

        self.sensorreadings = [self.gps, self.alt, self.accel, self.gyro, self.mag, self.temp, self.message]

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
        """
        Reads from serial input and updates the attribute that holds this reading, then attempts
        to update each sensor attribute if the reading is in the expected format.
        """
        self.ser.reset_output_buffer()
        self.jstr = self.ser.readline().decode("utf-8")
        self.f = open('data.csv', 'a')
        self.f.write(self.jstr)
        try:
            self.setValues()
            self.printValues()
        except:
            pass
        self.f.close()


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


"""
{"callsign": "KD2ZGA", "altitude_abs": 1207, "altitude_rel": 1, "sd_init": 1,
 "radio_init": 1, "altitude_armed": 1, "keyswitch_armed": 0, "id", 21932}
"""
