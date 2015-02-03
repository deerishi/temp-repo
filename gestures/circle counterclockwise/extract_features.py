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
	vector_file=open(r'train_cc_label0.txt','w')
	label_file=open(r'label_0cc.txt','w')
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
			
			column_wise_vector[1].append(np.mean(datax)) 	#Feature 1 :: Meanx
			column_wise_vector[2].append(np.mean(datay))	#Feature 2 :: Meany
			column_wise_vector[3].append(np.mean(dataz))	#Feature 3 :: Meanz
			
			column_wise_vector[4].append(np.std(datax))		#Feature 4 :: Stdx
			column_wise_vector[5].append(np.std(datay))		#Feature 5 :: Stdy
			column_wise_vector[6].append(np.std(dataz))		#Feature 6 :: Stdz
			
			array_xy=np.asarray([datax,datay])
			array_yz=np.asarray([datay,dataz])
			array_zx=np.asarray([dataz,datax])
			
			column_wise_vector[7].append(np.cov(array_xy)[0][1])	#Feature 7 :: COVxy
			column_wise_vector[8].append(np.cov(array_yz)[0][1])	#Feature 8 :: COVyz
			column_wise_vector[9].append(np.cov(array_zx)[0][1])	#Feature 9 :: COVzx
			
			datax=[]
			datay=[]
			dataz=[]
			labels.append(0.00)
		else:
			datax.append(linex)
			datay.append(liney)
			dataz.append(linez)
			
	print ''		
	final_feature_array=np.asarray(column_wise_vector)
	print ' the final feature vector array is ',final_feature_array
	np.save(vector_file,final_feature_array)
	vector_file.close();
	label_array=np.asarray(labels)
	print 'the label array is ',label_array
	np.save(label_file,label_array)
	print 'the size is ',len(label_array),' and of data ',len(final_feature_array[0])
	
if __name__=='__main__':
	extract_features()
			
