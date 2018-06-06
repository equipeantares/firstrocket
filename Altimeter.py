# Equipe Antares - UNICAMP
# Altimeter functions and control

def bmp ():
	# Creates file
	var dir = '/home/pi/script/Rocket Data.csv';
	file = open(dir, 'w')
	
	# Initiates sensor
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
	print("Process Finished.")
	return