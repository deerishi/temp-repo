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
#print 'data x is ',datax

x=len(datax)
print 'The length of the gesture is ',len(datax)

#print 'the std of data x is ',np.std(datax), ' the std of data y is ',np.std(datay), ' the std of data z is ',np.std(dataz)
start=int(0.2*x)
end=int(0.8*x)

#print 'the mean of data x is ',np.mean(datax[start:end]), ' the mean of data y is ',np.mean(datay[start:end]), ' the mean of data z is ',np.mean(dataz[start:end])
if x<=23:
	if np.std(datax)>np.std(datay) and np.std(datax)>np.std(datay):
		if np.mean(datax[start:end])>0 :
			print 'Possible right swipe'
			sys.exit(0)
	elif np.std(datay)>np.std(datax) and np.std(datay)>np.std(dataz):
		if np.mean(datay[start:end])>0 :
			print 'Possible right swipe'
			sys.exit(0)
	elif np.std(dataz)>np.std(datax) and np.std(dataz)>np.std(datax):
		if np.mean(dataz[start:end])>0 :
			print 'Possible right swipe'
			sys.exit(0)
		
	if np.std(datax)>np.std(datay) and np.std(datax)>np.std(datay):
		if np.mean(datax[start:end])<0 :
			print 'Possible left swipe'
			sys.exit(0)
	if np.std(datay)>np.std(datax) and np.std(datay)>np.std(dataz):
		if np.mean(datay[start:end])<0 :
			print 'Possible left swipe'
			sys.exit(0)
	if np.std(dataz)>np.std(datax) and np.std(dataz)>np.std(datax):
		if np.mean(dataz[start:end])<0 :
			print 'Possible left swipe'
			sys.exit(0)

test_set=[[],[],[],[],[],[],[],[],[],[]]
f=open('normalization_parameters_letters_vs_cc.txt','r')
normalization_params=np.load(f)
test_set[0].append((length))
#x=np.mean(datax)+np.mean(datay)+np.mean(dataz)

test_set[1].append(max(datax)) 	#Feature 1 :: Max_X
test_set[2].append(max(datay))	#Feature 2 :: Max_Y
test_set[3].append(max(dataz))	#Feature 3 :: Max_Z
			
test_set[4].append(min(datax))		#Feature 4 :: Min_X
test_set[5].append(min(datay))		#Feature 5 :: Min_Y
test_set[6].append(min(dataz))		#Feature 6 :: Min_Z
			
test_set[7].append(np.mean(datax))	#Feature 7 :: Mean_X
test_set[8].append(np.mean(datay))	#Feature 8 :: Mean_Y
test_set[9].append(np.mean(dataz))	#Feature 9 :: Mean_Z

dim=10
# Now transforming the test set by the normalization parameters of the training set
for i in range(0,dim):
	test_set[i]=(test_set[i]-normalization_params[0][i])/normalization_params[1][i]
	
"""test_set=[[],[],[],[],[],[],[],[],[],[]]
test_set[0].append((length))

test_set[1].append(np.mean(datax)) #mean of test set
test_set[2].append(np.mean(datay))
test_set[3].append(np.mean(dataz))

test_set[4].append(np.std(datax)) #std of each axis
test_set[5].append(np.mean(datay))
test_set[6].append(np.mean(dataz))

array_xy=np.asarray([datax,datay])
array_yz=np.asarray([datay,dataz])
array_zx=np.asarray([dataz,datax])

test_set[7].append(np.cov(array_xy)[0][1])
test_set[8].append(np.cov(array_xy)[0][1])
test_set[9].append(np.cov(array_xy)[0][1])"""


test_array=np.asarray(test_set)
print 'the test array is ',test_array
f3=open('test_for_cc.txt','w')
np.save(f3,test_array)
test_feature=RealFeatures(test_array)

svm=LibLinear()
file_classifier= SerializableHdf5File(r'letters_vs_cc/ZLabel1accuracy=0.964285714286 liblinear_cc_vs_Z_svm_classifier_with_C_10_and_normalized.h5','r')
status=svm.load_serializable(file_classifier)
output=svm.apply(test_feature).get_labels()
print 'output is ',output
if int(output[0])==1:
	print 'You just made the mirrored letter Z '
elif  int(output[0])==-1:
	print 'You just made a counterclockwise circle '

