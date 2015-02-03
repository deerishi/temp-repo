import numpy as np
import re

def combine():
	f1=open('vector_files.txt','r')
	name=f1.readline().split('\n')[0]
	circle=open(name,'r')
	circle_data=np.load(circle)
	print 'length of circle data is ',len(circle_data[0])
	print 'circle data is ',circle_data
	
	name=f1.readline().split('\n')[0]
	Z=open(name,'r')
	Z_data=np.load(Z)
	print 'length of Z data is ',len(Z_data[0])
	print 'Z data is ',Z_data
	
	name=f1.readline().split('\n')[0]
	swipe_left=open(name,'r')
	swipe_left_data=np.load(swipe_left)
	print 'length of swipe left data is ',len(swipe_left_data[0])
	print 'swipe left data is ',swipe_left_data
	
	name=f1.readline().split('\n')[0]
	swipe_right=open(name,'r')
	swipe_right_data=np.load(swipe_right)
	print 'length of swipe right data is ',len(swipe_right_data[0])
	print 'swipe right data is ',swipe_right_data
	
	combine_vector=np.hstack((circle_data,Z_data,swipe_left_data,swipe_right_data))
	for i in range(0,10):
		combine_vector[i]=(combine_vector[i]-np.mean(combine_vector[i]))/np.std(combine_vector[i])
	
	print 'as a checksum the mean of the combine_vector[0] is ',np.mean(combine_vector[0])
	f2=open('combined_feature_vector.txt','w')
	np.save(f2,combine_vector)
	
if __name__=='__main__':
	combine()
		

