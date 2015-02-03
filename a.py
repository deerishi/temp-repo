import serial,re

fx=open('gestures/trialx4.txt','w');
fy=open('gestures/trialy4.txt','w');
fz=open('gestures/trialz4.txt','w');
ser = serial.Serial('/dev/ttyACM0', 9600)
a=['1','1','1','1']
i=1
while(a[1]!='999999'):
	s=ser.readline()
	
	try:
		a=re.split('[a-zA-Z:,]+',s)
		if a[1] and a[2] and a[3]:
			
			try:
				temp1=int(float(a[1]))
				temp2=int(float(a[2]))
				temp3=int(float(a[3]))
				fx.write(a[1])
				fx.write('\n')
				fy.write(a[2])
				fy.write('\n')
				fz.write(a[3])
				fz.write('\n')
				print 'a= ',a 
			except:
				pass
	except:	
		a=['1','1','1','1']
	

