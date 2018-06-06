# Equipe Antares - UNICAMP
# Camera functions and control

# Records flight and saves in file
def camera ():
	#Records flight for 20 seconds
	os.system("raspivid -o /home/pi/script/destronfeznada.h264 -t 20000")
	return