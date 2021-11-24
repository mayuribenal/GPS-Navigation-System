import serial
#import serial pacakge
from time import sleep
import webbrowser
#import package for opening link in browser
import sys
#import system package
def GPS_Info():
global NMEA_buff
global lat_in_degrees
global long_in_degrees
nmea_time = []
nmea_latitude = []
nmea_longitude = []
nmea_time = NMEA_buff[0]
nmea_latitude = NMEA_buff[1]
nmea_longitude = NMEA_buff[3]
#extract time from GPGGA string
#extract latitude from GPGGA string
#extract longitude from GPGGA string
print("NMEA Time: ", nmea_time,'\n')
print ("NMEA Latitude:", nmea_latitude,"NMEA Longitude:", nmea_longitude,'\n')
lat = float(nmea_latitude)
longi = float(nmea_longitude)
#convert string into float for calculation
#convertr string into float for calculation
lat_in_degrees = convert_to_degrees(lat)
#get latitude in degree decimal format
long_in_degrees = convert_to_degrees(longi) #get longitude in degree decimal format
#convert raw NMEA string into degree decimal format
def covert_to_degrees(raw_value):
decimal_value = raw_value/100.00
degrees = int(decimal_value)
mm_mmmm = (decimal_value - int(decimal_value))/0.6
position = degrees + mm_mmmm
position = "%.4f" %(position)
return position
gpgga_info = "$GPGGA,"
ser = serial.Serial ("/dev/ttyS0")
GPGGA_buffer = 0
NMEA_buff = 0
lat_in_degrees = 0
long_in_degrees = 0
#Open port with baud rate
try:
while True:
received_data = (str)(ser.readline())
GPGGA_data_available = received_data.find(gpgga_info)
if (GPGGA_data_available>0):
GPGGA_buffer = received_data.split("$GPGGA,",1)[1]
"$GPGGA," string
NMEA_buff = (GPGGA_buffer.split(','))
buffer
GPS_Info()
n')
#read NMEA string received
#check for NMEA GPGGA string
#store data coming after
#store comma separated data in
#get time, latitude, longitude
print("lat in degrees:", lat_in_degrees," long in degree: ", long_in_degrees, '\
map_link = 'http://maps.google.com/?q=' + lat_in_degrees + ',' + long_in_degrees
#create link to plot location on Google map
print("<<<<<<<<press ctrl+c to plot location on google maps>>>>>>\n")
#press ctrl+c to plot on map and exit
print("------------------------------------------------------------\n")
except KeyboardInterrupt:
webbrowser.open(map_link)
sys.exit(0)
