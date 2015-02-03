import numpy as np
import re

def combine():
	f1=open('label_files.txt','r')
	name=f1.readline().split('\n')[0]
	circle=open(name,'r')
	circle_data=np.load(circle)
	print 'length of circle labels is ',len(circle_data)
	print 'circle label data is ',circle_data
	
	name=f1.readline().split('\n')[0]
	Z=open(name,'r')
	Z_data=np.load(Z)
	print 'length of Z label data is ',len(Z_data)
	print 'Z label data is ',Z_data
	
	name=f1.readline().split('\n')[0]
	swipe_left=open(name,'r')
	swipe_left_data=np.load(swipe_left)
	print 'length of swipe left label data is ',len(swipe_left_data)
	print 'swipe left label data is ',swipe_left_data
	
	name=f1.readline().split('\n')[0]
	swipe_right=open(name,'r')
	swipe_right_data=np.load(swipe_right)
	print 'length of swipe right label data is ',len(swipe_right_data)
	print 'swipe right label data is ',swipe_right_data
	
	combine_vector=np.hstack((circle_data,Z_data,swipe_left_data,swipe_right_data))
	print ' the combined label is ', combine_vector
	f2=open('combined_label_vector.txt','w')
	np.save(f2,combine_vector)
	
if __name__=='__main__':
	combine()
		

