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
	vector_file=open(r'train_Z_10_dim.txt','w')
	label_file=open(r'label_1_Z.txt','w')
	#vector_file2=open('vector_file2.txt','w')
	column_wise_vector=[[],[],[],[],[],[],[],[],[],[]]
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
			column_wise_vector[0].append(len(datax)) #Feature 0 :: Length
			x=np.mean(datax) + np.mean(datay)+np.mean(dataz)
			
			"""column_wise_vector[1].append(np.mean(datax))	#Feature 7 :: Mean_X
			column_wise_vector[2].append(np.mean(datay))	#Feature 8 :: Mean_Y
			column_wise_vector[3].append(np.mean(dataz))	#Feature 9 :: Mean_Z
			
			column_wise_vector[4].append(max(datax)) 	#Feature 1 :: Max_X
			column_wise_vector[5].append(max(datay))	#Feature 2 :: Max_Y
			column_wise_vector[6].append(max(dataz))	#Feature 3 :: Max_Z
			
			column_wise_vector[7].append(min(datax))		#Feature 4 :: Min_X
			column_wise_vector[8].append(min(datay))		#Feature 5 :: Min_Y
			column_wise_vector[9].append(min(dataz))		#Feature 6 :: Min_Z"""
			
			column_wise_vector[1].append(max(datax)) 	#Feature 1 :: Max_X
			column_wise_vector[2].append(max(datay))	#Feature 2 :: Max_Y
			column_wise_vector[3].append(max(dataz))	#Feature 3 :: Max_Z
			
			column_wise_vector[4].append(min(datax))		#Feature 4 :: Min_X
			column_wise_vector[5].append(min(datay))		#Feature 5 :: Min_Y
			column_wise_vector[6].append(min(dataz))		#Feature 6 :: Min_Z
			
			column_wise_vector[7].append(np.mean(datax))	#Feature 7 :: Mean_X
			column_wise_vector[8].append(np.mean(datay))	#Feature 8 :: Mean_Y
			column_wise_vector[9].append(np.mean(dataz))	#Feature 9 :: Mean_Z
			
			#array_xy=np.asarray([datax,datay])
			#array_yz=np.asarray([datay,dataz])
			#array_zx=np.asarray([dataz,datax])
			
			
			
			datax=[]
			datay=[]
			dataz=[]
			labels.append(1.00)
		else:
			datax.append(linex*0.004)
			datay.append(liney*0.004)
			dataz.append(linez*0.004)
			
	print ''		
	final_feature_array=np.asarray(column_wise_vector)
	print ' the final feature vector array is ',final_feature_array,' and its dimensions are ',len(final_feature_array)
	np.save(vector_file,final_feature_array)
	vector_file.close();
	label_array=np.asarray(labels)
	print 'the label array is ',label_array
	np.save(label_file,label_array)
	print 'the size is ',len(label_array),' and of data ',len(final_feature_array[0])
	
if __name__=='__main__':
	extract_features()
			
