#Equipe Antares - UNICAMP

#This code read data from BMP180 sensor and store it in an excel file and records the flight for 20 seconds

import time
import os
import Adafruit_BMP.BMP085 as BMP085
import threading

def camera ():
	#filma com a camera por 20 segundos.
	os.system("raspivid -o /home/pi/script/destronfeznada.h264 -t 20000")
	return
	
def bmp ():
	file = open('/home/pi/script/Rocket Data.csv', 'w')
	
	sensor = BMP085.BMP085()
	
	#save the initial time
	time_base = time.time()
	
	#save the initial altitude
	alt_base = sensor.read_altitude()
	
	#define the column names
	
	file.write('Time;Altitude;Temperature;Pressure;\n')
	
	tmp = 1
	
	#colect data from bmp180 and save in the excel file
	while tmp <= 20:
		t = time.time() - time_base
	
		altitude = sensor.read_altitude() - alt_base
	
		temperature = sensor.read_temperature()
	
		pressure = sensor.read_pressure()
		
		
		file.write(str(t) + '; ' +
			   str(altitude) + '; ' +
			   str(temperature) + '; ' +
			   str(pressure) + ';\n')
	
		tmp = tmp + 1
		time.sleep(1)

	file.close();
	print("Terminou leitura bmp.")
	return

threads = []
b = threading.Thread(target=camera)
threads.append(b)
b.start()
	
a = threading.Thread(target=bmp)
threads.append(a)
a.start()