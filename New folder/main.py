import serial

ser = serial.Serial("COM4", 9600)
temp = ''
while 1:
	data=ser.readline()
	print data
    i = int(data, 16)
	data=data.strip()
	print data
	if data[:1]=="0":
		#print "\a"
		#trimdata = data.replace(" ","")
		#thedata =(trimdata)
		#uri = config.keyuri+'%input%ktp%'+trimdata
		#thedata =(uri)
		#webbrowser.open_new(config.host+thedata)
