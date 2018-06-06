#Equipe Antares - UNICAMP

# This is the Main Rocket Controller using the Raspberry pi.
# A different thread is created and instantiated for each component.
# In this version, there is a PiCamera and a BMP180.
# The PiCamera records the flight for 20 seconds and then stops. The file is saved in a given directory.
# The BMP takes 20 measures and saves in a csv file.
# Next step is to adapt the BMP data gathering to work with the parachutes algorithm.  

# System imports
import time
import os
import time
import Adafruit_BMP.BMP085 as BMP085
import threading

# Files imports
from Altimeter import *
from Camera import *

# Create a list of threads
threads = []

# Append the Camera and altimeter threads
Cam = threading.Thread(target=camera)
threads.append(Cam)
Alt = threading.Thread(target=bmp)
threads.append(Alt)

# Start the threads
Cam.start()
Alt.start()