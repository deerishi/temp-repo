import numpy as np
import re

def extract_features():
	f=open('filenames.txt','r')
	line=f.readline().split('\n')[0]
	fx=open(line,'r')
	line=f.readline().split('\n')[0]
	fy=open(line,'r')
	line=f.readline().split('\n')[0]
	fz=open(line,'r')
	vector_file=open(r'test/test_set.txt','w')
	#label_file=open(r'/home/deepak/python_gesture/feature_vectors/swipe right label 3/label_3_swipe_right.txt','w')
	#vector_file2=open('vector_file2.txt','w')
	column_wise_vector=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
	print 'the len is column_wise_vector is ',len(column_wise_vector)
	datax=[]
	datay=[]
	dataz=[]
	labels=[]
	for line in fx:
		linex=int(float(line.split('\n')[0]))
		liney=int(float(fy.readline().split('\n')[0]))
		linez=int(float(fz.readline().split('\n')[0]))
		if linex==999999 and datax:
			length=len(datax)
			datax1=datax[:len(datax)/3]
			datax2=datax[len(datax)/3:(len(datax)/3)*2]
			datax3=datax[(len(datax)/3)*2:]
			#print 'data x1 is ',len(datax1)
			#print ''
			#print 'data x2 is ',len(datax2)
			#print ''
			#print 'data x3 is ',len(datax3)
			#print ''
			column_wise_vector[0].append(len(datax))
			column_wise_vector[1].append(np.mean(datax1))
			column_wise_vector[2].append(np.mean(datax2))
			column_wise_vector[3].append(np.mean(datax3))
			column_wise_vector[4].append(np.std(datax1))
			
			column_wise_vector[5].append(np.std(datax2))
			column_wise_vector[6].append(np.std(datax3))
			
			datay1=datay[:len(datay)/3]
			datay2=datay[len(datay)/3:(len(datay)/3)*2]
			datay3=datay[(len(datay)/3)*2:]
			column_wise_vector[7].append(np.mean(datay1))
			column_wise_vector[8].append(np.mean(datay2))
			column_wise_vector[9].append(np.mean(datay3))
			column_wise_vector[10].append(np.std(datay1))
			column_wise_vector[11].append(np.std(datay2))
			column_wise_vector[12].append(np.std(datay3))
			
			dataz1=dataz[:len(dataz)/3]
			dataz2=dataz[len(dataz)/3:(len(dataz)/3)*2]
			dataz3=dataz[(len(dataz)/3)*2:]
			
			column_wise_vector[13].append(np.mean(dataz1))
			column_wise_vector[14].append(np.mean(dataz2))
			column_wise_vector[15].append(np.mean(dataz3))
			column_wise_vector[16].append(np.std(dataz1))
			column_wise_vector[17].append(np.std(dataz2))
			column_wise_vector[18].append(np.std(dataz3))
			
			array_xy1=np.asarray([datax1,datay1])
			array_xy2=np.asarray([datax2,datay2])
			array_xy3=np.asarray([datax3,datay3])
			
			column_wise_vector[19].append(np.cov(array_xy1)[0][1])
			column_wise_vector[20].append(np.cov(array_xy2)[0][1])
			column_wise_vector[21].append(np.cov(array_xy3)[0][1])
			datax=[]
			datay=[]
			dataz=[]
			labels.append(3.00)
		else:
			datax.append(linex)
			datay.append(liney)
			dataz.append(linez)
			
	print ''		
	final_feature_array=np.asarray(column_wise_vector)
	print ' the final feature vector array is ',final_feature_array
	np.save(vector_file,final_feature_array)
	vector_file.close();
	#label_array=np.asarray(labels)
	#print 'the label array is ',label_array
	#np.save(label_file,label_array)
	
if __name__=='__main__':
	extract_features()
			
