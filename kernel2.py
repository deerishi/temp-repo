#!/usr/bin/env python
parameter_list = [[1,2],[2,8]]


def classifier_custom_kernel_modular (C=1,dim=7):
	from modshogun import RealFeatures, BinaryLabels, CustomKernel, LibSVM
	from numpy import diag,ones,sign
	from numpy.random import rand,seed
	seed((C,dim))
	#help(CustomKernel)
	lab=sign(2*rand(dim) - 1)
	data=rand(20, dim)
	print 'data is ',data
	data2=data*data.T 
	print 'data2 is ',data2
	symdata=data*data.T + diag(ones(10))
	#print 'sym-data is ',symdata
	kernel=CustomKernel()
	#print 'kernel is ',kernel
	
	kernel.set_full_kernel_matrix_from_full(data)
	print 'kernel is ',kernel.get_kernel_matrix()
	labels=BinaryLabels(lab)
	svm=LibSVM(C, kernel, labels)
	svm.train()
	predictions =svm.apply()
	print 'predictions are ',predictions
	out=svm.apply().get_labels()
	#print 'out is ', 
	return svm,out

if __name__=='__main__':
	print('custom_kernel')
	classifier_custom_kernel_modular(*parameter_list[0])
	
	
