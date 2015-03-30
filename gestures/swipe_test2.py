import serial,re,sys
import numpy as np
from modshogun import RealFeatures,MulticlassLabels,SerializableHdf5File,GMNPSVM,GaussianKernel,MulticlassLibSVM,LibLinear
fx=open('testing_trialx4.txt','w');
fy=open('testing_trialy4.txt','w');
fz=open('trialz4.txt','w');
ser = serial.Serial('/dev/ttyACM0', 9600)
a=['1','1','1','1']
i=1
datax=[]
datay=[]
dataz=[]
while(a[1]!='999999'):
	s=ser.readline()
	
	try:
		a=re.split('[a-zA-Z:,]+',s)
		if a[1] and a[2] and a[3]:
			
			try:
				temp1=float(a[1])
				temp2=float(a[2])
				temp3=float(a[3])
				datax.append(temp1*0.004)
				datay.append(temp2*0.004)
				dataz.append(temp3*0.004)
				print 'a= ',a 
			except:
				pass
	except:	
		a=['1','1','1','1']


length=len(datax)	
if(length<10):	
	sys.exit(0)
datax=datax[:length-1]
datay=datay[:length-1]
dataz=dataz[:length-1]
x=len(datax)
print 'the length is ',len(datax)

print 'the std of data x is ',np.std(datax), ' the std of data y is ',np.std(datay), ' the std of data z is ',np.std(dataz)
start=int(0.2*x)
end=int(0.8*x)

print 'the mean of data x is ',np.mean(datax[start:end]), ' the mean of data y is ',np.mean(datay[start:end]), ' the mean of data z is ',np.mean(dataz[start:end])

if np.std(datax)>np.std(datay) and np.std(datax)>np.std(datay):
	if np.mean(datax[start:end])>0 :
		print 'Possible right swipe'
elif np.std(datay)>np.std(datax) and np.std(datay)>np.std(dataz):
	if np.mean(datay[start:end])>0 :
		print 'Possible right swipe'
elif np.std(dataz)>np.std(datax) and np.std(dataz)>np.std(datax):
	if np.mean(dataz[start:end])>0 :
		print 'Possible right swipe'
		
if np.std(datax)>np.std(datay) and np.std(datax)>np.std(datay):
	if np.mean(datax[start:end])<0 :
		print 'Possible left swipe'
if np.std(datay)>np.std(datax) and np.std(datay)>np.std(dataz):
	if np.mean(datay[start:end])<0 :
		print 'Possible left swipe'
if np.std(dataz)>np.std(datax) and np.std(dataz)>np.std(datax):
	if np.mean(dataz[start:end])<0 :
		print 'Possible left swipe'
		
		
