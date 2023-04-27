# GUI2023
Ground Station GUI - 2023


This repo contains two versions of the Ground Station GUI.

All files not including "test" in the name are used in the first version, which does not embed the Map Graph or the Altimeter Graph. Instead, it spawns three windows: the main GUI window, the Map Graph window, and the Altimeter Graph window. This version is more stable, but still seems to have some bugs with closing all windows. To run this version, run: python GroundStationGUI.py. Line 84 is set to read serial inputs from port COM3, so edit this line for whichever serial port you are using.

The second version attempts to embed the two graphs into the main GUI window. It has more bugs, as it is unable to quit the windows and spawns additional windows for the Map Graph and Altimeter Graph in addition to embedding these graphs in the main window. I am still working on trying to solve this issue. This version is written into the files including "test" in the title. To run this version, run: python test.py. Line 80 is set to read serial inputs from port COM3, so edit this line for whichever serial port you are using.

Also included in this repo is an Arduino script called json.ino, which loops infinitely over several JSON objects and outputs these over serial. Run this file with an Arduino while running either GroundStationGUI.py or test.py to output serial data that the GUI can receive.
